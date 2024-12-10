from Models.Operaciones import OperacionBase

class Sumar(OperacionBase):
    def calcular(self, num1, num2):
        resultado = num1 + num2
        self.guardar_operacion(num1, num2, "+", resultado)
        return resultado
