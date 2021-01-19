import requests
import random

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
js_keywords = ['break','byte','case','catch','char','class','const','continue','debugger','default','delete','do','double','else','enum','eval','export','extends','false','final','finally','float','for','function','goto','if','implements','import','in','instanceof','int','interface','let','long','native','new','null','package','private','protected','public','return','short','static','super','switch','synchronized','this','throw','throws','transient','true','try','typeof','var','void','volatile','while','with','yield']
response = requests.get(word_site)
WORDS = response.content.splitlines()
intents = []
snippets = []
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

variables = ['variable named var0 with the value var1','initialize variable var0 with value var1', 'initialize var0 to var1'] #var0 = var, #var1 = var/num/bool (if string add quotes)
variables_code = 'var var0 = var1;'
for a in variables:
    for b in range(139):
        val0 = get_var()
        val1 = str(get_all_1())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(variables_code.replace('var0', val0).replace('var1', val1))
prompts = ['input dialog with text var0', 'input dialog that says var0']
prompts_code = 'prompts("var0","0");'
for a in prompts:
    for b in range(139):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(prompts_code.replace('var0', val0))
yes_no = ['yes/no dialog with text var0', 'yes/no dialog that says var0']
yes_no_code = 'confirm("var0");'
for a in yes_no:
    for b in range(139):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(yes_no_code.replace('var0', val0))
alerts = ['alert that says var0', 'alert with text var0']
alerts_code = 'alert("var0");'
for a in alerts:
    for b in range(139):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(alerts_code.replace('var0', val0))

console_log = ['print var0', 'log that says var0', 'write var0 to browser console']
console_log_code = 'console.log("var0");'
for a in console_log:
    for b in range(139):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(console_log_code.replace('var0', val0))
delay = ['delay for varX seconds', 'pause for varX seconds']
delay_code = 'setTimeout(function () {}, varX000);' #varX = int
for a in delay:
    for b in range(139):
        val0 = str(get_int())
        intents.append(a.replace('varX', val0))
        snippets.append(delay_code.replace('varX', val0))
list_of_len_3 = ['list named var0 containing var1, var2, var3', 'array named var0 containing var1, var2, var3', 'array named var0 of var1, var2, var3', 'list named var0 of var1, var2, var3']
list_of_len_3_code = 'var var0 = [var1, var2, var3];' #if string add quotes
for a in list_of_len_3:
    for b in range(139):
        val0 = get_var()
        val1 = str(get_all())
        val2 = str(get_all())
        val3 = str(get_all())
        intents.append(a.replace('var0', val0).replace('var1', val1.replace('"','')).replace('var2', val2.replace('"','')).replace('var3', val3.replace('"','')))
        snippets.append(list_of_len_3_code.replace('var0', val0).replace('var1', val1).replace('var2', val2).replace('var3', val3))

list_of_len_2 = ['list named var0 containing var1 and var2', 'array named var0 containing var1 and var2', 'array named var0 of var1 and var2', 'list named var0 of var1 and var2']
list_of_len_2_code = 'var var0 = [var1, var2];' #if string add quotes
for a in list_of_len_2:
    for b in range(139):
        val0 = get_var()
        val1 = str(get_all())
        val2 = str(get_all())
        intents.append(a.replace('var0', val0.replace('"','')).replace('var1', val1.replace('"','')).replace('var2', val2.replace('"','')))
        snippets.append(list_of_len_2_code.replace('var0', val0).replace('var1', val1).replace('var2', val2))
add = ['var0 equals var1 plus var2']
add_code = 'var0 = var1 + var2;'
for a in add:
    for b in range(139):
        val0 = get_var()
        val1 = str(get_all_3())
        val2 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1).replace('var2', val2))
        snippets.append(add_code.replace('var0', val0).replace('var1', val1).replace('var2', val2))
subtract = ['var0 equals var1 minus var2']
subtract_code = 'var0 = var1 - var2;'
for a in subtract:
    for b in range(139):
        val0 = get_var()
        val1 = str(get_all_3())
        val2 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1).replace('var2', val2))
        snippets.append(subtract_code.replace('var0', val0).replace('var1', val1).replace('var2', val2))
divide = ['var0 equals var1 divided by var2']
divide_code = 'var0 = var1 / var2;'
for a in divide:
    for b in range(139):
        val0 = get_var()
        val1 = str(get_all_3())
        val2 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1).replace('var2', val2))
        snippets.append(divide_code.replace('var0', val0).replace('var1', val1).replace('var2', val2))
