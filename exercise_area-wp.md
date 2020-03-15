# 攻防世界WEB入门题目write up

## 1. view_source

### 原理

右键无法使用，即右键无法查看网页源码，故尝试使用浏览器开发者工具

### 工具

Firefox

### 步骤

使用Firefox打开网页，按下F12，跳转到开发者模式，使用查看器查看网页源码，得到flag为`cyberpeace{abe8c9af5df02f72f83dde7d362c7df6}`

![1564381171925](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564381171925.png)

## 2. get_post

### 原理

http的数据请求post和get原理

### 工具

Firefox、HackBar

### 步骤

1. 在Firefox浏览器中打开网页，提示要用GET方式提交一个值为1的变量a

2. 使用HackBar通过get方式提交变量a=1,或者直接在URL输入框中输入`http://111.198.29.45:40308?a=1`
   ![1564388248797](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564381171925.png)

3. 根据提示继续以GET的方式提交a=1并以POST的方式提交值为2的变量b（勾选Post data即可）,返回flag为`cyberpeace{e0619fdbb17fe505fcded7b3869b9495}`
   ![1564388398442](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564381171925.png)

   

## 3. robots

### 原理

robots.txt文件是一个协议，是搜索引擎中访问网站的时候要查看的第一个文件。robots.txt文件告诉蜘蛛程序在服务器上什么文件是可以被查看的。当一个搜索蜘蛛访问一个站点时，它会首先检查该站点根目录下是否存在robots.txt，如果存在，搜索机器人就会按照该文件中的内容来确定访问的范围；如果该文件不存在，所有的搜索蜘蛛将能够访问网站上所有没有被口令保护的页面。

### 工具

