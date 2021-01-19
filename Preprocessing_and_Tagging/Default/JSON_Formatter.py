import json
import random
import math
import re

escape_dict={'\a':r'\a',
           '\b':r'\b',
           '\c':r'\c',
           '\f':r'\f',
           '\n':r'\n',
           '\r':r'\r',
           '\s':r'\s',
           '\t':r'\t',
           '\v':r'\v',
           '\'':r'\'',
           '\"':r'\"',
           '\0':r'\0',
           '\1':r'\1',
           '\2':r'\2',
           '\3':r'\3',
           '\4':r'\4',
           '\5':r'\5',
           '\6':r'\6',
           '\7':r'\7',
           '\8':r'\8',
           '\9':r'\9'}
'''for i in range(10000):
    str_val = str(i).zfill(4)'''



def raw(text):
    """Returns a raw string representation of text"""
    new_string=''
    for char in text:
        try: new_string+=escape_dict[char]
        except KeyError: new_string+=char
    return new_string

def random_split(input_json_arr, test_percent):
    if test_percent < 0 or test_percent > 100:
        print("percent split must be between 0-100")
        return
    test_arr = []
    test_val = math.floor(len(input_json_arr) * (test_percent/100))
    for i in range(test_val):
        random_index = random.randint(0, len(input_json_arr)-1)
        random_val = input_json_arr[random_index]
        test_arr.append(random_val)
        del input_json_arr[random_index]

    output_json_file = open('testJSON.json', 'w')
    json_string = "["
    for i in range(len(test_arr)):
        if (i < len(test_arr) - 1):
            json_string = json_string + str(test_arr[i]) + ","
        else:
            json_string = json_string + str(test_arr[i])
    json_string = json_string + "]"
    output_json_file.write(json_string)
    output_json_file.close()

    random.shuffle(input_json_arr)
    output_json_file = open('trainJSON.json', 'w')
    json_string = "["
    for i in range(len(input_json_arr)):
        if (i < len(input_json_arr) - 1):
            json_string = json_string + str(input_json_arr[i]) + ","
        else:
            json_string = json_string + str(input_json_arr[i])
    json_string = json_string + "]"
    output_json_file.write(json_string)
    output_json_file.close()

def json_from_txt(text_arr, code_arr):
    if len(text_arr) == len(code_arr):
        json_arr = []
        counter = 0
        for file_1_line, file_2_line in zip(text_arr, code_arr):
            json_data = {"intent": file_1_line.strip(), "rewritten_intent": file_1_line.strip(),
                         "snippet": file_2_line.strip(), "question_id": counter}
            json_temp = json.dumps(json_data)
            json_final = json.loads(json_temp)
            json_arr.append(json_final)
            counter = counter + 1
        clean_json_file(json_arr)
    else:
        print("test file sizes don't match")

def clean_json_file(json_file_arr):
    if len(json_file_arr) > 0:
        clean_json_arr = []
        for i in range(len(json_file_arr)):
            current_json = json_file_arr[i]
            del current_json['question_id']
            #intent_str = current_json['intent']
            #rewritten_intent_str = current_json['rewritten_intent']
            #snippet_str = current_json['snippet']
            '''if len(intent_str) == 0 or len(rewritten_intent_str) == 0 or len(snippet_str) == 0:
                continue'''
            clean_intent_str = ''
            clean_rewritten_intent_str = ''
            clean_snippet_str = ''
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            digits = '0123456789'
            special = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
            '''for a in range(len(intent_str)):
                current_char = intent_str[a]
                if ((current_char in digits) or (current_char.lower() in alphabet)) or current_char.isspace() or (current_char in special):
                    clean_intent_str = clean_intent_str + current_char

            for b in range(len(rewritten_intent_str)):
                current_char = rewritten_intent_str[b]
                if ((current_char in digits) or (current_char.lower() in alphabet)) or current_char.isspace() or (current_char in special):
                    clean_rewritten_intent_str = clean_rewritten_intent_str + current_char
            '''
            #current_json['intent'] = clean_intent_str
            #current_json['rewritten_intent'] = clean_rewritten_intent_str
            #current_json['snippet'] = current_json['snippet'] #raw(current_json['snippet'])
            json_data = {"intent": current_json['intent'], "rewritten_intent": current_json['rewritten_intent'],
                         "snippet": current_json['snippet']}
            json_temp = json.dumps(json_data)
            clean_json_arr.append(json_temp)
        random_split(clean_json_arr, 20)
    else:
        print('json is empty')

