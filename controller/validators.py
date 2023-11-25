import re

def is_valid_email(email):
    # Utiliza una expresión regular para validar el formato del correo electrónico
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    return re.match(pattern, email)