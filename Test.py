import re
import pandas as pd
word = ['--Бураба',
        '--Геоботаника',
        '--Геология',
        '--Жер',
        '--жылдар',
        '--Зерттел',
        '--Иондауш',
        '--Кен',
        '--қа',
        '--Қазақс',
        '--Қазақс',
        '--Қазақс',
        '--Қазақс',
        '--Мұздық',
        '--нен',
        '--Орталық',
        '--Республика',
        '--Төрттік',
        '--Тұщы',
        '--Экономика',
        '-ағаш',
        '-ағзаның',
        '-ағылш',
        '-ағым',
        '-ағыс',
        '-адамш',
        '-азамат',
        '-аймағ',
        '-аймағ',
        '-аймақ',
        '-аймақ',
        '-аймақ',
        '-Айналай',
        '-акроза',
        '-ақпан',
        '-Ақпарат-']

print(word)

for i in range(len(word)):
    result = re.sub(r'^[-]+|[-]+$','', word[i])
    word[i] = result

print(word)

new_list = []
for i in word:
    if i not in new_list:
        new_list.append(i)

new_list.sort()
print(new_list)

df = pd.DataFrame()
df['source'] = new_list
df.to_excel(r'Filter.xlsx',index=False,header=True)
