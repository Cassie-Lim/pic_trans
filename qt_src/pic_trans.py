from PyQt5 import QtWidgets
from qt_window import Ui_SRS # 导入ui文件转换后的py文件
from PyQt5.QtWidgets import QFileDialog
import pandas as pd

import cv2
import argparse
import numpy as np

class mywindow(QtWidgets.QWidget, Ui_SRS):
    def  __init__ (self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.write_folder)
        self.pushButton.clicked.connect(self.read_file)

        self.pushButton_4.clicked.connect(self.process1)  # 风格1
        self.pushButton_5.clicked.connect(self.process2)  # 风格2
        self.pushButton_6.clicked.connect(self.process3)  # 风格3
        self.pushButton_7.clicked.connect(self.process4)  # 风格4
        self.pushButton_8.clicked.connect(self.process5)  # 风格5
        self.pushButton_9.clicked.connect(self.process6)  # 风格6

    def read_file(self):
        #选取文件
        filename, filetype =QFileDialog.getOpenFileName(self, "选取文件", "C:/", "All Files(*);;Text Files(*.csv)")
        print(filename, filetype)
        self.lineEdit.setText(filename)

    def write_folder(self):
        #选取文件夹
        foldername = QFileDialog.getExistingDirectory(self, "选取文件夹", "C:/")
        print(foldername)
        self.lineEdit_2.setText(foldername)

    # 进行处理
    def process1(self):
        try:
            #获取文件路径
            file_path = self.lineEdit.text()
            #获取文件夹路径
            folder_path = self.lineEdit_2.text()

            # 中间可以进行对文件的任意操作
            ap = argparse.ArgumentParser()
            ap.add_argument('-p', '--picture-path', type=str, help='path to input picture')
            ap.add_argument('-op', '--operation', type=int,
                            help='operation: 1 for pencil-mode; 2 for Chinese painting; 3 for line drawing; 4 for western painting;'
                                 ' 5 for pencil sketch')
            args = vars(ap.parse_args())
            op = args['operation']
            img = cv2.imread(file_path)
            cv2.imshow('original', img)

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Blur the image using Gaussian Blur
            # 高斯核服从正态分布，核数越大，越模糊
            gray_blur = cv2.GaussianBlur(gray, (75, 75), 0)
            # Convert the image into pencil sketch
            cartoon = cv2.divide(gray, gray_blur, scale=250.0)
            cv2.imwrite(folder_path + '\cartoon.jpg', cartoon)
            cv2.imshow('cartoon.jpg', cartoon)
            cv2.waitKey()
            cv2.destroyAllWindows()

            success_result = r'转换成功！'
            self.label_3.setText(success_result)

        except:
            print(file_path)
            fail_result = r'转换失败！'
            self.label_3.setText(fail_result)

    def process2(self):
        try:
            # 获取文件路径
            file_path = self.lineEdit.text()
            # 获取文件夹路径
            folder_path = self.lineEdit_2.text()

            # 中间可以进行对文件的任意操作
            ap = argparse.ArgumentParser()
            ap.add_argument('-p', '--picture-path', type=str, help='path to input picture')
            ap.add_argument('-op', '--operation', type=int,
                            help='operation: 1 for pencil-mode; 2 for Chinese painting; 3 for line drawing; 4 for western painting;'
                                 ' 5 for pencil sketch')
            args = vars(ap.parse_args())
            op = args['operation']
            img = cv2.imread(file_path)

            # convert the image into grayscale image
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Blur the grayscale image with median blur中值滤波
            gray_blur = cv2.medianBlur(gray, 3)
            # Apply adaptive thresholding to detect edges检测图像边缘
            edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9,
                                          9)  # 自适应均值滤波
            # Sharpen the image锐化图像
            color = cv2.detailEnhance(img, sigma_s=5, sigma_r=0.5)
            Chinese_painting = cv2.bitwise_and(color, color, mask=edges)
            cv2.imwrite(folder_path + '\Chinese_painting.jpg', Chinese_painting)
            cv2.imshow('Chinese_painting.jpg', Chinese_painting)
            cv2.waitKey()
            cv2.destroyAllWindows()

            success_result = r'转换成功！'
            self.label_3.setText(success_result)

        except:
            print(file_path)
            fail_result = r'转换失败！'
            self.label_3.setText(fail_result)

    def process3(self):
        try:
            # 获取文件路径
            file_path = self.lineEdit.text()
            # 获取文件夹路径
            folder_path = self.lineEdit_2.text()

            # 中间可以进行对文件的任意操作
            ap = argparse.ArgumentParser()
            ap.add_argument('-p', '--picture-path', type=str, help='path to input picture')
            ap.add_argument('-op', '--operation', type=int,
                            help='operation: 1 for pencil-mode; 2 for Chinese painting; 3 for line drawing; 4 for western painting;'
                                 ' 5 for pencil sketch')
            args = vars(ap.parse_args())
            op = args['operation']
            img = cv2.imread(file_path)

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 3)
            edges = cv2.Laplacian(gray, -1, ksize=5)
            edges_inv = 255 - edges
            dummy, line_drawing = cv2.threshold(edges_inv, 0, 255, cv2.THRESH_BINARY)
            cv2.imwrite(folder_path + '\line_drawing.jpg', line_drawing)
            cv2.imshow('line_drawing.jpg', line_drawing)
            cv2.waitKey()
            cv2.destroyAllWindows()

            success_result = r'转换成功！'
            self.label_3.setText(success_result)

        except:
            print(file_path)
            fail_result = r'转换失败！'
            self.label_3.setText(fail_result)

    def process4(self):
        try:
            # 获取文件路径
            file_path = self.lineEdit.text()
            # 获取文件夹路径
            folder_path = self.lineEdit_2.text()

            # 中间可以进行对文件的任意操作
            ap = argparse.ArgumentParser()
            ap.add_argument('-p', '--picture-path', type=str, help='path to input picture')
            ap.add_argument('-op', '--operation', type=int,
                            help='operation: 1 for pencil-mode; 2 for Chinese painting; 3 for line drawing; 4 for western painting;'
                                 ' 5 for pencil sketch')
            args = vars(ap.parse_args())
            op = args['operation']
            img = cv2.imread(file_path)

            mix_pixel = int(img.shape[0] / 150)
            oil_painting = cv2.xphoto.oilPainting(img, mix_pixel, 1)
            cv2.imwrite(folder_path + '\oil_painting.jpg', oil_painting)
            cv2.imshow('oil_painting.jpg', oil_painting)
            cv2.waitKey()
            cv2.destroyAllWindows()

            success_result = r'转换成功！'
            self.label_3.setText(success_result)

        except:
            print(file_path)
            fail_result = r'转换失败！'
            self.label_3.setText(fail_result)

    def process5(self):
        try:
            # 获取文件路径
            file_path = self.lineEdit.text()
            # 获取文件夹路径
            folder_path = self.lineEdit_2.text()

            # 中间可以进行对文件的任意操作
            ap = argparse.ArgumentParser()
            ap.add_argument('-p', '--picture-path', type=str, help='path to input picture')
            ap.add_argument('-op', '--operation', type=int,
                            help='operation: 1 for pencil-mode; 2 for Chinese painting; 3 for line drawing; 4 for western painting;'
                                 ' 5 for pencil sketch')
            args = vars(ap.parse_args())
            op = args['operation']
            img = cv2.imread(file_path)

            grey, color = cv2.pencilSketch(img, sigma_s=20, sigma_r=0.15, shade_factor=0.04)
            cv2.imwrite(folder_path + '\grey.jpg', grey)
            cv2.imshow('grey.jpg', grey)
            cv2.waitKey()
            cv2.destroyAllWindows()

            success_result = r'转换成功！'
            self.label_3.setText(success_result)

        except:
            print(file_path)
            fail_result = r'转换失败！'
            self.label_3.setText(fail_result)

    def process6(self):
        try:
            # 获取文件路径
            file_path = self.lineEdit.text()
            # 获取文件夹路径
            folder_path = self.lineEdit_2.text()

            # 中间可以进行对文件的任意操作
            ap = argparse.ArgumentParser()
            ap.add_argument('-p', '--picture-path', type=str, help='path to input picture')
            ap.add_argument('-op', '--operation', type=int,
                            help='operation: 1 for pencil-mode; 2 for Chinese painting; 3 for line drawing; 4 for western painting;'
                                 ' 5 for pencil sketch')
            args = vars(ap.parse_args())
            op = args['operation']
            img = cv2.imread(file_path)

            grey, color = cv2.pencilSketch(img, sigma_s=20, sigma_r=0.15, shade_factor=0.04)
            cv2.imwrite(folder_path + '\color.jpg', color)
            cv2.imshow('color.jpg', color)
            cv2.waitKey()
            cv2.destroyAllWindows()

            success_result = r'转换成功！'
            self.label_3.setText(success_result)

        except:
            print(file_path)
            fail_result = r'转换失败！'
            self.label_3.setText(fail_result)

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())