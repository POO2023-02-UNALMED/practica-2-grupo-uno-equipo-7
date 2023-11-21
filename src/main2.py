from tkinter import *
from GUI.manager import *
from gestorAplicacion.Cliente import *
from gestorAplicacion.Factura import *
from gestorAplicacion.Plato import *
from gestorAplicacion.Restaurante import *
from gestorAplicacion.Caja import *
from gestorAplicacion.Item import *
from gestorAplicacion.inventarioaply import *
from gestorAplicacion.Reserva import *
from gestorAplicacion.Pedido import *



if __name__ == "__main__":
    cliente1 = Cliente("Juan Perez", 1, "Calle 123", "555-1234", "juanperez@example.com", "2021-01-01")
    cliente2 = Cliente("Maria Garcia", 2, "Calle 456", "555-5678", "mariagarcia@example.com", "2021-02-01")
    cliente3 = Cliente("Pedro Rodriguez", 3, "Calle 789", "555-9012", "pedrorodriguez@example.com", "2021-03-01")

    cliente1 = Cliente("Juan Perez", 1, "Calle 123", "555-1234", "juanperez@example.com", "2021-01-01")
    cliente2 = Cliente("Maria Garcia", 2, "Calle 456", "555-5678", "mariagarcia@example.com", "2021-02-01")
    cliente3 = Cliente("Pedro Rodriguez", 3, "Calle 789", "555-9012", "pedrorodriguez@example.com", "2021-03-01")

    inventario1 = Inventarioaply()
    inventario2 = Inventarioaply()
    inventario3 = Inventarioaply()
    inventario4 = Inventarioaply()

    item1 = Item("Tortilla",10, 1000,"2024-12-31", inventario1)
    item2 = Item("Carne",15, 2000,"2022-12-31", inventario1)
    item3 = Item("Queso",10, 3000,"2022-12-31", inventario1)
    item4 = Item("Lechuga",10, 4000,"2024-12-31", inventario1)
    item5 = Item("Tomate",5, 5000,"2022-12-31", inventario1)
    item6 = Item("Tortilla",10, 1000,"2022-12-31", inventario2)
    item7 = Item("Carne",10, 2000,"2022-12-31", inventario2)
    item8 = Item("Queso",5, 3000,"2022-12-31", inventario2)
    

    ingredientes1 = [item1, item2, item3, item4, item5]
    ingredientes2 = [item6, item2, item3, item4, item5]
    ingredientes3 = [item7, item2, item3, item4, item5]
    ingredientes4 = [item1, item2, item3, item4, item5]
    ingredientes5 = [item1, item8]
    
    plato1 = Plato("Taco", ingredientes1, 1000)
    plato2 = Plato("Tostada", ingredientes2, 2000)
    plato3 = Plato("Sope", ingredientes3, 3000)
    plato4 = Plato("Enchilada", ingredientes4, 4000)
    plato5 = Plato("Quesadilla", ingredientes5, 5000)


    Factura(1, 1, 1, "2021-01-01", 10, [plato1, plato2])
    Factura(2, 2, 2, "2021-02-01", 20, [plato2, plato3])
    Factura(3, 3, 3, "2021-03-01", 30, [plato3, plato4])
    Factura(1, 1, 1, "2021-04-01", 40, [plato4, plato5])
    Factura(2, 2, 2, "2021-05-01", 50, [plato5, plato1])
    Factura(3, 3, 3, "2021-06-01", 60, [plato1, plato2])
    Factura(1, 1, 1, "2021-07-01", 70, [plato2, plato3])
    Factura(2, 2, 2, "2021-08-01", 80, [plato3, plato4])
    Factura(3, 3, 3, "2021-09-01", 90, [plato4, plato5])
    factura1 = Factura(1, 1, 1, "2022-11-01", 0, [plato1, plato2])
    factura1 = Factura(1, 1, 1, "2022-11-01", 0, [plato1, plato2])
    factura1 = Factura(1, 1, 1, "2022-11-01", 0, [plato2, plato3])
    factura2 = Factura(2, 2, 2, "2022-11-02", 0, [plato4, plato2])

    #crear pedidos nombre: str, identificacion:int, direccionPedido: str, tipoPedido: str 
    pedido1 = Pedido("Sergio Perez", 1054456608, "El Chagualo", "De envio")
    pedido2 = Pedido("Carlos Sainz", 1033556576, "Barrio España", "Para recoger")
    pedido3 = Pedido("Fernando Alonso", 1984543324, "Barrio España", "Para Recoger")
    pedido4 = Pedido("Juan Montoya", 4344434434, "Barrio America", "De envio")


    # crear restaurantes 
  

    Restaurante("Sede: Envigado", "Calle 1", inventario1,
                                 Caja(1000000, 1234), 1234567, date.today(), Plato.getListadoplatos(), [])
    Restaurante("Sede: Sandiego", "Calle 2", inventario2,
                                 Caja(10000000, 1235), 1234567, date.today(), Plato.getListadoplatos(), [])
    Restaurante("Sede: Belen", "Calle 3", inventario3,
                                 Caja(10000000, 1236), 1234567, date.today(), Plato.getListadoplatos(), [])
    Restaurante("Sede: La America", "Calle 4", inventario4,
                                 Caja(10000000,1237), 1234567, date.today(), Plato.getListadoplatos(), [])
   

    #(self, nombre, cargo, sueldo, codigoSede):
    Empleado("David Silva", "Gerente Administrativo", "1", 3000, 1)
    Empleado("Andres Guido", "Gerente Administrativo", "2", 3000, 1)
    Empleado("Manuel Menza", "Gerente Administrativo", "3", 3000, 2)
    Empleado("Maria Jose Restrepo", "Gerente Administrativa", "4", 3000, 2)
    Empleado("Maria Camila Rios", "Gerente Administrativa", "5", 3000, 3)
    Empleado("Camilo Palacio", "Mesero", "6", 1700, 1)

    Mesa("Mesa uno", "Dos personas", "Sede: Las Americas")
    Mesa("Mesa dos", "Tres personas", "Sede: Envigado")
    Mesa("Mesa tres", "Cuatro o más personas", "Sede: Belen")
    Mesa("Mesa cinco", "Dos personas", "Sede: Belen")
    Mesa("Mesa siete", "Tres personas", "Sede: Las Americas")
    Mesa("Mesa siete", "Cuatro o más personas", "Sede: Sandiego")
    Mesa("Mesa tres", "Dos personas", "Sede: Envigado")

    Reserva(cliente1, Restaurante.sedes[0].get_ubicacion(),  Mesa.listaMesas[1], "2023-10-25 14:00 PM")
    
    app = Manager()
    app.mainloop()
    
    
    
    