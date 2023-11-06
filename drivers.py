import var, eventos, conexion
from PyQt6 import QtWidgets, QtCore

class Drivers():
    def cargarFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDataDriver.setText(str(data))
            var.calendar.hide()

        except Exception as error:
            print("error en cargar fecha", error)

    def validarDNI(self=None):
        try:
            dni = var.ui.txtDNI.text()
            dni = dni.upper()
            var.ui.txtDNI.setText(dni)
            tabla = "TRWAGMYFPDXBNJZSVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            if len(dni) == 9:                   # Comprueba que son 9 caracteres
                dig_control = dni[8]            # Tomo la letra del DNI
                dni = dni[:8]                   # Tomo los números del DNI
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblValidarDNI.setText('V')
                    var.ui.lblValidarDNI.setStyleSheet('color:green;')
                else:
                    var.ui.lblValidarDNI.setText('X')
                    var.ui.lblValidarDNI.setStyleSheet('color:red;')
                    var.ui.txtDNI.clear()
            else:
                var.ui.lblValidarDNI.setText('X')
                var.ui.lblValidarDNI.setStyleSheet('color:red;')
                var.ui.txtDNI.clear()

        except Exception as error:
            print("error en validar dni ", error)



    def limpiarPanel(self):
        try:
            listaWidgets = [var.ui.txtDNI, var.ui.txtDataDriver, var.ui.txtApel, var.ui.txtNombre, var.ui.txtDirDriver,
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


            driver = [var.ui.txtDNI,
                      var.ui.txtDataDriver,
                      var.ui.txtNombre,
                      var.ui.txtApel,
                      var.ui.txtDirDriver,
                      var.ui.txtMovilDriver,
                      var.ui.txtSalario]
            newdriver=[]
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


        except Exception as error:
            print("Error con alta driver", error)

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
                var.ui.tabDrivers.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print('error en alta cliente', error)

    def cargardrivers(self):
        try:
            Drivers.limpiarPanel(self)

            row = var.ui.tabDrivers.selectedItems()

            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.onedriver(fila[0])

            datos = [var.ui.lblCodBD, var.ui.txtDNI, var.ui.txtDataDriver, var.ui.txtApel,
                     var.ui.txtNombre, var.ui.txtDirDriver, var.ui.cmbProv, var.ui.cmbMuni,
                     var.ui.txtMovilDriver, var.ui.txtSalario]
            j = 0
            for i in datos:
                i.setText(str(registro[j]))
                if j == 6:
                    i.setCurrentText(str(registro[j]))

                j = j + 1



        except Exception as error:
            print('error al cargar driver', error)
