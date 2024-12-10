from Models.Operaciones import OperacionBase

class Dividir(OperacionBase):
    def calcular(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        resultado = num1 / num2
        self.guardar_operacion(num1, num2, "/", resultado)
        return resultado
