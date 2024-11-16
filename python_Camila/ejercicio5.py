#Ejemplo de polimorfismo

class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito en las clases derivadas")

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

# Función que usa el polimorfismo
def hacer_sonido_animal(animal):
    print(animal.hacer_sonido())

mi_perro = Perro()
mi_gato = Gato()


hacer_sonido_animal(mi_perro) 
hacer_sonido_animal(mi_gato)    
