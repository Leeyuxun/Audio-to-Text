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
    time.sleep(5)
    driver1.execute_script("arguments[0].click();", driver1.find_element_by_xpath("//span[contains(text(),'开始转换')]"))
    time.sleep(35)
    print('开始下载文件')
    driver1.execute_script("arguments[0].click();", driver1.find_element_by_xpath("//a[contains(text(),'立即下载')]"))#定位txt下载按钮并下载
    print('文件下载成功')
print('所有文件下载完成')
