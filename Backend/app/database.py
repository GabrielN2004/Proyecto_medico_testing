import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

class DatabaseConnection:
    _connection = None

    @classmethod
    def get_connection(cls):
        """Establece y reutiliza una conexión única a la base de datos."""
        try:
            if cls._connection is None or not cls._connection.is_connected():
                cls._connection = mysql.connector.connect(
                    host=os.getenv('DB_HOST'),
                    database=os.getenv('DB_NAME'),
                    user=os.getenv('DB_USER'),
                    password=os.getenv('DB_PASSWORD')
                )
            return cls._connection
        except Error as e:
            print(f"Error connecting to the database: {e}")
            return None

    @classmethod
    def execute_query(cls, query, params=None):
        """Ejecuta una consulta SQL y realiza un commit si es necesario."""
        connection = cls.get_connection()
        if connection:
            cursor = connection.cursor()
            try:
                print(f"Executing query: {query}")
                print(f"With params: {params}")
                cursor.execute(query, params)
                connection.commit()  # Commit solo si es necesario
            except Error as e:
                print(f"Error executing query in execute_query: {e}")
                connection.rollback()  # Revertir cambios si ocurre un error
            finally:
                cursor.close()
        else:
            print("Connection not available.")


    @classmethod
    def fetch_one(cls, query, params=None):
        """Obtiene un solo resultado de una consulta."""
        connection = cls.get_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query, params)
                return cursor.fetchone()
            except Error as e:
                print(f"Error fetching data in fetch_one: {e}")
                return None
            finally:
                cursor.close()
        return None

    @classmethod
    def fetch_all(cls, query, params=None):
        """Obtiene todos los resultados de una consulta."""
        connection = cls.get_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query, params)
                return cursor.fetchall()
            except Error as e:
                print(f"Error fetching data in fetch_all: {e}")
                return None
            finally:
                cursor.close()
        return None

    @classmethod
    def close_connection(cls):
        """Cierra la conexión a la base de datos si está abierta."""
        if cls._connection and cls._connection.is_connected():
            cls._connection.close()
            cls._connection = None
