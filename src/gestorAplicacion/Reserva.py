class Reserva:
    clientes = []
    listaReservas = []

    def __init__(self, cliente, miSede=None, miMesa=None, fecha=None):
        self.cliente = cliente
        self.miSede = miSede
        self.miMesa = miMesa
        self.fecha = fecha
        Reserva.listaReservas.append(self)

    def getCliente(self):
        return self.cliente

    def setCliente(self, cliente):
        self.cliente = cliente

    def getMiSede(self):
        return self.miSede

    def setMiSede(self, miSede):
        self.miSede = miSede

    def getMiMesa(self):
        return self.miMesa

    def setMiMesa(self, miMesa):
        self.miMesa = miMesa

    def getFecha(self):
        return self.fecha

    def setFecha(self, fecha):
        self.fecha = fecha

    def __str__(self):
        return f"El cliente {self.getCliente().getId()} tiene su reservación para la fecha {self.getFecha()} en la {self.getMiSede()} y, escogió la mesa {self.getMiMesa().getTipoMesa()}"
    
    @classmethod
    def getLista(cls):
        return cls.listaReservas