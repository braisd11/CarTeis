# Form implementation generated from reading ui file '.\templates\AboutWindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgAbout(object):
    def setupUi(self, dlgAbout):
        dlgAbout.setObjectName("dlgAbout")
        dlgAbout.resize(391, 267)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dlgAbout.sizePolicy().hasHeightForWidth())
        dlgAbout.setSizePolicy(sizePolicy)
        dlgAbout.setMinimumSize(QtCore.QSize(391, 267))
        dlgAbout.setMaximumSize(QtCore.QSize(391, 267))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/img/car_icon_155695.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        dlgAbout.setWindowIcon(icon)
        dlgAbout.setStyleSheet("QDialog{\n"
"    background-color:#84b6f4;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.lblAutor = QtWidgets.QLabel(parent=dlgAbout)
        self.lblAutor.setGeometry(QtCore.QRect(30, 240, 111, 16))
        self.lblAutor.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lblAutor.setObjectName("lblAutor")
        self.frame = QtWidgets.QFrame(parent=dlgAbout)
        self.frame.setGeometry(QtCore.QRect(180, 20, 191, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.lblVersion = QtWidgets.QLabel(parent=self.frame)
        self.lblVersion.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.lblVersion.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.lblVersion.setObjectName("lblVersion")
        self.lblNomApp = QtWidgets.QLabel(parent=self.frame)
        self.lblNomApp.setGeometry(QtCore.QRect(10, 0, 51, 31))
        self.lblNomApp.setObjectName("lblNomApp")
        self.lblIcon = QtWidgets.QLabel(parent=dlgAbout)
        self.lblIcon.setGeometry(QtCore.QRect(20, 10, 121, 121))
        self.lblIcon.setText("")
        self.lblIcon.setPixmap(QtGui.QPixmap(":/iconos/img/car_icon_155695.ico"))
        self.lblIcon.setScaledContents(True)
        self.lblIcon.setObjectName("lblIcon")
        self.lblDescrip = QtWidgets.QLabel(parent=dlgAbout)
        self.lblDescrip.setGeometry(QtCore.QRect(30, 150, 251, 51))
        self.lblDescrip.setStyleSheet("")
        self.lblDescrip.setWordWrap(True)
        self.lblDescrip.setObjectName("lblDescrip")

        self.retranslateUi(dlgAbout)
        QtCore.QMetaObject.connectSlotsByName(dlgAbout)

    def retranslateUi(self, dlgAbout):
        _translate = QtCore.QCoreApplication.translate
        dlgAbout.setWindowTitle(_translate("dlgAbout", "CarTeis Acerca De"))
        self.lblAutor.setText(_translate("dlgAbout", "Brais Díaz Rodríguez"))
        self.lblVersion.setText(_translate("dlgAbout", "Versión 0.1"))
        self.lblNomApp.setText(_translate("dlgAbout", "CarTeis"))
        self.lblDescrip.setText(_translate("dlgAbout", "Aplicación dedicada al alquiler de coches por parte de ususarios."))
