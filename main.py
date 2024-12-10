from Controllers.SumarController import SumarController
from Controllers.RestarController import RestarController
from Controllers.MultiplicarController import MultiplicarController
from Controllers.DividirController import DividirController
from Controllers.OperacionesController import ControladorOperacion 
from Views.OperacionesViews import VistaOperacion  
from Models.Operaciones import OperacionBase  

def main():
    modelo = OperacionBase()  
    controlador_historial = ControladorOperacion(modelo) 
    vista_historial = VistaOperacion(controlador_historial)  

    while True:
        print("\nElige una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Consultar Historial") 
        print("0. Salir")

        opcion = input("Opción: ")
        if opcion == "1":
            controller = SumarController()
            controller.realizar_suma()
        elif opcion == "2":
            controller = RestarController()
            controller.realizar_resta()
        elif opcion == "3":
            controller = MultiplicarController()
            controller.realizar_multiplicacion()
        elif opcion == "4":
            controller = DividirController()
            controller.realizar_division()
        elif opcion == "5":
            vista_historial.mostrar_menu()  
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
