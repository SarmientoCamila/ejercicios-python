#Define una clase Animal que tenga los atributos especie y edad.
#Crea un objeto perro y un objeto gato de la clase Animal con valores diferentes para sus atributos.

class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def mostrar(self):
        print(f"El animal es de la especie {self.especie} y tiene {self.edad} años.")
        return self.especie, self.edad


perro = Animal("perro", 8)
gato = Animal("gato", 2)


print(perro.mostrar())
print(gato.mostrar())
