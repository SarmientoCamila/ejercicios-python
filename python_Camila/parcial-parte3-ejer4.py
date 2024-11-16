#Define una excepción personalizada EdadInvalidaError que se levante cuando una persona introduzca una edad negativa. Implementa el manejo de esta excepción en un programa.
class EdadInvalidaError(Exception):
    pass

class Persona:
    def __init__(self, nombre, edad):
        if edad < 0:
            raise EdadInvalidaError("La edad no puede ser negativa")
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")  