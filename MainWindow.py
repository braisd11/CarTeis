# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 768))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/a22braisdr/.designer/backup/img/driver.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabPrincipal = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabPrincipal.setMinimumSize(QtCore.QSize(980, 700))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabPrincipal.setFont(font)
        self.tabPrincipal.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.tabPrincipal.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.tabPrincipal.setObjectName("tabPrincipal")
        self.tabDrivers = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabDrivers.sizePolicy().hasHeightForWidth())
        self.tabDrivers.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tabDrivers.setFont(font)
        self.tabDrivers.setObjectName("tabDrivers")
        self.frame = QtWidgets.QFrame(parent=self.tabDrivers)
        self.frame.setGeometry(QtCore.QRect(70, 10, 839, 128))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblCodigo = QtWidgets.QLabel(parent=self.frame)
        self.lblCodigo.setMinimumSize(QtCore.QSize(50, 20))
        self.lblCodigo.setObjectName("lblCodigo")
        self.gridLayout_2.addWidget(self.lblCodigo, 0, 0, 1, 1)
        self.lblCodBD = QtWidgets.QLabel(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCodBD.sizePolicy().hasHeightForWidth())
        self.lblCodBD.setSizePolicy(sizePolicy)
        self.lblCodBD.setMinimumSize(QtCore.QSize(100, 20))
        self.lblCodBD.setStyleSheet("background-color: rgb(247, 255, 158);")
        self.lblCodBD.setText("")
        self.lblCodBD.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblCodBD.setObjectName("lblCodBD")
        self.gridLayout_2.addWidget(self.lblCodBD, 0, 1, 1, 1)
        self.lblDNI = QtWidgets.QLabel(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDNI.sizePolicy().hasHeightForWidth())
        self.lblDNI.setSizePolicy(sizePolicy)
        self.lblDNI.setMinimumSize(QtCore.QSize(50, 20))
        self.lblDNI.setObjectName("lblDNI")
        self.gridLayout_2.addWidget(self.lblDNI, 0, 2, 1, 1)
        self.txtDNI = QtWidgets.QLineEdit(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDNI.sizePolicy().hasHeightForWidth())
        self.txtDNI.setSizePolicy(sizePolicy)
        self.txtDNI.setMinimumSize(QtCore.QSize(120, 20))
        self.txtDNI.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtDNI.setObjectName("txtDNI")
        self.gridLayout_2.addWidget(self.txtDNI, 0, 3, 1, 1)
        self.lblValidarDNI = QtWidgets.QLabel(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.lblValidarDNI.sizePolicy().hasHeightForWidth())
        self.lblValidarDNI.setSizePolicy(sizePolicy)
        self.lblValidarDNI.setMinimumSize(QtCore.QSize(60, 30))
        self.lblValidarDNI.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.lblValidarDNI.setFont(font)
        self.lblValidarDNI.setText("")
        self.lblValidarDNI.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblValidarDNI.setObjectName("lblValidarDNI")
        self.gridLayout_2.addWidget(self.lblValidarDNI, 0, 4, 1, 1)
        self.lblFechaAlta = QtWidgets.QLabel(parent=self.frame)
        self.lblFechaAlta.setObjectName("lblFechaAlta")
        self.gridLayout_2.addWidget(self.lblFechaAlta, 0, 5, 1, 2)
        self.txtFechaAlta = QtWidgets.QLineEdit(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.txtFechaAlta.sizePolicy().hasHeightForWidth())
        self.txtFechaAlta.setSizePolicy(sizePolicy)
        self.txtFechaAlta.setMinimumSize(QtCore.QSize(80, 20))
        self.txtFechaAlta.setMaximumSize(QtCore.QSize(80, 20))
        self.txtFechaAlta.setObjectName("txtFechaAlta")
        self.gridLayout_2.addWidget(self.txtFechaAlta, 0, 7, 1, 1)
        self.btnCalendar = QtWidgets.QPushButton(parent=self.frame)
        self.btnCalendar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/calendar.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCalendar.setIcon(icon1)
        self.btnCalendar.setObjectName("btnCalendar")
        self.gridLayout_2.addWidget(self.btnCalendar, 0, 8, 1, 1)
        self.lblApel = QtWidgets.QLabel(parent=self.frame)
        self.lblApel.setMinimumSize(QtCore.QSize(60, 20))
        self.lblApel.setObjectName("lblApel")
        self.gridLayout_2.addWidget(self.lblApel, 1, 0, 1, 1)
        self.txtApel = QtWidgets.QLineEdit(parent=self.frame)
        self.txtApel.setMinimumSize(QtCore.QSize(300, 20))
        self.txtApel.setObjectName("txtApel")
        self.gridLayout_2.addWidget(self.txtApel, 1, 1, 1, 3)
        self.lblNombre = QtWidgets.QLabel(parent=self.frame)
        self.lblNombre.setObjectName("lblNombre")
        self.gridLayout_2.addWidget(self.lblNombre, 1, 5, 1, 1)
        self.txtNombre = QtWidgets.QLineEdit(parent=self.frame)
        self.txtNombre.setObjectName("txtNombre")
        self.gridLayout_2.addWidget(self.txtNombre, 1, 7, 1, 2)
        self.lblDirDriver = QtWidgets.QLabel(parent=self.frame)
        self.lblDirDriver.setObjectName("lblDirDriver")
        self.gridLayout_2.addWidget(self.lblDirDriver, 2, 0, 1, 1)
        self.txtDirDriver = QtWidgets.QLineEdit(parent=self.frame)
        self.txtDirDriver.setMinimumSize(QtCore.QSize(300, 20))
        self.txtDirDriver.setObjectName("txtDirDriver")
        self.gridLayout_2.addWidget(self.txtDirDriver, 2, 1, 1, 3)
        self.lblProv = QtWidgets.QLabel(parent=self.frame)
        self.lblProv.setObjectName("lblProv")
        self.gridLayout_2.addWidget(self.lblProv, 2, 5, 1, 1)
        self.cmbLocalidad_2 = QtWidgets.QComboBox(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.cmbLocalidad_2.sizePolicy().hasHeightForWidth())
        self.cmbLocalidad_2.setSizePolicy(sizePolicy)
        self.cmbLocalidad_2.setMinimumSize(QtCore.QSize(120, 20))
        self.cmbLocalidad_2.setMaximumSize(QtCore.QSize(120, 20))
        self.cmbLocalidad_2.setObjectName("cmbLocalidad_2")
        self.gridLayout_2.addWidget(self.cmbLocalidad_2, 2, 6, 1, 2)
        self.lblLoc = QtWidgets.QLabel(parent=self.frame)
        self.lblLoc.setObjectName("lblLoc")
        self.gridLayout_2.addWidget(self.lblLoc, 2, 8, 1, 1)
        self.cmbLocalidad = QtWidgets.QComboBox(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.cmbLocalidad.sizePolicy().hasHeightForWidth())
        self.cmbLocalidad.setSizePolicy(sizePolicy)
        self.cmbLocalidad.setMinimumSize(QtCore.QSize(120, 20))
        self.cmbLocalidad.setMaximumSize(QtCore.QSize(120, 20))
        self.cmbLocalidad.setObjectName("cmbLocalidad")
        self.gridLayout_2.addWidget(self.cmbLocalidad, 2, 9, 1, 1)
        self.lblMovilDriver = QtWidgets.QLabel(parent=self.frame)
        self.lblMovilDriver.setObjectName("lblMovilDriver")
        self.gridLayout_2.addWidget(self.lblMovilDriver, 3, 0, 1, 1)
        self.txtMovilDriver = QtWidgets.QLineEdit(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtMovilDriver.sizePolicy().hasHeightForWidth())
        self.txtMovilDriver.setSizePolicy(sizePolicy)
        self.txtMovilDriver.setMinimumSize(QtCore.QSize(120, 20))
        self.txtMovilDriver.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtMovilDriver.setObjectName("txtMovilDriver")
        self.gridLayout_2.addWidget(self.txtMovilDriver, 3, 1, 1, 1)
        self.lblSalario = QtWidgets.QLabel(parent=self.frame)
        self.lblSalario.setObjectName("lblSalario")
        self.gridLayout_2.addWidget(self.lblSalario, 3, 2, 1, 1)
        self.txtSalario = QtWidgets.QLineEdit(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtSalario.sizePolicy().hasHeightForWidth())
        self.txtSalario.setSizePolicy(sizePolicy)
        self.txtSalario.setMinimumSize(QtCore.QSize(120, 20))
        self.txtSalario.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtSalario.setObjectName("txtSalario")
        self.gridLayout_2.addWidget(self.txtSalario, 3, 3, 1, 1)
        self.tabPrincipal.addTab(self.tabDrivers, "")
        self.tab_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy)
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(310, 250, 191, 16))
        self.label_2.setObjectName("label_2")
        self.tabPrincipal.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabPrincipal, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuAyuda = QtWidgets.QMenu(parent=self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtGui.QAction(parent=MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAcerca_de = QtGui.QAction(parent=MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        self.tabPrincipal.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CarTeis"))
        self.lblCodigo.setText(_translate("MainWindow", "Código:"))
        self.lblDNI.setText(_translate("MainWindow", "DNI:"))
        self.lblFechaAlta.setText(_translate("MainWindow", "Fecha Alta:"))
        self.lblApel.setText(_translate("MainWindow", "Apellidos:"))
        self.lblNombre.setText(_translate("MainWindow", "Nombre:"))
        self.lblDirDriver.setText(_translate("MainWindow", "Dirección:"))
        self.lblProv.setText(_translate("MainWindow", "Provincia:"))
        self.lblLoc.setText(_translate("MainWindow", "Localidad:"))
        self.lblMovilDriver.setText(_translate("MainWindow", "Móvil:"))
        self.lblSalario.setText(_translate("MainWindow", "Salario:"))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tabDrivers), _translate("MainWindow", "Conductores"))
        self.label_2.setText(_translate("MainWindow", "Label super cutre"))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de..."))
