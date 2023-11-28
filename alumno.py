
class alumno:
    def __init__(self,Nombre, Apellido,Edad, Nacionalidad):
        self.Nombre         = Nombre
        self.Apellido       = Apellido
        self.Edad           = Edad
        self.Nota           = None
        self.Nacionalidad   = Nacionalidad
    
    def setNota(self,Nota):
        self.Nota = Nota
    
    def leerNota(self):
        return self.Nota
    
    def registrarNota(self,notaAlumno):
        if 0<=notaAlumno<=20:
            self.Nota = notaAlumno
            return True
        else:
            return False
        