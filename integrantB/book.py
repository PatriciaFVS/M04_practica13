""" Crear un arxiu de nom book.py. En aquest arxiu s’ha de crear una class de nom university.Con 6 atributos"""
class book:
    def __int__(self, nombre, autor, any, tapa, genero, idioma):
        self.nombre = nombre
        self.autor = autor
        self.any = any
        self.tapa = tapa
        self.genero = genero
        self.idioma = idioma

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getAutor(self):
        return self.autor
    def setAutor(self, autor):
        self.nombre = autor

    def getAny(self):
        return self.any
    def setAny(self, any):
        self.any = any

    def getTapa(self):
        return self.tapa
    def setTapa(self, tapa):
        self.tapa = tapa

    def getGenero(self):
        return self.genero
    def setGenero(self, genero):
        self.genero = genero

    def getIdioma(self):
        return self.idioma
    def setIdioma(self, idioma):
        self.idioma = idioma

    def info(self):
        print("Nombre: "+ self.nombre)
        print("Autor: " + self.autor)
        print("Año: " + self.any)
        print("Tapa: " + self.tapa)
        print("Genero: " + self.genero)
        print("Idioma: " + self.idioma)
