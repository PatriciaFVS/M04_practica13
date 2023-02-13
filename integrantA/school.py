""" Clase school que tindrà un constructor amb 6 atributs d'una escola i com a nom de métode: info"""
class school:
    def __init__(self, numalumn, numprofs, cursos, numpatis, preumatri, extraescolars):
        self.numalumn = numalumn
        self.numprofs = numprofs
        self.cursos = cursos
        self.numpatis = numpatis
        self.preumatri = preumatri
        self.extraescolars = extraescolars

    def getNumalumn(self):
        return self.numalumn

    def setNumalumn(self, numalumn):
        self.numalumn = numalumn

    def getNumprofs(self):
        return self.numprofs

    def setNumprofs(self,numprofs):
        self.numprofs = numprofs

    def getCursos(self):
        return self.cursos

    def setCursos(self, cursos):
        self.cursos = cursos

    def getNumpatis(self):
        return self.numpatis

    def setNumpatis(self, numpatis):
        self.numpatis = numpatis

    def getPreumatri(self):
        return self.preumatri

    def setPreumatri(self, preumatri):
        self.preumatri = preumatri

    def getExtraescolars(self):
        return self.extraescolars

    def setExtraescolars(self, extraescolars):
        self.extraescolars = extraescolars

    def info(self):
        print("El número de alumnes al centre és: " + self.numalumn)
        print("El número de professors al centre és: " + self.numprofs)
        print("El número de cursos al centre son: " + self.cursos)
        print("El centre disposa de : " + self.numpatis + " patis")
        print("El preu de la matrícula és: " + self.preumatri)
        print("El centre : " + self.extraescolars + "disposa de extraescolars")
