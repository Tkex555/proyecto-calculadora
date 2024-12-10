from Views.SumarViews import SumarView
from Models.Sumar import Sumar

class SumarController:
    def __init__(self):
        self.model = Sumar()
        self.view = SumarView()

    def realizar_suma(self):
        num1, num2 = self.view.obtener_numeros()
        resultado = self.model.calcular(num1, num2)
        self.view.mostrar_resultado(num1, num2, "+", resultado)
