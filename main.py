import locale
import sys
import var

import conexion
from AboutWindow import *
from MainWindow import *
from windowaux import *

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)  # Método encargado de generar la interfaz
        var.calendar = Calendar()
        var.exitWindow = Exit()
        var.aboutWindow = About()
        var.dlgModificarBajaWindow = Baja()
        var.dlgCalendarbaja = CalendarBaja()
        var.dlgabrir = FileDialogAbrir()
        conexion.Conexion.conexion()
        conexion.Conexion.cargaprov()

        '''
        
            Zona de eventos de botones
        
        '''

        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)
        var.ui.btnAltaDriver.clicked.connect(drivers.Drivers.altaDriver)
        var.ui.cmbProv.currentIndexChanged.connect(conexion.Conexion.selMuni)
        var.ui.btnBuscar.clicked.connect(drivers.Drivers.buscadriver)
        var.ui.btnModifDriver.clicked.connect(drivers.Drivers.modifDri)
        var.ui.btnBajaDriver.clicked.connect(drivers.Drivers.borrarDriv)

        '''
            
            Zona de eventos del menubars
        
        '''

        var.ui.actionSalir.triggered.connect(eventos.Eventos.showSalir)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.acercade)
        var.ui.actionCrear_Copia_de_Seguridad.triggered.connect(eventos.Eventos.crearbackup)
        var.ui.actionRestaurar_Copia_Seguridad.triggered.connect(eventos.Eventos.restaurarbackup)
        var.ui.actionExportar_Datos_Excel.triggered.connect(eventos.Eventos.exportardatosxls)

        '''
        
            Zona de eventos de las cajas de texto
        
        '''
        var.ui.txtDNI.editingFinished.connect(eventos.Eventos.letraCapital)
        var.ui.txtApel.editingFinished.connect(eventos.Eventos.letraCapital)
        var.ui.txtNombre.editingFinished.connect(eventos.Eventos.letraCapital)
        var.ui.txtSalario.editingFinished.connect(eventos.Eventos.compruebaFormatoSalario)
        var.ui.txtMovilDriver.editingFinished.connect(eventos.Eventos.compruebaMovil)

        '''
            
            Zona de eventos de la toolbar
        '''

        var.ui.actionSalir.triggered.connect(eventos.Eventos.showSalir)
        var.ui.actionlimpiarPanel.triggered.connect(drivers.Drivers.limpiarPanel)

        '''
            Zona de ejecución de accionas al iniciar programa
        '''
        conexion.Conexion.mostrardrivers()
        eventos.Eventos.cargastatusbar(self)
        var.ui.btnGroupEstado.buttonClicked.connect(drivers.Drivers.selEstado)

        '''
        
            Eventos de Tablas
        '''
        eventos.Eventos.resizeTabdrivers()
        var.ui.tabDrivers.clicked.connect(drivers.Drivers.cargardrivers)

    def closeEvent(self, event):
        # event.ignore()
        # eventos.Eventos.showSalir(self)

        mbox = QtWidgets.QMessageBox.information(self, 'Salir', '¿Estás seguro de que quieres salir?',
                                                 QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if mbox == QtWidgets.QMessageBox.StandardButton.Yes:
            app.quit()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
