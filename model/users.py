from model.connection import Conexion
from flask import flash

class User:
    def __init__(self, codigo, nombres, apellidos, direccion, telefono, id_departamento, id_ciudad, nombre_usuario, correo, contraseña, rol):
        self.codigo = codigo
        self.nombre_usuario = nombre_usuario
        self.correo = correo
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.id_departamento = id_departamento
        self.id_ciudad = id_ciudad
        self.contraseña = contraseña
        self.rol = rol
        
    def get_all_usuarios():
        conexion = Conexion.connection_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM `usuarios`")
        lista_usuarios = cursor.fetchall()
        conexion.commit()
        return lista_usuarios

    def get_usuario(correo):
        # print("---------DATOS----------")
        # print(correo)
    
        try:
            conexion_db = Conexion.connection_bd()
            cursor = conexion_db.cursor(dictionary=True)
            sql = "SELECT * FROM usuarios WHERE correo=%s"
            valores = (correo,)
            cursor.execute(sql, valores)
            account = cursor.fetchone()
            
            # print("Cuenta bd---------------------------------", account)
    
        except Exception as error:
            print("Error al ejecutar la consulta:", error)
            conexion_db.rollback()
        finally:
            cursor.close()
            conexion_db.close()
    
        return account


    def registrar_usuario(usuario):
        
        print("Cod -------------", usuario.codigo)
        
        conexion_db = Conexion.connection_bd()
        cursor = conexion_db.cursor(dictionary=True)
    
        try:
            # Verificar si el nombre de usuario o el correo ya están en uso
            sql = "SELECT * FROM usuarios WHERE nombre_usuario = %s OR correo = %s"
            cursor.execute(sql, (usuario.nombre_usuario, usuario.correo))
            usuario_existente = cursor.fetchone()
    
            if usuario_existente:
                if usuario_existente['nombre_usuario'] == usuario.nombre_usuario:
                    flash('El nombre de usuario ingresado ya se encuentra en uso', 'error')
                elif usuario_existente['correo'] == usuario.correo:
                    flash('El correo ingresado ya se encuentra en uso', 'error')
                return False
            else:
                # Insertar el nuevo usuario en la base de datos
                sql = "INSERT INTO usuarios (codigo, nombres, apellidos, direccion, id_departamento, id_ciudad, correo, telefono, contraseña, nombre_usuario, rol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                valores = (
                    usuario.codigo,
                    usuario.nombres,
                    usuario.apellidos,
                    usuario.direccion,
                    usuario.id_departamento,
                    usuario.id_ciudad,
                    usuario.correo,
                    usuario.telefono,
                    usuario.contraseña,
                    usuario.nombre_usuario,
                    usuario.rol
                )  
                cursor.execute(sql, valores)
                conexion_db.commit()
                return True
            
        except Exception as error:
            print("Error al registrar el usuario:", error)
            flash('Error al registrar el usuario', 'error')
            conexion_db.rollback()
            return False
        finally:
            cursor.close()
            conexion_db.close()