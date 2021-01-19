from annot_model import AnnotRunner
from annotmined_model import  MinedRunner
import os
import shutil
import zipfile
import sys


#Add your options here and update the loop in ultraLauncher.bash
ant_mined_options = [
    MinedRunner(model_type='unigram',epochs= 10,layers = 1,layer_dim =100, embedding = 'embeddings/conala-annotmined-input-unstemmed.vec',
                trg_embedding = 'embeddings/conala-annotmined-output-stemmed.vec',mined_data = 'conala-unique_mined'),MinedRunner(model_type='unigram',epochs= 100,layers = 1,layer_dim =128, mined_data = 'conala-trainnodev+all_prob50_mined'), MinedRunner(model_type='unigram',epochs= 10,layers = 2,layer_dim =128, mined_data = 'conala-unique_mined')
]

ant_mined = ant_mined_options[1]

ant_mined_select = int(sys.argv[1])
if ant_mined_select < len(ant_mined_options):
    print("Setting ant_mined")
    ant_mined = ant_mined_options[ant_mined_select]
else:
    print("Failed to set ant_mined...., using default")

ant_mined.run()
