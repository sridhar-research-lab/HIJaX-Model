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
        #del WORDS[index]
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

replace = ['Replace all occurrences of String \'var0\' with String \'var1\' using REGEX']
replace_code = 'anotherString = someString.replace(/var0/g, \'var1\');' #var, num
for a in replace:
    for b in range(4):
        val0 = get_var()
        val1 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(replace_code.replace('var0', val0).replace('var1', val1))

replace_2 = ['Replace all occurrences of a String \'var0\' with \'var1\'']
replace_2_code = 'str = str.split(\'var0\').join(\'var1\');' #var, num

for a in replace_2:
    for b in range(4):
        val0 = str(get_all_3())
        val1 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(replace_2_code.replace('var0', val0).replace('var1', val1))

replace_3 = ['Replace the first occurrences of a String \'var0\' with \'var1\'']
replace_3_code = 'str = str.replace(\'var0\', \'var1\');'

for a in replace_3:
    for b in range(4):
        val0 = str(get_all_3())
        val1 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(replace_3_code.replace('var0', val0).replace('var1', val1))

contain = ['Check if the String in variable \'var0\' contains the String in variable \'var1\'']
contain_code = 'var c = var0.includes(var1);'

for a in contain:
    for b in range(4):
        val0 = get_var()
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(contain_code.replace('var0', val0).replace('var1', val1))

index_of_sub = ['Return the index of the substring \'var0\' in the String \'var1\'']
index_of_sub_code = 'var c = var1.indexOf(var0) !== -1;'

for a in index_of_sub:
    for b in range(4):
        val0 = get_var()
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(index_of_sub_code.replace('var0', val0).replace('var1', val1))

check_sub = ['Check if the String in variable \'var0\' contains the substring \'var1\'']
check_sub_code = 'var c = var0.search(\'var1\') !== -1;' #var0
for a in check_sub:
    for b in range(4):
        val0 = get_var()
        val1 = str(get_all_3())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(check_sub_code.replace('var0', val0).replace('var1', val1))

remove_prop = ['Remove the property \'var0\' from an object \'var1\'']
remove_prop_code = 'delete var1.var0;' #var0
for a in remove_prop:
    for b in range(4):
        val0 = get_var()
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(remove_prop_code.replace('var0', val0).replace('var1', val1))

remove_prop_2 = ['Remove the property \'var0\' from an object \'var1\'']
remove_prop_2_code = 'delete var1[\'var0\'];' #var0
for a in remove_prop_2:
    for b in range(4):
        val0 = get_var()
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(remove_prop_2_code.replace('var0', val0).replace('var1', val1))

remove_prop_3 = ['Remove the property \'regex\' at index 3 in object \'var0\'']
remove_prop_3_code = 'var0.splice(3,1);' #var0
for a in remove_prop_3:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(remove_prop_3_code.replace('var0', val0))

import_nodejs = ['Import the Node.js module \'var0\'']
import_nodejs_code = 'const myModule = require(\'./var0\');' #var0
for a in import_nodejs:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(import_nodejs_code.replace('var0', val0))

for_console = ['Loop through all the items in array \'var0\' and log each entry to the console']
for_console_code = 'var0.forEach(function(entry){console.log(entry);});'
for a in for_console:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(for_console_code.replace('var0', val0))

for_console_2 = ['Loop through all the items in array \'var0\' and log each entry to the console']
for_console_2_code = 'for (index = 0; index < var0.length; ++index){console.log(var0[index]);}'
for a in for_console_2:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(for_console_2_code.replace('var0', val0))

for_console_3 = ['Loop through all the items in array \'var0\' and log each entry to the console']
for_console_3_code = 'for (const val of var0){console.log(val);}'
for a in for_console_3:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(for_console_3_code.replace('var0', val0))

check_arr = ['Check if an array includes string \'var0\'']
check_arr_code = '[\'joe\', \'jane\', \'mary\'].includes(\'var0\');'
for a in check_arr:
    for b in range(4):
        val0 = str(get_all_3())
        intents.append(a.replace('var0', val0))
        snippets.append(check_arr_code.replace('var0', val0))

check_arr_2 = ['Check if an array \'var0\' includes integer \'var1\'']
check_arr_2_code = 'var0.includes(var1);'
for a in check_arr_2:
    for b in range(4):
        val0 = get_var()
        val1 = str(get_int())
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(check_arr_2_code.replace('var0', val0).replace('var1', val1))

