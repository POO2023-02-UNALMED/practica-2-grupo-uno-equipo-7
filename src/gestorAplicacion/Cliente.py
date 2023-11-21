import pickle
from typing import List
from datetime import date
from .Persona import Persona
from .Mesa import Mesa
from .Factura import Factura
from .Plato import Plato
from .Item import Item

class Cliente(Persona):
    clientes = []
    contadorClientes = 0
    # create 3 clients
    
    def __init__(self, nombre: str, id: str):
        super().__init__(nombre, id)   
        Cliente.clientes.append(self) 
    

    def __init__(self, nombre: str, cel: str, direccion: str = None, telefono: str = None, email: str = None, fechaRegistro: str = None):
        super().__init__(nombre, cel)
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fechaRegistro = fechaRegistro
        self.codigoCliente = Cliente.contadorClientes + 1
        Cliente.contadorClientes += 1
        Cliente.clientes.append(self)

    def getEmail(self):
        return self.email
    
    def setEmail(self, correo):
        self.email = correo
    
    def getTelefono(self):
        return self.telefono
    
    def setTelefono(self, tel):
        self.telefono = tel
        


    @staticmethod
    def buscarCliente(codigoCliente: int) -> 'Cliente':
        for cliente in Cliente.clientes:
            if cliente.codigoCliente == codigoCliente:
                return cliente
        return None

    @staticmethod
    def buscarClienteXNombre(nombre: str) -> 'Cliente':
        for cliente in Cliente.clientes:
            if cliente.nombre == nombre:
                return cliente
        return None

    @staticmethod
    def buscarPlatoPreferido(codigoCliente: int) -> List[Plato]:
        platoPreferido = []
        facturas = Factura.buscarFacturasPorCliente(codigoCliente)
        print(facturas)
        if len(facturas) < 2:
            print("No hay suficientes facturas para determinar el plato preferido")
            return None
        platos = {}
        for factura in facturas:
            for plato in factura.getPlatos():
                if plato.nombre in platos:
                    platos[plato.nombre] = platos[plato.nombre] + 1
                else:
                    platos[plato.nombre] = 1
        print(platos)
        mayorValor = 0
        for clave in platos:
            valor = platos[clave]
            if valor > mayorValor:
                mayorValor = valor
        for clave in platos:
            if platos[clave] == mayorValor:
                platoPreferido.append(clave)
        return platoPreferido

    @staticmethod
    def buscarPlatoRecomendado(codigoCliente: int) -> List[Plato]:
        platoPreferido = Cliente.buscarPlatoPreferido(codigoCliente)
        if platoPreferido is None:
            return None
        ingredientes = []
        platosRecomendados = []
        ingredientesSimilares = []
        for plato in Plato.platos:
            for preferido in platoPreferido:
                ingredientesSimilares = Plato.getIngredientesSimilares(plato, Plato.buscarPlato(preferido))
                if ingredientesSimilares[0] >= 3 and (plato.nombre not in platoPreferido) and (plato not in platosRecomendados):
                    platosRecomendados.append(plato)
                    for ingrediente in plato.ingredientes:
                        if ingrediente not in ingredientes:
                            ingredientes.append(ingrediente)
        return [platosRecomendados, ingredientes]

    @staticmethod
    def buscarPlatoRecomendadoPorIngredientes(ingredientes: List[str], eliminar) -> List[Plato]:
        platosRecomendados = []
        for plato in Plato.platos:
            ingredientesSimilares = 0
            for ingrediente in ingredientes:
                if Item.buscar_item(ingrediente) in plato.ingredientes and plato not in platosRecomendados and ingrediente != eliminar:
                    ingredientesSimilares += 1
            if ingredientesSimilares >= 3 and Item.buscar_item(eliminar) not in plato.ingredientes:
                platosRecomendados.append(plato)
        return platosRecomendados

    @staticmethod
    def registrarCliente() -> 'Cliente':
        nombre = input("¿Cuál es su nombre?")
        id = int(input("¿Cuál es su ID?"))
        return Cliente(nombre, id)

    def __str__(self):
        return f"{self.nombre} ({self.id})"

    def __repr__(self):
        return f"Cliente({self.nombre}, {self.id}, {self.direccion}, {self.telefono}, {self.email}, {self.fechaRegistro})"

    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.codigoCliente == other.codigoCliente
        return False

    def __hash__(self):
        return hash(self.codigoCliente)

    def toJSON(self):
        return {
            "nombre": self.nombre,
            "id": self.id,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "email": self.email,
            "fechaRegistro": self.fechaRegistro,
            "codigoCliente": self.codigoCliente
        }

    @staticmethod
    def fromJSON(json):
        return Cliente(json["nombre"], json["id"], json["direccion"], json["telefono"], json["email"], json["fechaRegistro"])
    
    @staticmethod
    def init_cliente():
        cliente1 = Cliente("Juan Perez", 1, "Calle 123", "555-1234", "juanperez@example.com", "2021-01-01")
        cliente2 = Cliente("Maria Garcia", 2, "Calle 456", "555-5678", "mariagarcia@example.com", "2021-02-01")
        cliente3 = Cliente("Pedro Rodriguez", 3, "Calle 789", "555-9012", "pedrorodriguez@example.com", "2021-03-01")
    