目录爆破工具[dirserach](https://github.com/evilsocket/dirsearch)

### 步骤

1. 查看源码，没有提示，根据提示robots协议，想到flag可能会存储在`robots.txt`上
2. 通过目录爆破工具[dirserach](https://github.com/evilsocket/dirsearch)扫描网站目录：`python3 dirsearch.py -u "http://111.198.29.45:55654/" -e *`，扫描到robots.txt文件
   ![1564409074044](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564381171925.png)
3. 访问`http://111.198.29.45:55654/robots.txt`，发现`Disallow: f1ag_1s_h3re.php`
   ![1564409225599](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564381171925.png)
4. 继续在URL中输入`http://111.198.29.45:55654/f1ag_1s_h3re.php`，尝试访问`f1ag_1s_h3re.php`，结果得到flag为`cyberpeace{841741b0c0780a80f91f6cd1148d0373}`
   ![1564409361854](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564381171925.png)

## 4. backup

### 原理
常见的备份文件后缀名有: `.git` `.svn` `.swp` `.svn` `.~` `.bak` `.bash_history`

### 工具

目录爆破工具[dirserach](https://github.com/evilsocket/dirsearch)，[notepad++](https://notepad-plus-plus.org/)

### 步骤

1. 查看源码，没有提示，根据提示忘记删除备份文件提示，想到flag可能会存储在备份文件上。
2. 通过目录爆破工具[dirserach](https://github.com/evilsocket/dirsearch)扫描网站目录：`python3 dirsearch.py -u "http://111.198.29.45:37766/" -e *`，扫描到index.php.bak备份文件
   
   ![1564632397780](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564632397780.png)
3. 继续在URL中输入`http://111.198.29.45:37766/index.php.bak`，讲备份文件保存到本地后使用[notepad++](https://notepad-plus-plus.org/)打开，发现flag为`cyberpeace{899ad51ca546f7e97b7f3f8f02d4e180}`
   ![1564632691681](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564632691681.png)


## 5. cookie

### 原理

Cookie是当主机访问Web服务器时，由 Web 服务器创建的，将信息存储在用户计算机上的文件。一般网络用户习惯用其复数形式 Cookies，指某些网站为了辨别用户身份、进行 Session 跟踪而存储在用户本地终端上的数据，而这些数据通常会经过加密处理。

### 工具

Firefox

### 步骤

1. 使用Firefox打开网页，按下F12，跳转到开发者模式，刷新后，在存储一栏，可看到名为look-here的cookie的值为cookie.php。
   ![1564665090877](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564665090877.png)
2. 访问`http://111.198.29.45:42848/cookie.php`，提示查看http响应包，在网络一栏，看到访问cookie.php的数据包，点击查看数据包，在消息头内发现flag为`cyberpeace{06ebc2f1032b90f947762c560d358194}`
   ![1564665238648](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564665238648.png)



## 6. disabled button

### 原理

前端HTML语言语法

### 工具

Firefox，HackBar

### 步骤

1. 使用Firefox打开网页，按下F12，跳转到开发者模式，在查看器窗口审查元素，发现按钮请求使用POST方式，`name="auth"`，`value="flag"`，`disabled=“”`。
   ![1564666215195](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564666215195.png)

2. 直接删除`disabled=“”`，或者将`disabled`改为`enabled`，使按钮变为可点击，点击按钮即获得flag；或者使用HackBar发送`auth=flag`的POST请求，也可获得flag为`cyberpeace{7fe886060fa0b82db931af33971587bd}`

   ![1564666694309](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564666694309.png)

## 7. simple js

### 原理

javascript的代码审计

### 工具

Firefox

### 步骤

1. 使用Firefox打开网页，按下F12，跳转到开发者模式，点击查看器查看源代码，可以发现js代码

![1564667544538](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564667544538.png)

2. 进行代码审计，发现不论输入什么都会跳到假密码，真密码位于 `fromCharCode`中 。

3. 使用python处理字符串，得到数组[55,56,54,79,115,69,114,116,107,49,50]，exp如下：

   ```python
   s="\x35\x35\x2c\x35\x36\x2c\x35\x34\x2c\x37\x39\x2c\x31\x31\x35\x2c\x36\x39\x2c\x31\x31\x34\x2c\x31\x31\x36\x2c\x31\x30\x37\x2c\x34\x39\x2c\x35\x30"
   print (s)
   ```

4. 将数字转换成ASCII码得到字符串`786OsErtk12`，exp如下：

   ```python
   a = [55,56,54,79,115,69,114,116,107,49,50]
   c = ""
   for i in a:
   b = chr(i)
   c = c + b
   print(c)
   ```

5. 根据flag格式提示，得到flag为`Cyberpeace{786OsErtk12}` 。

## 8. xff referer

### 原理

X-Forwarded-For简称XFF头，它代表客户端，也就是HTTP的请求端真实的IP，只有在通过了HTTP 代理或者负载均衡服务器时才会添加该项。HTTP Referer是header的一部分，当浏览器向web服务器发送请求的时候，一般会带上Referer，告诉服务器我是从哪个页面链接过来的

### 工具

Firefox，burpsuite

### 步骤

1. 使用Firefox打开网页，提示IP地址必须为`123.123.123.123`。

2. 使用burpsuite对Firefox进行代理拦截，在请求头添加`X-Forwarded-For: 123.123.123.123`，然后放行。收到包显示必须来自`https://www.google.com`：
   ![1564670056246](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564670056246.png)

3. 继续在请求头添加`Referer: https://www.google.com`，放行后获得flag为`cyberpeace{0dd83e102ef7baaee4b1332a71de72e5}`

   ![1564670223392](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564670223392.png)

## 9. weak auth

### 原理

弱口令爆破

### 工具

burpsuite、攻击字典

### 步骤

1. 使用Firefox打开网页，尝试输入任意用户名，提示要使用admin账户登录。
2. 用burpsuite截下登录的数据包。
   ![1564671594599](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564671594599.png)
4. 把数据包发送到intruder爆破，设置爆破点为password。
   ![1564671901275](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564671901275.png)
5. 导入攻击字典。
   ![1564672033296](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564672033296.png)
6. 开始攻击，查看响应包列表，发现密码为123456时，响应包的长度和别的不一样。查看响应包，找到flag为`cyberpeace{22ee862a8aabe56a849198cd2bd9d2a8}`。
   ![1564672188609](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564672188609.png)

## 10. webshell

### 原理

php一句话木马

### 工具

菜刀

### 步骤

1. 打开网页，发现提示`<?php @eval($_POST['shell']);?>` ，为PHP一句话木马。
2. 使用菜刀连接：
   ![1564710201148](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564710201148.png)
3. 网站目录下发现了f`lag.txt`文件：
   ![1564710259022](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564710259022.png)

4. 查看文件可获得flag为`cyberpeace{8733882b6647dada96f18da7f7f56754}`
   ![1564710354117](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564710354117.png)

## 11. command execution

### 原理

windows和linux下:
`command1 && command2` 先执行`command1`后执行`command2`
`command1 | command2` 只执行`command2`
`command1 & command2` 先执行`command2`后执行`command1`

### 工具

Firefox

### 步骤

1. 使用Firefox打开网页，在输入框输入`ping 111.198.29.45 | find / -name "flag.txt"`，寻找flag位置为`/home/flag.txt`
   ![1564711345518](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564711345518.png)

2. 继续输入命令`ping 111.198.29.45 | cat /home/flag.txt`打开flag.txt文件,获得flag为`cyberpeace{807ae4792ee2474774421999b765b97e}`
   ![1564711560625](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564711560625.png)

## 12. simple php

### 原理

PHP比较符号`===`和`==`

`===`会先比较字符串的类型再比较字符串的值

`==`会先将字符串换成相同类型，再作比较，属于弱类型比较

### 工具

Firefox

### 步骤

1. 使用Firefox 打开网页，发现PHP代码为

   ```php
   <?php
   	show_source(__FILE__);
   	include("config.php");
   	$a=@$_GET['a'];
   	$b=@$_GET['b'];
   	if($a==0 and $a){
   	    echo $flag1;
   	}
   	if(is_numeric($b)){
   	    exit();
   	}
   	if($b>1234){
   	    echo $flag2;
   	}
   ?>
   ```

2. 进行代码审计：通过`GET`方式传值`a`和`b`，需要满足`$a==0 && $a`且b不为数字或数字字符串且`$b>1234`。

3. 在URL输入栏中输入`http://111.198.29.45:31491/index.php?a=a&&b=1235b`，满足审计条件，获得flag为
   `Cyberpeace{647E37C7627CC3E4019EC69324F66C7C}`
   ![1564713453391](https://github.com/Leeyuxun/XCTF-WEB-Exercise_area-write_up/blob/master/exercise_area-images/1564713453391.png)
