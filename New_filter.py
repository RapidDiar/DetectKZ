import pandas as pd
import re

read_excel = pd.read_excel('All.xlsx',sheet_name='Sheet1')

words = [read_excel['source'][word] for word in read_excel.index]
for i in range(len(words)):
    result = re.sub(r'^[-]+|[-]+$','', words[i])
    words[i] = result

print(words)

new_list = []
for i in words:
    if i not in new_list:
        new_list.append(i)

new_list.sort()
print(len(new_list))

df = pd.DataFrame()
df['source'] = new_list
df.to_excel(r'Filter.xlsx',index=False,header=True)