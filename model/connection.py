import mysql.connector
from flask import flash

class Conexion:
    
    def __init__(self):
        self.mi_conexion = self.connection_bd()

    def connection_bd():
        mi_conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            db='abbystore'
        )
        if mi_conexion:
            print("Conexion exitosa")
        else:
            print("Error en la conexion")
        return mi_conexion

