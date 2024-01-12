from PyQt6 import QtWidgets, QtCore, QtSql

import conexion
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
    def cargadriverfac():
        try:
            var.ui.cmbConductor.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select apeldri from drivers')

            if query.exec():
                var.ui.cmbConductor.addItem("")

                while query.next():
                    var.ui.cmbConductor.addItem(query.value(0))

        except Exception as error:

            print("Error al mostar cmbConductor")


    @staticmethod
    def limpiarPanel():
        try:
            listaWidgets = [var.ui.lblCodFac, var.ui.txtcifcli, var.ui.txtDataFac]
            for i in listaWidgets:
                i.clear()

            var.ui.cmbConductor.setCurrentText('')

        except Exception as error:
            print("error al limpiar panel", error)