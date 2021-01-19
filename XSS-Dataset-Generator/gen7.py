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
        del WORDS[index]
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



replace_2 = ['Replace all occurrences of a String \'var0\' with \'var1\'']
replace_2_code = 'str = str.split(\'var0\').join(\'var1\');'  # var, num

for a in replace_2:
    for b in range(40):
        val0 = str(get_all_3())
        val1 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(replace_2_code.replace('var0', val0).replace('var1', val1))



remove_prop_2 = ['Remove the property \'var0\' from an object \'var1\'']
remove_prop_2_code = 'delete var1[\'var0\'];'  # var0
for a in remove_prop_2:
    for b in range(40):
        val0 = get_var()
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(remove_prop_2_code.replace('var0', val0).replace('var1', val1))


for_console_2 = ['Loop through all the items in array \'var0\' and log each entry to the console']
for_console_2_code = 'for (index = 0; index < var0.length; ++index){console.log(var0[index]);}'
for a in for_console_2:
    for b in range(40):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(for_console_2_code.replace('var0', val0))



check_prop = ['check if an object property \'var0\' exists in an object \'var1\'']
check_prop_code = 'var1.hasOwnProperty(var0)'
for a in check_prop:
    for b in range(40):
        val0 = get_var()
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(check_prop_code.replace('var0', val0).replace('var1', val1))


contain_key_2 = ['check if any array of objects \'var0\' contains the key value \'var1\'']
contain_key_2_code = 'var0.filter(var0 => var0.Name === \'var1\')'
for a in contain_key_2:
    for b in range(40):
        val0 = get_var()
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(contain_key_2_code.replace('var0', val0).replace('var1', val1))


if len(intents) == len(snippets):
    with open("intent-benign-so-high-200.txt", "w") as output:
        output.writelines("%s\n" % i for i in intents)
    with open("snippet-benign-so-high-200.txt", "w") as output:
        output.writelines("%s\n" % i for i in snippets)
else:
    print('intents and snippets are not the same size')