multiple = ['var0 equals var1 multiplied by var2', 'var0 equals var1 times var2']
multiple_code = 'var0 = var1 * var2;'
for a in multiple:
    for b in range(139):
        val0 = get_var()
        val1 = str(get_all_3())
        val2 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1).replace('var2', val2))
        snippets.append(multiple_code.replace('var0', val0).replace('var1', val1).replace('var2', val2))
modulus = ['var0 equals var1 mod var2', 'var0 equals var1 modulus var2', 'var0 equals the remainder of var1 and var2']
modulus_code = 'var0 = var1 % var2;'
for a in modulus:
    for b in range(139):
        val0 = get_var()
        val1 = str(get_all_3())
        val2 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1).replace('var2', val2))
        snippets.append(modulus_code.replace('var0', val0).replace('var1', val1).replace('var2', val2))
increment_1 = ['increment var0 by var1']
increment_1_code = 'var0 = var0 + var1;'
for a in increment_1:
    for b in range(139):
        val0 = get_var()
        val1 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(increment_1_code.replace('var0', val0).replace('var1', val1))
increment_2 = ['increment var0 by 1']
increment_2_code = 'var0++;'
for a in increment_2:
    for b in range(139):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(increment_2_code.replace('var0', val0))
decrement_1 = ['decrement var0 by var1']
decrement_1_code = 'var0 = var0 - var1;'
for a in decrement_1:
    for b in range(139):
        val0 = get_var()
        val1 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(decrement_1_code.replace('var0', val0).replace('var1', val1))
decrement_2 = ['decrement var0 by 1']
decrement_2_code = 'var0--;'
for a in decrement_2:
    for b in range(139):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(decrement_2_code.replace('var0', val0))
typeof = ['get the type of var0', 'find type of var0']
typeof_code = 'typeof var0;'
for a in typeof:
    for b in range(139):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(typeof_code.replace('var0', val0))
equals = ['var0 equals var1']
equals_code = 'var0 = var1;' #string, int, double, bool, var. if string add quotes
for a in equals:
    for b in range(139):
        val0 = get_var()
        val1 = str(get_all())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(equals_code.replace('var0', val0).replace('var1', val1))
not_equals = ['var0 does not equals var1']
not_equals_code = 'var0 != var1' #string, int, double, bool, var. if string add quotes
for a in not_equals:
    for b in range(139):
        val0 = get_var()
        val1 = str(get_all())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(not_equals_code.replace('var0', val0).replace('var1', val1))
compare = ['compare var0 to var1', 'see if var0 equals var1', 'see if var0 and var1 are equal']
compare_code = 'var0 == var1'   #var ,string, num
for a in compare:
    for b in range(139):
        val0 = get_var()
        val1 = str(get_all())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(compare_code.replace('var0', val0).replace('var1', val1))
less_than = ['see if var0 is less than var1', 'is var0 less than var1']
less_than_code = 'var0 < var1'  #var, num
for a in less_than:
    for b in range(139):
        val0 = get_var()
        val1 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(less_than_code.replace('var0', val0).replace('var1', val1))
less_than_equal = ['see if var0 is less than or equal to var1', 'is var0 less than or equal to var1']
less_than_equal_code = 'var0 <= var1' #var, num
for a in less_than_equal:
    for b in range(139):
        val0 = get_var()
        val1 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(less_than_equal_code.replace('var0', val0).replace('var1', val1))
greater_than_equal = ['see if var0 is greater than or equal to var1', 'is var0 greater than or equal to var1']
greater_than_equal_code = 'var0 >= var1' #var, num
for a in greater_than_equal:
    for b in range(139):
        val0 = get_var()
        val1 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(greater_than_equal_code.replace('var0', val0).replace('var1', val1))
greater_than = ['see if var0 is greater than var1', 'is var0 greater than var1']
greater_than_code = 'var0 > var1' #var, num
for a in greater_than:
    for b in range(139):
        val0 = get_var()
        val1 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(greater_than_code.replace('var0', val0).replace('var1', val1))
round = ['round var0']
round_code = 'Math.round(var0);'  #var, num
for a in round:
    for b in range(139):
        val0 = str(get_all_3())
        intents.append(a.replace('var0', val0))
        snippets.append(round_code.replace('var0', val0))

