text_file = open('preTransProcessedSnippets.txt', 'r')
text_array_1 = text_file.readlines()
text_array_2 = []
count = 0
for text in text_array_1:
    if count > 160000:
        break
    if count % 2 == 1:
        text_array_2.append(text)
    count += 1
with open('python-snippets.txt', 'w', encoding='utf-8') as filehandle:
    filehandle.writelines(text_array_2)