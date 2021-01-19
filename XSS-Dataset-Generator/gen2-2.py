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
        #del WORDS[index]
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


'''def get_double():
    val = random.uniform(1,10)
    return val'''


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


console_log = ['print var0', 'log that says var0', 'write var0 to browser console']
console_log_code = 'console.log("var0");'
for a in console_log:
    for b in range(14):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(console_log_code.replace('var0', val0))
delay = ['delay for varX seconds', 'pause for varX seconds']
delay_code = 'setTimeout(function () {}, varX000);'  # varX = int
for a in delay:
    for b in range(14):
        val0 = str(get_int())
        intents.append(a.replace('varX', val0))
        snippets.append(delay_code.replace('varX', val0))
list_of_len_3 = ['list named var0 containing var1, var2, var3', 'array named var0 containing var1, var2, var3',
                 'array named var0 of var1, var2, var3', 'list named var0 of var1, var2, var3']
list_of_len_3_code = 'var var0 = [var1, var2, var3];'  # if string add quotes
for a in list_of_len_3:
    for b in range(14):
        val0 = get_var()
        val1 = str(get_all())
        val2 = str(get_all())
        val3 = str(get_all())
        intents.append(a.replace('var0', val0).replace('var1', val1.replace('"', '')).replace('var2', val2.replace('"','')).replace('var3', val3.replace('"', '')))
        snippets.append(list_of_len_3_code.replace('var0', val0).replace('var1', val1).replace('var2', val2).replace('var3', val3))

power = ['var0 to the power var1', 'raise var0 to the power var1']
power_code = 'Math.pow(var0,var1);'  # var, num
for a in power:
    for b in range(14):
        val0 = str(get_all_3())
        val1 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(power_code.replace('var0', val0).replace('var1', val1))

toLower = ['var0 to lowercase', 'make var0 lowercase', 'convert var0 to lowercase', 'convert string var0 to lowercase']
toLower_code = 'var0.toLowerCase();'  # var0
for a in toLower:
    for b in range(14):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(toLower_code.replace('var0', val0))

if len(intents) == len(snippets):
    with open("intent-benign-high-200.txt", "w") as output:
        output.writelines("%s\n" % i for i in intents)
    with open("snippet-benign-high-200.txt", "w") as output:
        output.writelines("%s\n" % i for i in snippets)
else:
    print('intents and snippets are not the same size')