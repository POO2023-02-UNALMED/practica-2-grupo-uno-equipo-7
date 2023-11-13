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
    plato5 = Plato("Quesadillas", ["Tortilla", "Queso"],10)

    Factura(1, 1, 1, "2021-01-01", 10, [plato1, plato2])
    Factura(2, 2, 2, "2021-02-01", 20, [plato2, plato3])
    Factura(3, 3, 3, "2021-03-01", 30, [plato3, plato4])
    Factura(1, 1, 1, "2021-04-01", 40, [plato4, plato5])
    Factura(2, 2, 2, "2021-05-01", 50, [plato5, plato1])
    Factura(3, 3, 3, "2021-06-01", 60, [plato1, plato2])
    Factura(1, 1, 1, "2021-07-01", 70, [plato2, plato3])
    Factura(2, 2, 2, "2021-08-01", 80, [plato3, plato4])
    Factura(3, 3, 3, "2021-09-01", 90, [plato4, plato5])

    
    
    app = Manager()
    app.mainloop()
    
    
    
    