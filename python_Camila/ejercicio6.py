#a) Explica cómo se maneja una excepción en Python. ¿Cuál es la estructura de try-except?
#b) Escribe un código que pida al usuario un número, y si no se introduce un número válido, maneje la excepción mostrando un mensaje de error.

try:
    numero = int(input("Ingrese un número: "))
except ValueError:
    print("Error: No se ingresó un número válido.")
else:
    print("El número ingresado es:", numero)
finally:
    print("Fin del programa.")

