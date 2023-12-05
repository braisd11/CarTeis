import locale
import sys

import clientes
import eventos
import var
import templates.rc_icons
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
        conexion.Conexion.cargaprovcli()

        '''
        
            Zona de eventos de botones
        
        '''

        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)
        var.ui.btnAltaDriver.clicked.connect(drivers.Drivers.altaDriver)
        var.ui.btnAltacli.clicked.connect(clientes.Clientes.altacli)
        var.ui.cmbProv.currentIndexChanged.connect(conexion.Conexion.selMuni)
        var.ui.cmbProvcli.currentIndexChanged.connect(conexion.Conexion.selMunicli)
        var.ui.btnBuscar.clicked.connect(drivers.Drivers.buscadriver)
        var.ui.btnModifDriver.clicked.connect(drivers.Drivers.modifDri)
        var.ui.btnModifcli.clicked.connect(clientes.Clientes.modifcli)
        var.ui.btnBajaDriver.clicked.connect(drivers.Drivers.borrarDriv)
        var.ui.btnBajacli.clicked.connect(clientes.Clientes.borrarcli)

        '''
            
            Zona de eventos del menubars
        
        '''

        var.ui.actionSalir.triggered.connect(eventos.Eventos.showSalir)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.acercade)
        var.ui.actionCrear_Copia_de_Seguridad.triggered.connect(eventos.Eventos.crearbackup)
        var.ui.actionRestaurar_Copia_Seguridad.triggered.connect(eventos.Eventos.restaurarbackup)
        var.ui.actionExportar_Drivers.triggered.connect(eventos.Eventos.exportardatosxlsdriv)
        var.ui.actionExportar_Clientes.triggered.connect(eventos.Eventos.exportardatosxlscli)
        var.ui.actionImportar_Drivers.triggered.connect(eventos.Eventos.importardatosxlsdriv)
        var.ui.actionImportar_Clientes.triggered.connect(eventos.Eventos.importardatosxlscli)

        '''
        
            Zona de eventos de las cajas de texto
        
        '''
        var.ui.txtDNI.editingFinished.connect(eventos.Eventos.letraCapital)
        var.ui.txtDNIcli.editingFinished.connect(eventos.Eventos.letraCapital)
        var.ui.txtApel.editingFinished.connect(eventos.Eventos.letraCapital)
        var.ui.txtNombre.editingFinished.connect(eventos.Eventos.letraCapital)
        var.ui.txtNombrecli.editingFinished.connect(eventos.Eventos.letraCapital)
        var.ui.txtSalario.editingFinished.connect(eventos.Eventos.compruebaFormatoSalario)
        var.ui.txtMovilDriver.editingFinished.connect(eventos.Eventos.compruebaMovil)
        var.ui.txtMovilcli.editingFinished.connect(eventos.Eventos.compruebaMovilcli)

        '''
            
            Zona de eventos de la toolbar
        '''

        var.ui.actionSalir.triggered.connect(eventos.Eventos.showSalir)
        var.ui.actionlimpiarPanel.triggered.connect(drivers.Drivers.limpiarPanel)
        var.ui.actionlimpiarPanel.triggered.connect(clientes.Clientes.limpiarPanel)

        '''
            Zona de ejecución de accionas al iniciar programa
        '''
        conexion.Conexion.mostrardrivers()
        conexion.Conexion.mostrarclientes()
        eventos.Eventos.cargastatusbar(self)
        var.ui.btnGroupEstado.buttonClicked.connect(drivers.Drivers.selEstado)
        var.ui.chkTodoscli.clicked.connect(clientes.Clientes.selEstadocli)

        '''
        
            Eventos de Tablas
        '''
        eventos.Eventos.resizeTabdrivers()
        eventos.Eventos.resizeTabclientes()
        var.ui.tabDrivers.clicked.connect(drivers.Drivers.cargardrivers)
        var.ui.tabClientes.clicked.connect(clientes.Clientes.cargarclientes)

    def closeEvent(self, event):
        # event.ignore()
        # eventos.Eventos.showSalir(self)

        btnSi = QtWidgets.QMessageBox.StandardButton.Yes

        btnNo = QtWidgets.QMessageBox.StandardButton.No

        mbox = QtWidgets.QMessageBox.information(self, 'Salir', '¿Estás seguro de que quieres salir?',
                                                 btnSi | btnNo)

        if mbox == QtWidgets.QMessageBox.StandardButton.Yes:
            app.quit()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
