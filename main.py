import eventos
from MainWindow import *
from CalendarWindow import *
import sys, var
from datetime import datetime


class Calendar(QtWidgets.QDialog):

    def __init__(self):
        super(Calendar, self).__init__()
        var.calendar = Ui_dlgCalendar()
        var.calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)  # Método encargado de generar la interfaz
        var.calendar = Calendar()

        '''
        
            Zona de eventos de botones
        
        '''

        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)

        '''
            
            Zona de eventos del menubars
        
        '''

        var.ui.actionSalir.triggered.connect(eventos.Eventos.salir)


if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())



