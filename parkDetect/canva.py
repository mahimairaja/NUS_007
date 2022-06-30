
from tempfile import tempdir
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import tensorflow as tf
import sys
import os
import uuid
import cv2
import numpy as np
from preprocess import process_image
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QHBoxLayout
class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Parkinson's Detector")

        # setting geometry to main window
        self.setGeometry(256, 256, 500, 400)

        # creating image object
        self.image = QImage(self.size(), QImage.Format_RGB32)

        # making image color to white
        self.image.fill(Qt.white)

        # variables
        # drawing flag
        self.drawing = False
        # default brush size
        self.brushSize = 4
        # default color
        self.brushColor = Qt.black

        # QPoint object to tract the point
        self.lastPoint = QPoint()

        # creating menu bar
        mainMenu = self.menuBar()

        # creating clear
        clc = mainMenu.addMenu("Clear")

        # adding detect option to main menu
        detect = mainMenu.addMenu("Detect")
      
        # # creating save action
        # saveAction = QAction("Save", self)
        # saveAction.setShortcut("Ctrl + S")
        # fileMenu.addAction(saveAction)
        # saveAction.triggered.connect(self.save)

        # creating clear action
        clearAction = QAction("Clear", self)
        clearAction.setShortcut("Ctrl + C")
        clc.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        # creating  action for detecting spiral
        spiralDetect = QAction('Spiral', self)
        spiralDetect.setShortcut('Ctrl + P')
        detect.addAction(spiralDetect)
        spiralDetect.triggered.connect(self.detect_spiral)
       
     

        # options for output label
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        font = self.label1.font()
        font.setPointSize(25)
        self.label1.setFont(font)
        self.label1.setAlignment(Qt.AlignHCenter)
       

        font = self.label2.font()
        font.setPointSize(25)
        self.label2.setFont(font)
        self.label2.setAlignment(Qt.AlignHCenter)
        
        # self.label3 = QLabel(self)
         
        # loading image
        # self.pixmap = QPixmap('template.jpeg')
 
        # adding image to label
        # self.label3.setPixmap(self.pixmap)
 
        # Optional, resize label to image size
        # self.label3.resize(self.pixmap.width(),
        #                   self.pixmap.height())





        self.label1.setGeometry(100,150,300,300)
        self.label2.setGeometry(100,100,500,100)
        # self.label3.setGeometry(100,50,300,600)
        # creating options for brush sizes
        # creating action for selecting pixel of 4px
        # pix_4 = QAction("4px", self)
        # b_size.addAction(pix_4)
        # pix_4.triggered.connect(self.Pixel_4)

        # # repeat above steps for different sizes
        # pix_7 = QAction("7px", self)
        # b_size.addAction(pix_7)
        # pix_7.triggered.connect(self.Pixel_7)

        # pix_9 = QAction("9px", self)
        # b_size.addAction(pix_9)
        # pix_9.triggered.connect(self.Pixel_9)

        # pix_12 = QAction("12px", self)
        # b_size.addAction(pix_12)
        # pix_12.triggered.connect(self.Pixel_12)


    # method for checking mouse clicks
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    # method for tracking mouse activity
    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)

            # set the pen of the painter
            painter.setPen(QPen(self.brushColor, self.brushSize,
                                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

            # draw line from the last point of cursor to the current point
            # this will draw only one step
            painter.drawLine(self.lastPoint, event.pos())

            # change the last point
            self.lastPoint = event.pos()
            # update
            self.update()

    # method for mouse left button release
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            # make drawing flag false
            self.drawing = False

    # paint event
    def paintEvent(self, event):
        # create a canvas
        canvasPainter = QPainter(self)

        # draw rectangle  on the canvas
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())


    # # method for saving canvas
    # def save(self):
    #     filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
    #                                               "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

    #     if filePath == "":
    #         return
    #     self.image.save(filePath)

    # method for clearing every thing on canvas
    def clear(self):
        self.image.fill(Qt.white)
        self.label1.setText("")
        self.label2.setText("")
        self.update()

    
    # methods for detecting image
    def detect_spiral(self):
        # save temporary image
        json_file = open('models/model_structure.json','r')
        model_structure = json_file.read()
        json_file.close()
        model = tf.keras.models.model_from_json(model_structure)
        model.load_weights('models/model_weights.h5')
        self.image.save('temp.png', 'png')
        
        img=process_image('temp.png')
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imwrite('temporay.jpg',img)
        
        temp_img = cv2.imread('temporay.jpg')
        resize = tf.image.resize(temp_img, (256,256))
        pred = model.predict(np.expand_dims(resize/255, 0))

        # make predictions from image
        # pred = predict_image('temp.png', spiralModel)
        # output predictions red for parkinson's green for healthy
        p=str(pred)
        if(pred<0.5):
          self.label1.setText("Healthy")
          self.label2.setText(p)
          
          
        else:
            self.label1.setText("Likely to have parkinson's")
            self.label2.setText(p)
        self.label1.setStyleSheet(
            "color: green;") if pred < 0.5 else self.label1.setStyleSheet("color: red;")
        self.label2.setStyleSheet(
            "color: green;") if pred < 0.5 else self.label2.setStyleSheet("color: red;")

  # methods for changing pixel sizes
    # def Pixel_4(self):
    #     self.brushSize = 4

    # def Pixel_7(self):
    #     self.brushSize = 7

    # def Pixel_9(self):
    #     self.brushSize = 9

    # def Pixel_12(self):
    #     self.brushSize = 12


# create pyqt5 app
canva = QApplication(sys.argv)
window = Window()
window.show()

# start the app
sys.exit(canva.exec())