from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtCore import QTimer, QDir, Qt, QUrl
import os
import numpy as np
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QApplication,
                             QLabel, QFileDialog, QStyle, QVBoxLayout, QComboBox, QButtonGroup, QInputDialog,
                             QTableWidgetItem)

from AKBANKGui import Ui_MainWindow
import numpy
import sys
import cv2
import glob, random
import tensorflow as tf

from keras.models import load_model
# GUI FILE
from app_modules import *

MODEL = load_model('28-0.95.h5')
#MODEL = tf.keras.models.load_model('my_model.keras')

count = 0

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Main Window - Python Base')
        UIFunctions.labelTitle(self, 'Main Window - Python Base')
        UIFunctions.labelDescription(self, 'Artçı Kartallar')
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)

        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_new_user")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        image = cv2.imread("kapak.png")
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_BGR888)
        self.ui.label_66.setPixmap(QPixmap.fromImage(qImg))

        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "WM", "", True)

        ## ==> END ##

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################

        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################

        ## ==> QTableWidget RARAMETERS
        ########################################################################
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ## ==> END ##

        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

        ########################################################################
        ## MENUS ==> DYNAMIC MENUS FUNCTIONS
        ########################################################################


        self.fillLabels()
        self.ui.pushButton_1.clicked.connect(self.detect1)
        self.ui.pushButton_2.clicked.connect(self.detect2)
        self.ui.pushButton_3.clicked.connect(self.detect3)
        self.ui.pushButton_4.clicked.connect(self.detect4)
        self.ui.pushButton_5.clicked.connect(self.detect5)
        self.ui.pushButton_6.clicked.connect(self.detect6)
        self.ui.pushButton_7.clicked.connect(self.detect7)
        self.ui.pushButton_8.clicked.connect(self.detect8)
        self.ui.pushButton_9.clicked.connect(self.detect9)
        self.ui.pushButton_10.clicked.connect(self.detect10)
        self.ui.pushButton_11.clicked.connect(self.detect11)
        self.ui.pushButton_12.clicked.connect(self.detect12)

        self.ui.btn_home.clicked.connect(self.home)
        self.ui.btn_project.clicked.connect(self.project)
        self.ui.btn_model.clicked.connect(self.model)

    def home(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

    def project(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)

    def model(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.page)



    def droneS(self):

        file_path_type = ["./EQ_images/s.bina/*.jpg"]
        images = glob.glob(random.choice(file_path_type))
        random_image = random.choice(images)
        random_image = cv2.imread(random_image)
        return random_image

    def droneY(self):

        file_path_type = ["./EQ_images/y.bina/*.jpg"]
        images = glob.glob(random.choice(file_path_type))
        random_image = random.choice(images)
        random_image = cv2.imread(random_image)
        return random_image

    def fillLabels(self):

        #yıkık bina
        self.image1 = self.droneY()
        image = self.image1
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_BGR888)
        self.ui.label_1.setPixmap(QPixmap.fromImage(qImg))

        # sağlam bina
        self.image12 = self.droneS()
        image = self.image12
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_BGR888)
        self.ui.label_12.setPixmap(QPixmap.fromImage(qImg))

        # sağlam bina
        self.image2 = self.droneS()
        image = self.image2
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_BGR888)
        self.ui.label_2.setPixmap(QPixmap.fromImage(qImg))

        # sağlam bina
        self.image3 = self.droneS()
        image = self.image3
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_BGR888)
        self.ui.label_3.setPixmap(QPixmap.fromImage(qImg))

        # yıkık bina
        self.image4 = self.droneY()
        image = self.image4
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_BGR888)
        self.ui.label_4.setPixmap(QPixmap.fromImage(qImg))

        # yıkık bina
        self.image11 = self.droneY()
        image = self.image11
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_BGR888)
        self.ui.label_11.setPixmap(QPixmap.fromImage(qImg))

        # sağlam bina
        self.image10 = self.droneS()
        image = self.image10
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_BGR888)
        self.ui.label_10.setPixmap(QPixmap.fromImage(qImg))

        # sağlam bina
        self.image9 = self.droneS()
        image = self.image9
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_BGR888)
        self.ui.label_9.setPixmap(QPixmap.fromImage(qImg))

        # yıkık bina
        self.image8 = self.droneY()
        image  = self.image8
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_BGR888)
        self.ui.label_8.setPixmap(QPixmap.fromImage(qImg))

        # yıkık bina
        self.image7 = self.droneY()
        image = self.image7
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_BGR888)
        self.ui.label_7.setPixmap(QPixmap.fromImage(qImg))

        # yıkık bina
        self.image6 = self.droneY()
        image = self.image6
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_BGR888)
        self.ui.label_6.setPixmap(QPixmap.fromImage(qImg))

        # yıkık bina
        self.image5 = self.droneY()
        image = self.image5
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_BGR888)
        self.ui.label_5.setPixmap(QPixmap.fromImage(qImg))


    def detect1(self):
        global count
        self.image1 = cv2.resize(self.image1,(150,150))
        #self.image1  = cv2.cvtColor(self.image1 , cv2.COLOR_BGR2GRAY)
        self.image1 = self.image1 / 255.0
        self.image1 = numpy.expand_dims(self.image1,axis=0)
        prediction = MODEL.predict(self.image1)
        lat = "39.944"
        long = "32.869"
        result = ""
        if (np.argmax(prediction) == 0):
            self.ui.pushButton_1.setText("Saglam")
            result = "Saglam"
        else:
            self.ui.pushButton_1.setText("Yikik")
            result = "Yikik"
        self.ui.tableWidget.setItem(count, 0, QTableWidgetItem(lat))
        self.ui.tableWidget.setItem(count, 1, QTableWidgetItem(long))
        self.ui.tableWidget.setItem(count, 2, QTableWidgetItem(result))
        count = count + 1
        print(prediction)

    def detect2(self):
        global count
        self.image2 = cv2.resize(self.image2, (150, 150))
        #self.image2 = cv2.cvtColor(self.image2, cv2.COLOR_BGR2GRAY)
        self.image2 = self.image2 / 255.0
        self.image2 = numpy.expand_dims(self.image2, axis=0)
        prediction = MODEL.predict(self.image2)
        lat = "39.945"
        long = "32.870"
        result = ""
        if (np.argmax(prediction) == 0):
            self.ui.pushButton_2.setText("Saglam")
            result = "Saglam"
        else:
            self.ui.pushButton_2.setText("Yikik")
            result = "Yikik"
        self.ui.tableWidget.setItem(count, 0, QTableWidgetItem(lat))
        self.ui.tableWidget.setItem(count, 1, QTableWidgetItem(long))
        self.ui.tableWidget.setItem(count, 2, QTableWidgetItem(result))
        count = count + 1
        print(prediction)

    def detect3(self):
        global count
        self.image3 = cv2.resize(self.image3, (150, 150))
        #self.image3 = cv2.cvtColor(self.image3, cv2.COLOR_BGR2GRAY)
        self.image3 = self.image3 / 255.0
        self.image3 = numpy.expand_dims(self.image3, axis=0)
        prediction = MODEL.predict(self.image3)
        lat = "39.945"
        long = "32.872"
        result = ""
        if (np.argmax(prediction)==0):
            self.ui.pushButton_3.setText("Saglam")
            result = "Saglam"
        else:
            self.ui.pushButton_3.setText("Yikik")
            result = "Yikik"
        self.ui.tableWidget.setItem(count, 0, QTableWidgetItem(lat))
        self.ui.tableWidget.setItem(count, 1, QTableWidgetItem(long))
        self.ui.tableWidget.setItem(count, 2, QTableWidgetItem(result))
        count = count + 1
        print(prediction)

    def detect4(self):
        global count
        self.image4 = cv2.resize(self.image4, (150, 150))
        #self.image4 = cv2.cvtColor(self.image4, cv2.COLOR_BGR2GRAY)
        self.image4 = self.image4 / 255.0
        self.image4 = numpy.expand_dims(self.image4, axis=0)
        prediction = MODEL.predict(self.image4)
        lat = "39.945"
        long = "32.871"
        result = ""
        if (np.argmax(prediction) == 0):
            self.ui.pushButton_4.setText("Saglam")
            result = "Saglam"
        else:
            self.ui.pushButton_4.setText("Yikik")
            result = "Yikik"
        self.ui.tableWidget.setItem(count, 0, QTableWidgetItem(lat))
        self.ui.tableWidget.setItem(count, 1, QTableWidgetItem(long))
        self.ui.tableWidget.setItem(count, 2, QTableWidgetItem(result))
        count = count + 1
        print(prediction)

    def detect5(self):
        global count
        self.image5 = cv2.resize(self.image5, (150, 150))
        #self.image5 = cv2.cvtColor(self.image5, cv2.COLOR_BGR2GRAY)
        self.image5 = self.image5 / 255.0
        self.image5 = numpy.expand_dims(self.image5, axis=0)
        prediction = MODEL.predict(self.image5)
        lat = "39.944"
        long = "32.870"
        result = ""
        if (np.argmax(prediction) == 0):
            self.ui.pushButton_5.setText("Saglam")
            result = "Saglam"
        else:
            self.ui.pushButton_5.setText("Yikik")
            result = "Yikik"
        self.ui.tableWidget.setItem(count, 0, QTableWidgetItem(lat))
        self.ui.tableWidget.setItem(count, 1, QTableWidgetItem(long))
        self.ui.tableWidget.setItem(count, 2, QTableWidgetItem(result))
        count = count + 1
        print(prediction)

    def detect6(self):
        global count
        self.image6 = cv2.resize(self.image6, (150, 150))
        #self.image6 = cv2.cvtColor(self.image6, cv2.COLOR_BGR2GRAY)
        self.image6 = self.image6 / 255.0
        self.image6 = numpy.expand_dims(self.image6, axis=0)
        prediction = MODEL.predict(self.image6)
        lat = "39.945"
        long = "32.869"
        result = ""
        if (np.argmax(prediction) == 0):
            self.ui.pushButton_6.setText("Saglam")
            result = "Saglam"
        else:
            self.ui.pushButton_6.setText("Yikik")
            result = "Yikik"
        self.ui.tableWidget.setItem(count, 0, QTableWidgetItem(lat))
        self.ui.tableWidget.setItem(count, 1, QTableWidgetItem(long))
        self.ui.tableWidget.setItem(count, 2, QTableWidgetItem(result))
        count = count + 1
        print(prediction)

    def detect7(self):
        global count
        self.image7 = cv2.resize(self.image7, (150, 150))
        #self.image7 = cv2.cvtColor(self.image7, cv2.COLOR_BGR2GRAY)
        self.image7 = self.image7 / 255.0
        self.image7 = numpy.expand_dims(self.image7, axis=0)
        prediction = MODEL.predict(self.image7)
        lat = "39.943"
        long = "32.870"
        result = ""
        if (np.argmax(prediction) == 0):
            self.ui.pushButton_7.setText("Saglam")
            result = "Saglam"
        else:
            self.ui.pushButton_7.setText("Yikik")
            result = "Yikik"
        self.ui.tableWidget.setItem(count, 0, QTableWidgetItem(lat))
        self.ui.tableWidget.setItem(count, 1, QTableWidgetItem(long))
        self.ui.tableWidget.setItem(count, 2, QTableWidgetItem(result))
        count = count + 1
        print(prediction)

    def detect8(self):
        global count
        self.image8 = cv2.resize(self.image8, (150, 150))
        #self.image8 = cv2.cvtColor(self.image8, cv2.COLOR_BGR2GRAY)
        self.image8 = self.image8 / 255.0
        self.image8 = numpy.expand_dims(self.image8, axis=0)
        prediction = MODEL.predict(self.image8)
        lat = "39.943"
        long = "32.869"
        result = ""
        if (np.argmax(prediction) == 0):
            self.ui.pushButton_8.setText("Saglam")
            result = "Saglam"
        else:
            self.ui.pushButton_8.setText("Yikik")
            result = "Yikik"
        self.ui.tableWidget.setItem(count, 0, QTableWidgetItem(lat))
        self.ui.tableWidget.setItem(count, 1, QTableWidgetItem(long))
        self.ui.tableWidget.setItem(count, 2, QTableWidgetItem(result))
        count = count + 1
        print(prediction)

    def detect9(self):
        global count
        self.image9 = cv2.resize(self.image9, (150, 150))
        #self.image9= cv2.cvtColor(self.image9, cv2.COLOR_BGR2GRAY)
        self.image9 = self.image9 / 255.0
        self.image9 = numpy.expand_dims(self.image9, axis=0)
        prediction = MODEL.predict(self.image9)
        lat = "39.943"
        long = "32.868"
        result = ""
        if (np.argmax(prediction)==0):
            self.ui.pushButton_9.setText("Saglam")
            result = "Saglam"
        else:
            self.ui.pushButton_9.setText("Yikik")
            result = "Yikik"
        self.ui.tableWidget.setItem(count, 0, QTableWidgetItem(lat))
        self.ui.tableWidget.setItem(count, 1, QTableWidgetItem(long))
        self.ui.tableWidget.setItem(count, 2, QTableWidgetItem(result))
        count = count + 1
        print(prediction)

    def detect10(self):
        global count
        self.image10 = cv2.resize(self.image10, (150, 150))
        #self.image10 = cv2.cvtColor(self.image10, cv2.COLOR_BGR2GRAY)
        self.image10 = self.image10 / 255.0
        self.image10 = numpy.expand_dims(self.image10, axis=0)
        prediction = MODEL.predict(self.image10)
        lat = "39.944"
        long = "32.871"
        result = ""
        if (np.argmax(prediction) == 0):
            self.ui.pushButton_10.setText("Saglam")
            result = "Saglam"
        else:
            self.ui.pushButton_10.setText("Yikik")
            result = "Yikik"
        self.ui.tableWidget.setItem(count, 0, QTableWidgetItem(lat))
        self.ui.tableWidget.setItem(count, 1, QTableWidgetItem(long))
        self.ui.tableWidget.setItem(count, 2, QTableWidgetItem(result))
        count = count + 1
        print(prediction)

    def detect11(self):
        global count
        self.image11 = cv2.resize(self.image11, (150, 150))
        #self.image11 = cv2.cvtColor(self.image11, cv2.COLOR_BGR2GRAY)
        self.image11 = self.image11 / 255.0
        self.image11 = numpy.expand_dims(self.image11, axis=0)
        prediction = MODEL.predict(self.image11)
        lat = "39.943"
        long = "32.871"
        result = ""
        if (np.argmax(prediction) == 0):
            self.ui.pushButton_11.setText("Saglam")
            result = "Saglam"
        else:
            self.ui.pushButton_11.setText("Yikik")
            result = "Yikik"
        self.ui.tableWidget.setItem(count, 0, QTableWidgetItem(lat))
        self.ui.tableWidget.setItem(count, 1, QTableWidgetItem(long))
        self.ui.tableWidget.setItem(count, 2, QTableWidgetItem(result))
        count = count + 1
        print(prediction)

    def detect12(self):
        global count
        self.image12 = cv2.resize(self.image12, (150, 150))
        #self.image12 = cv2.cvtColor(self.image12, cv2.COLOR_BGR2GRAY)
        self.image12 = self.image12 / 255.0
        self.image12 = numpy.expand_dims(self.image12, axis=0)
        prediction = MODEL.predict(self.image12)
        lat = "39.944"
        long = "32.872"
        result = ""
        if (np.argmax(prediction) == 0):
            self.ui.pushButton_12.setText("Saglam")
            result = "Saglam"
        else:
            self.ui.pushButton_12.setText("Yikik")
            result = "Yikik"
        self.ui.tableWidget.setItem(count, 0, QTableWidgetItem(lat))
        self.ui.tableWidget.setItem(count, 1, QTableWidgetItem(long))
        self.ui.tableWidget.setItem(count, 2, QTableWidgetItem(result))
        count = count + 1
        print(prediction)


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
"""
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_model":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page)

        # PAGE NEW USER
        if btnWidget.objectName() == "btn_project":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
"""
    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################



if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
