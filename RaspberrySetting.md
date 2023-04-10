# 1.树莓派配置

## 1.1本次实验树莓派概述
&emsp;&emsp;树莓派型号为树莓派3B+（不带有屏幕和网线），电脑系统为Ubuntu20.04。树莓派通过SSH的方式与PC端进行远程连接，并利用VNC软件对树莓派进行远程操作，接下来将一一进行介绍。本次实验为2022年6月完成，若时间差距过大不建议参考本文章。

&nbsp;

## 1.2树莓派系统安装
&emsp;&emsp;树莓派系统的安装采用的工具是 [Raspberry Pi Image](https://www.raspberrypi.com/software/)
对MicroSD卡进行系统烧录。其中Raspberry Pi Image工具所下载的系统都为最新发布的系统，如果要安装其他版本可以进入
[Operating system images](https://www.raspberrypi.com/software/operating-systems/) 下载。

1.打开烧录软件，选择合适的系统，SD卡位置。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%281%29.png" width="500"/></div>

&nbsp;

2.本次实验选择 Raspberry PI OS (64-bit) 系统，期间也用过Ubuntu版本，但是在VNC连接的时候出现问题，未能成功解决。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%287%29.png" width="500"/></div>

&nbsp;

3.点击蓝框中所选中的设置按钮进行WIFI、SSH的账号密码设置。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%286%29_LI.jpg" width="500"/></div>

&nbsp;

4.电脑端和树莓派远程连接会用到SSH服务，所有步骤内唯一需要记住的就是这里所设置的账号和密码。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%2811%29.png" width="500"/></div>

&nbsp;

5.电脑端和树莓派远需要在一个局域网下才能通过SSH进行连接。本人采用手机热点进行WIFI部署。需要输入WIFI的账号密码，并把地区改成中国（CN）。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%288%29.png" width="500"/></div>

&nbsp;

6.最后点击烧录按键，等待烧录完成插入树莓派中，打开树莓派电源等待几十秒即可看见树莓派已经连上了WIFI，连上WIFI后即可进行下一步操作。

## 1.3 SSH、VNC
&emsp;&emsp;通过以上步骤后，树莓派连接到了WIFI，将树莓派和电脑连接到同一个wifi，通过手机查看所分配的IP地址并记住。接下来就开始SSH、VNC远程连接部分。

1.根据所分配的IP地址进行ssh连接，其中ssh的用户名，@后面的地址填写WIFI所分配的IP地址。（终端输入命令，下同）
```
ssh 用户名@地址
```

<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2022-05-13%2022-12-51%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png" width="500"/></div>
&emsp;&emsp;若以前此IP地址有进行连接过，如重装了系统等，则会出现报错。输入以下代码删除以前的记录，再次执行上面一步。输入Yes后根据ssh的密码进行填写，即可连接到树莓派。

```
rm -rf ~/.ssh/known_hosts
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2022-05-31%2018-42-49%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png" width="500"/></div>
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2022-05-31%2018-43-04%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png" width="500"/></div>

&nbsp;

2.通过下面的代码进行树莓派参数配置。

```
sudo raspi-config
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2022-05-31%2019-19-15%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png" width="500"/></div>
（1）Display Options控制桌面显示大小
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2022-06-20%2015-04-37%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png" width="500"/></div>
&emsp;&emsp;如果用VNC桌面，可以调整下面两个参数观察效果。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2022-06-20%2015-03-38%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png" width="500"/></div>
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2022-06-20%2015-03-41%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png" width="500"/></div>
（2）Interface Option接口设置，用于打开树莓派上的外部接口开关。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2022-06-20%2015-05-33%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png" width="500"/></div>
&emsp;&emsp;打开Camera、VNC开关。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2022-06-20%2015-05-45%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png" width="500"/></div>
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2022-06-20%2015-05-42%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png" width="500"/></div>

&nbsp;

3.开启VNC开关后，通过[VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/)软件对树莓派进行远程桌面连接。
&emsp;&emsp;

（1）输入需要连接的树莓派地址
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2022-06-20%2015-07-09%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png" width="500"/></div>
（2）输入ssh的账号和密码
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2022-06-20%2015-07-12%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png" width="500"/></div>

&nbsp;
## 1.4 换源
&emsp;&emsp;换源即把国外的源换成国内的，以防止传输速率不佳等问题。将前缀按照[清华源](https://mirrors.tuna.tsinghua.edu.cn/help/raspbian/)格式进行修改。

&nbsp;

1.更改sources.list（终端输入命令）

```
sudo nano /etc/apt/sources.list
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2022-05-13%2022-13-39%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png" width="500"/></div>

&emsp;&emsp;将其中的代码从如下所示
```
deb http://deb.debian.org/debian bullseye main contrib non-free
deb http://security.debian.org/debian-security bullseye-security main contrib non-free
deb http://deb.debian.org/debian bullseye-updates main contrib non-free
```
&emsp;&emsp;改为如下所示
```
deb http://mirrors.tuna.tsinghua.edu.cn/debian bullseye main contrib non-free
deb http://mirrors.tuna.tsinghua.edu.cn/debian-security bullseye-security main contrib non-free
deb http://mirrors.tuna.tsinghua.edu.cn/debian bullseye-updates main contrib non-free
```
&emsp;&emsp;改完后进行保存（nano命令）；ctrl+O保存，Enter确认，ctrl+x退出。

&nbsp;

2.更改raspi.list
```
sudo nano /etc/apt/sources.list.d/raspi.list
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2022-06-20%2016-57-48%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png" width="500"/></div>

&emsp;&emsp;将其中的代码从如下所示
```
deb http://mirrors.tuna.tsinghua.edu.cn/raspberrypi/ bullseye main
```
&emsp;&emsp;改为如下所示
```
deb http://mirrors.tuna.tsinghua.edu.cn/raspberrypi/ bullseye main
```
&emsp;&emsp;改完后进行保存（nano命令）；ctrl+O保存，Enter确认，ctrl+x退出。

&nbsp;

3.更改pip源

&emsp;&emsp;根据[清华源](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)官网给出的方案进行修改。
```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2022-06-20%2016-58-31%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png" width="500"/></div>

&nbsp;

4.更新软件源、升级软件
```
sudo apt-get update
```
```
sudo apt-get upgrade
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2022-06-20%2017-01-39%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png" width="500"/></div>

&nbsp;

5.重启树莓派
```
sudo reboot
```

&nbsp;
## 1.5 程序移植和深度学习环境配置

&nbsp;

1.将电脑端的文件传输到树莓派端有几种不同的选择，可以通过oss上传和下载，也可以通过[filezilla](https://www.filezilla.cn/)进行数据交换。推荐使用OSS，特别是数据量大的时候。filezilla简单易用些，但是数据传输速度很慢，本文使用filezilla。其中用户名合密码为ssh的账号合密码。
```
sftp://xxx.xxx.xx.xx  用户名：xxx  密码：xxx  端口：可不填写
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2022-06-20%2017-03-04%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png" width="500"/></div>
&emsp;&emsp;如图，我将YOLOv5文件夹移动到树莓派的Downloads文件夹下。

&nbsp;

2.下面进行树莓派端深度学习环境的配置。

（1）先进入YOLOv5文件夹所在区域
```
cd /home/pi/Downloads/yolov5
```
（2）用pip安装配置 requirements.txt所需要文件
```
pip3 install -r requirements.txt
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/1.png" width="500"/></div>
&emsp;&emsp;其中requirements.txt文件有几处地方需要改动，本人在实验时按照默认文件安装python库出现了不同报错，踩了很多。其中需要注意opencv、numpy、torch、torchvision的格式，如果默认安装在某个库卡住建议更换方法，不建议死磕到底。opencv不能直接用pip opencv-python进行安装，numpy需要指定一个版本。torch和torchvision建议试多个版本，我试了许多，只有torch == 1.8.1，torchvision ==0.9.1时可以正常使用。

```
# pip install -r requirements.txt

# Base ----------------------------------------
matplotlib>=3.2.2
numpy>=1.18.5
opencv-python>=4.1.2
Pillow>=7.1.2
PyYAML>=5.3.1
requests>=2.23.0
scipy>=1.4.1
torch>=1.7.0
torchvision>=0.8.1
tqdm>=4.41.0

```
&emsp;&emsp;改为以下内容
```
# pip install -r requirements.txt

# Base ----------------------------------------
matplotlib>=3.2.2
numpy == 1.22.4
opencv-contrib-python
Pillow>=7.1.2
PyYAML>=5.3.1
requests>=2.23.0
scipy>=1.4.1
torch == 1.8.1
torchvision ==0.9.1
tqdm>=4.41.0
```
&emsp;&emsp;若要装PyQt5则安装
```
opencv-python-headless
```

（3）安装onnx和onnxruntime工具

```
pip3 install onnx
```
```
pip3 install onnxruntime
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/2.png" width="500"/></div>

&nbsp;

3.安装和配置摄像头监控软件motion。

（1）下载motion
```
sudo apt-get install motion
```
（2）配置相机文件
```
sudo nano /etc/motion/motion.conf
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/4.png" width="500"/></div>

&emsp;&emsp;更改以下参数，stream_maxrate设置100或者以上，视频流虽然很流畅，但是运行YOLOv5的时候树莓派吃不消，具体参数可以自行搜索。

```
daemon on
stream_localhost off
stream_maxrate 15
```
（3）配置完后，重启motion。
```
sudo killall -TERM motion
```
```
sudo motion
```

&nbsp;
## 1.6 在树莓派端运行YOLOv5
（1）先进入YOLOv5文件夹所在区域
```
cd /home/pi/Downloads/yolov5
```
（2）启动相机
```
sudo motion
```
（3）防止报错
```
export OMP_NUM_THREADS=1
```
（4）运行项目
```
python3 detect.py
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/3.png" width="500"/></div>
（5）运行结果
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/raspberrypicture/%E5%AA%92%E4%BD%931%2000_00_00-00_00_30.gif" width="500"/></div>
