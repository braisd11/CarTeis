import drivers
import eventos
from windowaux import *
from MainWindow import *
from AboutWindow import *
import sys, var


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

        var.ui.actionbarSalir.triggered.connect(eventos.Eventos.showSalir)
        var.ui.actionlimpiarPanel.triggered.connect(eventos.Eventos.limpiarPanel)

        '''
            
            Zona de eventos de StatusBar
        '''
        var.ui.statusbar.showMessage(f"{datetime.today()} || version: {var.version}")

    def closeEvent(self, event):
        #event.ignore()
        #eventos.Eventos.showSalir(self)

        mbox = QtWidgets.QMessageBox.information(self, 'Salir', '¿Estás seguro de que quieres salir?',
                                                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if mbox == QtWidgets.QMessageBox.StandardButton.Yes:
            app.quit()
        else:
            event.ignore()


if __name__ == '__main__':
    var.version = "0.1.1"
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())



