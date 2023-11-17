import datetime
from datetime import datetime



class Item:
    listado_items=[]
    total_items=0
  

    def __init__(self, nombre, cantidad, precio, fecha_vencimiento, inventario):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.fecha_vencimiento = fecha_vencimiento
        self.inventario = inventario
        Item.listado_items.append(self)
        Item.total_items+=1
        
        

        
        inventario.añadir_items(self.nombre, self.cantidad)
        inventario.añadir_a_listado_items(self)

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def get_fecha_vencimiento(self):
        return self.fecha_vencimiento

    def set_fecha_vencimiento(self, fecha_vencimiento):
        self.fecha_vencimiento = fecha_vencimiento

    def esta_vencido(self):
        fecha_actual = datetime.now()  # Obtener la fecha y hora actual

        if self.fecha_vencimiento is not None and self.fecha_vencimiento < fecha_actual:
            return True  # El producto está vencido
        else:
            return False  # El producto no está vencido o no tiene f

    def calcular_valor_total(self):
        return self.cantidad * self.precio

    
    @staticmethod
    def buscar_item(nombre):
      for ing in Item.listado_items:
        if ing.nombre == nombre:
          return ing

    @staticmethod
    def get_listado_items():
        return Item.listado_items

    @staticmethod
    def set_listado_items(nuevo_listado_items):
        Item.listado_items = nuevo_listado_items
        

        
    