def json_to_text(json_file_arr):
    line_cnt = 0
    if len(json_file_arr) > 0:
        clean_intent = []
        clean_snippets = []
        for i in range(len(json_file_arr)):
            skip_flag = False
            current_json = json_file_arr[i]
            intent_str = raw(current_json['intent'])
            snippet_str = raw(current_json['snippet'])
            '''if len(intent_str) == 0 or len(snippet_str) == 0:
                continue'''
            clean_intent_str = ''
            clean_snippet_str = ''
            break_flag = False
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            digits = '0123456789'
            special = {'~', ':', "'", '+', '[', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
            special_2 = {'+', '[', '{', '(', '-', '*', ',', '}', '.', '=', ']', ')', '~', ':', "'", '"', '@', '^', '{', '%', '|', ',', '&', '<', '`', '_', '!', '>', '?', '#', '$'}
            '''for a in range(len(intent_str)):
                current_char = intent_str[a]
                if ((current_char in digits) or (current_char.lower() in alphabet)) or current_char.isspace() or (current_char in special_2):
                    clean_intent_str = clean_intent_str + current_char
                else:
                    break_flag = True
                    break

            for a in range(len(snippet_str)):
                current_char = snippet_str[a]
                if ((current_char in digits) or (current_char.lower() in alphabet)) or current_char.isspace() or (current_char in special_2):
                    clean_snippet_str = clean_snippet_str + current_char
                else:
                    break_flag = True
                    break
            if(not break_flag):
                clean_intent.append(raw(clean_intent_str))
                clean_snippets.append(raw(snippet_str))'''
            clean_intent.append(intent_str)
            clean_snippets.append(snippet_str)

        with open('output-intent.txt', 'w', encoding='utf-8') as filehandle:
            filehandle.writelines("%s\n" % text for text in clean_intent)

        with open('output-snippet.txt', 'w', encoding='utf-8') as filehandle:
            filehandle.writelines("%s\n" % text for text in clean_snippets)
        print('clean intent: ', len(clean_intent),', clean_snippets:', len(clean_snippets), ', line count:', line_cnt)
    else:
        print('json is empty')


num = input (".txt to .json enter (1), .json to .json (2), .jsonl to text(3), .json to text(4): ")

if num == '1':
    #load in text files
    text_file = open('./new_mal/intent-mal-very-high-200.txt', 'r', encoding='utf-8')
    code_file = open('./new_mal/snippet-mal-very-high-200.txt', 'r', encoding='utf-8')

    text_array = text_file.readlines()
    code_array = code_file.readlines()
    json_from_txt(text_array, code_array)

# or

elif num == '2':
    #load in JSON file to be formatted
    json_file = open('intentSnippet.json', 'r', encoding='utf-8')
    json_file_array = json.load(json_file)

    clean_json_file(json_file_array)

elif num == '3':
    #JSON to text files
    jsonl_file = open('conala-mined.jsonl', 'r') #conala-mined.jsonl
    jsonl_file_array = []
    mined_count = 0
    for info in jsonl_file:
        '''if mined_count >= 500000:
            break'''
        temp_json = json.loads(info)
        jsonl_file_array.append(temp_json)
        mined_count += 1
    json_to_text(jsonl_file_array)

elif num == '4':
    #JSON to text files
    x_file = open('conala-test.json', 'r')
    x_file_array = json.load(x_file)
    y_file = open('conala-train.json', 'r')
    y_file_array = json.load(y_file)
    train_output_intent = []
    train_output_snippet = []
    test_output_intent = []
    test_output_snippet = []
    for x_data in x_file_array:
        train_output_intent.append(x_data['intent'])
        train_output_snippet.append(x_data['snippet'])
    for y_data in y_file_array:
        test_output_intent.append(y_data['intent'])
        test_output_snippet.append(y_data['snippet'])

    with open('train-intent.txt', 'w', encoding='utf-8') as filehandle:
        filehandle.writelines("%s\n" % text for text in train_output_intent)

    with open('train-snippet.txt', 'w', encoding='utf-8') as filehandle:
        filehandle.writelines("%s\n" % text for text in train_output_snippet)

    with open('test-intent.txt', 'w', encoding='utf-8') as filehandle:
        filehandle.writelines("%s\n" % text for text in test_output_intent)

    with open('test-snippet.txt', 'w', encoding='utf-8') as filehandle:
        filehandle.writelines("%s\n" % text for text in test_output_snippet)
else:
    print("Choose 1, 2, or 3")
