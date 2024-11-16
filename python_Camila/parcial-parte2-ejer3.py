#escribe un código que implemente polimorfismo con una función que acepte objetos de diferentes clases (Estudiante y Profesor) y llame a un método común de cada clase.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
       

    def mostrar(self):
        print("Nombre: " , self.nombre)
        print("Edad: ", self.edad)
        print("")

class Estudiante:
    def __init__(self, nombre, edad, matricula):
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Matricula: {self.matricula}")


class Profesor:
    def __init__(self, nombre, edad, materia):
        self.nombre = nombre
        self.edad = edad
        self.materia = materia

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Materia: {self.materia}")


def mostrar_datos(persona):
    persona.mostrar()


estudiante = Estudiante("Camila", 30, "1254899")
profesor = Profesor("Inés", 35, "Python")

mostrar_datos(estudiante)
mostrar_datos(profesor)
