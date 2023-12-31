from gestorAplicacion.Sugerencia import Sugerencia
from gestorAplicacion.Queja import Queja
from gestorAplicacion.Pedido import Pedido
from gestorAplicacion.Reserva import Reserva
from gestorAplicacion.Resena import Resena
from gestorAplicacion.Devolucion import Devolucion
import os

import pickle

TodosLosPedidos = []
TodosLosPedidos = Pedido.mostrarListPedidos()
TodasSugerencias = []
TodasSugerencias = Sugerencia.getTAllSugerences()
TodasQuejas = []
TodasQuejas = Queja.getAllQuejas()
TodasResenas = []
TodasResenas = Resena.getRecopilatorio()
reservas =  []
reservas = Reserva.getLista()
TodasDevoluciones = Devolucion.getDevoluciones()


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
   
    ruta_absoluta = os.path.abspath("Sugerencias.pkl")
    with open(ruta_absoluta,"wb") as picklefile:
        pickle.dump(TodasSugerencias, picklefile)
    
def main2():

    q1 = Queja("Juan Perez", "Empleado", "Camilo Palacio", "Me cobro propina sin dar la autorización")
    q2 = Queja("Juan Perez", "Empleado", "Camilo Palacio", "Es muy grosero, me insulto por dejar, segun él, poca propina")
    q3 = Queja("Maria Lopez", "Sede", "Sede: Envigado", "No quisieron hacerme un domicilio")

    ruta_absoluta = os.path.abspath("Quejas.pkl")
    with open(ruta_absoluta,"wb") as picklefileQ:
        pickle.dump(TodasQuejas, picklefileQ)

def main3():
    pedido1 = Pedido("Sergio Perez", 1054456608, "El Chagualo", "De envio")
    pedido2 = Pedido("Carlos Sainz", 1033556576, "Barrio España", "Para recoger")
    pedido3 = Pedido("Fernando Alonso", 1984543324, "Barrio España", "Para Recoger")
    pedido4 = Pedido("Juan Montoya", 4344434434, "Barrio America", "De envio")


    ruta_absoluta = os.path.abspath("Pedidos.pkl")
    with open(ruta_absoluta,"wb") as picklefileP:
        pickle.dump(TodosLosPedidos, picklefileP)

def main4():

    r1 = Resena("Anonimo", "Gran lugar para pasar el tiempo en familia, muy buena la atención", 4)
    r2 = Resena("Julian Vargas", "Me gustaron los pozoles", 5)
    r3 = Resena("Marta Wayne", "La comida estaba fria y tardaron mucho en atendernos, mal ahí", 2)
    r4 = Resena("Barbara Gordon", "Muy buen servicio a domicilio, todo llego a tiempo y recien hecho", 5)
    r5 = Resena("Anonimo", "Que fea la sede de Belen, casi nos roban al salir", 1)
    r6 = Resena("Anonimo", "Mi mujer se enfermo despues de comer en una de sus sedes", 1)
    r7 = Resena("Carol Diaz", "Excelente atención", 5)
    r8 = Resena("Santiago Lopez", "Muy buenas porciones y de sabor delicioso", 5)
    r9 = Resena("Esteban Tabares", "La atención en el local de las Americas fue muy buena, hicimos un evento familiar y todo salio perfecto", 5)
    r10 = Resena("Elizabeth Bennet", "La tortilla estaba dura pero lo demas muy rico", 3)

    ruta_absoluta = os.path.abspath("Resena.pkl")
    with open(ruta_absoluta,"wb") as picklefileR:
        pickle.dump(TodasResenas, picklefileR)
    
def main5():
    ruta_absoluta = os.path.abspath("Reserva.pkl")
    with open(ruta_absoluta,"wb") as picklefileRe:
        pickle.dump(reservas, picklefileRe)

def main6():

    d1 = Devolucion("JUAN PEREZ","5236","juan@gmail.com","1","No me senti satisfecho con el pedido")
    d2 = Devolucion("JUAN PEREZ","5236","juan@gmail.com","2","Pese a que me comi todo no me gusto el sabor")
    d3 = Devolucion("JUAN PEREZ","5236","juan@gmail.com","3","No me habia dado cuenta pero me cobraron más de lo que consumi")
    d4 = Devolucion("JUAN PEREZ","5236","juan@gmail.com","4","Me parece una estafa todo lo que me cobraron por lo poco que consumi")
    d5 = Devolucion("JUAN PEREZ","5236","juan@gmail.com","5","La propina me la cobraron sin yo dar permiso")
    d6 = Devolucion("JUAN PEREZ","5236","juan@gmail.com","6","No me gusto la comida")
    d7 = Devolucion("JUAN PEREZ","5236","juan@gmail.com","7","Escuche al mesero renegando por la cantidad de propina que deposite")

    ruta_absoluta = os.path.abspath("Devoluciones.pkl")
    with open(ruta_absoluta,"wb") as picklefileD:
        pickle.dump(TodasDevoluciones, picklefileD)


