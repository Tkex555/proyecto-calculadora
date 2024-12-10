from Views.RestarViews import RestarView
from Models.Restar import Restar

class RestarController:
    def __init__(self):
        self.model = Restar()
        self.view = RestarView()

    def realizar_resta(self):
        num1, num2 = self.view.obtener_numeros()
        resultado = self.model.calcular(num1, num2)
        self.view.mostrar_resultado(num1, num2, "-", resultado)
