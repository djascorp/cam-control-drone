# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(855, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(35, 0))
        self.widget.setMaximumSize(QtCore.QSize(35, 16777215))
        self.widget.setStyleSheet("background-color: rgb(69, 83, 100);")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.btnMenu = QtWidgets.QToolButton(self.widget_4)
        self.btnMenu.setGeometry(QtCore.QRect(0, 0, 35, 27))
        self.btnMenu.setStyleSheet("border-radius: 0px;")
        self.btnMenu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui\\../images/menu_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMenu.setIcon(icon)
        self.btnMenu.setIconSize(QtCore.QSize(32, 24))
        self.btnMenu.setObjectName("btnMenu")
        self.btnPlay = QtWidgets.QToolButton(self.widget_4)
        self.btnPlay.setGeometry(QtCore.QRect(0, 50, 35, 27))
        self.btnPlay.setStyleSheet("border-radius: 0px;\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("gui\\../images/play_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlay.setIcon(icon1)
        self.btnPlay.setIconSize(QtCore.QSize(32, 24))
        self.btnPlay.setObjectName("btnPlay")
        self.btnReset = QtWidgets.QToolButton(self.widget_4)
        self.btnReset.setGeometry(QtCore.QRect(0, 100, 35, 27))
        self.btnReset.setStyleSheet("border-radius: 0px;\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("gui\\../images/restart_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReset.setIcon(icon2)
        self.btnReset.setIconSize(QtCore.QSize(32, 24))
        self.btnReset.setObjectName("btnReset")
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget)
        self.menuLabelContainer = QtWidgets.QWidget(self.centralwidget)
        self.menuLabelContainer.setMinimumSize(QtCore.QSize(180, 0))
        self.menuLabelContainer.setMaximumSize(QtCore.QSize(180, 16777215))
        self.menuLabelContainer.setStyleSheet("background-color: rgb(84, 104, 122);\n"
"color: rgb(255, 255, 255);")
        self.menuLabelContainer.setObjectName("menuLabelContainer")
        self.label = QtWidgets.QLabel(self.menuLabelContainer)
        self.label.setGeometry(QtCore.QRect(0, 0, 181, 31))
        self.label.setMinimumSize(QtCore.QSize(0, 24))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lblPlay = QtWidgets.QLabel(self.menuLabelContainer)
        self.lblPlay.setGeometry(QtCore.QRect(0, 50, 181, 31))
        self.lblPlay.setMinimumSize(QtCore.QSize(0, 24))
        self.lblPlay.setObjectName("lblPlay")
        self.lblRestart = QtWidgets.QLabel(self.menuLabelContainer)
        self.lblRestart.setGeometry(QtCore.QRect(0, 100, 181, 31))
        self.lblRestart.setMinimumSize(QtCore.QSize(0, 24))
        self.lblRestart.setObjectName("lblRestart")
        self.horizontalLayout.addWidget(self.menuLabelContainer)
        self.pandaContainer = QtWidgets.QWidget(self.centralwidget)
        self.pandaContainer.setObjectName("pandaContainer")
        self.horizontalLayout.addWidget(self.pandaContainer)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(280, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.widget_3)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.envList = QtWidgets.QListWidget(self.tab_3)
        self.envList.setObjectName("envList")
        self.verticalLayout_3.addWidget(self.envList)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 271, 33))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.nomObject = QtWidgets.QLabel(self.formLayoutWidget)
        self.nomObject.setObjectName("nomObject")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nomObject)
        self.nomObjectWidget = QtWidgets.QWidget(self.formLayoutWidget)
        self.nomObjectWidget.setObjectName("nomObjectWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.nomObjectWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.nomObjectWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nomObjectWidget)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout.addWidget(self.widget_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 855, 21))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuSimulation = QtWidgets.QMenu(self.menubar)
        self.menuSimulation.setObjectName("menuSimulation")
        self.menucamera = QtWidgets.QMenu(self.menubar)
        self.menucamera.setObjectName("menucamera")
        self.menuEnvironnement = QtWidgets.QMenu(self.menubar)
        self.menuEnvironnement.setObjectName("menuEnvironnement")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNouveau = QtWidgets.QAction(MainWindow)
        self.actionNouveau.setObjectName("actionNouveau")
        self.actionEnregistrer = QtWidgets.QAction(MainWindow)
        self.actionEnregistrer.setObjectName("actionEnregistrer")
        self.actionEnregistrer_2 = QtWidgets.QAction(MainWindow)
        self.actionEnregistrer_2.setObjectName("actionEnregistrer_2")
        self.actionEnregistrer_sous = QtWidgets.QAction(MainWindow)
        self.actionEnregistrer_sous.setObjectName("actionEnregistrer_sous")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionDemarrer_la_simulation = QtWidgets.QAction(MainWindow)
        self.actionDemarrer_la_simulation.setObjectName("actionDemarrer_la_simulation")
        self.actionMettre_en_pause = QtWidgets.QAction(MainWindow)
        self.actionMettre_en_pause.setObjectName("actionMettre_en_pause")
        self.actionRedemarrer_la_simulation = QtWidgets.QAction(MainWindow)
        self.actionRedemarrer_la_simulation.setObjectName("actionRedemarrer_la_simulation")
        self.actionRapprocher = QtWidgets.QAction(MainWindow)
        self.actionRapprocher.setObjectName("actionRapprocher")
        self.actionEloigner = QtWidgets.QAction(MainWindow)
        self.actionEloigner.setObjectName("actionEloigner")
        self.actionNouveau_drone = QtWidgets.QAction(MainWindow)
        self.actionNouveau_drone.setObjectName("actionNouveau_drone")
        self.menuFichier.addAction(self.actionNouveau)
        self.menuFichier.addAction(self.actionEnregistrer)
        self.menuFichier.addAction(self.actionEnregistrer_2)
        self.menuFichier.addAction(self.actionEnregistrer_sous)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuitter)
        self.menuSimulation.addAction(self.actionMettre_en_pause)
        self.menuSimulation.addAction(self.actionRedemarrer_la_simulation)
        self.menucamera.addAction(self.actionRapprocher)
        self.menucamera.addAction(self.actionEloigner)
        self.menuEnvironnement.addAction(self.actionNouveau_drone)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuSimulation.menuAction())
        self.menubar.addAction(self.menucamera.menuAction())
        self.menubar.addAction(self.menuEnvironnement.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnPlay.setText(_translate("MainWindow", "..."))
        self.btnReset.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">&nbsp;&nbsp;Menu</span></p></body></html>"))
        self.lblPlay.setText(_translate("MainWindow", "    Demarrer la simulation"))
        self.lblRestart.setText(_translate("MainWindow", "    Redemarrer la simulation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Environnement"))
        self.nomObject.setText(_translate("MainWindow", "Nom de l\'objet"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Propriétés"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuSimulation.setTitle(_translate("MainWindow", "Simulation"))
        self.menucamera.setTitle(_translate("MainWindow", "Camera"))
        self.menuEnvironnement.setTitle(_translate("MainWindow", "Environnement"))
        self.actionNouveau.setText(_translate("MainWindow", "Nouveau"))
        self.actionEnregistrer.setText(_translate("MainWindow", "Ouvrir..."))
        self.actionEnregistrer_2.setText(_translate("MainWindow", "Enregistrer"))
        self.actionEnregistrer_sous.setText(_translate("MainWindow", "Enregistrer sous ..."))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionDemarrer_la_simulation.setText(_translate("MainWindow", "Demarrer la simulation"))
        self.actionMettre_en_pause.setText(_translate("MainWindow", "Demarrer la simulation"))
        self.actionRedemarrer_la_simulation.setText(_translate("MainWindow", "Redemarrer la simulation"))
        self.actionRapprocher.setText(_translate("MainWindow", "Rapprocher"))
        self.actionEloigner.setText(_translate("MainWindow", "Eloigner"))
        self.actionNouveau_drone.setText(_translate("MainWindow", "Ajouter drone"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
