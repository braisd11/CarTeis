from PyQt6 import QtWidgets, QtSql, QtCore

import clientes
import drivers
import eventos
import facturas
import var
import datetime


class Conexion():
    @staticmethod
    def conexion():
        """
        Conecta la base de datos
        :return: True si se conectó a la base ded atos y False si no
        :rtype: Boolean
        """
        var.bbdd = 'bbdd(la que tiene datos).sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)

        if not db.open():

            print("Error de conexión")
            return False

        else:

            print("Base Datos conectada")
            return True

    @staticmethod
    def cargaprov():
        """
        Carga el combo box de las provincias
        """
        try:
            var.ui.cmbProvOrigen.clear()
            var.ui.cmbProvDestino.clear()
            var.ui.cmbProv.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')

            if query.exec():
                var.ui.cmbProv.addItem("")
                var.ui.cmbProvOrigen.addItem("")
                var.ui.cmbProvDestino.addItem("")

                while query.next():
                    var.ui.cmbProv.addItem(query.value(0))
                    var.ui.cmbProvDestino.addItem(query.value(0))
                    var.ui.cmbProvOrigen.addItem(query.value(0))

        except Exception as error:

            print("Error al mostar cmbProv")

    @staticmethod
    def cargaprovcli():
        """
        Carga las provincias en el combo box de provincias para clientes.
        """
        try:
            var.ui.cmbProvcli.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')

            if query.exec():
                var.ui.cmbProvcli.addItem("")

                while query.next():
                    var.ui.cmbProvcli.addItem(query.value(0))

        except Exception as error:
            print("Error al mostar cmbProvcli")

    def selMuni(self=None):
        """
        Selecciona y carga los municipios en el combo box de municipios
        basado en la provincia seleccionada para empleados.
        """
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

    def selMunicli(self=None):
        """
        Selecciona y carga los municipios en el combo box de municipios
        basado en la provincia seleccionada para clientes.
        """
        try:
            id = 0
            var.ui.cmbMunicli.clear()
            prov = var.ui.cmbProvcli.currentText()
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
                var.ui.cmbMunicli.addItem('')

                while query1.next():
                    var.ui.cmbMunicli.addItem(query1.value(0))

        except Exception as error:
            print("Error seleccion municipios clientes", error)

    def selMuniOri(self=None):
        """
        Selecciona y carga los municipios en el combo box de municipios
        basado en la provincia seleccionada para el origen.
        """
        try:
            id = 0
            var.ui.cmbLocOrigen.clear()
            prov = var.ui.cmbProvOrigen.currentText()
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
                var.ui.cmbLocOrigen.addItem('')

                while query1.next():
                    var.ui.cmbLocOrigen.addItem(query1.value(0))

        except Exception as error:
            print("Error seleccion municipios destino", error)

    def selMuniDest(self=None):
        """
        Selecciona y carga los municipios en el combo box de municipios
        basado en la provincia seleccionada para el destino.
        """
        try:
            id = 0
            var.ui.cmbLocDestino.clear()
            prov = var.ui.cmbProvDestino.currentText()
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
                var.ui.cmbLocDestino.addItem('')

                while query1.next():
                    var.ui.cmbLocDestino.addItem(query1.value(0))

        except Exception as error:
            print("Error seleccion municipios destino", error)

    @staticmethod
    def guardardri(newdriver):
        """
        Guarda un nuevo registro de conductor en la base de datos.
        """
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
                # Conexion.mostrardrivers()
                drivers.Drivers.selEstado()

        except Exception as error:
            print("Error al guardar el driver", error)

    @staticmethod
    def guardarcli(newcliente):
        """
        Guarda un nuevo registro de cliente en la base de datos.
        """
        try:
            if (newcliente[0].strip() == "" or newcliente[1].strip() == "" or newcliente[2].strip() == "" or newcliente[
                3].strip() == ""):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Faltan Datos. Debe introducir al menos \n"
                             "DNI, Nombre, Dirección, Móvil")
                mbox.exec()
            else:
                query = QtSql.QSqlQuery()
                query.prepare('insert into clientes (dnicli, razoncli, direccioncli, '
                              ' telefonocli, provcli, municli) VALUES (:dni, :nombrecli, '
                              ' :direccioncli, :movilcli, :provcli, :municli)')
                query.bindValue(':dni', str(newcliente[0]))
                query.bindValue(':nombrecli', str(newcliente[1]))
                query.bindValue(':direccioncli', str(newcliente[2]))
                query.bindValue(':movilcli', str(newcliente[3]))
                query.bindValue(':provcli', str(newcliente[4]))
                query.bindValue(':municli', str(newcliente[5]))

                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText("Cliente dado de alta")
                    mbox.exec()
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    print(query.lastError())
                    mbox.setText("Error al guardar el cliente")
                    mbox.exec()

                clientes.Clientes.selEstadocli()

        except Exception as error:
            print("Error al guardar el cliente", error)

    @staticmethod
    def mostrardrivers():
        """
        Muestra los conductores en la tabla.
        """
        try:
            estado = 1
            Conexion.selectDrivers(estado)

        except Exception as error:
            print("error al cargar la tabla", error)

    @staticmethod
    def mostrarclientes():
        """
        Muestra los clientes en la tabla.
        """
        try:
            estado = 1
            Conexion.selectClientes(estado)

        except Exception as error:
            print("error al cargar la tabla", error)

    def onedriver(id):
        """
        Retorna una lista con los datos de un conductor específico.
        """
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

    def onecli(id):
        """
        Retorna una lista con los datos de un cliente específico.
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from clientes where codcli = :id')

            query.bindValue(':id', int(id))
            if query.exec():
                while query.next():
                    for i in range(8):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print('error en fichero conexion dato de 1 cliente', error)

    def onefac(id):
        """
        Retorna una lista con los datos de una factura específica.
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from facturas where numfac = :id')

            query.bindValue(':id', int(id))
            if query.exec():
                while query.next():
                    for i in range(4):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print('error en fichero conexion dato de 1 factura', error)

    def buscacli(dni):
        """
        Busca un cliente en la base de datos y retorna sus datos en una lista.
        """
        try:
            registro = None
            query = QtSql.QSqlQuery()
            query.prepare('select codcli from clientes where dnicli = :dni')
            query.bindValue(':dni', str(dni))

            if query.exec():
                while query.next():
                    codigo = query.value(0)

                try:
                    registro = Conexion.onecli(codigo)

                except Exception as error:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("No existe nadie con ese DNI")
                    mbox.exec()
            return registro

        except Exception as error:
            print('error en buscarcli', error)

    def codDri(dni):
        """
        Busca el código de un conductor por su DNI y retorna sus datos en una lista.
        """
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
        """
        Comprueba la modificación de los datos de un conductor y realiza la acción correspondiente.
        """
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

    def comprobarModifCli(modifcliente):
        """
        Comprueba la modificación de los datos de un cliente y realiza la acción correspondiente.
        """
        try:
            codigo = var.ui.lblCodBDcli.text()

            if drivers.Drivers.comprobarfechabaja(codigo):
                eventos.Eventos.showModificarBaja()
                Conexion.modifCliente(modifcliente)

            else:
                Conexion.modifCliente(modifcliente)
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Datos cliente modificados")
                mbox.exec()

        except Exception as error:
            print("error en comprobarmodifcli conexion", error)

    @staticmethod
    def modifDriver(modifdriver):
        """
        Modifica los datos de un conductor en la base de datos.
        """
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
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Error al modificar los datos del conductor")
                mbox.exec()

        except Exception as error:
            print('error en modifdriver', error)

    @staticmethod
    def modifCliente(modifcliente):
        """
        Modifica los datos de un cliente en la base de datos.
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update clientes set dnicli = :dnicli, razoncli = :razoncli, '
                          'direccioncli = :direccioncli, telefonocli = :telefonocli,'
                          ' provcli = :provincia, municli = :municipio'
                          ' where codcli = :codcli')

            query.bindValue(':codcli', int(modifcliente[0]))
            query.bindValue(':dnicli', str(modifcliente[1]))
            query.bindValue(':razoncli', str(modifcliente[2]))
            query.bindValue(':direccioncli', str(modifcliente[3]))
            query.bindValue(':telefonocli', str(modifcliente[4]))
            query.bindValue(':provincia', str(modifcliente[5]))
            query.bindValue(':municipio', str(modifcliente[6]))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Datos del cliente modificados")
                mbox.exec()
                var.ui.lblValidarDNIcli.clear()

                clientes.Clientes.selEstadocli()

            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error al modificar los datos del cliente")
                mbox.exec()

        except Exception as error:
            print('error en modifcliente', error)

    def borraDriv(dni):
        """
        Da de baja a un conductor.
        """
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

    def borracli(dni):
        """
        Da de baja a un cliente.
        """
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('select bajacli from clientes where '
                           'dnicli = :dni')
            query1.bindValue(':dni', str(dni))
            if query1.exec():
                while query1.next():
                    valor = query1.value(0)

            if str(valor) == '':
                fecha = datetime.date.today()
                fecha = fecha.strftime('%d/%m/%Y')
                query = QtSql.QSqlQuery()
                query.prepare('update clientes set bajacli = :fechabaja where '
                              'dnicli = :dni')
                query.bindValue(':fechabaja', str(fecha))
                query.bindValue(':dni', str(dni))

                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText("Cliente dado de baja")
                    mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error al dar de baja el cliente")
                mbox.exec()

            pass
        except Exception as error:
            print("error en borracli en conexion", error)

    @staticmethod
    def selectDrivers(estado):
        """
        Selecciona los conductores según el estado y carga la tabla de conductores.
        """
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
    def selectClientes(estado):
        """
        Selecciona los clientes según el estado y carga la tabla de clientes.
        """
        try:
            registro = []

            consulta = "select * from clientes"

            if int(estado) == 0:
                consulta = consulta + " where bajacli is null"

            query = QtSql.QSqlQuery()
            query.prepare(consulta)

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registro.append(row)

                clientes.Clientes.cargartablacli(registro)

        except Exception as error:
            print('error al seleccionar factura', error)

    @staticmethod
    def selectFac():
        """
        Selecciona todas las facturas y carga la tabla de facturas.
        """
        try:

            registro = []

            consulta = "select * from facturas"

            query = QtSql.QSqlQuery()
            query.prepare(consulta)

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registro.append(row)

                facturas.Facturas.cargartablafac(registro)

        except Exception as error:
            print('error al seleccionar cliente', error)

    @staticmethod
    def selectclientestodos():
        """
        Selecciona todos los clientes y retorna una lista con sus datos.
        """
        try:
            registros = []

            query = QtSql.QSqlQuery()
            query.prepare('Select * from clientes')

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            return registros
        except Exception as error:
            print('error al devolver todos los clientes', error)

    @staticmethod
    def selectdriverstodos():
        """
        Selecciona todos los conductores y retorna una lista con sus datos.
        """
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
        """
        Borra la fecha de baja de un conductor en la base de datos.
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("update drivers set bajadri = null where codigo = :codigo")

            query.bindValue(':codigo', str(codigo))

            if query.exec():
                eventos.Eventos.sacarMbox("Driver dado de alta")

        except Exception as error:
            print('error al borrar fecha baja', error)

    @staticmethod
    def borrarfechabajacli(codigo):
        """
        Borra la fecha de baja de un cliente en la base de datos.
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("update clientes set bajacli = null where codcli = :codigo")

            query.bindValue(':codigo', str(codigo))

            if query.exec():
                eventos.Eventos.sacarMbox("Cliente dado de alta")

        except Exception as error:
            print('error al borrar fecha baja cliente', error)

    @staticmethod
    def guardarimport(new):
        """
        Guarda la información de un nuevo conductor importado en la base de datos.
        """
        try:
            if drivers.Drivers.validarDNI(str(new[1])):

                query = QtSql.QSqlQuery()

                if str(new[11]) == '':
                    query.prepare(
                        'insert into drivers values(null, :dni, :alta, :nombre, :apel, :direccion, :prov, :muni, '
                        ':movil, :salario, :carnet, null)'
                    )
                    query.bindValue(':dni', str(new[1]))
                    query.bindValue(':alta', str(new[2]))
                    query.bindValue(':nombre', str(new[3]))
                    query.bindValue(':apel', str(new[4]))
                    query.bindValue(':direccion', str(new[5]))
                    query.bindValue(':prov', str(new[6]))
                    query.bindValue(':muni', str(new[7]))
                    query.bindValue(':movil', str(new[8]))
                    query.bindValue(':salario', str(new[9]))
                    query.bindValue(':carnet', str(new[10]))
                else:
                    query.prepare(
                        'insert into drivers values(null, :dni, :alta, :nombre, :apel, :direccion, :prov, :muni, '
                        ':movil, :salario, :carnet, :baja)'
                    )
                    query.bindValue(':dni', str(new[1]))
                    query.bindValue(':alta', str(new[2]))
                    query.bindValue(':nombre', str(new[3]))
                    query.bindValue(':apel', str(new[4]))
                    query.bindValue(':direccion', str(new[5]))
                    query.bindValue(':prov', str(new[6]))
                    query.bindValue(':muni', str(new[7]))
                    query.bindValue(':movil', str(new[8]))
                    query.bindValue(':salario', str(new[9]))
                    query.bindValue(':carnet', str(new[10]))
                    query.bindValue(':baja', str(new[11]))

                if query.exec():
                    pass
                else:
                    print(query.lastError().text())
        except Exception as error:
            print('error en guardarimport', error)

    @staticmethod
    def guardarimportcli(new):
        """
        Guarda la información de un nuevo cliente importado en la base de datos.
        """
        try:
            if clientes.Clientes.validarDNIcli(str(new[0])):

                query = QtSql.QSqlQuery()

                query.prepare(
                    'insert into clientes values(null, :dni, :nombre, :direccion, :movil, :prov, :muni, null)'
                )
                query.bindValue(':dni', str(new[0]))
                query.bindValue(':nombre', str(new[1]))
                query.bindValue(':direccion', str(new[2]))
                query.bindValue(':movil', str(new[3]))
                query.bindValue(':prov', str(new[4]))
                query.bindValue(':muni', str(new[5]))

                if query.exec():
                    pass
                else:
                    print(query.lastError().text())
            else:
                print("dni no válido")
        except Exception as error:
            print('error en guardarimportcli', error)

    @staticmethod
    def altaFacturacion(registro):
        """
        Registra una nueva factura en la base de datos.
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("insert into facturas (dniCli, fecha, driver) "
                          "values (:dniCli, :fechaFact, :codDri)")
            query.bindValue(":dniCli", str(registro[0]))
            query.bindValue(":fechaFact", str(registro[1]))
            query.bindValue(":codDri", str(registro[2]))

            if query.exec():
                eventos.Eventos.sacarMbox("Factura creada correctamente")
            else:
                eventos.Eventos.sacarMbox("La Factura no se pudo crear")

        except Exception as error:
            print("Error en alta facturacion", error)

    @staticmethod
    def getApel(codigo):
        """
        Obtiene el apellido de un conductor según su código.
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("select apeldri from drivers where codigo = :codigo")
            query.bindValue(":codigo", int(codigo))

            if query.exec():
                while query.next():
                    apellido = query.value(0)
                    return apellido

            else:
                print(query.lastError())
        except Exception as error:
            print('Error al coger el apellido', error)

    @staticmethod
    def cargadriverfac():
        """
        Carga la lista de conductores disponibles en la interfaz de facturación.
        """
        try:
            var.ui.cmbConductor.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, apeldri from drivers where bajadri is null')

            if query.exec():
                var.ui.cmbConductor.addItem("")

                while query.next():
                    var.ui.cmbConductor.addItem(str(query.value(0)) + "- " + query.value(1))

        except Exception as error:
            print("Error al mostrar cmbConductor")

    @staticmethod
    def guardarviajeBD(registro):
        """
        Guarda la información de un nuevo viaje en la base de datos.
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'insert into viajes (factura, origen, destino, tarifa, km) values (:idfactura, :origen, :destino, :tarifa, :km)')
            query.bindValue(':idfactura', int(registro[0]))
            query.bindValue(':origen', str(registro[1]))
            query.bindValue(':destino', str(registro[2]))
            query.bindValue(':tarifa', str(registro[3]))
            query.bindValue(':km', str(registro[4]))

            if query.exec():
                eventos.Eventos.sacarMbox("Viaje guardado con éxito")
                facturas.Facturas.cargarviajes()
            else:
                eventos.Eventos.sacarMbox("El viaje no se pudo guardar correctamente")

        except Exception as error:
            print('error al guardar viaje en la base de datos')

    @staticmethod
    def seleccionarviajes():
        """
        Selecciona los viajes asociados a una factura específica.
        """
        try:
            registro = []

            query = QtSql.QSqlQuery()
            query.prepare('select * from viajes where factura = :factura')

            query.bindValue(':factura', int(var.ui.lblCodFac.text()))

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registro.append(row)

            return registro

        except Exception as error:
            print('error al consultar el viaje', error)

    def oneviaje(id):
        """
        Obtiene la información de un viaje específico según su identificador.
        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from viajes where idviaje = :id')
            query.bindValue(':id', int(id))

            if query.exec():
                while query.next():
                    for i in range(6):
                        registro.append(str(query.value(i)))

            return registro

        except Exception as error:
            print('error en oneviaje ', error)

    @staticmethod
    def borrarviaje():
        """
        Borra un viaje de la base de datos.
        """
        try:

            if eventos.Eventos.pedirConfirmacion("¿Desea Borrar el viaje?"):
                row = var.ui.tabViajes.selectedItems()

                query = QtSql.QSqlQuery()
                query.prepare('delete from viajes where idviaje = :id')

                query.bindValue(':id', int(row[0].text()))

                if query.exec():
                    query.next()

                facturas.Facturas.cargarviajes()

        except Exception as error:
            print('error al borrar viaje', error)

    @staticmethod
    def modifViaje():
        """
        Modifica un viaje en la base de datos.
        """
        try:

            if eventos.Eventos.pedirConfirmacion('¿Desea modificar el viaje con los datos actuales?'):
                row = var.ui.tabViajes.selectedItems()
                fila = [dato.text() for dato in row]
                idViaje = fila[0]
                datosModificados = facturas.Facturas.datosViaje()

                if (str(fila[1]) == str(datosModificados[1]) and str(fila[2]) == str(datosModificados[2]) and
                        str(fila[3]) == str(datosModificados[3]) and str(fila[4]) == str(datosModificados[4])):
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle("Aviso")
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("No hay datos que modificar.")
                    mbox.exec()
                else:
                    query = QtSql.QSqlQuery()
                    query.prepare("update viajes set "
                                  "origen = :origen, destino = :destino, km = :km, tarifa = :tarifa "
                                  "where idViaje = :idViaje")
                    query.bindValue(":origen", str(datosModificados[1]))
                    query.bindValue(":destino", str(datosModificados[2]))
                    query.bindValue(":km", str(datosModificados[3]))
                    query.bindValue(":tarifa", str(datosModificados[4]))
                    query.bindValue(':idViaje', int(idViaje))

                    if query.exec():
                        eventos.Eventos.sacarMbox("Viaje modificado correctamente")
                        facturas.Facturas.cargarviajes()
                    else:
                        eventos.Eventos.sacarMbox("El viaje no se pudo modificar")
                        print(query.lastError().text())
            else:
                eventos.Eventos.sacarMbox("El viaje no se modificó")

        except Exception as error:
            print('Error al borrar viaje ', error)


    @staticmethod
    def buscarFac():
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select numfac, dnicli from facturas where dnicli = :dni')

            query.bindValue(':dni', str(var.ui.txtcifcli.text()))

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registro.append(row)

            facturas.Facturas.cargartablafac(registro)

        except Exception as error:
            print('Error al buscar la factura de un cliente', error)