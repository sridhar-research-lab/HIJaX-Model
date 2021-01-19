import requests
import random

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
js_keywords = ['break','byte','case','catch','char','class','const','continue','debugger','default','delete','do','double','else','enum','eval','export','extends','false','final','finally','float','for','function','goto','if','implements','import','in','instanceof','int','interface','let','long','native','new','null','package','private','protected','public','return','short','static','super','switch','synchronized','this','throw','throws','transient','true','try','typeof','var','void','volatile','while','with','yield']
response = requests.get(word_site)
WORDS = response.content.splitlines()
intents = []
snippets = []
tags = []
alpha = 'abcdefghijklmnopqrstuvwxyz'
illegal = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
def get_var():
    while True:
        index = random.randint(0, len(WORDS) - 1)
        word = WORDS[index].decode('UTF-8')
        del WORDS[index]
        if bool([ele for ele in illegal if(ele in word)]):
            continue
        if ' ' in word:
            continue
        if word[0].lower() not in alpha and word[0] != '_':
            continue
        if word in js_keywords:
            continue
        return word

while len(tags) < 7:
    tag = get_var()
    if(len(tag) > 3):
        continue
    tags.append(tag)

console_log = ['print var0', 'log that says var0', 'write var0 to browser console']
console_log_code = 'console.log("var0");'
for i in range(9):
    val0 = get_var()
    for a in console_log:
        for c in range(8):
            if c == 0:
                intents.append(a.replace('var0', val0))
                snippets.append(console_log_code.replace('var0', val0+'-'+tags[0]))
            else:
                intents.append(a.replace('var0', val0+'-'+tags[c-1]))
                snippets.append(console_log_code.replace('var0', val0+'-'+tags[c-1]))


'''for a, b in zip(intents, snippets):
    print('intent:', a, '| snippet:', b)
print(len(intents))'''
if len(intents) == len(snippets):
    with open("intent-benign-low-200.txt", "w") as output:
        output.writelines("%s\n" % i for i in intents)
    with open("snippet-benign-low-200.txt", "w") as output:
        output.writelines("%s\n" % i for i in snippets)
else:
    print('intents and snippets are not the same size')
