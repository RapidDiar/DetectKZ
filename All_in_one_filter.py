import pandas as pd
import numpy as np
import os, glob
from itertools import groupby

word = []
word_filter = []
path = os.getcwd()
excel_read = pd.read_excel(path+'/Excel/All_in_one.xlsx',sheet_name='Sheet1')
for i in excel_read.index:
    word.append(excel_read['edited_1'][i])
word_filter = [el for el, _ in groupby(word)]
word_dict = {}
word_dict['source'] = word_filter
df = pd.DataFrame(word_dict)
write_excel = df.to_excel(r'All_in_one_filter.xlsx',index=False,header=True)


