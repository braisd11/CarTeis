import var, sys
from datetime import datetime
from PyQt6 import QtWidgets, QtCore, QtGui
import locale

locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

class Eventos():



    def showSalir(self):
        try:

            var.exitWindow.show()

        except Exception as error:
            print("error en modulo eventos", error)

    def confirmarSalir(self):
        try:

            sys.exit()

        except Exception as error:
            print("error en modulo eventos", error)

    def cancelarSalir(self):
        try:

            var.exitWindow.hide()

        except Exception as error:
            print("error en modulo eventos", error)

    def acercade(self):

        try:

            var.aboutWindow.show()

        except Exception as error:

            print("error abrir ventana acerca de ", error)

    def abrirCalendar(self):

        try:

            var.calendar.show()

        except Exception as error:

            print("error en abrir calendar", error)

    def cargastatusbar(self):
        try:
            '''

                Zona de eventos de StatusBar
            '''
            fecha = datetime.now().strftime("%A - " + "%d/%m/%Y")
            self.labelstatus = QtWidgets.QLabel(fecha, self)
            self.labelstatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            var.ui.statusbar.addPermanentWidget(self.labelstatus, 1)
            self.labelstatusversion = QtWidgets.QLabel("Versión: " + var.version, self)
            self.labelstatusversion.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            var.ui.statusbar.addPermanentWidget(self.labelstatusversion, 0)

        except Exception as error:

            print("error en cargar statusbar", error)

    def cargaprov(self):
        try:
            prov = ['A Coruña', 'Lugo', 'Ferrol', 'Vigo', 'Santiago de Compostela', 'Ourense', 'Pontevedra']
            var.ui.cmbProv.clear()
            var.ui.cmbProv.addItem("---")
            for i in prov:
                var.ui.cmbProv.addItem(str(i))

        except Exception as error:

            print("Error al mostar cmbProv")

    def selEstado(self):

        if var.ui.rbtTodos.isChecked():

            print("Pulsaste Todos")

        if var.ui.rbtAlta.isChecked():

            print("Pulsaste Alta")

        if var.ui.rbtBaja.isChecked():

            print("Pulsaste Baja")

    def resizeTabdrivers(self):
        try:
            header = var.ui.tabDrivers.horizontalHeader()
            for i in range(var.ui.tabDrivers.columnCount()):
                if i == 0 or i == 4 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print("error con resizeTabdrivers", error)

    def letraCapital(self = None):
        try:
            var.ui.txtApel.setText(var.ui.txtApel.text().title())
            var.ui.txtNombre.setText(var.ui.txtNombre.text().title())
            var.ui.txtDNI.setText(var.ui.txtDNI.text().title())

        except Exception as error:
            print("error con letra capital", error)


    def compruebaFormatoSalario(self = None):
        try:

            salario = var.ui.txtSalario.text()
            var.ui.txtSalario.setText(salario)

            salarioNum = float(salario)

            if salarioNum >= 0.00:
                var.ui.txtSalario.setText(str(locale.currency(float(var.ui.txtSalario.text()))))
            else:
                raise Exception()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Valor de Salario Incorrecto (00000.00)')
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
            msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.setWindowIcon(QtGui.QIcon('./img/driver.ico'))
            msg.exec()
            var.ui.txtSalario.setText("")
            var.ui.txtSalario.setFocus()

    def compruebaMovil(self = None):
        try:
            movil = var.ui.txtMovilDriver.text()
            var.ui.txtMovilDriver.setText(movil)

            if len(movil) == 9 or (movil.isdigit() and len(movil) == 9):
                pass
            else:
                raise Exception()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Valor de Móvil Incorrecto (9 dígitos)')
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
            msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.setWindowIcon(QtGui.QIcon('./img/driver.ico'))
            msg.exec()
            var.ui.txtMovilDriver.setText("")
            var.ui.txtMovilDriver.setFocus()