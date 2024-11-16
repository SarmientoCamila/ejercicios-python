#a) En la clase Persona, agrega un método llamado saludar que imprime un mensaje como "Hola, mi nombre es [nombre]". b) Modifica el atributo edadusando un método, asegurándote de aplicar encapsulamiento (haz que el atributo sea privado).


class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.__edad = edad
        self.nacionalidad = nacionalidad

    def mostrar(self):
        print("Nombre: " , self.nombre)
        print("Edad: ", self.__edad)
        print("Nacionalidad: ", self.nacionalidad)

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}."
    
    def modificar_edad(self, nueva_edad):
            if nueva_edad >= 0:  
                self._edad = nueva_edad
            else:
                print("La edad no puede ser negativa.")

persona_1 = Persona("Giana", 21, "Italiana")
persona_2 = Persona("Mara",46, "Argentina")

print(persona_1.saludar())
persona_1.mostrar()
print()
print(persona_2.saludar())
persona_2.mostrar()
print()

persona_2.modificar_edad(50)
persona_2.mostrar()
