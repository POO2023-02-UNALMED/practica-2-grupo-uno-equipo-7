from gestorAplicacion import Persona

class Cliente(Persona):
    
    Clientes = []

    def __init__(self, nombre, cedula, direccion, telefono, correo, fecha):
        super._nombre = nombre
        super._cedula = cedula
        self._direccion = direccion
        self._telefono = telefono
        self._email = correo
        self._fechaRegistro = fecha
        Cliente.Clientes.append(self)

    def setDireccion(self, direccion):
        self._direccion = direccion

    def getDireccion(self):
        return self._direccion
    
    def setTelefono(self, telefono):
        self._telefono = telefono
    
    def getTelefono(self):
        return self._telefono
    
    def setEmail(self, correo):
        self._email = correo

    def getEmail(self):
        return self._email
    
    def getFechaRegistro(self):
        return self._fechaRegistro
    
    @classmethod
    def getClientes(cls):
        return cls.Clientes
    
    @classmethod
    def cantidadClientes(cls):
        countClientes = len(cls.Clientes)
        return countClientes
    
    @classmethod
    def buscarClienteXNombre(cls, nombre):
        clientes = cls.getClientes()

        for cliente in clientes:
            if cliente.getNombre() == nombre:
                return cliente