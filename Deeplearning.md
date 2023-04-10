# 1.Linux深度学习环境配置

## 1.1本次实验软件和硬件概述
&emsp;&emsp;电脑显卡为RTX2060，电脑系统为Ubuntu22.10。本次实验会安装驱动、pycharm、miniconda、pytorch直到能够运行yolov5项目中的detect.py文件接下来将一一进行介绍。本次实验为2023年4月完成，若时间差距过大不建议参考本文章。

## 1.2Linux系统安装
&emsp;&emsp;Linux系统的安装采用的是官方的ISO文件 ，地址为[Ubuntu22.10](https://cn.ubuntu.com/download/desktop)
。下载好用利用[rufus](http://rufus.ie/en/) 软件进行烧录。因为安装双系统的截不了图的，大家自行上网搜索相关视频和文章。
本人分给了ubuntu 100G空间，其中/swap分区8G，/boot分区2G，/分区 30G，剩余都留给/home分区 。

## 1.3Linux系统深度学习环境极简安装

-------------------------------------------------------------------------------------
1.初始化系统
&nbsp;

①：更新软件
&nbsp;

②：换源
&nbsp;

第一步：更换软件源
&nbsp;

第二步：根据[清华源](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)提供的官方方案更换pip源
```
python -m pip install --upgrade pip
```
```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-10%2021-42-48.png" width="500"/></div>
&nbsp;
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-10%2021-43-08.png" width="500"/></div>
&nbsp;

③：安装基础软件
```
sudo apt install build-essential
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-06%2021-32-01.png" width="500"/></div>
&nbsp;

&emsp;&emsp;至此系统初始化完成！！！

-------------------------------------------------------------------------------------
&nbsp;

2.安装驱动
&nbsp;

打开终端分别输入命令,此命令可以自动检测显卡并安装对应的驱动，方便快捷！

```
ubuntu-drivers devices
```
```
sudo ubuntu-drivers autoinstall
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-06%2020-46-30.png" width="500"/></div>
&emsp;&emsp;至此驱动安装完成！！！

-------------------------------------------------------------------------------------
&nbsp;

3.安装Pycharm
&nbsp;

①到[Pycharm官网](https://www.jetbrains.com.cn/pycharm/download/)下载对应系统的安装包
&nbsp;

②将对应安装包进行提取操作
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-06%2020-55-49.png" width="500"/></div>
&nbsp;

③进入解压后的Pycharm文件夹，进入bin文件夹，右击鼠标运行终端
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-06%2020-56-50.png" width="500"/></div>
&nbsp;

④在终端输入命令，即可打开Pycharm软件
```
bash pycharm.sh
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-06%2020-57-15.png" width="500"/></div>
&nbsp;

⑤初始化Pycharm
&nbsp;

第一步：新建项目
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-06%2020-57-43.png" width="500"/></div>
&nbsp;

第二步：添加桌面快捷方式（省的天天用终端运行）。点击Tools栏中的Create Desktop Entry
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-06%2021-23-18.png" width="500"/></div>
&nbsp;

第三步：设置成中文。点击File中的Settings按键，

<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-06%2021-23-42.png" width="500"/></div>
&nbsp;

在Plugin中Markspace搜索Chinese，非SDk的一个，也就是下面一个，点击install，即可设置成中文。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-06%2021-23-58.png" width="500"/></div>
&nbsp;

&emsp;&emsp;至此Pycharm软件初始化完毕！！！

-------------------------------------------------------------------------------------

4.安装Miniconda
&nbsp;

①到[Miniconda官网](https://docs.conda.io/en/latest/miniconda.html)下载对应系统的安装包
或者右键复制链接，在终端执行wget命令,我执行的命令为
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-06%2021-00-30.png" width="500"/></div>
&nbsp;
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-06%2021-19-09.png" width="500"/></div>
&nbsp;

②下载完，打开下载文件所在文件夹，右键输入命令
```
bash Miniconda3-latest-Linux-x86_64.sh
```
然后一直点击回车，根据提示输入y或n。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-06%2021-19-49.png" width="500"/></div>
&nbsp;
&emsp;&emsp;至此完成Miniconda安装！！！

-------------------------------------------------------------------------------------

5.安装Pytorch

根据[Pytorch](https://pytorch.org/get-started)提供的官方方案安装torch、torchvision等，一步到位，等待完成
```
pip3 install torch torchvision torchaudio
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-10%2021-45-13.png" width="500"/></div>
&nbsp;
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-10%2021-49-23.png" width="500"/></div>
&nbsp;

&emsp;&emsp;至此完成Pytorch安装！！！

-------------------------------------------------------------------------------------

6.打开项目

①：在Pycharm中运用Miniconda环境，编译器选择Conda Environment，点击OK
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-06%2021-22-17.png" width="500"/></div>
&nbsp;
②：新建项目，选择设置好的项目，点击Create创建项目
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-06%2021-22-27.png" width="500"/></div>
&nbsp;

③：打开YOlOv5项目

④：打开Pycharm下方的终端，输入命令,等待安装完成
```
pip3 install -r requirements.txt
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-10%2021-50-14.png" width="500"/></div>
&nbsp;
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-10%2021-50-43.png" width="500"/></div>
&nbsp;

----------------------------------------------------------------------------------

7.运行项目
&nbsp;

①：下载yolov5s.pt，可以在程序中慢慢下载，也可以去github下载，会快很多，下载完放入yolov5文件夹下

②：运行detect.py，一起看看输出结果吧！！！
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-10%2021-53-47.png" width="500"/></div>
&nbsp;
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-10%2021-54-07.png" width="500"/></div>
&nbsp;
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-10%2021-54-15.png" width="500"/></div>
&nbsp;