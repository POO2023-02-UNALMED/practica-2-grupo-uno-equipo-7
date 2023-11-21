import pickle
from baseDatos import Serializador
from gestorAplicacion.Sugerencia import Sugerencia
from gestorAplicacion.Queja import Queja
from gestorAplicacion.Reserva import Reserva
import os

def imprimirAllSugerencias():
    Serializador.main()
    ruta_absoluta = os.path.abspath("Sugerencias.pkl")
    with open(ruta_absoluta,"rb") as picklefile:
        Sugerencias = pickle.load(picklefile)

    for sugerencia in Sugerencias:
        print(sugerencia)
        print("\n")

def imprimirSugerenciaXTipo(tipo):
    ruta_absoluta = os.path.abspath("Sugerencias.pkl")
    with open(ruta_absoluta,"rb") as picklefile:
        Sugerencias = pickle.load(picklefile)

    for sugerencia in Sugerencias:
        if sugerencia.getTipo() == tipo:
            print(sugerencia)
            print("\n")

            
def imprimirAllQuejas():
    Serializador.main2()
    ruta_absoluta = os.path.abspath("Quejas.pkl")
    with open(ruta_absoluta,"rb") as picklefile:
        Sugerencias = pickle.load(picklefile)

    for sugerencia in Sugerencias:
        print(sugerencia)
        print("\n")


def SugerenciaXTipo(tipo):
    Lista = []
    ruta_absoluta = os.path.abspath("Sugerencias.pkl")
    with open(ruta_absoluta,"rb") as picklefile:
        Sugerencias = pickle.load(picklefile)
    for sugerencia in Sugerencias:
        if sugerencia.getTipo() == tipo:
            Lista.append(sugerencia)
    
    return Lista

def SugerenciasT():
    Lista = []
    ruta_absoluta = os.path.abspath("Sugerencias.pkl")
    with open(ruta_absoluta,"rb") as picklefile:
        Sugerencias = pickle.load(picklefile)
    
    for sugerencia in Sugerencias:
        Lista.append(sugerencia)
    
    return Lista

def QuejasXTipo(tipo):
    Lista = []
    ruta_absoluta = os.path.abspath("Quejas.pkl")
    with open(ruta_absoluta,"rb") as picklefileQ:
        Quejas = pickle.load(picklefileQ)
    
    for queja in Quejas:
        if queja.getTipo() == tipo:
            Lista.append(queja)
    
    return Lista

def QuejasT():
    Lista = []
    ruta_absoluta = os.path.abspath("Quejas.pkl")
    with open(ruta_absoluta,"rb") as picklefileQ:
        Quejas = pickle.load(picklefileQ)
    
    for queja in Quejas:
        Lista.append(queja)
    
    return Lista

def PedidosT():
    Lista = []
    ruta_absoluta = os.path.abspath("Pedidos.pkl")
    with open(ruta_absoluta,"rb") as picklefileP:
        Pedidos = pickle.load(picklefileP)
    
    for Pedido in Pedidos:
        Lista.append(Pedido)
    
    return Lista

def deserializador_reservas():
    
    Lista = []
    ruta_absoluta = os.path.abspath("Reserva.pkl")
    with open(ruta_absoluta,"rb") as picklefileP:
        Reserva = pickle.load(picklefileP)
    
    for  reserva in Reserva:
        Lista.append(reserva)
    
    return Lista

def ResenasT():
    Lista = []
    ruta_absoluta = os.path.abspath("Resenas.pkl")
    with open(ruta_absoluta,"rb") as picklefileP:
        resenas = pickle.load(picklefileP)
    
    for resena in resenas:
        Lista.append(resena)
    
    return Lista

def countCalificacionResenas():
    count = 0
    promedio = 0
    Lista = []
    ruta_absoluta = os.path.abspath("Resenas.pkl")
    with open(ruta_absoluta,"rb") as picklefileP:
        resenas = pickle.load(picklefileP)
    
    for resena in resenas:
        Lista.append(resena)
    
    for cal in Lista:
        a = cal.getCalificacion()
        a = int(a)
        count += a
    
    cant = len(Lista)
    promedio = count/cant

    S = "El promedio de calificaciones es --> " + str(promedio)
        
    if promedio >=3 and promedio <4:
        S += "\nLa satisfacion general de los clientes es regular :/"
            
    elif promedio <3:
        S += "\nLa satisfacion general de los clientes es mala :c"
            
    else:
        S += "\nLa satisfacion general  de los clientes es buena :D"

    return S

def DevolucionesT():
    Lista = []
    ruta_absoluta = os.path.abspath("Devoluciones.pkl")
    with open(ruta_absoluta,"rb") as picklefileD:
        devoluciones = pickle.load(picklefileD)
    
    for devolucion in devoluciones:
        Lista.append(devolucion)
    
    return Lista

def DelXTipo(nombreIngreso):
    MisDevoluciones = []

    a = ""

    for letra in nombreIngreso:
        a +=str(letra)
    
    nombre = a.upper()
    
    ruta_absoluta = os.path.abspath("Devoluciones.pkl")
    with open(ruta_absoluta,"rb") as picklefileD:
        devoluciones = pickle.load(picklefileD)
    
    for devolucion in devoluciones:
        if nombre == devolucion.getNombre():
            MisDevoluciones.append(devolucion)
    
    return MisDevoluciones
    

    


    



    
