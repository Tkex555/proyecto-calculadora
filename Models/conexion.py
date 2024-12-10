import mysql.connector

class ConexionDB:
    def __init__(self):
        self.config = {
            "host": "localhost",
            "user": "root",
            "password": ""
        }
        self.db_name = "calculadora"
        self.conexion = mysql.connector.connect(**self.config)
        self.cursor = self.conexion.cursor()
        self._verificar_o_crear_db()

    def _verificar_o_crear_db(self):
        # Verificar y crear la base de datos si no existe
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_name}")
        self.conexion.database = self.db_name

        # Crear la tabla "historial" si no existe
        crear_tabla_historial = """
        CREATE TABLE IF NOT EXISTS historial (
            id INT AUTO_INCREMENT PRIMARY KEY,
            operacion VARCHAR(255) NOT NULL,
            resultado FLOAT NOT NULL
        )
        """
        self.cursor.execute(crear_tabla_historial)

        # Crear la tabla "operaciones" si no existe
        crear_tabla_operaciones = """
        CREATE TABLE IF NOT EXISTS operaciones (
            id INT AUTO_INCREMENT PRIMARY KEY,
            tipo_operacion VARCHAR(50) NOT NULL,
            numero1 FLOAT NOT NULL,
            numero2 FLOAT NOT NULL,
            resultado FLOAT NOT NULL
        )
        """
        self.cursor.execute(crear_tabla_operaciones)

    def obtener_conexion(self):
        return self.conexion
