import sys
from PyQt5 import QtWidgets, uic,QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from QPanda3D.QPanda3DWidget import QPanda3DWidget
from panda3d.ai import AIWorld, AICharacter

from  gui.Ui_main import Ui_MainWindow
from tools.mainpanda import PandaApp,Drone
from tools.cvcontrol import CvControl
from direct.stdpy import threading

import qdarkstyle

RESOURCE_DIR = "C:/Users/DjanivX/Pictures/"

class Ui(Ui_MainWindow):

    def __init__(self,MainWindow):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        # uic.loadUi('gui/main.ui', self)
        self.setupUi(MainWindow)

        # initialisation des variable
        self.showMenuLabel = True
        self.playState = False # Simulation non demarrer


        self.eventInit()
        self.initPandaWorld()
        self.initCvControl()

        MainWindow.show()
        MainWindow.setWindowTitle("Drone Simulator")

    def eventInit(self):
        self.btnMenu.clicked.connect(self.onMenu)
        self.btnPlay.clicked.connect(self.onPlay)
        self.actionMettre_en_pause.triggered.connect(self.onPlay)
        self.btnReset.clicked.connect(self.onRestart)
        self.actionQuitter.triggered.connect(self.onQuit)
        self.actionEloigner.triggered.connect(self.onEloigner)
        self.actionRapprocher.triggered.connect(self.onRapprocher)
        self.actionNouveau_drone.triggered.connect(self.onAddDrone)

    def initPandaWorld(self):


        self.pandaApp = PandaApp()
        pandaWidget = QPanda3DWidget(self.pandaApp)
        pandaWidget.setContentsMargins(0, 0, 0, 0)

        s = QSplitter(Qt.Vertical)
        s.setContentsMargins(0, 0, 0, 0)
        s.addWidget(pandaWidget)
        self.controlWidget = QWidget()
        self.controlWidget.setLayout(QVBoxLayout())
        self.controlLabel = QLabel()
        self.controlWidget.layout().addWidget(self.controlLabel)

        s.addWidget(self.controlWidget)

        self.pandaContainer.setLayout(QVBoxLayout())
        self.pandaContainer.layout().addWidget(pandaWidget)
        self.pandaContainer.setContentsMargins(0, 0, 0, 0)

        self.envList.insertItem(0,self.pandaApp.drone.nom)

    def initCvControl(self):
        self.cvControl = CvControl(self.pandaApp.drone)
        # self.cvthread = threading.Thread(target=cvControl.runControl)
        # self.cvthread.start()
        self.pandaApp.taskMgr.add(self.cvDetection,"CV Detection",priority=1)

    def cvDetection(self,task):
        self.cvControl.detectControl()
        return task.cont


    def onMenu(self):
        if self.showMenuLabel is True:
            # menuLabelContainer =QWidget()
            self.menuLabelContainer.hide()
            self.showMenuLabel = False
        else:
            self.menuLabelContainer.show()
            self.showMenuLabel = True

    def onPlay(self):
        if self.playState is True:
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("gui\\../images/play_24px.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)

            self.btnPlay.setIcon(icon1)
            self.lblPlay.setText("    Demarrer la simulation")
            self.actionMettre_en_pause.setText("Demarrer la simulation")
            self.playState = False

        else:
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(RESOURCE_DIR + "Drone Simulator/pause_24px.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)

            self.btnPlay.setIcon(icon1)
            self.lblPlay.setText("    Mettre en pause la simulation")
            self.actionMettre_en_pause.setText("Mettre en pause la simulation")
            self.playState = True
        self.pandaApp.appRunState = self.playState

    def onRestart(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("Confirmation")
        dlg.setText("Voulez-vous vraiment redemarrer la simulation?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            print("Yes!")
            self.pandaApp.reinit()

    def onQuit(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("Confirmation")
        dlg.setText("Voulez-vous vraiment fermer l'application?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            exit(0)

    def onAddDrone(self):
        n = len(self.pandaApp.droneList)
        drone = Drone("DRONE "+str(n))
        drone.attach(self.pandaApp.render)
        self.pandaApp.droneList.append(drone)
        self.envList.insertItem(n, drone.nom)

    def onRapprocher(self):
        self.pandaApp.CAM_POS = (0,-5,0)
    def onEloigner(self):
        self.pandaApp.CAM_POS = (0,5,0)




if __name__ == "__main__":
    dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyleSheet(dark_stylesheet)
    window = Ui(MainWindow)
    app.exec_()




#
# class MyWidget(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
#
#         self.button = QtWidgets.QPushButton("Click me!")
#         self.text = QtWidgets.QLabel("Hello World",
#                                      alignment=QtCore.Qt.AlignCenter)
#
#         self.layout = QtWidgets.QVBoxLayout(self)
#         self.layout.addWidget(self.text)
#         self.layout.addWidget(self.button)
#
#         self.button.clicked.connect(self.magic)
#
#     @QtCore.Slot()
#     def magic(self):
#         self.text.setText(random.choice(self.hello))
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#
#     widget = MyWidget()
#     widget.resize(800, 600)
#     widget.show()
#
#     sys.exit(app.exec_())