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
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre = fecha + '_listadoclientes.pdf'
            var.report = canvas.Canvas('informesClientes/' + nombre)
            titulo = 'LISTADO CLIENTES'
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)

            items = ['CÓDIGO', 'DNI', 'RAZÓN SOCIAL', 'MUNICIPIO', 'TELÉFONO', 'FECHA BAJA']

            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(50, 675, str(items[0]))
            var.report.drawString(100, 675, str(items[1]))
            var.report.drawString(165, 675, str(items[2]))
            var.report.drawString(280, 675, str(items[3]))
            var.report.drawString(380, 675, str(items[4]))
            var.report.drawString(460, 675, str(items[5]))
            var.report.line(50, 670, 525, 670)

            query = QtSql.QSqlQuery()
            query.prepare("select codcli, dnicli, razoncli, municli,"
                          " telefonocli, bajacli from clientes order by razoncli")

            if query.exec():
                i = 55
                j = 655
                while query.next():
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

                    var.report.setFont('Helvetica', size=9)
                    var.report.drawCentredString(i + 15, j, str(query.value(0)))
                    var.report.drawString(i + 40, j, str(query.value(1)))
                    var.report.drawString(i + 115, j, str(query.value(2)))
                    var.report.drawString(i + 235, j, str(query.value(3)))
                    var.report.drawString(i + 320, j, str(query.value(4)))
                    var.report.drawString(i + 420, j, str(query.value(5)))
                    j = j - 25

            var.report.save()
            rootPath = '.\\informesClientes'
            for file in os.listdir(rootPath):
                if file.endswith(nombre):
                    os.startfile('%s\\%s' % (rootPath, file))
        except Exception as error:
            print('Error LISTADO CLIENTES :', error)

    @staticmethod
    def reportconductores():
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre = fecha + '_listadoconductores.pdf'
            var.report = canvas.Canvas('informesConductores/' + nombre)
            titulo = 'LISTADO CONDUCTORES'
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)

            items = ['CÓDIGO', 'APELLIDOS', 'NOMBRE', 'MÓVIL', 'LICENCIAS', 'FECHA BAJA']

            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(50, 675, str(items[0]))
            var.report.drawString(110, 675, str(items[1]))
            var.report.drawString(205, 675, str(items[2]))
            var.report.drawString(290, 675, str(items[3]))
            var.report.drawString(380, 675, str(items[4]))
            var.report.drawString(460, 675, str(items[5]))
            var.report.line(50, 670, 525, 670)

            query = QtSql.QSqlQuery()
            query.prepare("select codigo, apeldri, nombredri, movildri,"
                          " carnet, bajadri from drivers order by apeldri")

            if query.exec():
                i = 55
                j = 655
                while query.next():
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

                    var.report.setFont('Helvetica', size=9)
                    var.report.drawCentredString(i + 15, j, str(query.value(0)))
                    var.report.drawString(i + 50, j, str(query.value(1)))
                    var.report.drawString(i + 155, j, str(query.value(2)))
                    var.report.drawString(i + 235, j, str(query.value(3)))
                    var.report.drawString(i + 340, j, str(query.value(4)))
                    var.report.drawString(i + 420, j, str(query.value(5)))
                    j = j - 25

            var.report.save()
            rootPath = '.\\informesConductores'
            for file in os.listdir(rootPath):
                if file.endswith(nombre):
                    os.startfile('%s\\%s' % (rootPath, file))
        except Exception as error:
            print('Error LISTADO CONDUCTORES :', error)

    def topInforme(titulo):
        try:
            ruta_logo = '.\\img\\logo.ico'
            logo = Image.open(ruta_logo)

            # Asegúrate de que el objeto 'logo' sea de tipo 'PngImageFile'
            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 525, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'Transportes Teis')
                var.report.drawString(240, 695, titulo)
                var.report.line(50, 690, 525, 690)

                # Dibuja la imagen en el informe
                var.report.drawImage(ruta_logo, 480, 725, width=40, height=40)

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

    def footInforme(titulo):
        try:
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber()))

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)

    def elegirInforme(self):
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle("Imprimir Informes")
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
            mbox.setText("Que informe quieres imprimir?")
            mbox.setStandardButtons(
                QtWidgets.QMessageBox.StandardButton.Cancel | QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.button(QtWidgets.QMessageBox.StandardButton.Cancel).setText('Cancelar')
            mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Conductores')
            mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('Clientes')
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Cancel)
            mbox.setEscapeButton(QtWidgets.QMessageBox.StandardButton.Cancel)

            option = mbox.exec()

            if option == QtWidgets.QMessageBox.StandardButton.Yes:
                Informes.reportconductores()
            elif option == QtWidgets.QMessageBox.StandardButton.No:
                Informes.reportclientes()

        except Exception as error:
            print('Error al elegir Informe a imprimir: ', error)