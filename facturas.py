from PyQt6 import QtWidgets, QtCore, QtSql

import clientes
import conexion
import drivers
import eventos
import var


class Facturas:

    def cargarFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDataFac.setText(str(data))
            var.calendarfac.hide()

        except Exception as error:
            print("error en cargar fecha en facturas", error)

    @staticmethod
    def abrirCalendar():

        try:

            var.calendarfac.show()

        except Exception as error:

            print("error en abrir calendar", error)



    @staticmethod
    def limpiarPanel():
        try:
            listaWidgets = [var.ui.lblCodFac, var.ui.txtcifcli, var.ui.txtDataFac]
            for i in listaWidgets:
                i.clear()

            var.ui.cmbConductor.setCurrentText('')

        except Exception as error:
            print("error al limpiar panel", error)

    @staticmethod
    def guardarFac():
        try:
            conductor = var.ui.cmbConductor.currentText()
            dni = var.ui.txtcifcli.text()
            codigoDri = conductor.split("-")[0]
            registro = [var.ui.txtcifcli.text(), var.ui.txtDataFac.text(), codigoDri]

            if eventos.Eventos.existeDni(dni):

                if eventos.Eventos.comprobarAltaFac(dni):

                    conexion.Conexion.altaFacturacion(registro)
                    conexion.Conexion.selectFac()

            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('El DNI no existe')
                msg.exec()

            eventos.Eventos.limpiartodo()

        except Exception as error:
            print('Error al guardar una factura', error)

    @staticmethod
    def cargarfacturas():
        try:
            Facturas.limpiarPanel()

            row = var.ui.tabFacturas.selectedItems()

            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.onefac(fila[0])
            apellido = conexion.Conexion.getApel(registro[3])
            txtCmb = str(registro[3]) + "- " + apellido

            datos = [var.ui.lblCodFac, var.ui.txtcifcli, var.ui.txtDataFac, var.ui.cmbConductor]

            for i, dato in enumerate(datos):

                if i == 3:
                    dato.setCurrentText(str(txtCmb))
                else:
                    dato.setText(str(registro[i]))

        except Exception as error:
            print('error al cargar cliente', error)

    @staticmethod
    def cargartablafac(registros):
        try:
            index = 0
            for registro in registros:
                var.ui.tabFacturas.setRowCount(index + 1)
                var.ui.tabFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print('error cargar dato en tabla facturas', error)
