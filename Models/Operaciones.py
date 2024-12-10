from Models.conexion import ConexionDB

class OperacionBase:
    def __init__(self):
        conexion_db = ConexionDB()
        self.db = conexion_db.obtener_conexion()
        self.cursor = self.db.cursor()

    def guardar_operacion(self, num1, num2, operador, resultado):
        operacion = f"{num1} {operador} {num2}"
        query = "INSERT INTO historial (operacion, resultado) VALUES (%s, %s)"
        valores = (operacion, resultado)
        self.cursor.execute(query, valores)
        self.db.commit()
        print("Operación guardada en el historial.")

    def mostrar_operaciones(self):
        query = "SELECT * FROM historial"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        
        if resultados:
            print("Historial de operaciones:")
            for operacion in resultados:
                print(f"{operacion[1]} = {operacion[2]}")
        else:
            print("No hay operaciones registradas en el historial.")
