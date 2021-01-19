from annot_model import AnnotRunner
from annotmined_model import  MinedRunner
import os
import shutil
import zipfile
import sys

#Add your options here and update the loop in ultraLauncher.bash
ant_options = [
  
    AnnotRunner(model_type='unigram',epochs= 60, layer_dim= 128, alpha= 0.001,min_freq= 8),
 AnnotRunner(model_type='unigram',epochs= 60, layer_dim= 128, alpha= 0.0001,min_freq= 8),
AnnotRunner(model_type='unigram',epochs= 30, layer_dim= 128, alpha= 0.01,min_freq= 10),

    
]

ant = ant_options[0]
print(sys.argv[1])
ant_select = int(sys.argv[1])
if ant_select < len(ant_options):
    print("Setting ant")
    ant = ant_options[ant_select]
else:
    print("Failed to set ant...., using default")

ant.run()
