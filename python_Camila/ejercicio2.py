# a) Defina una clase Persona que tenga como atributos nombre, edad y nacionalidad. b) Crea dos objetos de la clase Personacon diferentes valores y llama a los atributos correspondientes.
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def mostrar(self):
        print("Nombre: " , self.nombre)
        print("Edad: ", self.edad)
        print("Nacionalidad: ", self.nacionalidad)

persona_1 = Persona("Giana", 21, "Italiana")
persona_2 = Persona("Mara",46, "Argentina")

persona_1.mostrar()
persona_2.mostrar()