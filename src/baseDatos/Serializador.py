from gestorAplicacion.Sugerencia import Sugerencia
from gestorAplicacion.Queja import Queja
from gestorAplicacion.Pedido import Pedido
from gestorAplicacion.Reserva import Reserva
from gestorAplicacion.Resena import Resena

import pickle

TodosLosPedidos = []
TodosLosPedidos = Pedido.mostrarListPedidos()
TodasSugerencias = []
TodasSugerencias = Sugerencia.getTAllSugerences()
TodasQuejas = []
TodasQuejas = Queja.getAllQuejas()
TodasResenas = []
TodasResenas = Resena.getRecopilatorio()


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

    with open("src/baseDatos/Resenas.pkl","wb") as picklefileR:
        pickle.dump(TodasResenas, picklefileR)

#funciones

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
    
def agregarQuejaNueva(nueva_queja):
    # Cargar las quejas existentes del archivo pickle
    try:
        with open("src/baseDatos/Quejas.pkl", "rb") as picklefile:
            quejas_existentes = pickle.load(picklefile)
    except FileNotFoundError:
        quejas_existentes = []

    # Agregar la nueva queja a la lista de quejas
    quejas_existentes.append(nueva_queja)

    # Guardar la lista actualizada de quejas en el archivo pickle
    with open("src/baseDatos/Quejas.pkl", "wb") as picklefile:
        pickle.dump(quejas_existentes, picklefile)

def AgregarNuevoPedido(nuevo_pedido):
    # Cargar los pedidos existentes del archivo pickle
    try:
        with open("src/baseDatos/Pedidos.pkl", "rb") as picklefileP:
                Pedidos_existentes = pickle.load(picklefileP)
    except FileNotFoundError:
        Pedidos_existentes = []

    # Agregar el nuevo a la lista de pedidos
    Pedidos_existentes.append(nuevo_pedido)

    # Guardar la lista actualizada de pedidos en el archivo pickle
    with open("src/baseDatos/Pedidos.pkl", "wb") as picklefileP:
        pickle.dump(Pedidos_existentes, picklefileP)

def agregarResenaNueva(nueva_resena):
    # Cargar las reseñas existentes del archivo pickle
    try:
        with open("src/baseDatos/Resenas.pkl", "rb") as picklefileR:
            resenas_existentes = pickle.load(picklefileR)
    except FileNotFoundError:
        resenas_existentes = []

    # Agregar la nueva reseña a la lista de reseñas
    resenas_existentes.append(nueva_resena)

    # Guardar la lista actualizada de reseñas en el archivo pickle
    with open("src/baseDatos/Resenas.pkl", "wb") as picklefileR:
        pickle.dump(resenas_existentes, picklefileR)

def agregarReservaNueva(nueva_reserva):

    # Cargar las reservas existentes del archivo pickle
    try:
        with open("src/baseDatos/Reserva.pkl", "rb") as picklefileRe:
            reservas_existentes = pickle.load(picklefileRe)
    except FileNotFoundError:
        reservas_existentes = []

    # Agregar la nueva reserva a la lista de reservas
    reservas_existentes.append(nueva_reserva)

    # Guardar la lista actualizada de reserva en el archivo pickle
    with open("src/baseDatos/Reserva.pkl", "wb") as picklefileRe:
        pickle.dump(reservas_existentes, picklefileRe)


