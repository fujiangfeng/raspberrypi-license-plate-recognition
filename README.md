# 1.树莓派配置
## 1.1本次实验树莓派概述
&emsp;&emsp;树莓派型号为树莓派3B+（不带有屏幕和网线），电脑系统为Ubuntu20.04。树莓派通过SSH的方式与PC端进行远程连接，并利用VNC软件对树莓派进行远程操作，接下来将一一进行介绍。
## 1.2树莓派系统安装
&emsp;&emsp;树莓派系统的安装采用的工具是 [Raspberry Pi Image](https://www.raspberrypi.com/software/)
对MicroSD卡进行系统烧录。其中Raspberry Pi Image工具所下载的系统都为最新发布的系统，如果要安装其他版本可以进入
[Operating system images](https://www.raspberrypi.com/software/operating-systems/) 下载。

&emsp;&emsp;1.打开烧录软件，选择合适的系统，SD卡位置。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/picture/raspberrypicture/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%281%29.png?Expires=1654154577&OSSAccessKeyId=TMP.3KiQpVm3i9JEyLAK4W4JYFmdxFRbkAEgDrMY78YvXfVdjqE3jTnRzjfrQ2apkE7yuVRuG1CWoKyGvKHrAYbrXcyJXrVWFf&Signature=Qtx28Tyt9LhxLS6OcZlTWIx6jNI%3D" style="zoom:60%"/></div>
&emsp;&emsp;2.本次实验选择 Raspberry PI OS (64-bit) 系统，期间也用过Ubuntu版本，但是在VNC连接的时候出现问题，未能成功解决。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/picture/raspberrypicture/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%287%29.png?Expires=1654154610&OSSAccessKeyId=TMP.3KiQpVm3i9JEyLAK4W4JYFmdxFRbkAEgDrMY78YvXfVdjqE3jTnRzjfrQ2apkE7yuVRuG1CWoKyGvKHrAYbrXcyJXrVWFf&Signature=OqA3wo4gRRCVWeIzKjMFN3LjuKE%3D" style="zoom:60%"/></div>
&emsp;&emsp;3.点击蓝框中所选中的设置按钮进行WIFI、SSH的账号密码设置。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/picture/raspberrypicture/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%286%29_LI.jpg?Expires=1654154670&OSSAccessKeyId=TMP.3KiQpVm3i9JEyLAK4W4JYFmdxFRbkAEgDrMY78YvXfVdjqE3jTnRzjfrQ2apkE7yuVRuG1CWoKyGvKHrAYbrXcyJXrVWFf&Signature=z3ZOAFG3W0DqW5U%2BnhApS%2FDFA%2FI%3D" style="zoom:60%"/></div>
&emsp;&emsp;4.电脑端和树莓派远程连接会用到SSH服务，所有步骤内唯一需要记住的就是这里所设置的账号和密码。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/picture/raspberrypicture/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%2811%29.png?Expires=1654154731&OSSAccessKeyId=TMP.3KiQpVm3i9JEyLAK4W4JYFmdxFRbkAEgDrMY78YvXfVdjqE3jTnRzjfrQ2apkE7yuVRuG1CWoKyGvKHrAYbrXcyJXrVWFf&Signature=f8nEs%2BoR8%2B5zgY7Tu2oTqSJs2Xc%3D" style="zoom:60%"/></div>
&emsp;&emsp;5.电脑端和树莓派远需要在一个局域网下才能通过SSH进行连接。本人采用手机热点进行WIFI部署。需要输入WIFI的账号密码，并把地区改成中国（CN）。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/picture/raspberrypicture/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%288%29.png?Expires=1654154769&OSSAccessKeyId=TMP.3KiQpVm3i9JEyLAK4W4JYFmdxFRbkAEgDrMY78YvXfVdjqE3jTnRzjfrQ2apkE7yuVRuG1CWoKyGvKHrAYbrXcyJXrVWFf&Signature=I0IERk6%2BHQz5A4MQ6kyhz5UAtLg%3D" style="zoom:60%"/></div>
&emsp;&emsp;6.最后点击烧录按键，等待烧录完成插入树莓派中，打开树莓派电源等待几十秒即可看见树莓派已经连上了WIFI，连上WIFI后即可进行下一步操作。

## 1.3 SSH、VNC
&emsp;&emsp;通过以上步骤后，树莓派连接到了WIFI，将树莓派和电脑连接到同一个wifi，通过手机查看所分配的IP地址并记住。接下来就开始SSH、VNC远程连接部分。

&emsp;&emsp;1.根据所分配的IP地址进行ssh连接，其中pi字符所在部分填写步骤1.2中第4步的账号，@后面的地址填写WIFI所分配的IP地址。
```
ssh pi@192.168.43.110
```

<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/picture/raspberrypicture/2022-05-13%2022-12-51%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png?Expires=1654154795&OSSAccessKeyId=TMP.3KiQpVm3i9JEyLAK4W4JYFmdxFRbkAEgDrMY78YvXfVdjqE3jTnRzjfrQ2apkE7yuVRuG1CWoKyGvKHrAYbrXcyJXrVWFf&Signature=THn9GCsZv%2BpJqdijsmC4Rm3Xc3k%3D" style="zoom:60%"/></div>
&emsp;&emsp;若以前此IP地址有进行连接过，如重装了系统等，则会出现报错。输入以下代码删除以前的记录，再次执行上面一步。输入Yes后根据步骤1.2中第4步设置的密码进行填写，即可连接到树莓派。

```
rm -rf ~/.ssh/known_hosts
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/picture/raspberrypicture/2022-05-31%2018-42-49%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png?Expires=1654154811&OSSAccessKeyId=TMP.3KiQpVm3i9JEyLAK4W4JYFmdxFRbkAEgDrMY78YvXfVdjqE3jTnRzjfrQ2apkE7yuVRuG1CWoKyGvKHrAYbrXcyJXrVWFf&Signature=G%2F1OFHQBwt2PLmOEJ9ubi67kunU%3D" style="zoom:60%"/></div>
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/picture/raspberrypicture/2022-05-31%2018-43-04%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png?Expires=1654154822&OSSAccessKeyId=TMP.3KiQpVm3i9JEyLAK4W4JYFmdxFRbkAEgDrMY78YvXfVdjqE3jTnRzjfrQ2apkE7yuVRuG1CWoKyGvKHrAYbrXcyJXrVWFf&Signature=uBh1yk3cvDJiZ2958dflHNi3rd0%3D" style="zoom:60%"/></div>

&emsp;&emsp;2.通过下面的代码进行树莓派参数配置，如VNC。

```
sudo raspi-config
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/picture/raspberrypicture/2022-05-31%2019-19-15%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png?Expires=1654154377&OSSAccessKeyId=TMP.3KiQpVm3i9JEyLAK4W4JYFmdxFRbkAEgDrMY78YvXfVdjqE3jTnRzjfrQ2apkE7yuVRuG1CWoKyGvKHrAYbrXcyJXrVWFf&Signature=%2Fbz0mfVaBdvVrqdSAggDqgqryT8%3D" style="zoom:60%"/></div>
<div align=center><img src="" style="zoom:50%"/></div>

&emsp;&emsp;3.开启VNC后，通过[VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/)软件对树莓派进行远程桌面连接。


## 1.4 换源











