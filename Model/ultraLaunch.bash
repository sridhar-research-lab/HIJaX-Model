#!/bin/bash

#Exit as soon as something fails
#set -e

#The outer preproc loop
for i in `seq 0 0`; do #Change based on preprocess options
#	./conala-baseline/setup.bash $i
	for j in `seq 0 0`; do #Change based on model options
		#Run the model using whatever you have defined for that number
		./superLaunch.bash $j

		mv results ~/results_archive/id_$i_$j_$(date +%Y-%m-%d-%H-%M-%S)

#		zip -r ~/bak_results/result_$i_$j_$(date '+%A_%W_%Y_%X').zip ~/NLP-Project/results
		#zip -r "bak_results/result_$i_$j_$(date '+%A_%W_%Y_%X').zip" results
	done
done
