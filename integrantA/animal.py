""" Clase de nom animal, amb un constructor definint 6 atributs d'un animal i un métode amb nom: salutació"""

class animal:
    def __init__(self, type, paws, name, age, color, size ):
        self.type = type
        self.paws = paws
        self.name = name
        self.age = age
        self.color = color
        self.size = size

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getPaws(self):
        return self.paws

    def setPaws(self, paws):
        self.paws = paws

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def salutacio(self):
        print("El tipus d'animal és: " + self.type)
        print("El número de potes: " + self.paws)
        print("El nom de l'animal és: " + self.name)
        print("L'edat de l'animal és: " + self.age)
        print("El color de l'animal és: " + self.color)
        print("La grandària de l'animal és: " + self.size)
