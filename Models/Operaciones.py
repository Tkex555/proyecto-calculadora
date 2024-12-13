from Models.conexion import ConexionDB

class OperacionBase:
    def __init__(self):
        conexion_db = ConexionDB()
        self.db = conexion_db.obtener_conexion()
        self.cursor = self.db.cursor()

    def guardar_operacion(self, num1, num2, operador, resultado):
        operacion = f"{num1} {operador} {num2}"
        query = "INSERT INTO historial (operacion, resultado) VALUES (%s, %s)" #envia la operacion a la base de datos
        valores = (operacion, resultado)
        self.cursor.execute(query, valores) #guarda en la tabla historial
        self.db.commit()
        print("Operación guardada en el historial.")
    
        query = "INSERT INTO operaciones (tipo_operacion, numero1, numero2, resultado) VALUES (%s, %s, %s, %s)" #envia la operacion a la base de datos
        valores = ( operador, num1, num2, resultado)
        self.cursor.execute(query, valores)
        self.db.commit() #guarda en la tabla operaciones
        print("Operación guardada en las operaciones.")

    def mostrar_operaciones(self):
        self.db.reconnect()  #se reconecta a la base de datos 
        self.cursor = self.db.cursor()  #Se crea un nuevo cursor
        query = "SELECT * FROM historial"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall() 
        
        if resultados:
            print("Historial de operaciones:")
            for operacion in resultados:
                print(f"{operacion[1]} = {operacion[2]}") #recibe las operaciones y los resultados de la base de datos de calculadora y muestra todas las realizadas
        else:
            print("No hay operaciones registradas en el historial.")
