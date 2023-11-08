class Menu:
    def __init__(self, nombre, precio, disponible, platos):
        self.nombre = nombre
        self.precio = precio
        self.disponible = disponible
        self.platos = platos

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def is_disponible(self):
        return self.disponible

    def set_disponible(self, disponible):
        self.disponible = disponible

    def get_platos(self):
        return self.platos

    def set_platos(self, platos):
        self.platos = platos

    def agregar_plato(self, plato):
        self.platos.append(plato)

    def eliminar_plato(self, plato):
        self.platos.remove(plato)

    def calcular_costo_total(self):
        return self.precio * len(self.platos)

    def __str__(self):
        return "Nombre del Menú: " + self.nombre + "\nPrecio: " + str(self.precio) + "\nDisponible: " + str(self.disponible) + "\nPlatos en el Menú: " + str(self.platos)
