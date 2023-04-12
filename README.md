# raspberrypi-license-plate-recognition

&emsp;&emsp;写在最前面：将该项目上传网络的初衷是因为网上有很多优秀的贴子，但是有些年份较早，有些完整性不高，我就把很多帖子整合到一起，其中继承了很多大佬的经验，在此非常感谢各位前辈为我们留下很好的经验贴。因为我也是第一次接触深度学习，有不妥之处还望大佬指出。

&emsp;&emsp;本项目是基于树莓派的深度学习车牌检测和识别系统，采用YOLOv5+LPRNet+STNet。YOLOv5是用于检测车牌位置，LPRNet是用于车牌字符识别，STNet是用于矫正车牌，使得车牌字符识别率更高。
本项目训练了多个模型运行在树莓派上，包括yolov5 5.0版本。yolov5 6.1版本，yolov5 lite版本，最终采用yolov5 6.1版本的YOLOv5n对应的onnx文件，其运行速度和准确率相较于其他两个都有一定的提升。

&emsp;&emsp;目前已经编写了：

&emsp;&emsp;1.树莓派深度学习环境从0开始配置，详情请看RaspberrySetting.md。

&emsp;&emsp;2.Ubuntu深度学习环境从0开始配置，详情请看Deeplearning.md。

&emsp;&emsp;后续还会编写如何训练车牌检测以及识别等，有问题可以加群交流。

&emsp;&emsp;车牌识别交流群：
```
572145690
```
