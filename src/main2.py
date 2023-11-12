from tkinter import *
from GUI.manager import *
from gestorAplicacion.Cliente import *
from gestorAplicacion.Factura import *
from gestorAplicacion.Plato import *
from gestorAplicacion.Restaurante import *
from gestorAplicacion.inventarioaply import*
from gestorAplicacion.Caja import *

if __name__ == "__main__":
    cliente1 = Cliente("Juan Perez", 1, "Calle 123", "555-1234", "juanperez@example.com", "2021-01-01")
    cliente2 = Cliente("Maria Garcia", 2, "Calle 456", "555-5678", "mariagarcia@example.com", "2021-02-01")
    cliente3 = Cliente("Pedro Rodriguez", 3, "Calle 789", "555-9012", "pedrorodriguez@example.com", "2021-03-01")
    plato1 = Plato("Tacos", ["Tortilla", "Carne", "Cebolla", "Tomate", "Salsa"],10)
    plato2 = Plato("Tostadas", ["Tostada", "Carne", "Cebolla", "Tomate", "Salsa"],20)
    plato3 = Plato("Sopes", ["Sope", "Carne", "Cebolla", "Tomate", "Salsa"],30)
    plato4 = Plato("Enchiladas", ["Tortilla", "Carne", "Cebolla", "Tomate", "Salsa"],30)

    # Crear las facturas
    factura1 = Factura(1, 1, 1, "2022-11-01", 0, [plato1, plato2])
    factura1 = Factura(1, 1, 1, "2022-11-01", 0, [plato1, plato2])
    factura1 = Factura(1, 1, 1, "2022-11-01", 0, [plato2, plato3])
    factura2 = Factura(2, 2, 2, "2022-11-02", 0, [plato4, plato2])
    # crear restaurantes 
    inventario1 = Inventarioaply()
    inventario2 = Inventarioaply()
    inventario3 = Inventarioaply()
    inventario4 = Inventarioaply()

    Restaurante.sedes.append(Restaurante("Sede: Envigado", "Calle 1", inventario1,
                                 Caja(1000000, 1234), 1234567, date.today(), Plato.get_listado_platos(), []))
    Restaurante.sedes.append(Restaurante("Sede: Sandiego", "Calle 2", inventario2,
                                 Caja(10000000, 1235), 1234567, date.today(), Plato.get_listado_platos(), []))
    Restaurante.sedes.append(Restaurante("Sede: Belen", "Calle 3", inventario3,
                                 Caja(10000000, 1236), 1234567, date.today(), Plato.get_listado_platos(), []))
    Restaurante.sedes.append(Restaurante("Sede: La America", "Calle 4", inventario4,
                                 Caja(), 1234567, date.today(), Plato.get_listado_platos(), []))
    
    app = Manager()
    app.mainloop()
    
    
    
    