from PyQt6 import QtWidgets, QtCore, QtSql

import conexion
import var


class Clientes():

    @staticmethod
    def validarDNIcli(dni):
        try:
            dni = dni.upper()
            var.ui.txtDNIcli.setText(dni)
            tabla = "TRWAGMYFPDXBNJCSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"

            if len(dni) == 9:  # compruebo que son 9
                dig_control = dni[8]  # tomo la letra del dni
                dni = dni[:8]  # tomo los numeros del dni
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblValidarDNIcli.setStyleSheet('color:green;')
                    var.ui.lblValidarDNIcli.setText('V')
                    return True
                else:
                    var.ui.lblValidarDNIcli.setStyleSheet('color:red;')
                    var.ui.lblValidarDNIcli.setText('X')
                    var.ui.txtDNIcli.clear()
                    return False
            else:
                var.ui.lblValidarDNIcli.setStyleSheet('color:red;')
                var.ui.lblValidarDNIcli.setText('X')
                var.ui.txtDNIcli.clear()
                return False

        except Exception as error:
            print("error en validar dnicli ", error)

    @staticmethod
    def limpiarPanel():
        try:
            listaWidgets = [var.ui.lblCodBDcli, var.ui.txtDNIcli, var.ui.txtNombrecli, var.ui.txtDircli,
                            var.ui.txtMovilcli]
            for i in listaWidgets:
                i.clear()

            var.ui.cmbProvcli.setCurrentText('')
            var.ui.cmbMunicli.setCurrentText('')

        except Exception as error:
            print("error al limpiar panel", error)

    @staticmethod
    def cargarclientes():
        try:
            Clientes.limpiarPanel()

            row = var.ui.tabClientes.selectedItems()

            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.onecli(fila[0])

            datos = [var.ui.lblCodBDcli, var.ui.txtDNIcli, var.ui.txtNombrecli,
                     var.ui.txtDircli, var.ui.txtMovilcli, var.ui.cmbProvcli, var.ui.cmbMunicli]

            for i, dato in enumerate(datos):
                if i == 5 or i == 6:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))

        except Exception as error:
            print('error al cargar cliente', error)



    def cargartablacli(registros):
        try:
            index = 0
            for registro in registros:
                var.ui.tabClientes.setRowCount(index + 1)
                var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                var.ui.tabClientes.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[5])))
                var.ui.tabClientes.setItem(index, 6, QtWidgets.QTableWidgetItem(str(registro[6])))
                var.ui.tabClientes.setItem(index, 7, QtWidgets.QTableWidgetItem(str(registro[7])))
                var.ui.tabClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabClientes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabClientes.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print('error cargar dato en tabla clientes', error)

    @staticmethod
    def altacli():
        try:
            dni = var.ui.txtDNIcli.text()
            codigo = var.ui.lblCodBDcli.text()

            if codigo != "":

                if Clientes.comprobarfechabajacli(codigo):
                    if Clientes.validarDNIcli(dni):
                        conexion.Conexion.borrarfechabajacli(codigo)
                        Clientes.selEstadocli()
                    else:
                        mbox = QtWidgets.QMessageBox()
                        mbox.setWindowTitle('Aviso')
                        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                        mbox.setText("DNI no válido")
                        mbox.exec()
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("No puedes dar de alta a un empleado dado de alta")
                    mbox.exec()

            else:

                if Clientes.validarDNIcli(dni):
                    cliente = [var.ui.txtDNIcli,
                               var.ui.txtNombrecli,
                               var.ui.txtDircli,
                               var.ui.txtMovilcli]
                    newcliente = []
                    for i in cliente:
                        newcliente.append(i.text().title())

                    prov = var.ui.cmbProvcli.currentText()
                    newcliente.insert(5, prov)
                    muni = var.ui.cmbMunicli.currentText()
                    newcliente.insert(6, muni)

                    conexion.Conexion.guardarcli(newcliente)
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("DNI no válido")
                    mbox.exec()
                    var.ui.lblValidarDNIcli.setText('X')
                    var.ui.lblValidarDNIcli.setStyleSheet('color:red;')
                    var.ui.txtDNIcli.clear()
                    var.ui.txtDNIcli.setFocus()

        except Exception as error:
            print("Error con alta cliente", error)

    @staticmethod
    def buscarcli():
        try:
            dni = var.ui.txtDNIcli.text()
            registro = conexion.Conexion.buscacli(dni)
            if registro is not None:
                Clientes.buscarentabla(registro)
                var.ui.txtcifcli.setText(dni)
            else:
                var.ui.txtDNIcli.clear()

        except Exception as error:
            print('error al buscar cliente', error)

    def buscarentabla(registro):
        try:
            codigo = registro[0]

            for i in range(var.ui.tabClientes.rowCount()):
                if var.ui.tabClientes.item(i, 0).text() == codigo:
                    var.ui.tabClientes.selectRow(i)
                    var.ui.tabClientes.scrollToItem(var.ui.tabClientes.item(i, 0))

        except Exception as error:
            print("Error al buscar cliente en la tabla", error)

    @staticmethod
    def borrarcli():
        try:
            dni = var.ui.txtDNIcli.text()
            conexion.Conexion.borracli(dni)
            Clientes.selEstadocli()

        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("El cliente no existe o no se puede borrar")
            mbox.exec()


    @staticmethod
    def modifcli():
        try:
            dni = var.ui.txtDNIcli.text()

            if Clientes.validarDNIcli(dni):
                cliente = [var.ui.lblCodBDcli,
                           var.ui.txtDNIcli,
                           var.ui.txtNombrecli,
                           var.ui.txtDircli,
                           var.ui.txtMovilcli]
                modifcliente = []
                for i in cliente:
                    modifcliente.append(i.text().title())

                prov = var.ui.cmbProvcli.currentText()
                modifcliente.insert(5, prov)
                muni = var.ui.cmbMunicli.currentText()
                modifcliente.insert(6, muni)

                conexion.Conexion.modifCliente(modifcliente)

            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("DNI no válido")
                mbox.exec()
                var.ui.lblValidarDNIcli.setText('X')
                var.ui.lblValidarDNIcli.setStyleSheet('color:red;')
                var.ui.txtDNIcli.clear()
                var.ui.txtDNIcli.setFocus()

        except Exception as error:
            print("error en modif cliente en Clientes", error)

    def comprobarfechabajacli(codigo):
        try:
            baja = True
            query = QtSql.QSqlQuery()
            query.prepare("select bajacli from clientes where codcli = :codigo")
            query.bindValue(':codigo', int(codigo))
            if query.exec():
                while query.next():
                    fecha = query.value(0)
                    if fecha == "":
                        baja = False
            return baja

        except Exception as error:
            print('error al comprobar fecha baja cliente', error)


    @staticmethod
    def selEstadocli():

        if var.ui.chkTodoscli.isChecked():
            estado = 1
            conexion.Conexion.selectClientes(estado)

        else:
            estado = 0
            conexion.Conexion.selectClientes(estado)

    @staticmethod
    def comprobarbajacli(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("select bajacli from clientes where dnicli = :dni")

            query.bindValue(':dni', dni)

            if query.exec():
                while query.next():
                    fecha = query.value(0)
                    if fecha == "":
                        baja = False
                        return baja
                    else:
                        return True

        except Exception as error:
            print('error al comprobar la baja del cliente', error)

