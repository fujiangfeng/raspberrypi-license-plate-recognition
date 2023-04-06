import sys
import cv2
from appgui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtGui
import detect


class Demo(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        self.setupUi(self)
        self.solt_init()
        self.label_3.setText('状态：等待检测...')

    ''' 槽函数初始化 '''

    def solt_init(self):
        self.pushButton.clicked.connect(self.webcam_detect)
        self.pushButton_2.clicked.connect(self.video_detect)
        self.pushButton_3.clicked.connect(self.picture_detect)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.open_video)

    def webcam_detect(self):
        detect.parse_opt('http://192.168.43.110:8081')

    def video_detect(self):
        self.label_3.setText('状态：视频检测中...')
        filepath = QFileDialog.getOpenFileName(None, "打开", './resource/videos', )
        detect.parse_opt(filepath[0])
        self.label_3.setText('状态：视频检测完成')
        video = 'runs/detect/exp/' + filepath[0].split('/')[-1]
        self.cap = cv2.VideoCapture(video)
        self.timer.start(100)

    def picture_detect(self):
        self.label_3.setText('状态：图片检测中...')
        filepath = QFileDialog.getOpenFileName(None, '打开','/resource/images', )
        detect.main(filepath[0])
        imgPath = 'runs/detect/exp/' + filepath[0].split('/')[-1]
        frame = cv2.imread(imgPath)
        ''' 将opencv格式图片转化为二进制图片 '''
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(img.data, img.shape[1], img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(showImage))
        self.label.setScaledContents(True)  # 自适应大小
        self.label_3.setText('状态：图片检测完成')

    def open_video(self):
        if self.cap.isOpened() == True:
            ret, frame = self.cap.read()
            if ret:
                ''' 将opencv格式图片转化为二进制图片 '''
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                showImage = QtGui.QImage(img.data, img.shape[1], img.shape[0], img.shape[1] * 3,
                                         QtGui.QImage.Format_RGB888)
                self.label.setPixmap(QtGui.QPixmap.fromImage(showImage))
                self.label.setScaledContents(True)  # 自适应大小
            else:
                self.cap.release()
                self.timer.stop()



if __name__ == '__main__':
    # 此行代码解决designer设计与运行比例不一致
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
