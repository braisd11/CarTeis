# Form implementation generated from reading ui file '.\templates\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 795)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/a22braisdr/.designer/img/driver.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #ffffff;\n"
"    color:\'white\';\n"
"    font: 11pt \"Arial\";\n"
"    background-color:rgb(100,100,100);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.panelPrincipal = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.panelPrincipal.setMinimumSize(QtCore.QSize(980, 700))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.panelPrincipal.setFont(font)
        self.panelPrincipal.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.panelPrincipal.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.panelPrincipal.setObjectName("panelPrincipal")
        self.panelDrivers = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.panelDrivers.sizePolicy().hasHeightForWidth())
        self.panelDrivers.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.panelDrivers.setFont(font)
        self.panelDrivers.setObjectName("panelDrivers")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.panelDrivers)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.panelDrivers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 860, 174))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lblCodigo = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCodigo.sizePolicy().hasHeightForWidth())
        self.lblCodigo.setSizePolicy(sizePolicy)
        self.lblCodigo.setMinimumSize(QtCore.QSize(50, 20))
        self.lblCodigo.setObjectName("lblCodigo")
        self.horizontalLayout_9.addWidget(self.lblCodigo)
        self.lblCodBD = QtWidgets.QLabel(parent=self.layoutWidget)
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
        self.horizontalLayout_9.addWidget(self.lblCodBD)
        self.lblDNI = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDNI.sizePolicy().hasHeightForWidth())
        self.lblDNI.setSizePolicy(sizePolicy)
        self.lblDNI.setMinimumSize(QtCore.QSize(50, 20))
        self.lblDNI.setMaximumSize(QtCore.QSize(50, 20))
        self.lblDNI.setObjectName("lblDNI")
        self.horizontalLayout_9.addWidget(self.lblDNI)
        self.txtDNI = QtWidgets.QLineEdit(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDNI.sizePolicy().hasHeightForWidth())
        self.txtDNI.setSizePolicy(sizePolicy)
        self.txtDNI.setMinimumSize(QtCore.QSize(110, 20))
        self.txtDNI.setMaximumSize(QtCore.QSize(110, 16777215))
        self.txtDNI.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtDNI.setObjectName("txtDNI")
        self.horizontalLayout_9.addWidget(self.txtDNI)
        self.lblValidarDNI = QtWidgets.QLabel(parent=self.layoutWidget)
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
        self.horizontalLayout_9.addWidget(self.lblValidarDNI)
        self.btnBuscar = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBuscar.sizePolicy().hasHeightForWidth())
        self.btnBuscar.setSizePolicy(sizePolicy)
        self.btnBuscar.setMinimumSize(QtCore.QSize(28, 28))
        self.btnBuscar.setMaximumSize(QtCore.QSize(28, 28))
        self.btnBuscar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/a22braisdr/.designer/img/lupa.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnBuscar.setIcon(icon1)
        self.btnBuscar.setObjectName("btnBuscar")
        self.horizontalLayout_9.addWidget(self.btnBuscar)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 0, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblFechaAlta = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lblFechaAlta.setObjectName("lblFechaAlta")
        self.horizontalLayout_3.addWidget(self.lblFechaAlta)
        self.txtDataDriver = QtWidgets.QLineEdit(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.txtDataDriver.sizePolicy().hasHeightForWidth())
        self.txtDataDriver.setSizePolicy(sizePolicy)
        self.txtDataDriver.setMinimumSize(QtCore.QSize(80, 20))
        self.txtDataDriver.setMaximumSize(QtCore.QSize(80, 20))
        self.txtDataDriver.setObjectName("txtDataDriver")
        self.horizontalLayout_3.addWidget(self.txtDataDriver)
        self.btnCalendar = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btnCalendar.setMinimumSize(QtCore.QSize(40, 0))
        self.btnCalendar.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btnCalendar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/a22braisdr/.designer/img/calendar.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCalendar.setIcon(icon2)
        self.btnCalendar.setObjectName("btnCalendar")
        self.horizontalLayout_3.addWidget(self.btnCalendar)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lblApel = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lblApel.setMinimumSize(QtCore.QSize(60, 20))
        self.lblApel.setObjectName("lblApel")
        self.horizontalLayout_8.addWidget(self.lblApel)
        self.txtApel = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.txtApel.setMinimumSize(QtCore.QSize(350, 20))
        self.txtApel.setMaximumSize(QtCore.QSize(350, 16777215))
        self.txtApel.setObjectName("txtApel")
        self.horizontalLayout_8.addWidget(self.txtApel)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 1, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblNombre = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lblNombre.setObjectName("lblNombre")
        self.horizontalLayout_4.addWidget(self.lblNombre)
        self.txtNombre = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.txtNombre.setObjectName("txtNombre")
        self.horizontalLayout_4.addWidget(self.txtNombre)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 2, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lblDirDriver = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lblDirDriver.setObjectName("lblDirDriver")
        self.horizontalLayout_7.addWidget(self.lblDirDriver)
        self.txtDirDriver = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.txtDirDriver.setMinimumSize(QtCore.QSize(350, 20))
        self.txtDirDriver.setMaximumSize(QtCore.QSize(350, 16777215))
        self.txtDirDriver.setObjectName("txtDirDriver")
        self.horizontalLayout_7.addWidget(self.txtDirDriver)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 2, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblProv = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lblProv.setObjectName("lblProv")
        self.horizontalLayout_5.addWidget(self.lblProv)
        self.cmbProv = QtWidgets.QComboBox(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.cmbProv.sizePolicy().hasHeightForWidth())
        self.cmbProv.setSizePolicy(sizePolicy)
        self.cmbProv.setMinimumSize(QtCore.QSize(140, 20))
        self.cmbProv.setMaximumSize(QtCore.QSize(140, 20))
        self.cmbProv.setObjectName("cmbProv")
        self.horizontalLayout_5.addWidget(self.cmbProv)
        self.lblLoc = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lblLoc.setObjectName("lblLoc")
        self.horizontalLayout_5.addWidget(self.lblLoc)
        self.cmbMuni = QtWidgets.QComboBox(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.cmbMuni.sizePolicy().hasHeightForWidth())
        self.cmbMuni.setSizePolicy(sizePolicy)
        self.cmbMuni.setMinimumSize(QtCore.QSize(120, 20))
        self.cmbMuni.setMaximumSize(QtCore.QSize(120, 20))
        self.cmbMuni.setObjectName("cmbMuni")
        self.horizontalLayout_5.addWidget(self.cmbMuni)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 2, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblMovilDriver = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lblMovilDriver.setObjectName("lblMovilDriver")
        self.horizontalLayout_6.addWidget(self.lblMovilDriver)
        self.txtMovilDriver = QtWidgets.QLineEdit(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtMovilDriver.sizePolicy().hasHeightForWidth())
        self.txtMovilDriver.setSizePolicy(sizePolicy)
        self.txtMovilDriver.setMinimumSize(QtCore.QSize(120, 20))
        self.txtMovilDriver.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtMovilDriver.setObjectName("txtMovilDriver")
        self.horizontalLayout_6.addWidget(self.txtMovilDriver)
        self.lblSalario = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lblSalario.setObjectName("lblSalario")
        self.horizontalLayout_6.addWidget(self.lblSalario)
        self.txtSalario = QtWidgets.QLineEdit(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtSalario.sizePolicy().hasHeightForWidth())
        self.txtSalario.setSizePolicy(sizePolicy)
        self.txtSalario.setMinimumSize(QtCore.QSize(110, 20))
        self.txtSalario.setMaximumSize(QtCore.QSize(110, 16777215))
        self.txtSalario.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.txtSalario.setObjectName("txtSalario")
        self.horizontalLayout_6.addWidget(self.txtSalario)
        self.labelFormato = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelFormato.setObjectName("labelFormato")
        self.horizontalLayout_6.addWidget(self.labelFormato)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 3, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblHistorico = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lblHistorico.setObjectName("lblHistorico")
        self.horizontalLayout.addWidget(self.lblHistorico)
        self.rbtTodos = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.rbtTodos.setMinimumSize(QtCore.QSize(50, 20))
        self.rbtTodos.setMaximumSize(QtCore.QSize(50, 20))
        self.rbtTodos.setChecked(False)
        self.rbtTodos.setObjectName("rbtTodos")
        self.btnGroupEstado = QtWidgets.QButtonGroup(MainWindow)
        self.btnGroupEstado.setObjectName("btnGroupEstado")
        self.btnGroupEstado.addButton(self.rbtTodos)
        self.horizontalLayout.addWidget(self.rbtTodos)
        self.rbtAlta = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.rbtAlta.setMinimumSize(QtCore.QSize(50, 20))
        self.rbtAlta.setMaximumSize(QtCore.QSize(50, 20))
        self.rbtAlta.setChecked(True)
        self.rbtAlta.setObjectName("rbtAlta")
        self.btnGroupEstado.addButton(self.rbtAlta)
        self.horizontalLayout.addWidget(self.rbtAlta)
        self.rbtBaja = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.rbtBaja.setMinimumSize(QtCore.QSize(50, 20))
        self.rbtBaja.setMaximumSize(QtCore.QSize(50, 20))
        self.rbtBaja.setObjectName("rbtBaja")
        self.btnGroupEstado.addButton(self.rbtBaja)
        self.horizontalLayout.addWidget(self.rbtBaja)
        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labeltipocarnet = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labeltipocarnet.setObjectName("labeltipocarnet")
        self.horizontalLayout_2.addWidget(self.labeltipocarnet)
        self.chkA = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.chkA.setObjectName("chkA")
        self.horizontalLayout_2.addWidget(self.chkA)
        self.chkB = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.chkB.setObjectName("chkB")
        self.horizontalLayout_2.addWidget(self.chkB)
        self.chkC = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.chkC.setObjectName("chkC")
        self.horizontalLayout_2.addWidget(self.chkC)
        self.chkD = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.chkD.setObjectName("chkD")
        self.horizontalLayout_2.addWidget(self.chkD)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btnAltaDriver = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAltaDriver.sizePolicy().hasHeightForWidth())
        self.btnAltaDriver.setSizePolicy(sizePolicy)
        self.btnAltaDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnAltaDriver.setObjectName("btnAltaDriver")
        self.horizontalLayout_10.addWidget(self.btnAltaDriver)
        self.btnBajaDriver = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBajaDriver.sizePolicy().hasHeightForWidth())
        self.btnBajaDriver.setSizePolicy(sizePolicy)
        self.btnBajaDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnBajaDriver.setObjectName("btnBajaDriver")
        self.horizontalLayout_10.addWidget(self.btnBajaDriver)
        self.btnModifDriver = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnModifDriver.sizePolicy().hasHeightForWidth())
        self.btnModifDriver.setSizePolicy(sizePolicy)
        self.btnModifDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnModifDriver.setObjectName("btnModifDriver")
        self.horizontalLayout_10.addWidget(self.btnModifDriver)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 5, 1, 1, 2)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.tabDrivers = QtWidgets.QTableWidget(parent=self.panelDrivers)
        self.tabDrivers.setStyleSheet("QTableWidget::item:selected {\n"
"    background-color: rgb(100,100,100);\n"
"}")
        self.tabDrivers.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabDrivers.setAlternatingRowColors(True)
        self.tabDrivers.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabDrivers.setObjectName("tabDrivers")
        self.tabDrivers.setColumnCount(6)
        self.tabDrivers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(5, item)
        self.tabDrivers.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tabDrivers, 1, 0, 1, 1)
        self.panelPrincipal.addTab(self.panelDrivers, "")
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
        self.panelPrincipal.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.panelPrincipal, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuAyuda = QtWidgets.QMenu(parent=self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuHerramientas = QtWidgets.QMenu(parent=self.menubar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setStyleSheet("QHeaderView::section:horizontal\n"
"{\n"
"border-top: 1px solid #ffffff;\n"
"color:\'white\';\n"
"font: 11pt \"Arial\";\n"
"background-color:rgb(100,100,100);\n"
"}")
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionlimpiarPanel = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/a22braisdr/.designer/img/reload.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionlimpiarPanel.setIcon(icon3)
        self.actionlimpiarPanel.setObjectName("actionlimpiarPanel")
        self.actionAcerca_de = QtGui.QAction(parent=MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.actionSalir = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/a22braisdr/.designer/img/exit.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSalir.setIcon(icon4)
        self.actionSalir.setObjectName("actionSalir")
        self.actionCrear_Copia_de_Seguridad = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/a22braisdr/.designer/img/icon_upload.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCrear_Copia_de_Seguridad.setIcon(icon5)
        self.actionCrear_Copia_de_Seguridad.setObjectName("actionCrear_Copia_de_Seguridad")
        self.actionRestaurar_Copia_Seguridad = QtGui.QAction(parent=MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Users/a22braisdr/.designer/img/icon_download.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRestaurar_Copia_Seguridad.setIcon(icon6)
        self.actionRestaurar_Copia_Seguridad.setObjectName("actionRestaurar_Copia_Seguridad")
        self.actionExportar_Datos_Excel = QtGui.QAction(parent=MainWindow)
        self.actionExportar_Datos_Excel.setObjectName("actionExportar_Datos_Excel")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menuHerramientas.addAction(self.actionCrear_Copia_de_Seguridad)
        self.menuHerramientas.addAction(self.actionRestaurar_Copia_Seguridad)
        self.menuHerramientas.addSeparator()
        self.menuHerramientas.addAction(self.actionExportar_Datos_Excel)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.toolBar.addAction(self.actionlimpiarPanel)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSalir)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCrear_Copia_de_Seguridad)
        self.toolBar.addAction(self.actionRestaurar_Copia_Seguridad)

        self.retranslateUi(MainWindow)
        self.panelPrincipal.setCurrentIndex(0)
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
        self.labelFormato.setText(_translate("MainWindow", "(00000.00)"))
        self.lblHistorico.setText(_translate("MainWindow", "Histórico:"))
        self.rbtTodos.setText(_translate("MainWindow", "Todos"))
        self.rbtAlta.setText(_translate("MainWindow", "Alta"))
        self.rbtBaja.setText(_translate("MainWindow", "Baja"))
        self.labeltipocarnet.setText(_translate("MainWindow", "Tipo de carnet:"))
        self.chkA.setText(_translate("MainWindow", "A"))
        self.chkB.setText(_translate("MainWindow", "B"))
        self.chkC.setText(_translate("MainWindow", "C"))
        self.chkD.setText(_translate("MainWindow", "D"))
        self.btnAltaDriver.setText(_translate("MainWindow", "Alta"))
        self.btnBajaDriver.setText(_translate("MainWindow", "Baja"))
        self.btnModifDriver.setText(_translate("MainWindow", "Modificar"))
        item = self.tabDrivers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.tabDrivers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apellidos"))
        item = self.tabDrivers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tabDrivers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Móvil"))
        item = self.tabDrivers.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Licencias"))
        item = self.tabDrivers.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Fecha Baja"))
        self.panelPrincipal.setTabText(self.panelPrincipal.indexOf(self.panelDrivers), _translate("MainWindow", "Conductores"))
        self.label_2.setText(_translate("MainWindow", "Label super cutre"))
        self.panelPrincipal.setTabText(self.panelPrincipal.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.menuHerramientas.setTitle(_translate("MainWindow", "Herramientas"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionlimpiarPanel.setText(_translate("MainWindow", "limpiarPanel"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionCrear_Copia_de_Seguridad.setText(_translate("MainWindow", "Crear Copia de Seguridad"))
        self.actionCrear_Copia_de_Seguridad.setShortcut(_translate("MainWindow", "Alt+S"))
        self.actionRestaurar_Copia_Seguridad.setText(_translate("MainWindow", "Restaurar Copia Seguridad"))
        self.actionRestaurar_Copia_Seguridad.setShortcut(_translate("MainWindow", "Alt+R"))
        self.actionExportar_Datos_Excel.setText(_translate("MainWindow", "Exportar Datos Excel"))
