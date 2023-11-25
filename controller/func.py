from passlib.hash import bcrypt
import bcrypt
from model.users import User
import requests
import random, string
import aiohttp
import asyncio

def is_valid_login(correo, contraseña):
    # print("User class is_valid_login----------------------", user)
    usuario = User.get_usuario(correo)
    print("usuario--------------------: ", usuario)
    # Verifica si la contraseña en texto plano coincide con la contraseña hasheada en la BD
    if usuario and bcrypt.checkpw(contraseña.encode('utf-8'), usuario['contraseña'].encode('utf-8')):
        return usuario
    return None

def hashear_contraseña(contraseña):
    # Generar un salt aleatorio y hashear la contraseña
    salt = bcrypt.gensalt()
    contraseña_hasheada = bcrypt.hashpw(contraseña.encode('utf-8'), salt)
    return contraseña_hasheada


def obtener_opciones_ciudades(departamento_id):
    try:
        url = f'https://api-colombia.com/api/v1/department/{departamento_id}/cities'
        response = requests.get(url)
        data = response.json()
        # Obtener nombres de ciudades
        return [ciudad['id'] for ciudad in data]
    except Exception as e:
        print(f"Error al obtener ciudades: {e}")
        return []
    
def obtener_opciones_departamentos():
    try:
        url = f'https://api-colombia.com/api/v1/department'
        response = requests.get(url)
        data = response.json()
        # Obtener nombres de departamentos
        return [departamento['id'] for departamento in data]
    except Exception as e:
        print(f"Error al obtener departamentos: {e}")
        return []
    
    
    
    
    # --------------------------------------------------------------------- #
    
async def obtener_ciudad(id_ciudad):
    try:
        url = f'https://api-colombia.com/api/v1/city/{id_ciudad}/'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                print("Obtiene ciudad")
                return data['name']
    except Exception as e:
        return None

async def obtener_departamento(departamento_id):
    try:
        url = f'https://api-colombia.com/api/v1/department/{departamento_id}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                print("Obtiene depto")
                return data['name']
    except Exception as e:
        return None
    
async def obtener_datos_asincronos(usuarios):
    tareas_ciudades = [obtener_ciudad(usuario['id_ciudad']) for usuario in usuarios]
    tareas_deptos = [obtener_departamento(usuario['id_departamento']) for usuario in usuarios]

    ciudades = await asyncio.gather(*tareas_ciudades)
    departamentos = await asyncio.gather(*tareas_deptos)

    return ciudades, departamentos
    
def generar_codigo_usuario():
    letras_aleatorias = random.choices(string.ascii_letters, k=3)
    numeros_aleatorios = random.choices(string.digits, k=3)
    codigo_usuario = ''.join(letras_aleatorias + numeros_aleatorios)
    
    return codigo_usuario
