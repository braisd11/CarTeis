import drivers
import eventos
from MainWindow import *
from CalendarWindow import *
from ExitWindow import *
from AboutWindow import *
import sys, var
from datetime import datetime


class About(QtWidgets.QDialog):
    def __init__(self):
        super(About, self).__init__()
        var.aboutWindow = Ui_dlgAbout()
        var.aboutWindow.setupUi(self)


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


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)  # Método encargado de generar la interfaz
        var.calendar = Calendar()
        var.exitWindow = Exit()
        var.aboutWindow = About()

        '''
        
            Zona de eventos de botones
        
        '''

        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)
        '''
            
            Zona de eventos del menubars
        
        '''

        var.ui.actionSalir.triggered.connect(eventos.Eventos.showSalir)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.acercade)

        '''
        
            Zona de eventos de las cajas de texto
        
        '''

        var.ui.txtDNI.editingFinished.connect(drivers.Drivers.validarDNI)


        '''
            
            Zona de eventos de la toolbar
        '''

        var.ui.actionbarSalir.triggered.connect(eventos.Eventos.confirmarSalir)
        var.ui.actionlimpiarPanel.triggered.connect(eventos.Eventos.limpiarPanel)


if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())



