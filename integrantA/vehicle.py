""" Clase vehicle que tindrà un constructor amb 6 atributs de un vehicle i com a nom de métode parts"""

class vehicle:
    def __init__(self, brand, matricula, price, km, color, size):
        self.brand = brand
        self.matricula = matricula
        self.price = price
        self.km = km
        self.color = color
        self.size = size

    def getBrand(self):
        return self.brand

    def setBrand(self, brand):
        self.brand = brand

    def getMatricula(self):
        return self.matricula

    def setMatricula(self,matricula):
        self.matricula = matricula

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getKm(self):
        return self.km

    def setKm(self, km):
        self.km =km

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def parts(self):
        print("La marca de cotxe és: " + self.brand)
        print("La matrícula del cotxe: " + self.matricula)
        print("El preu del cotxe és: " + self.price)
        print("Els quilometres recorreguts del cotxe son: " + self.km)
        print("El color del cotxe és: " + self.color)
        print("La grandària del cotxe és: " + self.size)
