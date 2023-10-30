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
                    var.ui.txtDNI.setFocus()
            else:
                var.ui.lblValidarDNI.setText('X')
                var.ui.lblValidarDNI.setStyleSheet('color:red;')
                var.ui.txtDNI.clear()
                var.ui.txtDNI.setFocus()
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
                      var.ui.txtApel,
                      var.ui.txtNombre,
                      var.ui.txtDirDriver,
                      var.ui.txtMovilDriver,
                      var.ui.txtSalario]
            newdriver=[]
            newdriver.append(1)
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
            #conexion.Conexion.guardarcli()
            print(newdriver)
            index = 0

            '''
            var.ui.tabDrivers.setRowCount(index+1)  # Crea una fila
            
            # Debajo hay una opción sin for para cuando utilicemos BBDD
            for i in range(var.ui.tabDrivers.columnCount()-1):
                var.ui.tabDrivers.setItem(index, i, QtWidgets.QTableWidgetItem(str(newdriver[i])))
                if i == 3 or i == 4:
                    var.ui.tabDrivers.Item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            '''

            # OPCIÓN SIN FOR
                
                
            var.ui.tabDrivers.setRowCount(index + 1)  # Crea una fila
            var.ui.tabDrivers.setItem(index, 0, QtWidgets.QTableWidgetItem(str(newdriver[0])))
            var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(newdriver[1])))
            var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(newdriver[2])))
            var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(newdriver[3])))
            var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(newdriver[4])))
            var.ui.tabDrivers.Item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        except Exception as error:
            print("Error con alta driver", error)
