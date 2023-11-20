from gestorAplicacion.Sugerencia import Sugerencia
from gestorAplicacion.Queja import Queja
from gestorAplicacion.inventarioaply import *
from gestorAplicacion.Pedido import Pedido

import pickle
TodosLosPedidos = []
TodosLosPedidos = Pedido.mostrarListPedidos()
TodasSugerencias = []
TodasSugerencias = Sugerencia.getTAllSugerences()
TodasQuejas = []
TodasQuejas = Queja.getAllQuejas()

def main():
    #Objetos creados 
    s1 = Sugerencia("Otro","En general creo que las sillas deberian ser más comodas")
    s2 = Sugerencia("Empleado","La atencion fue muy buena pero no habian muchos menseros y eso hizo que el tiempo de espera fuera mayor, para mejorar deberian agregar contratar más meseros")
    s3 = Sugerencia("Menu","Me gustaría que vedieran hamburguesas, seguro que les quedan deliciosas")
    s4 = Sugerencia("Empleado","Contraten a mi primo, se llama Manolo Garza")
    s5 = Sugerencia("Menu", "Vendan salchipapas caleñas")
    s6 = Sugerencia("Sede", "Mas mesas para reservas en la sede de Envigado, siempre esta llena y no alcanzo a poder reservar ni una")
    s7 = Sugerencia("Otro", "Deberian considerar hacer parqueaderos")
    
   #Creacion del archivo pickle
   
    with open("src/baseDatos/Sugerencias.pkl","wb") as picklefile:
        pickle.dump(TodasSugerencias, picklefile)
    
def main2():

    q1 = Queja("Juan Perez", "Empleado", "Camilo Palacio", "Me cobro propina sin dar la autorización")
    q2 = Queja("Juan Perez", "Empleado", "Camilo Palacio", "Es muy grosero, me insulto por dejar, segun él, poca propina")
    q3 = Queja("Maria Lopez", "Sede", "Sede: Envigado", "No quisieron hacerme un domicilio")

    with open("src/baseDatos/Quejas.pkl","wb") as picklefileQ:
        pickle.dump(TodasQuejas, picklefileQ)

def main3():
    pedido1 = Pedido("Sergio Perez", 1054456608, "El Chagualo", "De envio")
    pedido2 = Pedido("Carlos Sainz", 1033556576, "Barrio España", "Para recoger")
    pedido3 = Pedido("Fernando Alonso", 1984543324, "Barrio España", "Para Recoger")
    pedido4 = Pedido("Juan Montoya", 4344434434, "Barrio America", "De envio")

    with open("src/baseDatos/Pedidos.pkl","wb") as picklefileP:
        pickle.dump(TodosLosPedidos, picklefileP)

def agregarSugerenciaNueva(nueva_sugerencia):
    # Cargar las sugerencias existentes del archivo pickle
    try:
        with open("src/baseDatos/Sugerencias.pkl", "rb") as picklefile:
            sugerencias_existentes = pickle.load(picklefile)
    except FileNotFoundError:
        sugerencias_existentes = []

    # Agregar la nueva sugerencia a la lista de sugerencias
    sugerencias_existentes.append(nueva_sugerencia)

    # Guardar la lista actualizada de sugerencias en el archivo pickle
    with open("src/baseDatos/Sugerencias.pkl", "wb") as picklefile:
        pickle.dump(sugerencias_existentes, picklefile)
    
def agregarQuejaNueva(nueva_sugerencia):
    # Cargar las quejas existentes del archivo pickle
    try:
        with open("src/baseDatos/Quejas.pkl", "rb") as picklefile:
            quejas_existentes = pickle.load(picklefile)
    except FileNotFoundError:
        quejas_existentes = []

    # Agregar la nueva sugerencia a la lista de sugerencias
    quejas_existentes.append(nueva_sugerencia)

    # Guardar la lista actualizada de sugerencias en el archivo pickle
    with open("src/baseDatos/Quejas.pkl", "wb") as picklefile:
        pickle.dump(quejas_existentes, picklefile)

def AgregarNuevoPedido(nuevo_pedido):
    # Cargar las sugerencias existentes del archivo pickle
    try:
        with open("src/baseDatos/Pedidos.pkl", "rb") as picklefileP:
                Pedidos_existentes = pickle.load(picklefileP)
    except FileNotFoundError:
        Pedidos_existentes = []

    # Agregar la nueva sugerencia a la lista de sugerencias
    Pedidos_existentes.append(nuevo_pedido)

    # Guardar la lista actualizada de sugerencias en el archivo pickle
    with open("src/baseDatos/Pedidos.pkl", "wb") as picklefileP:
        pickle.dump(Pedidos_existentes, picklefileP)

def aver():
    for queja in TodasSugerencias:
        print(queja)


