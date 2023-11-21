import var, eventos, conexion
from PyQt6 import QtWidgets, QtCore


def validarDNI():
    try:
        correcto = True
        dni = var.ui.txtDNI.text()
        dni = dni.upper()
        var.ui.txtDNI.setText(dni)
        tabla = "TRWAGMYFPDXBNJSZQVHCLKE"
        dig_ext = "XYZ"
        reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
        numeros = "1234567890"
        if len(dni) == 9:  # Comprueba que son 9 caracteres
            dig_control = dni[8]  # Tomo la letra del DNI
            dni = dni[:8]  # Tomo los números del DNI
            if dni[0] in dig_ext:
                dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
            if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23 == dig_control]:
                var.ui.lblValidarDNI.setText('V')
                var.ui.lblValidarDNI.setStyleSheet('color:green;')
                return correcto

            else:
                correcto = False
                return correcto

        else:
            correcto = False
            return correcto

    except Exception as error:
        print("error en validar dni ", error)


class Drivers():
    def cargarFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDataDriver.setText(str(data))
            var.calendar.hide()

        except Exception as error:
            print("error en cargar fecha", error)

    def limpiarPanel(self):
        try:
            listaWidgets = [var.ui.lblCodBD, var.ui.txtDNI, var.ui.txtDataDriver, var.ui.txtApel, var.ui.txtNombre,
                            var.ui.txtDirDriver,
                            var.ui.txtMovilDriver, var.ui.txtSalario, var.ui.lblValidarDNI]
            for i in listaWidgets:
                i.clear()

            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chklicencia:
                i.setChecked(False)
            var.ui.cmbProv.setCurrentText('')
            var.ui.cmbMuni.setCurrentText('')



        except Exception as error:
            print("error al limpiar panel", error)

    def altaDriver(self):
        try:
            if validarDNI():
                driver = [var.ui.txtDNI,
                          var.ui.txtDataDriver,
                          var.ui.txtNombre,
                          var.ui.txtApel,
                          var.ui.txtDirDriver,
                          var.ui.txtMovilDriver,
                          var.ui.txtSalario]
                newdriver = []
                for i in driver:
                    newdriver.append(i.text().title())

                prov = var.ui.cmbProv.currentText()
                newdriver.insert(5, prov)
                muni = var.ui.cmbMuni.currentText()
                newdriver.insert(6, muni)

                licencias = []
                chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
                for i in chklicencia:
                    if i.isChecked():
                        licencias.append(i.text())
                newdriver.append('/'.join(licencias))

                conexion.Conexion.guardardri(newdriver)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("DNI no válido")
                mbox.exec()
                var.ui.lblValidarDNI.setText('X')
                var.ui.lblValidarDNI.setStyleSheet('color:red;')
                var.ui.txtDNI.clear()
                var.ui.txtDNI.setFocus()

        except Exception as error:
            print("Error con alta driver", error)

    def selEstado(self):

        if var.ui.rbtTodos.isChecked():
            estado = 0
            conexion.Conexion.selectDrivers(estado)

        if var.ui.rbtAlta.isChecked():
            estado = 1
            conexion.Conexion.selectDrivers(estado)

        if var.ui.rbtBaja.isChecked():
            estado = 2
            conexion.Conexion.selectDrivers(estado)

    def cargartabladri(registros):
        try:
            index = 0
            for registro in registros:
                var.ui.tabDrivers.setRowCount(index + 1)
                var.ui.tabDrivers.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                var.ui.tabDrivers.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[5])))
                var.ui.tabDrivers.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print('error cargar dato en tabla', error)

    def cargardrivers(self):
        try:
            Drivers.limpiarPanel(self)

            row = var.ui.tabDrivers.selectedItems()

            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.onedriver(fila[0])

            datos = [var.ui.lblCodBD, var.ui.txtDNI, var.ui.txtDataDriver, var.ui.txtApel,
                     var.ui.txtNombre, var.ui.txtDirDriver, var.ui.cmbProv, var.ui.cmbMuni,
                     var.ui.txtMovilDriver, var.ui.txtSalario]

            for i, dato in enumerate(datos):
                if i == 6 or i == 7:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))

            if 'A' in registro[10]:
                var.ui.chkA.setChecked(True)
            if 'B' in registro[10]:
                var.ui.chkB.setChecked(True)
            if 'C' in registro[10]:
                var.ui.chkC.setChecked(True)
            if 'D' in registro[10]:
                var.ui.chkD.setChecked(True)



        except Exception as error:
            print('error al cargar driver', error)

    def buscadriver(self):
        try:
            dni = var.ui.txtDNI.text()
            registro = conexion.Conexion.codDri(dni)
            if registro is not None:
                Drivers.buscarentabla(registro)
                Drivers.cargardatos(registro)
            else:
                var.ui.txtDNI.clear()

        except Exception as error:
            print('error al buscar driver', error)

    def cargardatos(registro):
        try:
            datos = [var.ui.lblCodBD, var.ui.txtDNI, var.ui.txtDataDriver, var.ui.txtApel,
                     var.ui.txtNombre, var.ui.txtDirDriver, var.ui.cmbProv, var.ui.cmbMuni,
                     var.ui.txtMovilDriver, var.ui.txtSalario]

            for i, dato in enumerate(datos):
                if i == 6 or i == 7:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))

            if 'A' in registro[10]:
                var.ui.chkA.setChecked(True)
            if 'B' in registro[10]:
                var.ui.chkB.setChecked(True)
            if 'C' in registro[10]:
                var.ui.chkC.setChecked(True)
            if 'D' in registro[10]:
                var.ui.chkD.setChecked(True)
        except Exception as error:
            print("error al cargar datos del driver", error)


    def modifDri(self):
        try:
            driver = [var.ui.lblCodBD,
                      var.ui.txtDNI,
                      var.ui.txtDataDriver,
                      var.ui.txtApel,
                      var.ui.txtNombre,
                      var.ui.txtDirDriver,
                      var.ui.txtMovilDriver,
                      var.ui.txtSalario]
            modifdriver = []
            for i in driver:
                modifdriver.append(i.text().title())

            prov = var.ui.cmbProv.currentText()
            modifdriver.insert(6, prov)
            muni = var.ui.cmbMuni.currentText()
            modifdriver.insert(7, muni)

            licencias = []
            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chklicencia:
                if i.isChecked():
                    licencias.append(i.text())
            modifdriver.append('/'.join(licencias))
            conexion.Conexion.modifDriver(modifdriver)

        except Exception as error:
            print("error en modif driver en Drivers", error)

    def buscarentabla(registro):
        try:
            codigo = registro[0]
            for i in range(var.ui.tabDrivers.rowCount()):
                if var.ui.tabDrivers.item(i, 0).text() == codigo:
                    var.ui.tabDrivers.selectRow(i)
                    var.ui.tabDrivers.scrollToItem(var.ui.tabDrivers.item(i, 0))

        except Exception as error:
            print("Error al buscar driver en la tabla", error)



    def borrarDriv(self):
        try:
            dni = var.ui.txtDNI.text()
            conexion.Conexion.borraDriv(dni)
            conexion.Conexion.mostrardriversalta()


        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("El conductor no existe o no se puede borrar")
            mbox.exec()
