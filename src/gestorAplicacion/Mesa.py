
class Mesa:
    listaMesas = []

    def __init__(self, numMesa: str, tipoMesa: str, ubicacion: str):
        self.numMesa = numMesa
        self.tipoMesa = tipoMesa
        self.ubicacion = ubicacion
        Mesa.listaMesas.append(self)

    def getTipoMesa(self) -> str:
        return self.tipoMesa

    def setTipoMesa(self, tipoMesa: str):
        self.tipoMesa = tipoMesa

    def getUbicacion(self) -> str:
        return self.ubicacion

    def setUbicacion(self, ubicacion: str):
        self.ubicacion = ubicacion

    @staticmethod
    def getCliente():
        return Mesa.cliente

    def setCliente(self, cliente):
        Mesa.cliente = cliente

    def getNumMesa(self) -> str:
        return self.numMesa

    def setNumMesa(self, numMesa: str):
        self.numMesa = numMesa

    @staticmethod
    def mesasDisponibles(mesaDeseada: str):
        mesasQuePueden = []

        for mesa in Mesa.listaMesas:
            if mesa.getTipoMesa() == mesaDeseada:
                mesasQuePueden.append(mesa)

        return mesasQuePueden

