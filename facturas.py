from PyQt6 import QtWidgets, QtCore, QtSql, QtGui


import clientes
import conexion
import drivers
import eventos
import facturas
import var


class Facturas:

    def cargarFecha(qDate):
        """
        Método para el calendario
        """
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDataFac.setText(str(data))
            var.calendarfac.hide()

        except Exception as error:
            print("error en cargar fecha en facturas", error)

    @staticmethod
    def abrirCalendar():
        """
        Abre el calendario
        """
        try:

            var.calendarfac.show()

        except Exception as error:

            print("error en abrir calendar", error)



    @staticmethod
    def limpiarPanel():
        """
        Limpia el panel de facturas
        """
        try:
            listaWidgets = [var.ui.lblCodFac, var.ui.txtcifcli, var.ui.txtDataFac, var.ui.txtkm]
            for i in listaWidgets:
                i.clear()

            var.ui.tabViajes.setRowCount(0)

            var.ui.cmbConductor.setCurrentText('')
            var.ui.cmbProvOrigen.setCurrentText('')
            var.ui.cmbProvDestino.setCurrentText('')



        except Exception as error:
            print("error al limpiar panel", error)

    @staticmethod
    def guardarFac():
        """
        Guarda una factura
        """
        try:
            conductor = var.ui.cmbConductor.currentText()
            dni = var.ui.txtcifcli.text()
            codigoDri = conductor.split("-")[0]
            registro = [var.ui.txtcifcli.text(), var.ui.txtDataFac.text(), codigoDri]

            if eventos.Eventos.comprobarAltaFac(dni):

                if eventos.Eventos.existeDni(dni):

                    conexion.Conexion.altaFacturacion(registro)
                    conexion.Conexion.selectFac()

                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setText('El DNI no existe')
                    msg.exec()

            eventos.Eventos.limpiartodo()

        except Exception as error:
            print('Error al guardar una factura', error)

    @staticmethod
    def cargarfacturas():
        """
        Carga los datos en el panel de una factura
        """
        try:
            Facturas.limpiarPanel()

            row = var.ui.tabFacturas.selectedItems()

            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.onefac(fila[0])
            apellido = conexion.Conexion.getApel(registro[3])
            txtCmb = str(registro[3]) + "- " + apellido

            datos = [var.ui.lblCodFac, var.ui.txtcifcli, var.ui.txtDataFac, var.ui.cmbConductor]

            for i, dato in enumerate(datos):

                if i == 3:
                    dato.setCurrentText(str(txtCmb))
                else:
                    dato.setText(str(registro[i]))

            facturas.Facturas.cargarviajes()

        except Exception as error:
            print('error al cargar cliente', error)

    @staticmethod
    def cargartablafac(registros):
        """

        :param registros: datos de facturas
        :type registros: list
        """
        try:
            index = 0
            for registro in registros:
                var.ui.tabFacturas.setRowCount(index + 1)
                var.ui.tabFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print('error cargar dato en tabla facturas', error)

    @staticmethod
    def guardarviaje():
        """
        Llama al método guardarViajeBD() de la clase Conexion y guarda un registro en la base de datos
        """
        try:
            if var.ui.cmbLocOrigen.currentText().strip() == "" or var.ui.cmbLocDestino.currentText().strip() == "" or var.ui.txtkm.text().strip() == "" or var.ui.lblCodFac.text().strip() == "":
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Faltan datos por rellenar")
                mbox.exec()

            else:
                tarifa = Facturas.comprobarTarifa()
                registro = [var.ui.lblCodFac.text(), var.ui.cmbLocOrigen.currentText(), var.ui.cmbLocDestino.currentText(), tarifa, var.ui.txtkm.text()]

                conexion.Conexion.guardarviajeBD(registro)

        except Exception as error:
            print('error al guardar viaje en guardarviaje()', error)


    @staticmethod
    def cargartarifa():
        """
        Selecciona un radio button según los combo box de las provincias y localidades
        """
        try:
            if var.ui.cmbLocOrigen.currentText() != "" and var.ui.cmbLocDestino.currentText() != "":
                if var.ui.cmbLocDestino.currentText() == var.ui.cmbLocOrigen.currentText():

                    var.ui.rbtLocal.setChecked(True)

                elif var.ui.cmbProvDestino.currentText() == var.ui.cmbProvOrigen.currentText():

                    var.ui.rbtProvincial.setChecked(True)

                else:
                    var.ui.rbtNacional.setChecked(True)

                tarifa = Facturas.comprobarTarifa()

        except Exception as error:
            print('error al cargar la tarifa', error)

    @staticmethod
    def cargarviajes():
        """
        Carga los viajes en la tabla viajes
        """
        try:
            registros = conexion.Conexion.seleccionarviajes()

            index = 0
            subtotal = 0
            for registro in registros:
                var.ui.tabViajes.setRowCount(index + 1)
                var.ui.tabViajes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabViajes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabViajes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tabViajes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[5])))
                var.ui.tabViajes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                total = float(registro[4]) * float(registro[5])
                subtotal += total
                totalRound = round(total, 2)
                var.ui.tabViajes.setItem(index, 5, QtWidgets.QTableWidgetItem('%.2f' % totalRound))
                var.ui.tabViajes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabViajes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabViajes.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                botondel = QtWidgets.QPushButton()
                botondel.setFixedSize(40, 28)
                botondel.setIcon(QtGui.QIcon('img/basura.ico'))
                var.ui.tabViajes.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                var.ui.tabViajes.setColumnWidth(6, 50)
                var.ui.tabViajes.setCellWidget(index, 6, botondel)
                botondel.clicked.connect(conexion.Conexion.borrarviaje)

                index += 1

            var.ui.txtSubTotal.setText('%.2f' % (float(subtotal)) + ' €')
            var.ui.txtIva.setText('21%')
            var.ui.txtTotal.setText('%.2f' % (float(subtotal * 1.21)) + ' €')

        except Exception as error:
            print('error cargar dato en tabla viajes', error)

    @staticmethod
    def comprobarTarifa():
        """

        :return: tarifa del viaje
        :rtype: float
        """
        try:
            if var.ui.rbtNacional.isChecked():
                tarifa = 0.8
            elif var.ui.rbtLocal.isChecked():
                tarifa = 0.2
            else:
                tarifa = 0.4
            return tarifa

        except Exception as error:
            print('error al cargar el valor de la tarifa', error)

    @staticmethod
    def cargarViajesDatos():
        """
        Carga en el panel los datos del viaje
        """
        try:

            row = var.ui.tabViajes.selectedItems()

            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.oneviaje(fila[0])

            datos = [var.ui.cmbProvOrigen, var.ui.cmbLocOrigen, var.ui.cmbProvDestino, var.ui.cmbLocDestino,
                     var.ui.txtkm]

            muniOrg = registro[2]
            muniDest = registro[3]

            provOrg = facturas.Facturas.getProvByMuni(muniOrg)
            provDest = facturas.Facturas.getProvByMuni(muniDest)

            datos[0].setCurrentText(provOrg)
            datos[1].setCurrentText(muniOrg)
            datos[2].setCurrentText(provDest)
            datos[3].setCurrentText(muniDest)
            datos[4].setText(registro[5])

        except Exception as error:
            print("error ao cargar viaxe seleccionado ", error)

    def getProvByMuni(muni: str):
        """

        :return: provincia
        :rtype: String
        """
        try:

            query = QtSql.QSqlQuery()
            query.prepare(
                'select provincia from provincias where idprov = (select idprov from municipios where municipio = :mun)')
            query.bindValue(':mun', str(muni))

            if query.exec():
                query.next()
                return query.value(0)

            else:
                print(query.lastError())

        except Exception as error:
            print('error en getProvByMuni ', error)

    @staticmethod
    def datosViaje():
        """

        :return: registro de datos de un viaje
        :rtype: list
        """
        try:
            tarifa = Facturas.comprobarTarifa()
            registro = [var.ui.lblCodFac.text(), var.ui.cmbLocOrigen.currentText(), var.ui.cmbLocDestino.currentText()
                        , var.ui.txtkm.text(), tarifa]

            return registro
        except Exception as error:
            print('error en datosViaje()', error)


