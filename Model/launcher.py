from annot_runner import AnnotRunner
from annotmined_runner import  MinedRunner
import os
import shutil
import zipfile
from taisazero.email_tool import EmailTool

EXP_DIR = os.path.dirname(__file__)
ant_mined = MinedRunner(model_type='unigram',epochs= 30,layers = 3,layer_dim =128)
EXP_DIR = '.'
ant = AnnotRunner(model_type='unigram',epochs= 60, layer_dim= 100, alpha= 0.01)

#ant_mined.run()

#os.system('python '+str(EXP_DIR)+'/conala-baseline/'+'preproc/seq2seq_output_to_code.py results/annotmined.test.hyp conala-corpus/conala-test.json.seq2seq results/annotmined.test.json')
#os.system('python '+str(EXP_DIR)+'/conala-baseline/eval/conala_eval.py --strip_ref_metadata --input_ref conala-corpus/conala-test.json --input_hyp results/annotmined.test.json')

#shutil.copy(str(EXP_DIR)+'/results/annotmined.test.json',str(EXP_DIR)+'/results/answer_annotmined.txt')


#ant.run()
os.system('python '+str(EXP_DIR)+'/conala-baseline/'+'preproc/seq2seq_output_to_code.py results/annot.test.hyp conala-corpus/conala-test.json.seq2seq results/annot.test.json')
os.system('python '+str(EXP_DIR)+'/conala-baseline/eval/conala_eval.py --strip_ref_metadata --input_ref conala-corpus/conala-test.json --input_hyp results/annot.test.json')

shutil.copy(str(EXP_DIR)+'/results/annot.test.json',str(EXP_DIR)+'/results/answer_annot.txt')


#zip_file=zipfile.ZipFile('answers.zip','w')
#zip_file.write(str(EXP_DIR)+'/results/answer_annot.txt',compress_type=zipfile.ZIP_DEFLATED)
#zip_file.write(str(EXP_DIR)+'/results/answer_annotmined.txt',compress_type=zipfile.ZIP_DEFLATED)
#zip_file.close()


#Email results
#msg = 'Dear Meta-Programmer Member!\nYou\'re receiving this email to notify you that the latest CoNaLa experiment has completed running. This included unigrams, 3 layers and a dimension of 128.  Attached below are the results!\n-- Rumi'
cutie = '(づ｡◕‿‿◕｡)づ'
files = str(EXP_DIR)+'/answers.zip'

sender = EmailTool(['ealhossa@uncc.edu','molson10@uncc.edu','bbeckwi2@uncc.edu'],msg,'CoNaLa - Experiment Complete!',files)

#sender.send()
