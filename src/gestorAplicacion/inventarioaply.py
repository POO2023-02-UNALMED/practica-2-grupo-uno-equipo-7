from collections import defaultdict
from gestorAplicacion.Item import Item


class Inventarioaply:
    cantidad_total=0
    Inventarios=[]

    def __init__(self):
        self.diccionario_items = defaultdict(int)
        self.listado_items = []
        Inventarioaply.cantidad_total +=1
        Inventarioaply.Inventarios.append(self)
        

    def añadir_items(self, item, cantidad):
        if item not in self.diccionario_items:
            self.diccionario_items[item] = cantidad
        else:
            self.diccionario_items[item] += cantidad
        self.cantidad_total += cantidad
    
    
    
    def añadir_a_listado_items(self, item):
        self.listado_items.append(item)


    def retirar_items(self, item, cantidad):
        if item in self.diccionario_items:
            cantidad_actual = self.diccionario_items[item]
            if cantidad_actual >= cantidad:
                self.diccionario_items[item] -= cantidad
                self.cantidad_total -= cantidad
            else:
                print(f"No hay suficientes {item} en el inventario.")

    def mostrar_items_vencidos(self):
        items_vencidos = []
        for item in self.listado_items:
            if item.esta_vencido()==True:
                items_vencidos.append(item)
        return items_vencidos

    def eliminar_vencidos(self):
        elementos_vencidos = []
        for item in self.listado_items:
            if item.esta_vencido():
                elementos_vencidos.append(item)
        self.listado_items = [item for item in self.listado_items if item not in elementos_vencidos]
        for item in elementos_vencidos:
            self.retirar_items(item.nombre, item.cantidad)

    def hay_suficiente_stock(self, item, cantidad_deseada):
        if item in self.diccionario_items.keys():
            if self.diccionario_items[item] >= cantidad_deseada:
                return True
        return False

    def obtener_items_sin_stock(self):
        items_sin_stock = []
        for item in self.diccionario_items:
            if self.diccionario_items[item] == 0:
                items_sin_stock.append(item)
        return items_sin_stock

    @staticmethod
    def obtener_inventarios():
        return Inventarioaply.Inventarios

    @property
    def diccionario_items(self):
        return self._diccionario_items

    @diccionario_items.setter
    def diccionario_items(self, diccionario_items):
        self._diccionario_items = diccionario_items

    @property
    def listado_items(self):
        return self._listado_items

    @listado_items.setter
    def listado_items(self, listado_items):
        self._listado_items = listado_items

    def resetear_inventario(self):
        for item in self.diccionario_items:
            self.diccionario_items[item] = 0

