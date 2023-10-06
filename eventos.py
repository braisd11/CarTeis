import var, sys

class Eventos():

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
