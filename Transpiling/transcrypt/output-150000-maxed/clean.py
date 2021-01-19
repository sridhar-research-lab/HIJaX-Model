#text_file = open('Output.txt', 'r')
#text_file_2 = open('preTransProcessedIntents.txt', 'r')
text_file_3 = open('preTransProcessedSnippets.txt', 'r')

#text_array = text_file.readlines()
#text_array_2 = text_file_2.readlines()
text_array_py = text_file_3.readlines()
text_array_py_2 = []
for i in range(len(text_array_py)):
    if i % 2 == 1:
        text_array_py_2.append(text_array_py[i])

#text_array_3 = []
#text_array_4 = []
#text_array_5 = []
#cnt = 0
'''for text, text2, text3 in zip(text_array, text_array_2, text_array_py_2):
    if 'export' not in text:
        if text != '\n' and text2 != '\n' and text3 != '\n':
            text_array_3.append(text)
            text_array_4.append(text2)
            text_array_5.append(text3)'''
'''with open('final_snippet.txt', 'w') as filehandle:
    for item in text_array_3:
        filehandle.write(item)
with open('final_intent.txt', 'w') as filehandle:
    for item in text_array_4:
        filehandle.write(item)'''
with open('final_snippet_py.txt', 'w') as filehandle:
    for item in text_array_py_2:
        filehandle.write(item)