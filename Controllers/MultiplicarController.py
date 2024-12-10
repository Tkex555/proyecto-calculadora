from Views.MultiplicarViews import MultiplicarView
from Models.Multiplicar import Multiplicar

class MultiplicarController:
    def __init__(self):
        self.model = Multiplicar()
        self.view = MultiplicarView()

    def realizar_multiplicacion(self):
        num1, num2 = self.view.obtener_numeros()
        resultado = self.model.calcular(num1, num2)
        self.view.mostrar_resultado(num1, num2, "*", resultado)
