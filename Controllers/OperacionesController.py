class ControladorOperacion:
    def __init__(self, modelo):
        self.modelo = modelo

    def consultar_historial(self):
        """Consulta y retorna el historial de operaciones."""
        return self.modelo.mostrar_operaciones()

    def validar_numero(self, entrada):
        """
        Valida que la entrada sea un número.
        Si no es válido, retorna False.
        """
        try:
            return float(entrada)
        except ValueError:
            print("Por favor, ingrese un número válido.")
            return None