import drivers
import eventos
from CalendarWindow import *
from ExitWindow import *
from AboutWindow import *
import sys,var
from datetime import datetime


class About(QtWidgets.QDialog):
    def __init__(self):
        super(About, self).__init__()
        var.aboutWindow = Ui_dlgAbout()
        var.aboutWindow.setupUi(self)

        var.aboutWindow.lblVersion.setText(f"Versión: {var.version}")


class Calendar(QtWidgets.QDialog):

    def __init__(self):
        super(Calendar, self).__init__()
        var.calendar = Ui_dlgCalendar()
        var.calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        var.calendar.Calendar.setSelectedDate((QtCore.QDate(ano, mes, dia)))
        var.calendar.Calendar.clicked.connect(drivers.Drivers.cargarFecha)


class Exit(QtWidgets.QDialog):

    def __init__(self):
        super(Exit, self).__init__()
        var.exitWindow = Ui_dlgSalir()
        var.exitWindow.setupUi(self)

        '''
            Zona de Eventos de botones de dlgSalir
        '''

        var.exitWindow.btnSalirSi.clicked.connect(eventos.Eventos.confirmarSalir)
        var.exitWindow.btnSalirNo.clicked.connect(eventos.Eventos.cancelarSalir)


class FileDialogAbrir(QtWidgets.QFileDialog):

    def __init__(self):
        super(FileDialogAbrir, self).__init__()
