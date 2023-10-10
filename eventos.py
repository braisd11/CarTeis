import var, sys

class Eventos():

    def limpiarPanel(self):
        try:
            listaWidgets = [var.ui.txtDNI, var.ui.txtDataDriver, var.ui.txtApel, var.ui.txtNombre, var.ui.txtDirDriver, var.ui.txtMovilDriver, var.ui.txtSalario, var.ui.lblValidarDNI]
            for i in listaWidgets:
                i.clear()
        except Exception as error:
            print("error al limpiar panel", error)

    def showSalir(self):
        try:

            var.exitWindow.show()

        except Exception as error:
            print("error en modulo eventos", error)

    def confirmarSalir(self):
        try:

            sys.exit()

        except Exception as error:
            print("error en modulo eventos", error)

    def cancelarSalir(self):
        try:

            var.exitWindow.hide()

        except Exception as error:
            print("error en modulo eventos", error)

    def acercade(self):

        try:

            var.aboutWindow.show()

        except Exception as error:

            print("error abrir ventana acerca de ", error)

    def abrirCalendar(self):

        try:

            var.calendar.show()

        except Exception as error:

            print("error en abrir calendar", error)
