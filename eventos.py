import var, sys

class Eventos():

    def salir(self):
        try:

            sys.exit()

        except Exception as error:
            print("error en modulo eventos", error)


    def acercade(self):

        try:

            pass

        except Exception as error:

            print("error abrir ventana acerca de ", error)


    def abrirCalendar(self):

        try:

            var.calendar.show()

        except Exception as error:

            print("error en abrir calendar", error)
