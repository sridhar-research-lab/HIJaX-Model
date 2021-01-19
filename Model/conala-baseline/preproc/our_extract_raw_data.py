# -*- coding: utf-8 -*-

from __future__ import print_function

import sys

import json
import sys
import nltk
import traceback
import ast
import astor
from OurCanonical import *
from util import get_encoded_code_tokens, detokenize_code, encode_tokenized_code, encoded_code_tokens_to_code, tokenize, compare_ast

if __name__ == '__main__':

    canon = Canonical()
    
    #Add additional cannon objects here
    canonOptions = [
        Canonical(remove=["is there (a|any)?", 'how (do|can|should|would) (i|you)', '(programmatic|pythonic)(ally)?', '(with )?(in )?python', '[a-z ]*(possible|way|how) to ', '(is there an? )?(in a )?(simple)|(easy) way( to)?|simply|easily', 'cant?( (i)|(you)|(we))?'],
                  replace={' an? .]':' ', 'dictionary':'dict', " the ": " "},
                  lower=True,
                  stemmer=nltk.stem.PorterStemmer(),
                  remove_punctuation=True,
                  std_var=True
                  ),
        Canonical(remove=["is there (a|any)?", 'how (do|can|should|would) (i|you)',
                          '(programmatic|pythonic)(ally)?', '(with )?(in )?python', '[a-z ]*(possible|way|how) to ',
                          '(is there an? )?(in a )?(simple)|(easy) way( to)?|simply|easily', 'cant?( (i)|(you)|(we))?'],
                  replace={' an?[ .]': ' ', 'dictionary': 'dict', " the ": " "},
                  lower=True,
                  stemmer=None,
                  remove_punctuation=True,
                  std_var=True
                  ),
    ]

    canonSelect = int(sys.argv[1])
    if canonSelect < len(canonOptions):
        print("Setting canon")
        canon = canonOptions[canonSelect]
    else:
        print("Failed to set cannon...., using default")
    num_failed = 0
    total_snippets = 0
   # for file_path, file_type in [('conala-train.json', 'annotated'), ('conala-test.json', 'annotated'), ('conala-mined.jsonl', 'mined'),('conala-unique_mined.json','edited'),('conala-all_prob50_mined.json','edited'),('attack_code_test.txt','attack'),('attack_code_train.txt','attack'),('attack_text_train.txt','attack'),('attack_text_test.txt','attack')]:
    for file_path, file_type in [('conala-train.json', 'annotated'), ('conala-test.json', 'annotated'), ('conala-mined.jsonl', 'mined'),('conala-unique_mined.json','edited'),('conala-all_prob50_mined.json','edited')]:
        print('extracting {} file {}'.format(file_type, file_path), file=sys.stderr)

        if file_type == 'annotated':
            dataset = json.load(open(file_path))
        elif file_type == 'mined':
            dataset = []
            with open(file_path, 'r') as f:
                for line in f:
                    dataset.append(json.loads(line.strip()))
        elif file_type == 'edited':
            dataset = json.load(open(file_path))
       #rth, file_type in [('conala-train.json', 'annotated'), ('conala-test.json', 'annotated'), ('conala-mined.jsonl', 'mined'),('conala-unique_mined.json','edited'),('conala-all_prob50_mined.json','edited')]: TODO: Cclize attack files as well
       # elif file_type = 'attack':
           # dataset = []
             
        for i, example in enumerate(dataset):
            intent = example['intent']
            rewritten_intent = None
            if file_type == 'annotated' and example['rewritten_intent'] != None:
              rewritten_intent = example ['rewritten_intent']
            else:
              final_intent = canon.clean_intent(intent)

            
             
            snippet = example['snippet']
            # print(i)
            # code_tokens = get_encoded_code_tokens(snippet)
            # print(' '.join(code_tokens))

            failed = False
            intent_tokens = []
            total_snippets += 1
            if rewritten_intent != None:
                try:
                    canonical_intent, slot_map = canon.canonicalize_intent(rewritten_intent)
                    final_intent = canon.clean_intent(canonical_intent)
                    intent_tokens = nltk.word_tokenize(final_intent)

                    canonical_snippet = canon.canonicalize_code(snippet,slot_map)
                    decanonical_snippet = canon.decanonicalize_code(canonical_snippet,slot_map)
                    snippet_reconstr = astor.to_source(ast.parse(snippet)).strip()
                    decanonical_snippet_reconstr = astor.to_source(ast.parse(decanonical_snippet)).strip()
                    encoded_reconstr_code = get_encoded_code_tokens(decanonical_snippet_reconstr)
                    decoded_reconstr_code = encoded_code_tokens_to_code(encoded_reconstr_code)
                    print('.', end='')
                    #if not compare_ast(ast.parse(decoded_reconstr_code), ast.parse(snippet)):
                    print(i)
                    print('Intent: %s' % intent)
                    print('Original Snippet: %s' % snippet_reconstr)
                    print('Tokenized Snippet: %s' % ' '.join(encoded_reconstr_code))
                    print('decoded_reconstr_code: %s' % decoded_reconstr_code)

                except:
                    print("Exception")
                    print('*' * 20, file=sys.stderr)
                    print(i, file=sys.stderr)
                    print(intent, file=sys.stderr)
                    print(snippet, file=sys.stderr)
                    traceback.print_exc()

                    failed = True
                finally:
                    example['slot_map'] = slot_map

            if rewritten_intent is None and not failed:
                try:
                      encoded_reconstr_code = get_encoded_code_tokens(snippet.strip())
                except:
                      failed = True
                      traceback.print_exc()
            elif not failed:
                try:
                     encoded_reconstr_code = get_encoded_code_tokens(canonical_snippet.strip())
                except:
                      failed = True
                      traceback.print_exc() 
            else:
                num_failed += 1
                #del dataset[i]
                continue

            if not intent_tokens:
                intent_tokens = nltk.word_tokenize(final_intent)

            example['intent_tokens'] = intent_tokens
            example['snippet_tokens'] = encoded_reconstr_code
            
        print ('Number of snippets in the set: '+ str(total_snippets))
        print ('Number of snippets that don\'t compile and were excluded: '+ str(num_failed))
        print ('% failed is: ' + str(float(num_failed/total_snippets)))
        json.dump(dataset, open(file_path + '.seq2seq', 'w'), indent=2)
