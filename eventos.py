import os
import shutil
import xlrd, xlwt

import clientes
import conexion
import drivers
import facturas
import var, sys
from datetime import datetime
from PyQt6 import QtWidgets, QtCore, QtGui, QtSql
import zipfile
import locale

locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')


class Eventos():

    def showSalir(self):
        """
        Muestra la ventana de salir
        """
        try:

            var.exitWindow.show()

        except Exception as error:
            print("error en modulo eventos", error)

    def confirmarSalir(self):
        """
        Cierra el programa al pulsar el botón de aceptar salir
        """
        try:

            sys.exit()

        except Exception as error:
            print("error en modulo eventos", error)

    def cancelarSalir(self):
        """
        Cierra la ventana de salir
        """
        try:

            var.exitWindow.hide()

        except Exception as error:
            print("error en modulo eventos", error)

    @staticmethod
    def showModificarBaja():
        """
        Enseña el dialog para escoger una fecha para modificar la baja
        """
        try:

            var.dlgModificarBajaWindow.show()

        except Exception as error:
            print("error en modulo eventos", error)

    @staticmethod
    def confirmarModificar():
        """
        Confirmas la nueva fecha de baja
        """
        try:

            var.calendarbaja.show()

        except Exception as error:
            print("error en confirmarModificar", error)

    @staticmethod
    def cancelarModificar():
        """
        Cancelas la nueva fecha de baja
        """
        try:

            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
            mbox.setText("Datos conductor modificados")
            mbox.exec()
            var.dlgModificarBajaWindow.hide()


        except Exception as error:
            print("error en cancelarModificar", error)

    @staticmethod
    def acercade():
        """
        Muestra el dialog de Acerca de
        """
        try:

            var.aboutWindow.show()

        except Exception as error:

            print("error abrir ventana acerca de ", error)

    @staticmethod
    def abrirCalendar():
        """
        Abre el calendario
        """
        try:

            var.calendar.show()

        except Exception as error:

            print("error en abrir calendar", error)

    @staticmethod
    def abrirCalendarBaja():
        """
        Abre el calendario de baja
        """
        try:

            var.calendarbaja.show()

        except Exception as error:

            print("error en abrir calendar", error)

    def cargastatusbar(self):
        """
        Carga la status bar
        """
        try:
            '''

                Zona de eventos de StatusBar
            '''
            fecha = datetime.now().strftime("%A - " + "%d/%m/%Y")
            self.labelstatus = QtWidgets.QLabel(fecha, self)
            self.labelstatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            var.ui.statusbar.addPermanentWidget(self.labelstatus, 1)
            self.labelstatusversion = QtWidgets.QLabel("Versión: " + var.version, self)
            self.labelstatusversion.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            var.ui.statusbar.addPermanentWidget(self.labelstatusversion, 0)

        except Exception as error:

            print("error en cargar statusbar", error)

    @staticmethod
    def cargaprov():
        """
        Carga el combobox de provincias
        """
        try:
            prov = ['A Coruña', 'Lugo', 'Ferrol', 'Vigo', 'Santiago de Compostela', 'Ourense', 'Pontevedra']
            var.ui.cmbProv.clear()
            var.ui.cmbProv.addItem("---")
            for i in prov:
                var.ui.cmbProv.addItem(str(i))

        except Exception as error:

            print("Error al mostar cmbProv")

    @staticmethod
    def resizeTabdrivers():
        """
        Ajusta el tamaño de la tabla de Drivers
        """
        try:
            header = var.ui.tabDrivers.horizontalHeader()
            for i in range(var.ui.tabDrivers.columnCount()):
                if i == 0 or i == 4 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print("error con resizeTabdrivers", error)

    @staticmethod
    def resizeTabclientes():
        """
        Ajusta el tamaño de la tabla de clientes
        """
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(var.ui.tabClientes.columnCount()):
                if i == 0 or i == 4 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print("error con resize tabClientes", error)

    @staticmethod
    def letraCapital():
        """
        Ajusta el formato de los txt
        """
        try:
            var.ui.txtApel.setText(var.ui.txtApel.text().title())
            var.ui.txtNombre.setText(var.ui.txtNombre.text().title())
            var.ui.txtNombrecli.setText(var.ui.txtNombrecli.text().title())
            var.ui.txtDNI.setText(var.ui.txtDNI.text().title())
            var.ui.txtDNIcli.setText(var.ui.txtDNIcli.text().title())

        except Exception as error:
            print("error con letra capital", error)

    @staticmethod
    def compruebaFormatoSalario():
        """
        Ajusta el formato del salario
        """
        try:

            salario = var.ui.txtSalario.text()
            var.ui.txtSalario.setText(salario)

            salarioNum = float(salario)

            if salarioNum >= 0.00:
                var.ui.txtSalario.setText(str(locale.currency(float(var.ui.txtSalario.text()))))
            else:
                raise Exception()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Valor de Salario Incorrecto (00000.00)')
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
            msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.setWindowIcon(QtGui.QIcon('./img/driver.ico'))
            msg.exec()
            var.ui.txtSalario.setText("")
            var.ui.txtSalario.setFocus()


































    @staticmethod
    def compruebaMovil():
        """
        Comprueba que el teléfono sean 9 dígitos
        """
        try:
            movil = var.ui.txtMovilDriver.text()
            var.ui.txtMovilDriver.setText(movil)

            if not (len(movil) == 9 and movil.isdigit()):

                raise Exception()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Valor de Móvil Incorrecto (9 dígitos)')
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
            msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.setWindowIcon(QtGui.QIcon('./img/driver.ico'))
            msg.exec()
            var.ui.txtMovilDriver.setText("")
            var.ui.txtMovilDriver.setFocus()

    @staticmethod
    def compruebaMovilcli():
        """
        Comprueba que el teléfono del cliente sean 9 dígitos
        """
        try:
            movil = var.ui.txtMovilcli.text()
            var.ui.txtMovilcli.setText(movil)

            if not movil.isdigit():
                raise Exception()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Valor de Móvil Incorrecto (9 dígitos)')
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
            msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.setWindowIcon(QtGui.QIcon('./img/driver.ico'))
            msg.exec()
            var.ui.txtMovilcli.setText("")
            var.ui.txtMovilcli.setFocus()

    @staticmethod
    def crearbackup():
        """
        Crea un backup de la base de datos
        """
        try:
            fecha = datetime.today()

            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            copia = str(fecha) + '_backup.zip'

            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Copia Seguridad', copia, '.zip')

            if var.dlgabrir.accept and filename:
                fichzip = zipfile.ZipFile(copia, 'w')
                fichzip.write(var.bbdd, os.path.basename(var.bbdd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(copia), str(directorio))

                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Copia de Seguridad creada.')
                msg.exec()

        except Exception as error:

            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error en Copia de Seguridad')
            msg.exec()
            print("error al crear backup", error)

    @staticmethod
    def restaurarbackup():
        """
        Restaura un backup de la base de datos
        """
        try:

            filename = var.dlgabrir.getOpenFileName(None, 'Restaurar Copia de Seguridad',
                                                    '', '*.zip;;All Files(*)')

            file = filename[0]

            if var.dlgabrir.accept and file:

                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()

                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Copia de Seguridad restaurada')
                msg.exec()

                conexion.Conexion.mostrardrivers()
                conexion.Conexion.mostrarclientes()
                conexion.Conexion.selectFac()
                conexion.Conexion.cargadriverfac()

        except Exception as error:

            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al Restaurar Copia de Seguridad', error)
            msg.exec()

    @staticmethod
    def exportardatosxlsdriv():
        """
        Exporta los drivers en formato xls
        """
        try:
            fecha = datetime.today()

            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            file = str(fecha) + '_Datos.xls'

            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar Datos en xls', file, '.xls')

            if var.dlgabrir.accept and filename:
                wb = xlwt.Workbook()
                sheet1 = wb.add_sheet('Conductores')
                sheet1.write(0, 0, 'ID')
                sheet1.write(0, 1, 'DNI')
                sheet1.write(0, 2, 'Fecha Alta')
                sheet1.write(0, 3, 'Nombre')
                sheet1.write(0, 4, 'Apellidos')
                sheet1.write(0, 5, 'Dirección')
                sheet1.write(0, 6, 'Provincia')
                sheet1.write(0, 7, 'Municipio')
                sheet1.write(0, 8, 'Móvil')
                sheet1.write(0, 9, 'Salario')
                sheet1.write(0, 10, 'Carnet')
                sheet1.write(0, 11, 'Fecha Baja')

                registros = conexion.Conexion.selectdriverstodos()

                for fila, registro in enumerate(registros, 1):

                    for i, valor in enumerate(registro):

                        sheet1.write(fila, i, str(valor))

                wb.save(directorio)

                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Datos xls exportados!')
                msg.exec()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al Exportar datos', error)
            msg.exec()

    @staticmethod
    def importardatosxlsdriv():
        """
        Importa los Drivers en formato xls
        """
        try:
            filename, _ = var.dlgabrir.getOpenFileName(None, "Importar Datos ", "", "*.xls;;All Files(*)")

            if var.dlgabrir.accept and filename != "":

                documento = xlrd.open_workbook(filename)
                datos = documento.sheet_by_index(0)
                filas = datos.nrows
                columnas = datos.ncols

                for i in range(filas):
                    if i != 0:  # no coge la fila de los títulos
                        new = []
                        for j in range(columnas):
                            new.append(str(datos.cell_value(i, j)))
                        conexion.Conexion.guardarimport(new)

                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Datos importados')
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                msg.exec()
                var.ui.txtDNI.clear()
                var.ui.lblValidarDNI.clear()
                conexion.Conexion.mostrardrivers()
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setWindowIcon(QtGui.QIcon("./img/logo.ico"))
            msg.setText('Error al importarDatos' + str(error))
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
            msg.exec()

    @staticmethod
    def exportardatosxlscli():
        """
        Exporta los clientes en formato xls
        """
        try:
            fecha = datetime.today()

            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            file = str(fecha) + '_Datos.xls'

            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar Datos en xls', file, '.xls')

            if var.dlgabrir.accept and filename:
                wb = xlwt.Workbook()
                sheet1 = wb.add_sheet('Clientes')
                sheet1.write(0, 0, 'ID')
                sheet1.write(0, 1, 'DNI')
                sheet1.write(0, 2, 'Razón Social')
                sheet1.write(0, 3, 'Dirección')
                sheet1.write(0, 4, 'Teléfono')
                sheet1.write(0, 5, 'Provincia')
                sheet1.write(0, 6, 'Municipio')
                sheet1.write(0, 7, 'Fecha Baja')

                registros = conexion.Conexion.selectclientestodos()

                for fila, registro in enumerate(registros, 1):

                    for i, valor in enumerate(registro):
                        sheet1.write(fila, i, str(valor))

                wb.save(directorio)

                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Datos xls exportados!')
                msg.exec()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error al Exportar datos', error)
            msg.exec()

    @staticmethod
    def importardatosxlscli():
        """
        Importa los Clietnes en formato xls
        """
        try:
            filename, _ = var.dlgabrir.getOpenFileName(None, "Importar Datos ", "", "*.xls;;All Files(*)")

            if var.dlgabrir.accept and filename != "":

                documento = xlrd.open_workbook(filename)
                datos = documento.sheet_by_index(0)
                filas = datos.nrows
                columnas = datos.ncols

                for i in range(filas):
                    if i != 0:  # no coge la fila de los títulos
                        new = []
                        for j in range(columnas):
                            new.append(str(datos.cell_value(i, j)))
                        conexion.Conexion.guardarimportcli(new)

                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Datos importados')
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                msg.exec()
                var.ui.txtDNIcli.clear()
                var.ui.lblValidarDNIcli.clear()
                conexion.Conexion.mostrarclientes()
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setWindowIcon(QtGui.QIcon("./img/logo.ico"))
            msg.setText('Error al importarDatos' + str(error))
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
            msg.exec()

    @staticmethod
    def resizeTabfacturas():
        """
        Ajusta el tamaño de las facturas
        """
        try:
            header = var.ui.tabFacturas.horizontalHeader()
            for i in range(var.ui.tabFacturas.columnCount()):
                if i == 0 or i == 4 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print("error con resizeTabfacturas", error)

    @staticmethod
    def resizeTabviaje():
        """
        Ajusta el tamaño del panel de viajes
        """
        try:
            header = var.ui.tabViajes.horizontalHeader()
            for i in range(var.ui.tabViajes.columnCount()):
                if i == 0 or i == 4 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print("error con resizeTabviajes", error)

    @staticmethod
    def comprobarAltaFac(dni):
        """

        :param dni: recibe un dni
        :type dni: String
        :return: Si falta algún dato o no por cubrir y si está dado de baja algún cliente o no
        :rtype: Boolean

        Realiza las comprobaciones para saber si se puede dar de alta una factura
        """
        try:
            if (var.ui.txtDataFac.text().strip() == "" or dni.strip() == ""
                    or var.ui.cmbConductor.currentText() == ""):
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('Faltan datos por cubrir')
                msg.exec()

                return False        # Devuelve False si falta algún dato por cubrir

            else:
                if clientes.Clientes.comprobarbajacli(dni):
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setText('El cliente no puede estar dado de baja')
                    msg.exec()

                    return False    # Devuelve False si el cliente está dado de baja

                else:

                    return True     # Devuelve True si todos los campos están cubiertos

        except Exception as error:
            print('Error al comprobar alta fac', error)

    @staticmethod
    def existeDni(dni):
        """
        Comprueba si un cliente existe en la base de datos o no
        :param dni: Recibe un dni
        :type dni: String
        :return: Si existe el cliente o no
        :rtype: Boolean
        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select codcli from clientes where dnicli = :dni')

            query.bindValue(':dni', str(dni))

            if query.exec():
                if query.next():
                    return True     # Devuelve True si existe
            else:

                return False        # Devuelve False si no existe

        except Exception as error:
            print('error al comprobar si exitse el dni', error)

    @staticmethod
    def limpiartodo():
        """
        Limpia todos los paneles
        """
        try:
            drivers.Drivers.limpiarPanel()
            clientes.Clientes.limpiarPanel()
            facturas.Facturas.limpiarPanel()

        except Exception as error:
            print('error al limpiar todo', error)

