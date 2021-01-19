#!/bin/bash
set -e

SDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
WDIR=`pwd`

# Get the data
wget http://www.phontron.com/download/conala-corpus-v1.1.zip
unzip conala-corpus-v1.1.zip

# Extract data
cd $WDIR/subset_data
cp conala-unique_mined.json $WDIR/conala-corpus/conala-unique_mined.json

cp conala-all_prob50_mined.json $WDIR/conala-corpus/conala-all_prob50_mined.json
 
cd $WDIR/conala-corpus

python $SDIR/preproc/our_extract_raw_data.py 1 # > raw_data.txt

python $SDIR/preproc/json_to_seq2seq.py conala-train.json.seq2seq conala-train.intent conala-train.snippet
python $SDIR/preproc/json_to_seq2seq.py conala-test.json.seq2seq conala-test.intent conala-test.snippet
python $SDIR/preproc/json_to_seq2seq.py conala-mined.jsonl.seq2seq conala-mined.intent conala-mined.snippet

python $SDIR/preproc/json_to_seq2seq.py conala-unique_mined.json.seq2seq conala-unique_mined.intent conala-unique_mined.snippet

python $SDIR/preproc/json_to_seq2seq.py conala-all_prob50_mined.json.seq2seq conala-all_prob50_mined.intent conala-all_prob50_mined.snippet

# Split off a 400-line dev set from the training set
# Also, concatenate the first 100000 lines of mined data
for f in intent snippet; do
  head -n 400 < conala-train.$f > conala-dev.$f
  tail -n +401 < conala-train.$f > conala-trainnodev.$f
  cat conala-trainnodev.$f <(head -n 100000 conala-mined.$f) > conala-trainnodev+mined.$f
  cat conala-trainnodev.$f < conala-unique_mined.$f > conala-trainnodev+unique-mined.$f
 cat conala-trainnodev.$f < conala-all_prob50_mined.$f > conala-trainnodev+all_prob50_mined.$f
done

#for f in intent snippet; do
#    head -n 400 < conala-train.$f > conala-dev.$f
#    tail -n +401 < conala-train.$f > conala-trainnodev.$f
#    cat conala-trainnodev.$f <(conala-unique_mined.$f) > conala-trainnodev+unique-mined.$f
#done


cd $WDIR

rm conala-corpus-v1.1.zip

echo "Done!"

