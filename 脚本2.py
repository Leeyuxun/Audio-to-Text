import os
import shutil
from pydub import AudioSegment
from pydub.utils import make_chunks
from selenium import webdriver
import time
import re

dir_parent = 'D:\\测试音频'		#音频存放位置
dir_letter = dir_parent + '\\合并后的音频'	#合并后的音频存放的位置
dir_letter_letter = dir_parent + '\\切割后的音频'	#切割后的音频存放的位置
dir_letter_txt = dir_parent + '\\转换后的txt文件'	#下载转换后的txt文件存放的位置
add_sound = AudioSegment.from_wav('sample.wav')		#sample.wav是间隔音频，和脚本放在同一目录
sum_sound = add_sound

# 将所有txt文件合并
for file_name in os.listdir(dir_letter_txt):
    print(file_name)
    for line in open(dir_letter_txt+'\\'+file_name,encoding='UTF-8'):
        f = open("result.txt",'a')	# result.txt是创建的和脚本位于同一目录下的存放所有转换文字的文件
        f.write(line)
        f.close()

# 整理了txt文件内容
# 将文件中的句号转换成空格
f=open('result.txt','r')
alllines=f.readlines()
f.close()
f=open('result.txt','w+')
for eachline in alllines:
    a=re.sub('。',' ',eachline)
    f.writelines(a)
f.close()
# 将文件中的逗号转换成空格
f=open('result.txt','r')
alllines=f.readlines()
f.close()
f=open('result.txt','w+')
for eachline in alllines:
    a=re.sub('，',' ',eachline)
    f.writelines(a)
f.close()
# 将文件中的顿号转换成空格
f=open('result.txt','r')
alllines=f.readlines()
f.close()
f=open('result.txt','w+')
for eachline in alllines:
    a=re.sub('、','',eachline)
    f.writelines(a)
f.close()

# 将间隔音频转换的文字转换成换行符，方便查看
f=open('result.txt','r')	
alllines=f.readlines()
f.close()
f=open('result.txt','w+')
for eachline in alllines:
    a=re.sub('AAAA','\n',eachline)		#AAAA是间隔音频转换的文字内容
    f.writelines(a)
f.close()
print("txt处理完成，请查看result.txt文件")
