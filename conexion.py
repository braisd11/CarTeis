from PyQt6 import QtWidgets, QtSql, QtCore

import drivers
import eventos
import var
import datetime


class Conexion():
    def conexion(self=None):
        var.bbdd = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)

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
            if (newdriver[0].strip() == "" or newdriver[1].strip() == "" or newdriver[2].strip() == ""):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Faltan Datos. Debe introducir al menos \n"
                             "DNI, Apellidos, Nombre, Fecha de Alta, Móvil")
                mbox.exec()

            else:
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
                #Conexion.mostrardrivers()
                drivers.Drivers.selEstado()


        except Exception as error:
            print("Error al guardar el driver", error)

    @staticmethod
    def mostrardrivers():
        try:
            estado = 1
            Conexion.selectDrivers(estado)


        except Exception as error:
            print("error al cargar la tabla", error)

    def onedriver(id):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from drivers where codigo = :id')

            query.bindValue(':id', int(id))
            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))
            return registro


        except Exception as error:
            print('error en fichero conexion dato de 1 driver', error)

    def codDri(dni):
        try:
            registro = None
            query = QtSql.QSqlQuery()
            query.prepare('select codigo from drivers where dniDri = :dni')
            query.bindValue(':dni', str(dni))

            if query.exec():
                while query.next():
                    codigo = query.value(0)
            try:

                registro = Conexion.onedriver(codigo)
            except Exception as error:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("No existe nadie con ese DNI")
                mbox.exec()
            return registro

        except Exception as error:
            print('error al buscar el dni', error)

    def comprobarModifDriver(modifdriver):
        try:
            codigo = var.ui.lblCodBD.text()

            if drivers.Drivers.comprobarfechabaja(codigo):
                eventos.Eventos.showModificarBaja()
                Conexion.modifDriver(modifdriver)

            else:

                Conexion.modifDriver(modifdriver)
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Datos conductor modificados")
                mbox.exec()

        except Exception as error:
            print("error en comprobarmodifdriver conexion", error)

    @staticmethod
    def modifDriver(modifdriver):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update drivers set dnidri = :dni, altadri = :alta ,nombredri = :nombre, apeldri = :apel, '
                          'direcciondri = :direccion, provdri = :provincia, munidri = :municipio,'
                          'movildri = :movil, salario = :salario, carnet = :carnet where codigo = :codigo')

            query.bindValue(':codigo', int(modifdriver[0]))
            query.bindValue(':dni', str(modifdriver[1]))
            query.bindValue(':alta', str(modifdriver[2]))
            query.bindValue(':apel', str(modifdriver[3]))
            query.bindValue(':nombre', str(modifdriver[4]))
            query.bindValue(':direccion', str(modifdriver[5]))
            query.bindValue(':provincia', str(modifdriver[6]))
            query.bindValue(':municipio', str(modifdriver[7]))
            query.bindValue(':movil', str(modifdriver[8]))
            query.bindValue(':salario', str(modifdriver[9]))
            query.bindValue(':carnet', str(modifdriver[10]))

            if query.exec():

                drivers.Drivers.selEstado()

            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error al modificar los datos del conductor")
                mbox.exec()

        except Exception as error:
            print('error en modifdriver', error)

    def borraDriv(dni):
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('select bajadri from drivers where '
                           'dnidri = :dni')
            query1.bindValue(':dni', str(dni))
            if query1.exec():
                while query1.next():
                    valor = query1.value(0)

            if str(valor) == '':
                fecha = datetime.date.today()
                fecha = fecha.strftime('%d/%m/%Y')
                query = QtSql.QSqlQuery()
                query.prepare('update drivers set bajadri = :fechabaja where '
                              'dnidri = :dni')
                query.bindValue(':fechabaja', str(fecha))
                query.bindValue(':dni', str(dni))

                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText("Conductor dado de baja")
                    mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error al dar de baja el conductor")
                mbox.exec()

            pass
        except Exception as error:
            print("error en borradriv en conexion", error)

    def selectDrivers(estado):
        try:
            registro = []

            consulta = "select codigo, apeldri, nombredri, movildri, carnet, bajadri from drivers"

            if int(estado) == 1:

                consulta = consulta + " where bajadri is null"

            elif int(estado) == 2:

                consulta = consulta + " where bajadri is not null"

            query = QtSql.QSqlQuery()
            query.prepare(consulta)

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registro.append(row)
            drivers.Drivers.cargartabladri(registro)

        except Exception as error:
            print('error al seleccionar driver', error)

    @staticmethod
    def selectdriverstodos():
        try:
            registros = []

            query = QtSql.QSqlQuery()
            query.prepare('Select * from drivers order by apeldri')
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            return registros
        except Exception as error:
            print('error al devolver todos los drivers', error)

    @staticmethod
    def borrarfechabaja(codigo):
        try:

            query = QtSql.QSqlQuery()
            query.prepare("update drivers set bajadri = null where codigo = :codigo")

            query.bindValue(':codigo', str(codigo))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Driver dado de alta")
                mbox.exec()

        except Exception as error:
            print('error al borrar fecha baja', error)
