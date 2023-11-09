import pickle
from typing import List
from datetime import date
from .Persona import Persona
from .Mesa import Mesa
from .Factura import Factura
from .Plato import Plato

class Cliente(Persona):
    clientes = []
    contadorClientes = 0

    def __init__(self, nombre: str, id: int, direccion: str = None, telefono: str = None, email: str = None, fechaRegistro: str = None):
        super().__init__(nombre, id)
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fechaRegistro = fechaRegistro
        self.codigoCliente = Cliente.contadorClientes + 1
        Cliente.contadorClientes += 1
        Cliente.clientes.append(self)

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
        if len(facturas) < 2:
            return None
        platos = {}
        for factura in facturas:
            for plato in factura.platos:
                if plato in platos:
                    platos[plato] += 1
                else:
                    platos[plato] = 1
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
                ingredientesSimilares = Plato.getIngredientesSimilares(plato, preferido)
                if ingredientesSimilares[0] >= 3 and plato not in platoPreferido and plato not in platosRecomendados:
                    platosRecomendados.append(plato)
                    for ingrediente in plato.ingredientes:
                        if ingrediente not in ingredientes:
                            ingredientes.append(ingrediente)
        return platosRecomendados

    @staticmethod
    def buscarPlatoRecomendadoPorIngredientes(ingredientes: List[str], item: str, itemAgregar: str = None) -> List[Plato]:
        platosRecomendados = []
        for plato in Plato.platos:
            ingredientesSimilares = 0
            for ingrediente in ingredientes:
                if ingrediente in plato.ingredientes and plato not in platosRecomendados:
                    ingredientesSimilares += 1
                    if ingredientesSimilares > 2 and item not in plato.ingredientes and (itemAgregar is None or itemAgregar in plato.ingredientes):
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
