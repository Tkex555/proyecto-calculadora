class VistaOperacion:
    def __init__(self, controlador):
        self.controlador = controlador

    def mostrar_menu(self):
        """Muestra el menú principal para la consulta de historial."""
        while True:
            print("\n--- Menú de Operaciones ---")
            print("1. Consultar historial")
            print("2. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.consultar_historial()
            elif opcion == "2":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def consultar_historial(self):
        """Muestra el historial de operaciones en la consola."""
        print("\n--- Historial de Operaciones ---")
        operaciones = self.controlador.consultar_historial()
        if operaciones:
            for operacion in operaciones:
                print(operacion)
        else:
            print("Ya no hay mas operaciones.")
