import pandas as pd
import numpy as np

source = []
edited = []
edited_1 = []

file_source = open('Final/FinalKZ.txt',"r")
file_edited = open('Final/Array_word_match.txt',"r")
file_edited_1 = open('Final/Array_word.txt',"r")

lines_file_source = file_source.readlines()
lines_file_edited = file_edited.readlines()
lines_file_edited_1 = file_edited_1.readlines()

for i in range(len(lines_file_source)):
    source.append(lines_file_source[i].rstrip())
    edited.append(lines_file_edited[i].rstrip())
    edited_1.append(lines_file_edited_1[i].rstrip())

word_data = {}
word_data['source'] = source
word_data['edited'] = edited
word_data['edited_1'] = edited_1

wd = pd.DataFrame(word_data)
print(wd)
txt_to_excel = wd.to_excel(r'Final.xlsx', index=None, header=True)