to_bool = ['Convert object \'var0\' to boolean']
to_bool_code = 'var c = !!var0;'
for a in to_bool:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(to_bool_code.replace('var0', val0))

check_empty = ['Check if the object \'var0\' is empty']
check_empty_code = 'Object.keys(var0).length === 0 && var0.constructor === Object'
for a in check_empty:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(check_empty_code.replace('var0', val0))

check_exist = ['Check if the key \'var0\' exists in the object \'var1\'']
check_exist_code = '\'var0\' in var1'
for a in check_exist:
    for b in range(4):
        val0 = get_var()
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(check_exist_code.replace('var0', val0).replace('var1', val1))

print_pair = ['print key-value pairs of an object \'var0\'']
print_pair_code = 'for (var key in var0){ if (var0.hasOwnProperty(key)){ console.log(key + ' ' + var0[key]);}}'
for a in print_pair:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(print_pair_code.replace('var0', val0))

get_length = ['get length of an object \'var0\'']
get_length_code = 'var size = Object.keys(var0).length'
for a in get_length:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(get_length_code.replace('var0', val0))

get_length_2 = ['get length of an object \'var0\'']
get_length_2_code = 'Object.keys(var0).length'
for a in get_length_2:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(get_length_2_code.replace('var0', val0))

insert_arr = ['insert the string \'var0\' into the array \'var1\' at index 2']
insert_arr_code = 'var1.splice(2,0,\'var0\');'
for a in insert_arr:
    for b in range(4):
        val0 = str(get_all_3())
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(insert_arr_code.replace('var0', val0).replace('var1', val1))

merge_obj = ['merge object \'var0\' with object \'var1\'']
merge_obj_code = 'Object.assign(var0, var1)'
for a in merge_obj:
    for b in range(4):
        val0 = get_var()
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(merge_obj_code.replace('var0', val0).replace('var1', val1))

time_out = ['wait \'var0\' milliseconds to call function \'var1\'']
time_out_code = 'setTimeout(var1, var0);'
for a in time_out:
    for b in range(4):
        val0 = str(get_int())
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(time_out_code.replace('var0', val0).replace('var1', val1))

append_arr = ['append string \'var0\' to array \'var1\'']
append_arr_code = 'var1.push(\'var0\');'
for a in append_arr:
    for b in range(4):
        val0 = str(get_all_3())
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(append_arr_code.replace('var0', val0).replace('var1', val1))

append_arr_2 = ['append string \'var0\' and string \'var1\' to array \'var2\'']
append_arr_2_code = 'var2.push(\'var0\',\'var1\');'
for a in append_arr_2:
    for b in range(4):
        val0 = str(get_all_3())
        val1 = str(get_all_3())
        val2 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1).replace('var2', val2))
        snippets.append(append_arr_2_code.replace('var0', val0).replace('var1', val1).replace('var2', val2))

append_arr_3 = ['append array \'var0\' to array \'var1\'']
append_arr_3_code = 'var1.concat(var0)'
for a in append_arr_3:
    for b in range(4):
        val0 = get_var()
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(append_arr_3_code.replace('var0', val0).replace('var1', val1))

is_arr = ['check if object \'var0\' is an array']
is_arr_code = 'Array.isArray(var0)'
for a in is_arr:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(is_arr_code.replace('var0', val0))

loop_obj = ['loop through the objects contained in object \'var0\'']
loop_obj_code = 'Object.keys(var0).forEach(function(key){});'
for a in loop_obj:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(loop_obj_code.replace('var0', val0))

count_obj = ['count the number of keys in an object \'var0\'']
count_obj_code = 'Object.keys(var0).length'
for a in count_obj:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(count_obj_code.replace('var0', val0))

count_obj_2 = ['count the number of keys in an object \'var0\'']
count_obj_2_code = 'for (var k in var0){ if(var0.hasOwnProperty(k)) ++count; }'
for a in count_obj_2:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(count_obj_2_code.replace('var0', val0))

to_hex_str = ['convert decimal \'var0\' to a hexadecimal string']
to_hex_str_code = 'hexString = var0.toString(16)'
for a in to_hex_str:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(to_hex_str_code.replace('var0', val0))

to_hex_str_2 = ['convert a hexadecimal string \'var0\' to an integer']
to_hex_str_2_code = 'yourNumber = parseInt(var0, 16);'
for a in to_hex_str_2:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(to_hex_str_2_code.replace('var0', val0))

para_from_url = ['get the parameter \'var0\' from url \'var1\'']
para_from_url_code = 'var1.searchParams.get(\'var0\')'
for a in para_from_url:
    for b in range(4):
        val0 = get_var()
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(para_from_url_code.replace('var0', val0).replace('var1', val1))

