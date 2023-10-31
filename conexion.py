from PyQt6 import QtWidgets, QtSql, QtCore

import drivers
import var

class Conexion():
    def conexion(self=None):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('bbdd.sqlite')

        if not db.open():

            print("Error de conexión")
            return False

        else:

            print("Base Datos conectada")
            return True

    def cargaprov(self=None):
        try:
            var.ui.cmbProv.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')

            if query.exec():
                var.ui.cmbProv.addItem("")

                while query.next():
                    var.ui.cmbProv.addItem(query.value(0))


        except Exception as error:

            print("Error al mostar cmbProv")

    def selMuni(self=None):
        try:
            id = 0
            var.ui.cmbMuni.clear()
            prov = var.ui.cmbProv.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select idprov from provincias where provincia = :prov')
            query.bindValue(':prov', prov)

            if query.exec():

                while query.next():
                    id = query.value(0)

            query1 = QtSql.QSqlQuery()
            query1.prepare('select municipio from municipios where idprov = :id')
            query1.bindValue(':id', int(id))

            if query1.exec():

                var.ui.cmbMuni.addItem('')

                while query1.next():
                    var.ui.cmbMuni.addItem(query1.value(0))

        except Exception as error:
            print("Error seleccion municipios", error)

    @staticmethod
    def guardardri(newdriver):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into drivers (dnidri, altadri, nombredri, apeldri, '
                          'direcciondri, provdri, munidri, movildri, salario, carnet) VALUES (:dni, :alta, :nombre, '
                          ':apel, :direccion, :prov, :muni, :movil, :salario, :carnet)')
            query.bindValue(':dni', str(newdriver[0]))
            query.bindValue(':alta', str(newdriver[1]))
            query.bindValue(':nombre', str(newdriver[2]))
            query.bindValue(':apel', str(newdriver[3]))
            query.bindValue(':direccion', str(newdriver[4]))
            query.bindValue(':prov', str(newdriver[5]))
            query.bindValue(':muni', str(newdriver[6]))
            query.bindValue(':movil', str(newdriver[7]))
            query.bindValue(':salario', str(newdriver[8]))
            query.bindValue(':carnet', str(newdriver[9]))

            if query.exec():
                print(newdriver)
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Empleado dado de alta")
                mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error al guardar el driver")
                mbox.exec()
            #drivers.Drivers.cargartabla(datosdri)

        except Exception as error:
            print("Error al guardar el driver", error)
