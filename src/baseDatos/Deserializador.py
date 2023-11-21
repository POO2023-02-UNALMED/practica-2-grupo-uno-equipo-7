import pickle
from baseDatos import Serializador
from gestorAplicacion.Sugerencia import Sugerencia
from gestorAplicacion.Queja import Queja
from gestorAplicacion.Reserva import Reserva

def imprimirAllSugerencias():
    Serializador.main()
    with open("src/baseDatos/Sugerencias.pkl","rb") as picklefile:
        Sugerencias = pickle.load(picklefile)

    for sugerencia in Sugerencias:
        print(sugerencia)
        print("\n")

def imprimirSugerenciaXTipo(tipo):
    with open("src/baseDatos/Sugerencias.pkl","rb") as picklefile:
        Sugerencias = pickle.load(picklefile)

    for sugerencia in Sugerencias:
        if sugerencia.getTipo() == tipo:
            print(sugerencia)
            print("\n")

            
def imprimirAllQuejas():
    Serializador.main2()
    with open("src/baseDatos/Quejas.pkl","rb") as picklefile:
        Sugerencias = pickle.load(picklefile)

    for sugerencia in Sugerencias:
        print(sugerencia)
        print("\n")


def SugerenciaXTipo(tipo):
    Lista = []
    with open("src/baseDatos/Sugerencias.pkl","rb") as picklefile:
        Sugerencias = pickle.load(picklefile)
    for sugerencia in Sugerencias:
        if sugerencia.getTipo() == tipo:
            Lista.append(sugerencia)
    
    return Lista

def SugerenciasT():
    Lista = []
    with open("src/baseDatos/Sugerencias.pkl","rb") as picklefile:
        Sugerencias = pickle.load(picklefile)
    
    for sugerencia in Sugerencias:
        Lista.append(sugerencia)
    
    return Lista

def QuejasXTipo(tipo):
    Lista = []
    with open("src/baseDatos/Quejas.pkl", "rb") as picklefileQ:
        Quejas = pickle.load(picklefileQ)
    
    for queja in Quejas:
        if queja.getTipo() == tipo:
            Lista.append(queja)
    
    return Lista

def QuejasT():
    Lista = []
    with open("src/baseDatos/Quejas.pkl","rb") as picklefileQ:
        Quejas = pickle.load(picklefileQ)
    
    for queja in Quejas:
        Lista.append(queja)
    
    return Lista

def PedidosT():
    Lista = []
    with open("src/baseDatos/Pedidos.pkl","rb") as picklefileP:
        Pedidos = pickle.load(picklefileP)
    
    for Pedido in Pedidos:
        Lista.append(Pedido)
    
    return Lista

def deserializador_reservas():
    
    with open("src/baseDatos/Reservas.pkl","rb") as picklefile:
        reservas = pickle.load(picklefile)
        for reservas in Reserva:
            Reserva.listaReservas.append(reservas)
        return reservas

def ResenasT():
    Lista = []
    with open("src/baseDatos/Resenas.pkl","rb") as picklefileP:
        resenas = pickle.load(picklefileP)
    
    for resena in resenas:
        Lista.append(resena)
    
    return Lista

def countCalificacionResenas():
    count = 0
    promedio = 0
    Lista = []
    with open("src/baseDatos/Resenas.pkl","rb") as picklefileP:
        resenas = pickle.load(picklefileP)
    
    for resena in resenas:
        Lista.append(resena)
    
    for cal in Lista:
        a = cal.getCalificacion()
        a = int(a)
        count += a
    
    cant = len(Lista)
    promedio = count/cant

    S = "El promedio de calificaciones es --> " + promedio
        
    if promedio >=3 and promedio <4:
        S += "\nLa satisfacion general de los clientes es regular :/"
            
    elif promedio <3:
        S += "\nLa satisfacion general de los clientes es mala :c"
            
    else:
        S += "\nLa satisfacion general  de los clientes es buena :D"

    return S
    



    
