from Views.DividirViews import DividirView
from Models.Dividir import Dividir

class DividirController:
    def __init__(self):
        self.model = Dividir()
        self.view = DividirView()

    def realizar_division(self):
        num1, num2 = self.view.obtener_numeros()
        try:
            resultado = self.model.calcular(num1, num2)
            self.view.mostrar_resultado(num1, num2, "/", resultado)
        except ZeroDivisionError as e:
            self.view.mostrar_error(str(e))
