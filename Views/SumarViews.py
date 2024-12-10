class SumarView:
    def obtener_numeros(self):
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("Error: Por favor, ingrese números válidos.")
            return self.obtener_numeros()

    def mostrar_resultado(self, num1, num2, operador, resultado):
        print(f"El resultado de {num1} {operador} {num2} es: {resultado}")
