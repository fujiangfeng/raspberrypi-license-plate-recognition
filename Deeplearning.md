# 1.Linux深度学习环境配置
&emsp;&emsp;写在最前面：将该项目上传网络的初衷是因为网上有很多优秀的贴子，但是有些年份较早，有些完整性不高，我就把很多帖子整合到一起，其中继承了很多大佬的经验，在此非常感谢各位前辈为我们留下很好的经验贴。因为我也是第一次接触深度学习，有不妥之处还望大佬指出。

## 1.1本次实验软件和硬件概述
&emsp;&emsp;电脑显卡为RTX2060，电脑系统为Ubuntu22.10。本次实验会介绍如何安装驱动、CUDA、Pycharm、Miniconda、pytorch等，目的是为了能够运行深度学习目标检测算法yolov5，接下来将一一进行介绍。本次实验为2023年4月完成，若时间差距过大不建议参考本文章。

## 1.2Linux系统安装
&emsp;&emsp;Linux系统的安装采用的是官方的ISO文件 ，版本为[Ubuntu22.10](https://cn.ubuntu.com/download/desktop)
。利用[rufus](http://rufus.ie/en/) 软件进行u盘烧录。因为Ubuntu的安装自己也不太了解，大家可以自行上网搜索相关视频和文章。
本人分给了ubuntu 100G空间，其中/swap分区8G，/boot分区2G，/分区 30G，剩余都留给/home分区 。

## 1.3Linux系统深度学习环境极简安装
Ubuntu系统的复制快捷键是shift+ctrl+c,粘贴的快捷键是shift+ctrl+v，与windows操作不同，注意！！！

-------------------------------------------------------------------------------------
1.初始化系统
&nbsp;

①：更新软件
&nbsp;

第一步：连接wifi（系统设置都在Ubuntu的右上方）
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/%E6%88%AA%E5%9B%BE%202023-04-12%2015-20-37.png" width="300"/></div>
&nbsp;

第二步：更新语言支持（按提示执行即可）
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/QQ%E5%9B%BE%E7%89%8720230412081446.png" width="500"/></div>
&nbsp;

②：换源
&nbsp;

第一步：更换软件源
&nbsp;

&emsp;&emsp;打开菜单中的软件和更新
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/QQ%E6%88%AA%E5%9B%BE20230412081629.png" width="500"/></div>
&nbsp;

&emsp;&emsp;打开下载自的箭头选择其他
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/QQ%E6%88%AA%E5%9B%BE20230412081800.png" width="500"/></div>
&nbsp;

&emsp;&emsp;点击选择最佳服务器
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/QQ%E5%9B%BE%E7%89%8720230412081823.png" width="500"/></div>
&nbsp;

&emsp;&emsp;经过一段时间的测试，它会自动选择服务器，点击确定即可
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/QQ%E6%88%AA%E5%9B%BE20230412081851.png" width="500"/></div>
&nbsp;

第二步：更新软件
&nbsp;

&emsp;&emsp;打开菜单中的软件更新器
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/QQ%E5%9B%BE%E7%89%8720230412081636.png" width="500"/></div>
&nbsp;

&emsp;&emsp;点击立即安装，等待几分钟更新软件
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/QQ%E6%88%AA%E5%9B%BE20230412081905.png" width="500"/></div>
&nbsp;


第三步：
&nbsp;

&emsp;&emsp;安装pip
```
sudo apt-get install python-pip
```
```
sudo apt-get install python3-pip
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/%E6%88%AA%E5%9B%BE%202023-04-12%2015-27-23.png" width="500"/></div>
&nbsp;
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/%E6%88%AA%E5%9B%BE%202023-04-12%2015-28-57.png" width="500"/></div>
&nbsp;

&emsp;&emsp;根据[清华源](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)提供的官方方案更换pip源
```
python3 -m pip install --upgrade pip
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

2.安装驱动和cuda
&nbsp;

&emsp;&emsp;打开终端分别输入命令,此命令可以自动检测显卡并安装对应的驱动和cuda，方便快捷！如果想安装其他驱动或者CUDA版本，可以自己去网上找资料，这里就不再介绍。
这里安装的东西比较多，请大家耐心等待。

```
ubuntu-drivers devices
```
```
sudo ubuntu-drivers autoinstall
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-06%2020-46-30.png" width="500"/></div>
&nbsp;

&emsp;&emsp;安装NVIDIA工具包.这里安装的东西比较多，请大家耐心等待。
```
sudo apt install nvidia-cuda-toolkit
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/%E6%88%AA%E5%9B%BE%202023-04-12%2015-33-23.png" width="500"/></div>
&nbsp;

&emsp;&emsp;输入命令查看CUDA版本。本电脑的安装的CUDA版本为11.5，如下图所示。请记住该版本，后续在Pytorch部分会用到。
```
nvcc -V
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/%E6%88%AA%E5%9B%BE%202023-04-12%2015-40-26.png" width="500"/></div>
&nbsp;


&emsp;&emsp;至此驱动和cuda安装完成！！！
&nbsp;

-------------------------------------------------------------------------------------

3.安装Pycharm
&nbsp;

①到[Pycharm官网](https://www.jetbrains.com.cn/pycharm/download/)下载对应系统的安装包。本文选择Pycharm Community版本
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/QQ%E6%88%AA%E5%9B%BE20230412082108.png" width="500"/></div>
&nbsp
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

&emsp;&emsp;在Plugin中Markspace搜索Chinese，非SDk的一个，也就是下面一个，点击install，即可设置成中文。
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
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-06%2021-19-49.png" width="500"/></div>
&nbsp;

&emsp;&emsp;一直点击回车到空白处输入一个字符如q，接下来根据提示输入yes或者no。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/%E6%88%AA%E5%9B%BE%202023-04-12%2015-46-32.png" width="500"/></div>
&nbsp;&nbsp;
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/%E6%88%AA%E5%9B%BE%202023-04-12%2015-52-35.png" width="500"/></div>
&nbsp;&nbsp;

&emsp;&emsp;至此完成Miniconda安装！！！

-------------------------------------------------------------------------------------

5.安装Pytorch

&emsp;&emsp;根据[Pytorch](https://pytorch.org/get-started)提供的官方方案安装torch、torchvision
&nbsp;

&emsp;&emsp;以我为例，在nvcc -V终端执行后我们知道安装CUDA版本为11.5，那么我们安装的Pytorch版本只能比11.5低，也就是11.7、11.8不符合，我们需要安装早些版本的Pytorch，点击上方的红色字体进入寻找合适版本
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/QQ%E6%88%AA%E5%9B%BE20230412091200.png" width="500"/></div>
&nbsp;

&emsp;&emsp;从下图可以看到，1.12.1版本有CUDA版本为11.3的，低于我们自身的CUDA版本11.5，可以运行，找到pip安装命令（用conda也行，但是我们没换源，可能会很慢）。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/QQ%E6%88%AA%E5%9B%BE20230412091247.png" width="500"/></div>
&nbsp;

<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/QQ%E6%88%AA%E5%9B%BE20230412092048.png" width="500"/></div>
&nbsp;

```
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
```
&emsp;&emsp;别着急去终端安装，我们需要把Pytorch安装到虚环境中，因为不同的项目可能需要不同的Pytorch版本，如果Pytorch版本过高可能会导致运行不了。

&emsp;&emsp;所以Pytorch安装我们放到第6步中！！！

-------------------------------------------------------------------------------------

6.打开项目

①：下载[YOlOv5项目](https://github.com/ultralytics/yolov5/tree/v6.2)，解压并打开

②：点击右下方的解释器，将其设置为conda
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/%E6%88%AA%E5%9B%BE%202023-04-12%2015-57-23.png" width="500"/></div>
&nbsp;
③：打开左下方的终端，如果前面出现base字样说明进入虚环境了，如果没有请百度解决。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/%E6%88%AA%E5%9B%BE%202023-04-12%2015-57-51.png" width="500"/></div>
&nbsp;
&emsp;&emsp;输入上一步的命令，在虚环境中安装Pytorch

```
pip3 install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
```
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/%E6%88%AA%E5%9B%BE%202023-04-12%2015-58-58.png" width="500"/></div>
&nbsp;
&emsp;&emsp;输入命令，安装YOLOv5作者提供的需求文件中所需要的Python库

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

①：下载[yolov5s.pt](https://github.com/ultralytics/yolov5/tree/v6.2)
&nbsp;

&emsp;&emsp;在github端，进入YOLOv5项目，点击release，找到你下载的YOLOv5的对应版本的对应pt文件，不同版本的pt文件是不通用的，pt文件的详细解释可以看看别的文章，本文不再过多介绍。
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/QQ%E6%88%AA%E5%9B%BE20230412093548.png" width="500"/></div>
&nbsp;
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20%283%29/QQ%E6%88%AA%E5%9B%BE20230412093635.png" width="500"/></div>
&nbsp;

②：运行detect.py，一起看看输出结果吧！！！
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-10%2021-53-47.png" width="500"/></div>
&nbsp;
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-10%2021-54-07.png" width="500"/></div>
&nbsp;
<div align=center><img src="https://fjf-zdc.oss-cn-hangzhou.aliyuncs.com/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/%E6%88%AA%E5%9B%BE%202023-04-10%2021-54-15.png" width="500"/></div>
&nbsp;