timing = ['measure the time taken for the function \'var0()\' to execute as \'var1\'']
timing_code = 'var t0 = performance.now(); var0(); var t1 = performance.now(); var var1 = t1 - t0;'
for a in timing:
    for b in range(4):
        val0 = get_var()
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(timing_code.replace('var0', val0).replace('var1', val1))

compare_str = ['case insensitive compare string \'var0\' to string \'var1\'']
compare_str_code = 'var0.toUpperCase() === var1.toUpperCase()'
for a in compare_str:
    for b in range(4):
        val0 = get_var()
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(compare_str_code.replace('var0', val0).replace('var1', val1))

replace_html = ['parse string \'var0\' into JSON']
replace_html_code = 'JSON.parse(var0)'
for a in replace_html:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(replace_html_code.replace('var0', val0))
        
obj_prop = ['list the properties of the object \'var0\'']
obj_prop_code = 'Object.keys(var0)'
for a in obj_prop:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(obj_prop_code.replace('var0', val0))
        
sort_arr = ['sort the integer array \'var0\'']
sort_arr_code = 'var0.sort((a, b) => a - b)'
for a in sort_arr:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(sort_arr_code.replace('var0', val0))
        
sum_arr = ['find the sum of array \'var0\' within initial value 0']
sum_arr_code = 'var0.reduce((a,b) => a + b, 0)'
for a in sum_arr:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(sum_arr_code.replace('var0', val0))
        
seperate = ['convert comma \',\' separated items in string \'var0\' to an array']
seperate_code = 'var0.split(\',\')'
for a in seperate:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(seperate_code.replace('var0', val0))
        
       
check_prop = ['check if an object property \'var0\' exists in an object \'var1\'']
check_prop_code = 'var1.hasOwnProperty(var0)'
for a in check_prop:
    for b in range(4):
        val0 = get_var()
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(check_prop_code.replace('var0', val0).replace('var1', val1))

check_prop_2 = ['check if an object property \'var0\' exists in an object \'var1\'']
check_prop_2_code = '\'var0\' in var1'
for a in check_prop_2:
    for b in range(4):
        val0 = str(get_all_3())
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(check_prop_2_code.replace('var0', val0).replace('var1', val1))
        
contain_key = ['check if any array of objects \'var0\' contains the key value \'var1\'']
contain_key_code = 'vendors.filter(function(var0){ return vendor.Name === \'var1\' })'
for a in contain_key:
    for b in range(4):
        val0 = get_var()
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(contain_key_code.replace('var0', val0).replace('var1', val1))

contain_key_2 = ['check if any array of objects \'var0\' contains the key value \'var1\'']
contain_key_2_code = 'var0.filter(var0 => var0.Name === \'var1\')'
for a in contain_key_2:
    for b in range(4):
        val0 = get_var()
        val1 = get_var()
        intents.append(a.replace('var0', val0).replace('var1', val1))
        snippets.append(contain_key_2_code.replace('var0', val0).replace('var1', val1))
        
round_prec = ['round floating point \'var0\' to 15 significant digits']
round_prec_code = 'parseFloat(var0).toPrecision(15)'
for a in round_prec:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(round_prec_code.replace('var0', val0))
        
get_prop = ['access the first property of an object \'var0\'']
get_prop_code = 'var0[Object.keys(var0)[0]]'
for a in get_prop:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(get_prop_code.replace('var0', val0))
        
get_prop_2 = ['access the first property of an object \'var0\'']
get_prop_2_code = 'Object.values(var0)[0]'
for a in get_prop_2:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(get_prop_2_code.replace('var0', val0))
        
first_char = ['get the first character of string \'var0\'']
first_char_code = 'var0.charAt(0)'
for a in first_char:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(first_char_code.replace('var0', val0))

first_char_2 = ['get the first character of string \'var0\'']
first_char_2_code = 'var0.substring(0, 1)'
for a in first_char_2:
    for b in range(4):
        val0 = get_var()
        intents.append(a.replace('var0', val0))
        snippets.append(first_char_2_code.replace('var0', val0))

if len(intents) == len(snippets):
    with open("intent-benign-so-very-high-200.txt", "w") as output:
        output.writelines("%s\n" % i for i in intents)
    with open("snippet-benign-so-very-high-200.txt", "w") as output:
        output.writelines("%s\n" % i for i in snippets)
else:
    print('intents and snippets are not the same size')