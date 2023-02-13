"""Crear un arxiu de nom university.py. En aquest arxiu s’ha de crear una class de nom university. Con 6 atributos"""
class university:
    def __int__(self, nombre, direccion, telefono, alumnos, correo, director):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.alumnos = alumnos
        self.correo = correo
        self.director = director

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getDireccion(self):
        return self.direccion
    def setDireccion(self, direccion):
        self.direccion = direccion

    def getTelefono(self):
        return self.telefono
    def setTelefono(self, telefono):
        self.telefono = telefono

    def getAlumnos(self):
        return self.alumnos
    def setAlumnos(self, alumnos):
        self.alumnos = alumnos

    def getCorreo(self):
        return self.correo
    def setCorreo(self, correo):
        self.correo = correo

    def getDirector(self):
        return self.director
    def setDirector(self, director):
        self.director = director

    def info(self):
        print("Nombre: "+ self.nombre)
        print("Dirección Postal: " + self.direccion)
        print("Télefono: " + self.telefono)
        print("Alumnos Matriculados: " + self.alumnos)
        print("Correo electrónico: " + self.correo)
        print("Director de la univaersidad: " + self.director)
