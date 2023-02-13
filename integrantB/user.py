"""Crear un arxiu de nom user.py. En aquest arxiu s’ha de crear una class de nom user. Con 6 atributos"""
class user:
    def __int__(self, nombre, apellidos, usuario, contrasenya, anyoNacimiento, correo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.usuario = usuario
        self.contrasenya = contrasenya
        self.anyoNacimiento = anyoNacimiento
        self.correo = correo

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getApellidos(self):
        return self.apellidos
    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def getUsuario(self):
        return self.usuario
    def setUsuario(self, usuario):
        self.usuario = usuario

    def getContrasenya(self):
        return self.contrasenya
    def setContrasenya(self, contrasenya):
        self.contrasenya = contrasenya

    def getAnyoNacimiento(self):
        return self.anyoNacimiento
    def setAnyoNacimiento(self, anyoNacimiento):
        self.anyoNacimiento = anyoNacimiento

    def getCorreo(self):
        return self.correo
    def setCorreo(self, correo):
        self.correo = correo

    def salutacio(self):
        print("Nombre: "+ self.nombre)
        print("Apellidos: " + self.apellidos)
        print("Usauario: " + self.usuario)
        print("Contraseña: " + self.contrasenya)
        print("Año de Nacimiento: " + self.anyoNacimiento)
        print("Correo: " + self.correo)