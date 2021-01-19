import os
import random

import numpy as np


from xnmt.modelparts.attenders import MlpAttender
from xnmt.batchers import WordSrcBatcher,InOrderBatcher,Batcher
from xnmt.modelparts.bridges import CopyBridge
from xnmt.modelparts.decoders import AutoRegressiveDecoder
from xnmt.modelparts.embedders import SimpleWordEmbedder, DenseWordEmbedder, PretrainedSimpleWordEmbedder
from xnmt.eval.tasks import LossEvalTask, AccuracyEvalTask
from xnmt.experiments import Experiment,ExpGlobal
from xnmt.inferences import AutoRegressiveInference
from xnmt.input_readers import PlainTextReader
from xnmt.transducers.recurrent import BiLSTMSeqTransducer, UniLSTMSeqTransducer
from xnmt.modelparts.transforms import AuxNonLinear
from xnmt.modelparts.scorers import Softmax
from xnmt.optimizers import AdamTrainer
from xnmt.param_collections import ParamManager
from xnmt.persistence import save_to_file
import xnmt.tee
from xnmt.train.regimens import SimpleTrainingRegimen
from xnmt.models.translators import DefaultTranslator
from xnmt.vocabs import Vocab
from xnmt.preproc import PreprocVocab,PreprocTokenize,PreprocRunner,SentencepieceTokenizer,VocabFiltererFreq
from xnmt.search_strategies import BeamSearch
from xnmt.length_norm import PolynomialNormalization

