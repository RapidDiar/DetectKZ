import os
import glob

all_txt = []
path = os.getcwd()
os.chdir(path+'/OutputKZ/')
for i in glob.glob('*.txt'):
    file_read = open(i,"r")
    file_lines = file_read.readlines()
    for x in file_lines:
        all_txt.append(x)
    file_lines.clear()

file_write = open(path+'/Final/FinalKZ.txt','w+')
file_write.writelines(all_txt)
file_write.close()

