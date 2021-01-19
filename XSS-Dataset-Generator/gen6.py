import requests
import random

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
js_keywords = ['break', 'byte', 'case', 'catch', 'char', 'class', 'const', 'continue', 'debugger', 'default', 'delete',
               'do', 'double', 'else', 'enum', 'eval', 'export', 'extends', 'false', 'final', 'finally', 'float', 'for',
               'function', 'goto', 'if', 'implements', 'import', 'in', 'instanceof', 'int', 'interface', 'let', 'long',
               'native', 'new', 'null', 'package', 'private', 'protected', 'public', 'return', 'short', 'static',
               'super', 'switch', 'synchronized', 'this', 'throw', 'throws', 'transient', 'true', 'try', 'typeof',
               'var', 'void', 'volatile', 'while', 'with', 'yield']
response = requests.get(word_site)
WORDS = response.content.splitlines()
intents = []
snippets = []
alpha = 'abcdefghijklmnopqrstuvwxyz'
illegal = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.',
           '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']


def get_var():
    while True:
        index = random.randint(0, len(WORDS) - 1)
        word = WORDS[index].decode('UTF-8')
        # del WORDS[index]
        if bool([ele for ele in illegal if (ele in word)]):
            continue
        if ' ' in word:
            continue
        if word[0].lower() not in alpha and word[0] != '_':
            continue
        if word in js_keywords:
            continue
        return word


def get_str():
    index = random.randint(0, len(WORDS) - 1)
    word = WORDS[index].decode('UTF-8')
    del WORDS[index]
    word = '"' + word + '"'
    return word


def get_int():
    val = random.randint(1, 500)
    return val


def get_bool():
    val = random.randint(0, 1)
    if val == 0:
        return 'true'
    else:
        return 'false'


def get_all():
    val = random.randint(1, 4)
    if val == 1:
        temp1 = get_int()
        return temp1
    if val == 2:
        temp2 = get_var()
        return temp2
    if val == 3:
        temp3 = get_str()
        return temp3
    if val == 4:
        temp4 = get_bool()
        return temp4


def get_all_1():
    val = random.randint(1, 3)
    if val == 1:
        temp1 = get_int()
        return temp1
    if val == 2:
        temp2 = get_var()
        return temp2
    if val == 3:
        temp3 = get_bool()
        return temp3


def get_all_2():
    val = random.randint(1, 3)
    if val == 1:
        temp1 = get_int()
        return temp1
    if val == 2:
        temp2 = get_var()
        return temp2
    if val == 3:
        temp3 = get_str()
        return temp3


def get_all_3():
    val = random.randint(1, 2)
    if val == 1:
        temp1 = get_int()
        return temp1
    if val == 2:
        temp2 = get_var()
        return temp2


def get_all_4():
    val = random.randint(1, 2)
    if val == 1:
        temp1 = get_str()
        return temp1
    if val == 2:
        temp2 = get_var()
        return temp2


import_nodejs = ['Import the Node.js module \'var0\'']
import_nodejs_code = 'const myModule = require(\'./var0\');'  # var0
for a in import_nodejs:
    for b in range(200):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(import_nodejs_code.replace('var0', val0))


if len(intents) == len(snippets):
    with open("intent-benign-so-low-200.txt", "w") as output:
        output.writelines("%s\n" % i for i in intents)
    with open("snippet-benign-so-low-200.txt", "w") as output:
        output.writelines("%s\n" % i for i in snippets)
else:
    print('intents and snippets are not the same size')