class AnnotRunner():
    def __init__(self,vocab_size = 4000,model_type ='unigram',min_freq=2,layers=1,layer_dim=128,alpha=0.001,epochs=5):
        self.vocab_size = vocab_size
        self.model_type = model_type
        self.min_freq = min_freq
        self.layers = layers
        self.layer_dim = layer_dim
        self.alpha = alpha
        self.epochs = epochs
    def run(self):
        seed=13
        random.seed(seed)
        np.random.seed(seed)

        EXP_DIR = os.path.dirname(__file__)
        EXP = "annot"

        model_file = f"{EXP_DIR}/results/{EXP}.mod"
        log_file = f"{EXP_DIR}/results/{EXP}.log"
        xnmt.tee.utils.dy.DynetParams().set_mem(1024) #Doesnt work figure out how to set memory
        xnmt.tee.set_out_file(log_file,exp_name=EXP)

        ParamManager.init_param_col()
        ParamManager.param_col.model_file = model_file

        pre_runner=PreprocRunner(tasks= [PreprocTokenize(in_files=[#f'{EXP_DIR}/conala-corpus/conala-trainnodev.snippet',
                                                                   #f'{EXP_DIR}/conala-corpus/conala-trainnodev.intent',
                                                                   #f'{EXP_DIR}/conala-corpus/conala-dev.intent',
                                                                   #f'{EXP_DIR}/conala-corpus/conala-dev.snippet',
                                                                   #f'{EXP_DIR}/conala-corpus/conala-test.intent',
                                                                   #f'{EXP_DIR}/conala-corpus/conala-test.snippet',
								   f'{EXP_DIR}/conala-corpus/attack_code_train.txt',
								   f'{EXP_DIR}/conala-corpus/attack_text_train.txt',
                                                                   f'{EXP_DIR}/conala-corpus/attack_code_test.txt',
                                                                   f'{EXP_DIR}/conala-corpus/attack_text_test.txt'
                                                                       
                                                                   #f'{EXP_DIR}/conala-corpus/all.code',
                                                                   #f'{EXP_DIR}/conala-corpus/all.anno'
                                                                  ],
                                                         out_files= [#f'{EXP_DIR}/conala-corpus/conala-trainnodev.tmspm4000.snippet',
                                                                     #f'{EXP_DIR}/conala-corpus/conala-trainnodev.tmspm4000.intent',
                                                                     #f'{EXP_DIR}/conala-corpus/conala-dev.tmspm4000.intent',
                                                                     #f'{EXP_DIR}/conala-corpus/conala-dev.tmspm4000.snippet',
                                                                     #f'{EXP_DIR}/conala-corpus/conala-test.tmspm4000.intent',
                                                                     #f'{EXP_DIR}/conala-corpus/conala-test.tmspm4000.snippet',
                                                                     f'{EXP_DIR}/conala-corpus/attack-train.tmspm4000.snippet',
                                                                     f'{EXP_DIR}/conala-corpus/attack-train.tmspm4000.intent',
                                                                     f'{EXP_DIR}/conala-corpus/attack-test.tmspm4000.snippet',
                                                                     f'{EXP_DIR}/conala-corpus/attack-test.tmspm4000.intent'
                                                                     #f'{EXP_DIR}/conala-corpus/django.tmspm4000.snippet',
                                                                     #f'{EXP_DIR}/conala-corpus/django.tmspm4000.intent'
                                                                    ],
                                                         specs= [{'filenum':'all',
                                                                 'tokenizers':[SentencepieceTokenizer(hard_vocab_limit=False,
                                                                     train_files= [f'{EXP_DIR}/conala-corpus/attack_text_train.txt',
                                                                                   f'{EXP_DIR}/conala-corpus/attack_code_train.txt'],vocab_size=self.vocab_size,
                                                                 model_type= self.model_type,model_prefix= 'conala-corpus/attack-train.tmspm4000.spm')]}])
            ,PreprocVocab(in_files= [f'{EXP_DIR}/conala-corpus/attack-train.tmspm4000.intent',
                                     f'{EXP_DIR}/conala-corpus/attack-train.tmspm4000.snippet'],
                          out_files=[f'{EXP_DIR}/conala-corpus/attack-train.tmspm4000.intent.vocab',
                                     f'{EXP_DIR}/conala-corpus/attack-train.tmspm4000.snippet.vocab'],
                          specs=[{'filenum':'all','filters':[VocabFiltererFreq(min_freq = self.min_freq)]}])],overwrite=False)

        src_vocab = Vocab(vocab_file=f"{EXP_DIR}/conala-corpus/attack-train.tmspm4000.intent.vocab")
        trg_vocab = Vocab(vocab_file=f"{EXP_DIR}/conala-corpus/attack-train.tmspm4000.snippet.vocab")

        batcher = Batcher(batch_size=64)

        inference = AutoRegressiveInference(search_strategy= BeamSearch(len_norm= PolynomialNormalization(apply_during_search=True),beam_size= 5),post_process= 'join-piece')

        layer_dim = self.layer_dim

        model = DefaultTranslator(
          src_reader=PlainTextReader(vocab=src_vocab),
          trg_reader=PlainTextReader(vocab=trg_vocab),
          src_embedder=SimpleWordEmbedder(emb_dim=layer_dim,vocab = src_vocab),

          encoder=BiLSTMSeqTransducer(input_dim=layer_dim, hidden_dim=layer_dim, layers=self.layers),
          attender=MlpAttender(hidden_dim=layer_dim, state_dim=layer_dim, input_dim=layer_dim),
          trg_embedder=SimpleWordEmbedder(emb_dim=layer_dim,vocab = trg_vocab),

            decoder=AutoRegressiveDecoder(input_dim=layer_dim,
                                                                         rnn=UniLSTMSeqTransducer(input_dim=layer_dim, hidden_dim=layer_dim,
                                                                                                  ),
                                                                        transform=AuxNonLinear(input_dim=layer_dim, output_dim=layer_dim,
                                                                                              aux_input_dim=layer_dim),
                                                                      scorer=Softmax(vocab_size=len(trg_vocab), input_dim=layer_dim),
                                                                    trg_embed_dim=layer_dim,
                                                                    input_feeding= False,
                                                                    bridge=CopyBridge(dec_dim=layer_dim)),
          inference=inference)

        #decoder = AutoRegressiveDecoder(bridge=CopyBridge(),inference=inference))

        train = SimpleTrainingRegimen(
          name=f"{EXP}",
          model=model,
          batcher=WordSrcBatcher(avg_batch_size=64),
          trainer=AdamTrainer(alpha=self.alpha),
          patience= 3,
          lr_decay= 0.5,
          restart_trainer= True,
          run_for_epochs=self.epochs,
          src_file= f"{EXP_DIR}/conala-corpus/attack-train.tmspm4000.intent",
          trg_file= f"{EXP_DIR}/conala-corpus/attack-train.tmspm4000.snippet",
          dev_tasks=[LossEvalTask(src_file=f"{EXP_DIR}/conala-corpus/attack-test.tmspm4000.intent",
                                  ref_file= f'{EXP_DIR}/conala-corpus/attack-test.tmspm4000.snippet',
                                  model=model,
                                  batcher=WordSrcBatcher(avg_batch_size=64)),
                     AccuracyEvalTask(eval_metrics= 'bleu',
                                      src_file= f'{EXP_DIR}/conala-corpus/attack-test.tmspm4000.intent',
                                      ref_file= f'{EXP_DIR}/conala-corpus/attack_text_test.txt',
                                      hyp_file= f'results/{EXP}.dev.hyp',
                                      model = model)])

        evaluate = [AccuracyEvalTask(eval_metrics="bleu",
                                     #src_file=f"{EXP_DIR}/conala-corpus/conala-test.tmspm4000.intent",
                                     src_file = f"{EXP_DIR}/conala-corpus/attack-test.tmspm4000.intent",
                                     #ref_file=f"{EXP_DIR}/conala-corpus/all.code",
				     #ref_file = f"{EXP_DIR}/conala-corpus/conala-test.snippet",
                                     ref_file = f"{EXP_DIR}/conala-corpus/attack_text_test.txt",
                                     hyp_file=f"results/{EXP}.test.hyp",
                                     inference=inference,
                                     model=model)]

        standard_experiment = Experiment(
          exp_global= ExpGlobal(default_layer_dim= 512, dropout= 0.3,
                                log_file= log_file,model_file=model_file),
          name="annot",
          model=model,
          train=train,
          evaluate=evaluate
        )


        # run experiment
        standard_experiment(save_fct=lambda: save_to_file(model_file, standard_experiment))

        exit()
