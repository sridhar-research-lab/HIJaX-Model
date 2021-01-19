import json
import random
import math
import spacy
import re
from randomwordgenerator import randomwordgenerator

score = 0
entries = 0
nlp = spacy.load('en')
escape_dict={'\a':r'\a',
           '\b':r'\b',
           '\c':r'\c',
           '\f':r'\f',
           '\n':r'\n',
           '\r':r'\r',
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

def canonicalize_intent(intent):
    s = set()
    slot_map_old = dict()
    QUOTED_STRING_RE = re.compile(r"(?P<quote>[`'\"])(?P<string>.*?)(?P=quote)")
    str_matches_1 = QUOTED_STRING_RE.findall(intent)
    for i in range(len(str_matches_1)):
        s.add(str_matches_1[i][1])
    URL_STRING_RE = re.compile(r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))""")
    str_matches_2 = URL_STRING_RE.findall(intent)
    for i in range(len(str_matches_2)):
        s.add(str_matches_2[i])
    clean_file_1_line = intent
    for cur_word in s:
        clean_file_1_line = clean_file_1_line.replace(cur_word, "")
    doc = nlp(clean_file_1_line.strip())
    cleaned = [y for y in doc if not y.is_stop and y.pos_ != 'PUNCT']
    raw = [(x.lemma_, x.pos_) for x in cleaned]
    clean_raw = []
    for i in range(len(raw)):
        if raw[i][1] == 'PROPN':
            s.add(raw[i][0])
        else:
            clean_raw.append(raw[i])
    add_flag = False
    for i in range(len(clean_raw)):
        if add_flag:
            s.add(clean_raw[i][0])
        if len(clean_raw) >= 3 and clean_raw[i][1] == 'VERB' and i > 0 and len(clean_raw) == (i + 2):
            add_flag = True
    var_num = 0
    #unique_words = set()
    for val in s:
        #str_val = randomwordgenerator.generate_random_words(1)
        #while (str_val in unique_words) or (str_val in val):
            #str_val = randomwordgenerator.generate_random_words(1)
        slot_map_old[val] = 'var' + str(var_num)
        var_num = var_num + 1
        #unique_words.add(str_val)
        #slot_map_old[val] = str_val
    intent = intent.replace('\'', '')
    intent = intent.replace('\"', '')
    intent = intent.replace('`', '')
    intent_arr = intent.split()
    for key in slot_map_old:
        for i in range(len(intent_arr)):
            if key == intent_arr[i]:
                intent_arr[i] = slot_map_old[key]
    intent = " ".join(intent_arr)
    slot_map = dict()
    for key in slot_map_old:
        val = slot_map_old[key]
        if 'https://www.' in key:
            key = key.replace('https://www.', '')
        if 'http://www.' in key:
            key = key.replace('http://www.', '')
        '''if 'www.' in key:
            key = key.replace('www.', '')'''
        slot_map[key] = val
    return intent, slot_map, slot_map_old

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

    output_json_file = open('trainJSON-simple.json', 'w')
    json_string = "["
    for i in range(len(test_arr)):
        if (i < len(test_arr) - 1):
            json_string = json_string + str(test_arr[i]) + ","
        else:
            json_string = json_string + str(test_arr[i])
    json_string = json_string + "]"
    output_json_file.write(json_string)
    output_json_file.close()

    output_json_file = open('trainJSON-simple.json', 'w')
    json_string = "["
    for i in range(len(input_json_arr)):
        if (i < len(input_json_arr) - 1):
            json_string = json_string + str(input_json_arr[i]) + ","
        else:
            json_string = json_string + str(input_json_arr[i])
    json_string = json_string + "]"
    output_json_file.write(json_string)
    output_json_file.close()

def no_split(input_json_arr):
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
    global score
    global entries
    if len(text_arr) == len(code_arr):
        json_arr = []
        counter = 0
        for file_1_line, file_2_line in zip(text_arr, code_arr):
            if '\'' in file_1_line:
                file_1_line = file_1_line.replace('\'')
            if '\"' in file_1_line:
                file_1_line = file_1_line.replace('\"')
            if '`' in file_1_line:
                file_1_line = file_1_line.replace('`')
            intent, slot_map, slot_map_old = canonicalize_intent(file_1_line)
            print(intent, slot_map)
            quoted_intent = file_1_line.strip()
            key_list = []
            #key_list_2 = []
            for key in slot_map:
                key_list.append(key)
            '''for key in slot_map_old:
                key_list_2.append(key)'''
            if len(key_list) > 0:
                for i in range(len(key_list)):
                    start = quoted_intent.find(key_list[i])
                    end = start + len(key_list[i])
                    #start_old = quoted_intent.find(key_list_2[i])
                    #end_old = quoted_intent.find(key_list_2[i])
                    '''if (start > 0 and end < len(quoted_intent)):
                        if ((quoted_intent[start-1] == '\'' and quoted_intent[end] == '\'') or (quoted_intent[start-1] == '\"' and quoted_intent[end] == '\"') or (quoted_intent[start-1] == '`' and quoted_intent[end] == '`')):
                            continue'''
                    quoted_intent = quoted_intent[:start] + "\'" + quoted_intent[start:end] + "\'" + quoted_intent[end:]
            json_data = {"intent": quoted_intent, "rewritten_intent": quoted_intent,
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
            intent_str = current_json['intent']
            rewritten_intent_str = current_json['rewritten_intent']
            snippet_str = current_json['snippet']
            if len(intent_str) == 0 or len(rewritten_intent_str) == 0 or len(snippet_str) == 0:
                continue
            '''clean_intent_str = ''
            clean_rewritten_intent_str = ''
            clean_snippet_str = ''
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            digits = '0123456789'
            special = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
            for a in range(len(intent_str)):
                current_char = intent_str[a]
                if ((current_char in digits) or (current_char.lower() in alphabet)) or current_char.isspace() or (current_char in special):
                    clean_intent_str = clean_intent_str + current_char

            for b in range(len(rewritten_intent_str)):
                current_char = rewritten_intent_str[b]
                if ((current_char in digits) or (current_char.lower() in alphabet)) or current_char.isspace() or (current_char in special):
                    clean_rewritten_intent_str = clean_rewritten_intent_str + current_char'''

            #current_json['intent'] = clean_intent_str
            #current_json['rewritten_intent'] = clean_rewritten_intent_str
            #current_json['snippet'] = raw(current_json['snippet'])
            json_data = {"intent": current_json['intent'], "rewritten_intent": current_json['rewritten_intent'],
                         "snippet": current_json['snippet']}
            json_temp = json.dumps(json_data)
            clean_json_arr.append(json_temp)
        #random_split(clean_json_arr, 20)
        no_split(clean_json_arr)
    else:
        print('json is empty')

num = input ("To load from txt files enter (1). To load from a JSON file enter (2):")

if num == '1':
    #load in text files
    text_file = open('./mal-very-high/200_new/train-intent.txt', 'r')
    code_file = open('./mal-very-high/200_new/train-snippet.txt', 'r')

    text_array = text_file.readlines()
    code_array = code_file.readlines()
    json_from_txt(text_array, code_array)
    print('score:', score, '| entries:', entries)
# or

elif num == '2':
    #load in JSON file to be formatted
    json_file = open('testJSON.json', 'r')
    json_file_array = json.load(json_file)

    clean_json_file(json_file_array)

else:
    print("Choose 1 or 2")
