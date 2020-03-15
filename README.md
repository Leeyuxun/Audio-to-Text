# Audio-to-text

## 前言 

最近做起工具人，对大量音频进行文字标注。工作太枯燥，费时，就写了一个脚本，借助迅捷音频转文字在线工具，个人感觉在一定程度上提高了效率<!--more-->

## 过程

很简单

1. 将大量短音频合并，中间用特殊的音频分隔
2. 将大的音频分隔成固定大小的音频（迅捷在线语音转换一次最多只能免费转换20M的音频）
3. 上传到迅捷音频转换页面，进行转换，并把txt文件下载
4. 整理txt文件，删除标点和间隔语音转换的文字，并把所有文字合并到同一个txt文件里面

## 语言

python 3.7

## 引用库

```python
import os
import shutil
from pydub import AudioSegment
from pydub.utils import make_chunks
from selenium import webdriver
import time
import re
```

具体原理相关库已经说明，可以使用pip直接下载，也可以手动下载安装，遇到问题直接Google求助，这里不再说明

## 代码

脚本1，将音频合并切割并转换成txt

```python
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

# 分别和并同一文件夹下的所有音频
for path,dir_list,file_list in os.walk(dir_parent):
    for dir_name in dir_list:
        dir_child = dir_parent + '\\' + dir_name
        for path,dir_list,file_list in os.walk(dir_child):
            for file_name in file_list:
                #print(file_name)
                front_path = os.path.join(path, file_name)
                #print(front_path)
                front_sound = AudioSegment.from_wav(front_path)
                sum_sound = sum_sound + front_sound + add_sound
        sum_sound.export(dir_child+'已合并.wav',format="wav")
        sum_sound = add_sound
        print(dir_child+'文件下的音频合并完成')
        
# 将处理过的音频放入同一文件夹内
os.makedirs(dir_letter)
for file in os.listdir(dir_parent):
    if os.path.isfile(dir_parent + '\\' + file):
        if '已合并' in file:
            shutil.move(dir_parent + '\\' + file,dir_letter)   
print("所有音频合并完成")


# 切割合并后的音频
chunk_length_ms = 325000 # 分块的毫秒数（测试wav文件每个音频如果在325s内刚好不多于20M,当然也可以改成300s）
os.makedirs(dir_letter_letter)  # 创建切割音频的文件夹
for path,dir_list,file_list in os.walk(dir_letter):
    for file_name in file_list:
        audio = AudioSegment.from_file(dir_letter+'\\'+file_name , "wav") 
        chunks = make_chunks(audio, chunk_length_ms) #将音频切割
        #保存切割的音频到文件
        # 下面两行目的是对文件名进行简单处理，保证文件名都是数字，排序时方便整理，这个因文件名而异
        file_name_change1 = file_name.strip('已合并.wav')
        file_name_change2 = file_name_change1.strip('AAAAA')	#AAAAA是file_name的前缀
        for i, chunk in enumerate(chunks):
            chunk_name = dir_letter_letter+"\\"+file_name_change2+"{0}.wav".format(i)
            chunk.export(chunk_name, format="wav")
        print ("音频"+file_name_change2+"切割完成")
print("所有音频切割完成")

# 转换音频文件
# 更改firefox默认下载设置，不懂可自行Google
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.dir',dir_letter_letter)
profile.set_preference('browser.download.folderList',2)
profile.set_preference('browser.download.manager.showWhenStarting',False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk','text/plain')

# 历遍文件夹内的文件并返回一个列表
path_list = os.listdir(dir_letter_letter)
# 利用循环历遍path_list列表
for file_name in path_list:
    #print(filename)
    #启动浏览器
    driver1 = webdriver.Firefox(firefox_profile=profile)
    driver1.get("https://app.xunjiepdf.com/voice2text/")	#打开迅捷转换网页
    print('开始上传'+file_name+'音频文件')
    upload = driver1.find_element_by_name('file')	#寻找上传按钮
    upload.send_keys(dir_letter_letter+'\\'+file_name)  #上传文件
    print('音频文件'+file_name+'上传成功')
    time.sleep(50)	#睡眠50S等待音频转换完成
    print('开始下载文件')
    driver1.execute_script("arguments[0].click();", driver1.find_element_by_xpath("//a[contains(text(),'立即下载')]"))	#定位txt下载按钮并下载
    print('文件下载成功')
print('所有文件下载完成')
```

脚本2，整理txt

```python
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
```

脚本写的比较匆忙，自己对python也不是很熟悉，没有使用函数，凑活用，直接是个单线程的程序，尝试处理八百多条音频时间二十分钟左右，识别率挺高，没有用多线程是因为脚本运行过程中多次调用firefox，担心程序崩溃。

## 附

脚本成功运行的条件是音频放在多个文件夹里面，多个文件夹同时有放在同一个名为“测试音频”的文件夹里面，相当于是三级目录。
