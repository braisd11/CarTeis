import var
from datetime import datetime

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
