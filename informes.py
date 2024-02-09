import os, var, shutil
from PIL import Image
from PyQt6 import QtSql, QtWidgets
from reportlab.pdfgen import canvas
from datetime import datetime
from svglib.svglib import svg2rlg
import conexion


class Informes:

    @staticmethod
    def reportclientes():
        """
        Genera un informe en formato PDF con el listado de clientes.
        """
        try:
            # Obtiene la fecha actual
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            # Define el nombre del archivo PDF con la fecha actual
            nombre = fecha + '_listadoclientes.pdf'
            # Crea un objeto de tipo canvas para el informe
            var.report = canvas.Canvas('informesClientes/' + nombre)
            # Define el título del informe
            titulo = 'LISTADO CLIENTES'
            # Genera la cabecera y pie de página del informe
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)

            # Define los elementos de la tabla
            items = ['CÓDIGO', 'DNI', 'RAZÓN SOCIAL', 'MUNICIPIO', 'TELÉFONO', 'FECHA BAJA']

            # Configura la fuente y posición de los elementos en la tabla
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(50, 675, str(items[0]))
            var.report.drawString(100, 675, str(items[1]))
            var.report.drawString(165, 675, str(items[2]))
            var.report.drawString(280, 675, str(items[3]))
            var.report.drawString(380, 675, str(items[4]))
            var.report.drawString(460, 675, str(items[5]))
            var.report.line(50, 670, 525, 670)

            # Realiza la consulta a la base de datos
            query = QtSql.QSqlQuery()
            query.prepare("select codcli, dnicli, razoncli, municli,"
                          " telefonocli, bajacli from clientes order by razoncli")

            if query.exec():
                i = 55
                j = 655
                while query.next():
                    # Verifica si es necesario pasar a la siguiente página
                    if j <= 80:
                        var.report.showPage()
                        Informes.topInforme(titulo)
                        Informes.footInforme(titulo)
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(50, 675, str(items[0]))
                        var.report.drawString(100, 675, str(items[1]))
                        var.report.drawString(165, 675, str(items[2]))
                        var.report.drawString(280, 675, str(items[3]))
                        var.report.drawString(380, 675, str(items[4]))
                        var.report.drawString(460, 675, str(items[5]))
                        var.report.line(50, 670, 525, 670)
                        i = 55
                        j = 655

                    # Configura la fuente y posición de los datos en la tabla
                    var.report.setFont('Helvetica', size=9)
                    var.report.drawCentredString(i + 15, j, str(query.value(0)))
                    var.report.drawString(i + 40, j, str(query.value(1)))
                    var.report.drawString(i + 115, j, str(query.value(2)))
                    var.report.drawString(i + 235, j, str(query.value(3)))
                    var.report.drawString(i + 320, j, str(query.value(4)))
                    var.report.drawString(i + 420, j, str(query.value(5)))
                    j = j - 25

            # Guarda el informe generado
            var.report.save()
            rootPath = '.\\informesClientes'
            for file in os.listdir(rootPath):
                if file.endswith(nombre):
                    os.startfile('%s\\%s' % (rootPath, file))
        except Exception as error:
            print('Error LISTADO CLIENTES :', error)

    @staticmethod
    def reportconductores():
        """
        Genera un informe en formato PDF con el listado de conductores.
        """
        try:
            # Obtiene la fecha actual
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            # Define el nombre del archivo PDF con la fecha actual
            nombre = fecha + '_listadoconductores.pdf'
            # Crea un objeto de tipo canvas para el informe
            var.report = canvas.Canvas('informesConductores/' + nombre)
            # Define el título del informe
            titulo = 'LISTADO CONDUCTORES'
            # Genera la cabecera y pie de página del informe
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)

            # Define los elementos de la tabla
            items = ['CÓDIGO', 'APELLIDOS', 'NOMBRE', 'MÓVIL', 'LICENCIAS', 'FECHA BAJA']

            # Configura la fuente y posición de los elementos en la tabla
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(50, 675, str(items[0]))
            var.report.drawString(110, 675, str(items[1]))
            var.report.drawString(205, 675, str(items[2]))
            var.report.drawString(290, 675, str(items[3]))
            var.report.drawString(380, 675, str(items[4]))
            var.report.drawString(460, 675, str(items[5]))
            var.report.line(50, 670, 525, 670)

            # Realiza la consulta a la base de datos
            query = QtSql.QSqlQuery()
            query.prepare("select codigo, apeldri, nombredri, movildri,"
                          " carnet, bajadri from drivers order by apeldri")

            if query.exec():
                i = 55
                j = 655
                while query.next():
                    # Verifica si es necesario pasar a la siguiente página
                    if j <= 80:
                        var.report.showPage()
                        Informes.topInforme(titulo)
                        Informes.footInforme(titulo)
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(50, 675, str(items[0]))
                        var.report.drawString(110, 675, str(items[1]))
                        var.report.drawString(205, 675, str(items[2]))
                        var.report.drawString(290, 675, str(items[3]))
                        var.report.drawString(380, 675, str(items[4]))
                        var.report.drawString(460, 675, str(items[5]))
                        var.report.line(50, 670, 525, 670)
                        i = 55
                        j = 655

                    # Configura la fuente y posición de los datos en la tabla
                    var.report.setFont('Helvetica', size=9)
                    var.report.drawCentredString(i + 15, j, str(query.value(0)))
                    var.report.drawString(i + 50, j, str(query.value(1)))
                    var.report.drawString(i + 155, j, str(query.value(2)))
                    var.report.drawString(i + 235, j, str(query.value(3)))
                    var.report.drawString(i + 340, j, str(query.value(4)))
                    var.report.drawString(i + 420, j, str(query.value(5)))
                    j = j - 25

            # Guarda el informe generado
            var.report.save()
            rootPath = '.\\informesConductores'
            for file in os.listdir(rootPath):
                if file.endswith(nombre):
                    os.startfile('%s\\%s' % (rootPath, file))
        except Exception as error:
            print('Error LISTADO CONDUCTORES :', error)

    def topInforme(titulo):
        """
        Genera la cabecera del informe con el título especificado.
        """
        try:
            # Ruta de la imagen del logo
            ruta_logo = 'img/logo.png'
            logo = Image.open(ruta_logo)

            # Asegúrate de que el objeto 'logo' sea de tipo 'PngImageFile'
            if isinstance(logo, Image.Image):
                # Línea horizontal superior
                var.report.line(50, 800, 525, 800)
                # Configuración de la fuente y posición del nombre de la empresa
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'Transportes Teis')
                # Configuración de la fuente y posición del título del informe
                var.report.drawString(240, 695, titulo)
                # Línea horizontal inferior
                var.report.line(50, 690, 525, 690)

                # Dibuja la imagen en el informe
                var.report.drawImage(ruta_logo, 480, 725, width=40, height=40)

                # Configuración de la fuente y posición de la información de la empresa
                var.report.setFont('Helvetica', size=9)
                var.report.drawString(55, 770, 'CIF: A12345678')
                var.report.drawString(55, 755, 'Avda. Galicia - 101')
                var.report.drawString(55, 740, 'Vigo - 36216 - España')
                var.report.drawString(55, 725, 'Teléfono: 986 132 456')
                var.report.drawString(55, 710, 'e-mail: cartesteisr@mail.com')
            else:
                print(f'Error: No se pudo cargar la imagen en {ruta_logo}')
        except Exception as error:
            print('Error en cabecera informe:', error)

    @staticmethod
    def topInformeViajes():
        """
        Genera la cabecera específica para informes de viajes.
        """
        try:
            # Configuración de la fuente y posición del número de factura en el informe
            var.report.setFont('Helvetica-Bold', size=12)
            var.report.drawString(300, 785, 'NÚMERO FACTURA: ' + var.ui.lblCodFac.text())

            # Configuración de la fuente y posición de la información del cliente en el informe
            var.report.setFont('Helvetica', size=9)
            var.report.drawString(300, 770, 'CIF: ' + var.ui.txtcifcli.text())
            var.report.drawString(300, 755, 'Razón Social: Kontroller')
            var.report.drawString(300, 740, 'Dirección: Pza. Fuensanta 40 6ºa')
            var.report.drawString(300, 725, 'Provincia: Alicante')
            var.report.drawString(300, 710, 'Teléfono:  688957121')

        except Exception as error:
            print('Error en cabecera informe:', error)

    def footInforme(titulo):
        """
        Genera el pie de página del informe con el título especificado.
        """
        try:
            # Línea horizontal inferior
            var.report.line(50, 50, 525, 50)
            # Obtención de la fecha actual
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            # Configuración de la fuente y posición de la fecha
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            # Configuración de la fuente y posición del título del informe
            var.report.drawString(250, 40, str(titulo))
            # Configuración de la fuente y posición del número de página
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber()))

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)

    @staticmethod
    def reportviajes():
        """
        Genera un informe en formato PDF con el listado de viajes.
        """
        try:
            if var.ui.lblCodFac.text() != "":
                # Obtiene la fecha actual
                fecha = datetime.today()
                fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
                # Define el nombre del archivo PDF con la fecha actual
                nombre = fecha + '_listadoviajes.pdf'
                # Crea un objeto de tipo canvas para el informe
                var.report = canvas.Canvas('informesViajes/' + nombre)
                # Define el título del informe
                titulo = 'LISTADO VIAJES'
                # Genera la cabecera y pie de página del informe
                Informes.topInforme(titulo)
                Informes.topInformeViajes()
                Informes.footInforme(titulo)

                # Define los elementos de la tabla
                items = ['IDVIAJE', 'FACTURA', 'ORIGEN', 'DESTINO', 'TARIFA', 'KM', 'TOTAL']

                # Configura la fuente y posición de los elementos en la tabla
                var.report.setFont('Helvetica-Bold', size=10)
                var.report.drawString(50, 675, str(items[0]))
                var.report.drawString(110, 675, str(items[1]))
                var.report.drawString(195, 675, str(items[2]))
                var.report.drawString(290, 675, str(items[3]))
                var.report.drawString(375, 675, str(items[4]))
                var.report.drawString(440, 675, str(items[5]))
                var.report.drawString(480, 675, str(items[6]))
                var.report.line(50, 670, 525, 670)

                # Realiza la consulta a la base de datos
                query = QtSql.QSqlQuery()
                query.prepare("select idviaje, factura, origen, destino,"
                              " tarifa, km from viajes where factura = :factura")

                query.bindValue(':factura', int(var.ui.lblCodFac.text()))

                subtotal = 0
                if query.exec():
                    i = 55
                    j = 655
                    while query.next():
                        # Verifica si es necesario pasar a la siguiente página
                        if j <= 80:
                            var.report.showPage()
                            Informes.topInforme(titulo)
                            Informes.footInforme(titulo)
                            var.report.setFont('Helvetica-Bold', size=10)
                            var.report.drawString(50, 675, str(items[0]))
                            var.report.drawString(125, 675, str(items[1]))
                            var.report.drawString(195, 675, str(items[2]))
                            var.report.drawString(290, 675, str(items[3]))
                            var.report.drawString(375, 675, str(items[4]))
                            var.report.drawString(440, 675, str(items[5]))
                            var.report.drawString(480, 675, str(items[6]))
                            var.report.line(50, 670, 525, 670)
                            i = 55
                            j = 655

                        # Configura la fuente y posición de los datos en la tabla
                        var.report.setFont('Helvetica', size=9)
                        var.report.drawCentredString(i + 15, j, str(query.value(0)))
                        var.report.drawString(i + 70, j, str(query.value(1)))
                        var.report.drawString(i + 145, j, str(query.value(2)))
                        var.report.drawString(i + 235, j, str(query.value(3)))
                        var.report.drawString(i + 335, j, str(query.value(4)))
                        var.report.drawString(i + 390, j, str(query.value(5)))
                        total = float(query.value(4)) * float(query.value(5))
                        subtotal += total
                        totalRound = round(total, 2)
                        var.report.drawString(i + 430, j, '%.2f' % (float(totalRound)) + '€')
                        var.report.line(50, j + 15, 525, j + 15)
                        j = j - 25

                    # Configura la fuente y posición del resumen del informe
                    var.report.line(50, 140, 525, 140)
                    var.report.drawRightString(i + 450, 130,
                                               'Subtotal: ' + (var.ui.txtSubTotal.text()))
                    var.report.drawRightString(i + 450, 115, 'IVA: ' + var.ui.txtIva.text()[0:2] + ' %')
                    var.report.drawRightString(i + 450, 100,
                                               'Total: ' + (var.ui.txtTotal.text()))

                # Guarda el informe generado
                var.report.save()
                rootPath = '.\\informesViajes'
                for file in os.listdir(rootPath):
                    if file.endswith(nombre):
                        os.startfile('%s\\%s' % (rootPath, file))
            else:
                # Muestra un mensaje si no hay ninguna factura seleccionada
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("No hay ninguna factura seleccionada")
                mbox.exec()

        except Exception as error:
            print('Error LISTADO VIAJES :', error)

    def elegirInforme(self):
        """
        Abre un cuadro de diálogo para seleccionar los informes a generar.
        """
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setStyleSheet("QDialog{background-color: #84b6f4;} "
                               "QLabel {color: rgb(0, 0, 0);} ")
            mbox.setWindowTitle("Realizar Informe")
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("Seleccione informe/es")

            # Configuración de los checkboxes en el cuadro de diálogo
            conductorcheck = QtWidgets.QCheckBox("Informe de conductores")
            clientecheck = QtWidgets.QCheckBox("Informe de clientes")
            viajecheck = QtWidgets.QCheckBox("Informe de Viajes")

            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(conductorcheck)
            layout.addWidget(clientecheck)
            layout.addWidget(viajecheck)

            container = QtWidgets.QWidget()
            container.setLayout(layout)

            mbox.layout().addWidget(container, 1, 1, 1, mbox.layout().columnCount())

            # Configuración de los botones en el cuadro de diálogo
            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Aceptar')
            mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('Cancelar')

            resultado = mbox.exec()

            if resultado == QtWidgets.QMessageBox.StandardButton.Yes:
                # Genera los informes según los checkboxes seleccionados
                if conductorcheck.isChecked():
                    Informes.reportconductores()
                if clientecheck.isChecked():
                    Informes.reportclientes()
                if viajecheck.isChecked():
                    Informes.reportviajes()

        except Exception as error:
            print("Error en checkbox_informe", error)
