
class Persona:
    def __init__(self, nombre=None, id=0):
        self.nombre = nombre
        self.id = id
    
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
    
    def __str__(self):
        return "Nombre: " + self.nombre
    
    @staticmethod
    def init_personas():
        persona1 = Persona("Persona 1", 1)
        persona2 = Persona("Persona 2", 2)
        persona3 = Persona("Persona 3", 3)
        persona4 = Persona("Persona 4", 4)
        persona5 = Persona("Persona 5", 5)
        persona6 = Persona("Persona 6", 6)
        persona7 = Persona("Persona 7", 7)
        persona8 = Persona("Persona 8", 8)
        persona9 = Persona("Persona 9", 9)
        persona10 = Persona("Persona 10", 10)
        persona11 = Persona("Persona 11", 11)
        persona12 = Persona("Persona 12", 12)
        persona13 = Persona("Persona 13", 13)
        persona14 = Persona("Persona 14", 14)
        persona15 = Persona("Persona 15", 15)
