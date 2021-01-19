#!/bin/bash

exec > >(tee -ia ~/log.txt | tee -ia >(grep -e 'BLUE4' -e 'Date' >> ~/shortLog.txt))
exec 2>&1

#set -e

#echo "Date: $(date '+%A %W %Y %X')"

#echo "Running annotmined\n"

#python annotmined_shell.py $1

#Moved from annotmined_launcher.py
#python conala-baseline/preproc/seq2seq_output_to_code.py results/annotmined.test.hyp conala-corpus/conala-test.json.seq2seq results/annotmined.test.json
#python conala-baseline/eval/conala_eval.py --strip_ref_metadata --input_ref conala-corpus/conala-test.json --input_hyp results/annotmined.test.json
#cp results/annotmined.test.json results/answer_annotmined.txt

echo "Date: $(date '+%A %W %Y %X')"
echo "Running annot\n"

python annot_shell.py $1

#Moved from annot_shell.py
python conala-baseline/preproc/seq2seq_output_to_code.py results/annot.test.hyp conala-corpus/conala-test.json.seq2seq results/annot.test.json
python conala-baseline/eval/conala_eval.py --strip_ref_metadata --input_ref conala-corpus/conala-test.json --input_hyp results/annot.test.json
cp results/annot.test.json results/answer_annot.txt

date '+%A %W %Y %X'
echo "Date: $(date '+%A %W %Y %X')"
echo "Done!"

