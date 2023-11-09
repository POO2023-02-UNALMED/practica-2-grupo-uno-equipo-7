class Persona:
    def __init__(self, nombre, cedula = 0):
        self._nombre = nombre
        self._cedula = cedula

    def setNombre(self,nombre):
        self._nombre = nombre
    
    def getNombre(self):
        return self._nombre
    
    def setCedula(self, id):
        self._cedula = id

    def getCedula(self):
        return self._cedula
    
    def __str__(self):
        return "Nombre" + self.getNombre() + "\nCedula:" + self.getCedula()