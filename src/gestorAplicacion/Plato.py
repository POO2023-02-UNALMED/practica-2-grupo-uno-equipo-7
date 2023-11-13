from typing import List
import pickle
from .Item import Item

class Plato:
    pl = []
    listadoplatos = []
    platos = {}

    def __init__(self, nombre: str, ingredientes: [], precio: int):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.precio = precio
        self.disponibilidad = True
        self.platos[self] = ingredientes
        Plato.listadoplatos.append(self)
        Plato.pl.append(self)
    
    

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def disponibilidad(self):
        return self._disponibilidad

    @disponibilidad.setter
    def disponibilidad(self, disponibilidad):
        self._disponibilidad = disponibilidad

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def getIngredientes(self):
        return self.ingredientes

    def mostrarInformacionDetallada(self):
        print("Nombre del Plato: ", self.nombre)
        print("Ingredientes:")
        for ingrediente in self.ingredientes:
            print("- ", ingrediente.getNombre())
        print("Precio Total: ", self.precio)

    def calcularPrecioTotal(self):
        precioTotal = 0
        for ingrediente in self.ingredientes:
            precioTotal += ingrediente.getPrecio()
        return "$" + str(precioTotal)

    @classmethod
    def getPlatos(cls):
        return cls.platos

    @classmethod
    def buscarPlato(cls, nombre):
        for plato in cls.platos.keys():
            if plato.nombre == nombre:
                return plato
        return None

    @classmethod
    def existePlato(cls, nombre):
        for plato in cls.pl:
            if plato.getNombre() == nombre:
                return True
        return False

    @staticmethod
    def getNombrePlato(plato):
        return plato.nombre()

    @staticmethod
    def getIngredientesSimilares(plato1, plato2):
        ingredientesSimilares = 0
        ingredientes = []
        for ingrediente1 in plato1.getIngredientes():
            for ingrediente2 in plato2.getIngredientes():
                if ingrediente1 == ingrediente2 and ingrediente1 not in ingredientes:
                    ingredientes.append(ingrediente1.get_nombre())
                    ingredientesSimilares += 1
        return [ingredientesSimilares, ingredientes]

    def disponibilidadPlato(self):
        for i in self.ingredientes:
            if not i:
                continue
            if not i.getInventario().haySuficienteStock(i, 1):
                self.disponibilidad = False

    def IngredientesFaltantes(self):
        listadoFaltantes = []
        for i in self.ingredientes:
            if not i:
                continue
            if not i.getInventario().haySuficienteStock(i, 1):
                listadoFaltantes.append(i.getNombre())
        return listadoFaltantes

    @classmethod
    def getListadoplatos(cls):
        return cls.listadoplatos

    def __str__(self):
        return f"Plato [nombre={self.nombre}, ingredientes={self.ingredientes}, precio={self.precio}, disponibilidad={self.disponibilidad}]"


