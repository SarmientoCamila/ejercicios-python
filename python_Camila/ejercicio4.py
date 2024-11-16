#Crea una clase Estudiante que herede de la clase Persona. Agregue un atributo adicional matricula y un método mostrar_datos que muestre la información completa del estudiante (incluyendo nombre, edad y matrícula).
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.__edad = edad  # Atributo privado
        self.nacionalidad = nacionalidad

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.__edad)
        print("Nacionalidad:", self.nacionalidad)

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}."
    
    def modificar_edad(self, nueva_edad):
        if nueva_edad >= 0:  
            self.__edad = nueva_edad  
        else:
            print("La edad no puede ser negativa.")

class Estudiante(Persona):  # Herencia de Persona
    def __init__(self, nombre, edad, nacionalidad, matricula):
        super().__init__(nombre, edad, nacionalidad)  
        self.matricula = matricula

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self._Persona__edad) # Acceso al atributo privado de la clase padre
        print("Nacionalidad:", self.nacionalidad)
        print("Matrícula:", self.matricula)


estudiante_1 = Estudiante("Giana", 21, "Italiana", "3536437")
estudiante_2 = Estudiante("Mara", 46, "Argentina", "6516374")

estudiante_1.mostrar_datos()
print()
estudiante_2.mostrar_datos()