power = ['var0 to the power var1', 'raise var0 to the power var1']
power_code = 'Math.pow(var0,var1);' #var, num
for a in power:
    for b in range(139):
        val0 = str(get_all_3())
        val1 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(power_code.replace('var0', val0).replace('var1', val1))

square = ['square of var0', 'var0 squared']
square_code = 'Math.pow(var0,2);' #var, num
for a in square:
    for b in range(139):
        val0 = str(get_all_3())
        intents.append(a.replace('var0', val0))
        snippets.append(square_code.replace('var0', val0))
square_root = ['square root of var0', 'root of var0']
square_root_code = 'Math.sqrt(var0);'
for a in square_root:
    for b in range(139):
        val0 = str(get_all_3())
        intents.append(a.replace('var0', val0))
        snippets.append(square_root_code.replace('var0', val0))
round_up = ['round up var0']
round_up_code = 'Math.ceil(var0);'  #var, num
for a in round_up:
    for b in range(139):
        val0 = str(get_all_3())
        intents.append(a.replace('var0', val0))
        snippets.append(round_up_code.replace('var0', val0))
round_down = ['round down var0']
round_down_code = 'Math.floor(var0);'  #var, num
for a in round_down:
    for b in range(139):
        val0 = str(get_all_3())
        intents.append(a.replace('var0', val0))
        snippets.append(round_down_code.replace('var0', val0))
sin = ['sin of var0']
sin_code = 'Math.sin(var0);' #var, num
for a in sin:
    for b in range(139):
        val0 = str(get_all_3())
        intents.append(a.replace('var0', val0))
        snippets.append(sin_code.replace('var0', val0))
cos = ['cos of var0']
cos_code = 'Math.cos(var0);' #var, num
for a in cos:
    for b in range(139):
        val0 = str(get_all_3())
        intents.append(a.replace('var0', val0))
        snippets.append(cos_code.replace('var0', val0))
minimum_1 = ['smallest value in var0, var1, var2', 'smallest value of var0, var1, var2', 'lowest value in var0, var1, var2', 'lowest value of var0, var1, var2', 'smallest number in var0, var1, var2', 'smallest number of var0, var1, var2', 'lowest number in var0, var1, var2', 'lowest number of var0, var1, var2']
minimum_1_code= 'Math.min(var0, var1, var2);' #var, num
for a in minimum_1:
    for b in range(139):
        val0 = str(get_all_3())
        val1 = str(get_all_3())
        val2 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1).replace('var2', val2))
        snippets.append(minimum_1_code.replace('var0', val0).replace('var1', val1).replace('var2', val2))
minimum_2 = ['smallest value in var0, var1', 'smallest value of var0, var1', 'lowest value in var0, var1', 'lowest value of var0, var1', 'smallest number in var0, var1', 'smallest number of var0, var1', 'lowest number in var0, var1', 'lowest number of var0, var1']
minimum_2_code= 'Math.min(var0, var1);' #var, num
for a in minimum_2:
    for b in range(139):
        val0 = str(get_all_3())
        val1 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(minimum_2_code.replace('var0', val0).replace('var1', val1))
maximum_1 = ['largest value in var0, var1, var2', 'largest value of var0, var1, var2', 'highest value in var0, var1, var2', 'highest value of var0, var1, var2', 'largest number in var0, var1, var2', 'largest number of var0, var1, var2', 'highest number in var0, var1, var2', 'highest number of var0, var1, var2']
maximum_1_code= 'Math.max(var0, var1, var2);' #var, num
for a in maximum_1:
    for b in range(139):
        val0 = str(get_all_3())
        val1 = str(get_all_3())
        val2 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1).replace('var2', val2))
        snippets.append(maximum_1_code.replace('var0', val0).replace('var1', val1).replace('var2', val2))
maximum_2 = ['largest value in var0, var1', 'largest value of var0, var1', 'highest value in var0, var1', 'highest value of var0, var1', 'largest number in var0, var1', 'largest number of var0, var1', 'highest number in var0, var1', 'highest number of var0, var1']
maximum_2_code= 'Math.max(var0, var1);' #var, num
for a in maximum_2:
    for b in range(139):
        val0 = str(get_all_3())
        val1 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(maximum_2_code.replace('var0', val0).replace('var1', val1))

