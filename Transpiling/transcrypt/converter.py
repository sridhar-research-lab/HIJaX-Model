
import os
import re
import locale
import ast
import time
import json

test = open('./conala/conala-test.json',)
train = open('./conala/conala-test.json',)

data_1 = json.load(test)
data_2 = json.load(train)
intentsArr = []
snippetsArr = []
cnt = 0

for i in data_1:
    intentsArr.append(i['intent'])
    snippetsArr.append(i['snippet'])

for i in data_2:
    intentsArr.append(i['intent'])
    snippetsArr.append(i['snippet'])
# stream = os.popen('echo Returned output')
# output =  stream.read()
# print(output)

print(snippetsArr)

def is_valid_python(code):
   try:
       ast.parse(code)
   except SyntaxError:
       return False
   return True

#add Python snippets to file for transpiling
with open ('./conala/dummyIntents.txt','r', encoding='utf-8', errors='ignore') as initialIntents, open ('./conala/dummySnippets.txt','r', encoding='utf-8') as initialSnippets:
    with open ('./preTransProcessedIntents.txt', 'w') as processedIntents, open('./preTransProcessedSnippets.txt', 'w') as processedSnippets:
        #initialIntentLine = initialIntents.readline()
        #initialSnippetLine = initialSnippets.readline()
        initialIntents = intentsArr[cnt]
        initialSnippets = snippetsArr[cnt]
        initialIntentLine = initialIntents
        initialSnippetLine = initialSnippets
        count = 0
        while initialSnippetLine:
            print('COUNTER:', cnt)
            cnt = cnt + 1
            #print(initialIntentLine)
            #print(initialSnippetLine)
            #print('processing snippet %s: ' %count + initialSnippetLine)
            #
            # Check for invalid/non-ascii characters
            #
            try:
                mynewstring = initialSnippetLine.encode('ascii')
                print('is ascii')
            except UnicodeEncodeError:
                print("there are non-ascii characters in there - ommitting line %s in output file" %count)
                initialIntentLine = initialIntents #initialIntents.readline()
                initialSnippetLine = initialSnippets #initialSnippets.readline()
                count += 1
                continue
            #
            # Remove in-line comments
            #
            initialSnippetLine = re.sub('#SPACE#',' ',initialSnippetLine)
            initialSnippetLine = re.sub('#NEWLINE#','\n', initialSnippetLine)
            initialSnippetLine = re.sub('#INDENT#','    ', initialSnippetLine)

            #
            # Removes 'return'  & 'del' for lines beginning with return and del statements
            #
            '''if (initialSnippetLine.startswith('return')):
                initialSnippetLine = initialSnippetLine.replace('return ', '', 1)
            
            if (initialSnippetLine.startswith('del ')):
                initialSnippetLine = initialSnippetLine.replace('del ', 'delete', 1)
            if ('super\n' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('super ' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('super(' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('super[' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('super{' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('super)' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('super]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('super}' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('super,' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('super/' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('yield\n' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('yield ' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('yield(' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('yield[' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('yield{' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('yield)' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('yield]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('yield}' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('yield,' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('yield/' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('pass\n' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('pass ' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if (initialSnippetLine.startswith('global ')):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('property(' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if (initialSnippetLine.startswith('type()')):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('import ' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('3' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('function' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('None' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('export' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('var\n' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('var ' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('var(' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('var[' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('var{' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('var)' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('var]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('var}' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('var,' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('var/' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('var.' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('(enum)' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('break' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if('np.maximum.accumulate((A2 < 0)[:, ::-1], axis=1)[:, ::-1]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if('self.myList = (self.myList + [0] * 4)[:4]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('lid = x.dot(np.append(1, (x.max(0) + 1)[::-1][:-1].cumprod())[::-1])' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('df[(id.cumsum() == 1)[:-2]]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('it = pool.imap_unordered(do, glob.iglob(aglob), chunksize=100)' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('out = x[sidx[(np.convolve(mask, [1, 1]) > 1)[1:-1]]]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('package' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('[...]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('(2)[(customer, 0.0171786268847), (footfall, 0.012)]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('this ' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('spsolve(coeff_mat.tocsr(), const).reshape((-1, 1))' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('(100)[0, 255, 0]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('((s + s.shift(-1)) / 2)[::2]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue

            if ('const ' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue

            if (')[1, 2]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue

            if ('rows = np.repeat(tmp_range, (tmp_range + 1)[::-1])' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue

            if ('.__mul__' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue

            if ('hdf = (pd.DataFrame(prtns) / pd.DataFrame(h).cummax()[1:len(h)] - 1)[1:len(h)]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue

            if ('(50)[255, 255, 0]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue

            if ('set(s)' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue

            if ('(np.cumsum(A2[:, ::-1] < 0, 1) > 0)[:, ::-1]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('list(filter((2).__ne__, x))' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if('print((42).__doc__)'in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('p.map(do, list(range(start_i, end_i)))' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('(0).__class__' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('Iterable([1, 2, 1, 2, 1, 2]).filter((1).__eq__)[:2].as_list()' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('print(netifaces.ifaddresses(interface)[netifaces.AF_INET])' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('(1)[action, romance, comedy]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if('(0)[255, 0, 0]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('(11)[Tom, Tim]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue

            if ('debugger.reset()' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('interface' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue

            if ('(0)[FEB, MAR, APR, NOV]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue

            if ('(0)[a, b]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue

            if ('(2)[a, b]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('(1)[' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('continue' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('break' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('(5).bit_length()' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('samples = np.ascontiguousarray(a).view(dtype((void, a.strides[0])))' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('(7)[JAN, FEB, APR, JUL, OCT, NOV, DEC]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('(2)[4, 1](1, 4)' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('static' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('(5)[0, 10][2, 2]' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('return' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('private' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('SF, NYG' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('(0)[1, 0](2, 1)' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('void' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('debugger' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('(9)[1, 0](4, 5)' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('0)[' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('1)[' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('2)[' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('3)[' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('4)[' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('5)[' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('6)[' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('7)[' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('8)[' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('9)[' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('extends' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('do.call' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('print(const.A, const.B, const.C)' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('printer(let, secgen)' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('catch' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('delete(A, B, C)' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('public' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('do\n' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('do ' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if (' do ' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('do,' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('do(' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('do[' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('do{' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('implements' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue
            if ('const.' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue'''
            '''if ('x, x' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue'''
            '''if ('range()' in initialSnippetLine):
                initialIntentLine = initialIntents.readline()
                initialSnippetLine = initialSnippets.readline()
                count += 1
                continue'''

            #
            # Checks for valid Python Syntax
            #
            if (is_valid_python(initialSnippetLine)):
                print('valid')
                
                processedSnippets.write('delimiter\n')
                processedSnippets.write('%s' %initialSnippetLine)
                processedIntents.write('%s' %initialIntentLine)
                
            else:
                print('invalid') 
            
            
            # next line
            initialIntentLine = initialIntents #initialIntents.readline()
            initialSnippetLine = initialSnippets #initialSnippets.readline()
            count += 1
    

# Create the Py file with filtered snippets
with open('./preTransProcessedSnippets.txt','r', encoding='utf-8') as infile, open('./P2JSnippets.py','w') as P2J:
    line = infile.readline()
    while line:
        P2J.write('%s' %line)
        
        line = infile.readline()

#
# Trancrypt Python to JavaScript
#
print(locale.getpreferredencoding())
os.system('transcrypt ./P2JSnippets.py')


while not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)))):
    print('not ready')
    time.sleep(10)

print('#######################################################')
#
# Parse the transpiled JavaScript to create the final .snippet file (Output.txt) that corresponds to preTransProccessedIntent.txt
#
with open (os.path.join(os.path.dirname(os.path.abspath(__file__)), '__target__\P2JSnippets.js'), 'r') as infile, open('Output.txt', 'w') as outfile:
    data = infile.read()
    data = data.replace('\r','').replace('\n','').split('delimiter;')
    data.pop(0)
    print(data[-1])
    data[-1] = data[-1].replace('//# sourceMappingURL=P2JSnippets.map', '')
    print(data[-1])

    for line in data:
        outfile.write(line + "\n")
    print('done')