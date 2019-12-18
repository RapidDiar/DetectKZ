import pandas as pd
import os, glob

path = os.getcwd()
os.chdir(path+'/Excel')
word_list = ['source','edited','edited_1']
words = [[],[],[]]
word_dict = {}
for i in glob.glob('*.xlsx'):
    excel_read = pd.read_excel(i,sheet_name='Sheet1')
    for z in range(len(word_list)):
        for x in excel_read.index:
            words[z].append(excel_read[word_list[z]][x])

for i in range(len(word_list)):
    word_dict[word_list[i]] = words[i]

datf = pd.DataFrame(word_dict)
print(datf)
excel_write = datf.to_excel(r'All_in_one.xlsx',index=None,header=True)