log_of = ['log of var0', 'find the log of var0', 'take the log of var0', 'find the logarithm of var0', 'take the logarithm of var0']
log_of_code = 'Math.log(var0);' #var, num
for a in log_of:
    for b in range(139):
        val0 = str(get_all_3())
        intents.append(a.replace('var0', val0))
        snippets.append(log_of_code.replace('var0', val0))    
        
exp_of = ['exponential of var0', 'exponent of var0', 'take the exponent of var0', 'find the exponent of var0', 'find the exponential of var0']
exp_of_code = 'Math.exp(var0);' #var, num
for a in exp_of:
    for b in range(139):
        val0 = str(get_all_3())
        intents.append(a.replace('var0', val0))
        snippets.append(exp_of_code.replace('var0', val0))
        
to_num = ['cast string var0 to a number', 'cast var0 to a number', 'convert var0 to a number', 'make var0 a number']
to_num_code = 'Number(var0);' #var, string
for a in to_num:
    for b in range(139):
        val0 = str(get_all_4())
        intents.append(a.replace('var0', val0))
        snippets.append(to_num_code.replace('var0', val0))   

random_list = ['random number between var0 and var1']
random_list_code = 'Math.floor(Math.random() * var1) + var0;' #var, num
for a in random_list:
    for b in range(139):
        val0 = str(get_all_3())
        val1 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(random_list_code.replace('var0', val0).replace('var1', val1))
to_string = ['var0 to string', 'make var0 a string', 'convert var0 to string', 'cast var0 to string', 'make var0 a string']
to_string_code = 'var0.toString();' #var
for a in to_string:
    for b in range(139):
        val0 = str(get_var())
        intents.append(a.replace('var0', val0))
        snippets.append(to_string_code.replace('var0', val0))
length = ['get length of var0', 'get size of var0', 'find the size of var0', 'find the length of var0', 'number of elements in var0']
length_code = 'var0.length;' #var
for a in length:
    for b in range(139):
        val0 = str(get_var())
        intents.append(a.replace('var0', val0))
        snippets.append(length_code.replace('var0', val0))
pop = ['remove last element from var0', 'remove last element of var0']
pop_code = 'var0.pop();' #var
for a in pop:
    for b in range(139):
        val0 = str(get_var())
        intents.append(a.replace('var0', val0))
        snippets.append(pop_code.replace('var0', val0))
shift = ['remove first element from var0', 'remove first element of var0']
shift_code = 'var0.shift();' #var
for a in shift:
    for b in range(139):
        val0 = str(get_var())
        intents.append(a.replace('var0', val0))
        snippets.append(shift_code.replace('var0', val0))
unshift = ['add var0 to the front of var1', 'add var0 to the beginning of var1', 'add var0 as the first element of var1', 'append var0 to the front of var1', 'append var0 to the beginning of var1', 'append var0 as the first element of var1']
unshift_code = 'var1.unshift(var0);' #var1: var , var0: var, string(add quotes)
for a in unshift:
    for b in range(139):
        val1 = get_var()
        val0 = str(get_all_4())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(unshift_code.replace('var0', val0).replace('var1', val1))
sort = ['sort var0', 'sort array var0', 'sort list var0', 'sort var0 in alphabetical order', 'sort var0 in ascending order']
sort_code = 'var0.sort();' #var0
for a in sort:
    for b in range(139):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(sort_code.replace('var0', val0))
reverse = ['reverse var0', 'reverse array var0', 'reverse list var0', 'sort var0 in descending order']
reverse_code = 'var0.reverse();' #var0
for a in reverse:
    for b in range(139):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(reverse_code.replace('var0', val0))
toUpper = ['var0 to uppercase', 'make var0 uppercase', 'convert var0 to uppercase', 'convert string var0 to uppercase']
toUpper_code = 'var0.toUpperCase();' #var0
for a in toUpper:
    for b in range(139):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(toUpper_code.replace('var0', val0))
        
toLower = ['var0 to lowercase', 'make var0 lowercase', 'convert var0 to lowercase', 'convert string var0 to lowercase']
toLower_code = 'var0.toLowerCase();' #var0
for a in toLower:
    for b in range(139):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(toLower_code.replace('var0', val0))

if len(intents) == len(snippets):
    with open("intent-benign-very-high-20000.txt", "w") as output:
        output.writelines("%s\n" % i for i in intents)
    with open("snippet-benign-very-high-20000.txt", "w") as output:
        output.writelines("%s\n" % i for i in snippets)
else:
    print('intents and snippets are not the same size')