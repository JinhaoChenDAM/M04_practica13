# Classe animal
class animal:
    # Constructor de classe animal
    def __init__(self, animal, color, nLegs, nEyes, height, age):
        self.animal = animal
        self.color = color
        self.nLegs = nLegs
        self.nEyes = nEyes
        self.height = height
        self.age = age

    # Getters y Setters
    def getAnimal(self):
        return self.animal

    def setAnimal(self, animal):
        self.animal = animal

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getNLegs(self):
        return self.nLegs

    def setNLegs(self, nLegs):
        self.nLegs = nLegs

    def getNEyes(self):
        return self.NEyes

    def setNEyes(self, NEyes):
        self.NEyes = NEyes

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    # Imprime todos los attributos por la pantalla
    def salutacio(self):
        print(
            "animal {animal} es de color {color}, tiene {nLegs} patas y {nEyes} ojos, mide {height}cm de altura y tiene {age} años"
            .format(animal=self.animal, color=self.color, nLegs=self.nLegs, nEyes=self.nEyes, height=self.height,
                    age=self.age))
