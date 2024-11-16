#Escribe un programa que use una expresión regular para verificar si una cadena es un correo electrónico válido.

import re

def es_correo_electronico_valido(correo):
    # Expresión regular para validar un correo electrónico
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Verifica si la cadena coincide con el patrón
    return re.match(patron, correo) is not None

# Ejemplos de uso
correos_a_verificar = [
    "ejemplo@dominio.com",
    "usuario@sub.dominio.com",
    "usuario@dominio.co.uk",
    "usuario@.com",        # Inválido
    "usuario@dominio",     # Inválido
    "usuario@dominio.c",   # Inválido
    "usuario@dominio..com" # Inválido
]

for correo in correos_a_verificar:
    if es_correo_electronico_valido(correo):
        print(f"{correo} es un correo electrónico válido.")
    else:
        print(f"{correo} no es un correo electrónico válido.")
