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

    
    
    app = Manager()
    app.mainloop()
    
    
    
    