#funciones

def agregarSugerenciaNueva(nueva_sugerencia):
    # Cargar las sugerencias existentes del archivo pickle
    try:
        ruta_absoluta = os.path.abspath("Sugerencias.pkl")
        with open(ruta_absoluta,"rb") as picklefile:
            sugerencias_existentes = pickle.load(picklefile)
    except FileNotFoundError:
        sugerencias_existentes = []

    # Agregar la nueva sugerencia a la lista de sugerencias
    sugerencias_existentes.append(nueva_sugerencia)

    # Guardar la lista actualizada de sugerencias en el archivo pickle
    ruta_absoluta = os.path.abspath("Sugerencias.pkl")
    with open(ruta_absoluta,"wb") as picklefile:
        pickle.dump(sugerencias_existentes, picklefile)
    
def agregarQuejaNueva(nueva_queja):
    # Cargar las quejas existentes del archivo pickle
    try:
        ruta_absoluta = os.path.abspath("Quejas.pkl")
        with open(ruta_absoluta,"rb") as picklefileQ:
                Quejas_existentes = pickle.load(picklefileQ)
    except FileNotFoundError:
        Quejas_existentes = []

    # Agregar el nuevo a la lista de pedidos
    Quejas_existentes.append(nueva_queja)

    # Guardar la lista actualizada de pedidos en el archivo pickle
    ruta_absoluta = os.path.abspath("Quejas.pkl")
    with open(ruta_absoluta,"wb") as picklefileQ:
        pickle.dump(Quejas_existentes, picklefileQ)


def AgregarNuevoPedido(nuevo_pedido):
    # Cargar los pedidos existentes del archivo pickle
    try:
        ruta_absoluta = os.path.abspath("Pedidos.pkl")
        with open(ruta_absoluta,"rb") as picklefileP:
                Pedidos_existentes = pickle.load(picklefileP)
    except FileNotFoundError:
        Pedidos_existentes = []

    # Agregar el nuevo a la lista de pedidos
    Pedidos_existentes.append(nuevo_pedido)

    # Guardar la lista actualizada de pedidos en el archivo pickle
    ruta_absoluta = os.path.abspath("Pedidos.pkl")
    with open(ruta_absoluta,"wb") as picklefileP:
        pickle.dump(Pedidos_existentes, picklefileP)

def agregarResenaNueva(nueva_resena):
    # Cargar las reseñas existentes del archivo pickle
    try:
        ruta_absoluta = os.path.abspath("Resenas.pkl")
        with open(ruta_absoluta,"rb") as picklefileR:
            resenas_existentes = pickle.load(picklefileR)
    except FileNotFoundError:
        resenas_existentes = []

    # Agregar la nueva reseña a la lista de reseñas
    resenas_existentes.append(nueva_resena)

    # Guardar la lista actualizada de reseñas en el archivo pickle
    ruta_absoluta = os.path.abspath("Resenas.pkl")
    with open(ruta_absoluta,"wb") as picklefileR:
        pickle.dump(resenas_existentes, picklefileR)

def agregarReservaNueva(nueva_reserva):

    # Cargar las reservas existentes del archivo pickle
    try:
        ruta_absoluta = os.path.abspath("Reserva.pkl")
        with open(ruta_absoluta, "rb") as picklefileRe:
            reservas_existentes = pickle.load(picklefileRe)
    except FileNotFoundError:
        reservas_existentes = []

    # Agregar la nueva reserva a la lista de reservas
    reservas_existentes.append(nueva_reserva)

    # Guardar la lista actualizada de reserva en el archivo pickle
    ruta_absoluta = os.path.abspath("Reserva.pkl")
    with open(ruta_absoluta, "wb") as picklefileRe:
        pickle.dump(reservas_existentes, picklefileRe)

def agregarSolicitudNueva(nueva_solicitud):

    # Cargar las reservas existentes del archivo pickle
    try:
        ruta_absoluta = os.path.abspath("Devoluciones.pkl")
        with open(ruta_absoluta,"rb") as picklefileD:
            del_existentes = pickle.load(picklefileD)
    except FileNotFoundError:
        del_existentes = []

    # Agregar la nueva reserva a la lista de reservas
    del_existentes.append(nueva_solicitud)

    # Guardar la lista actualizada de reserva en el archivo pickle
    ruta_absoluta = os.path.abspath("Devoluciones.pkl")
    with open(ruta_absoluta,"wb") as picklefileD:
        pickle.dump(del_existentes, picklefileD)


