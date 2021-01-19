text_file = open('initialPythonSnippets.txt', 'r', encoding='utf-8')
text_array_1 = text_file.readlines()
text_array_2 = []
count = 0
for text in text_array_1:
    if count > 230715:
        break
    text_array_2.append(text)
    count += 1
with open('initialPythonSnippets-2.txt', 'w', encoding='utf-8') as filehandle:
    filehandle.writelines(text_array_2)