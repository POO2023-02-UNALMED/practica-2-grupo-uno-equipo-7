import pickle
from baseDatos import Serializador
from gestorAplicacion.Sugerencia import Sugerencia
from gestorAplicacion.Queja import Queja

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
    with open("src/baseDatos/Quejas.pkl","rb") as picklefile:
        Quejas = pickle.load(picklefile)
    for queja in Quejas:
        if queja.getTipo() == tipo:
            Lista.append(queja)
    
    return Lista

def QuejasT():
    Lista = []
    with open("src/baseDatos/Quejas.pkl","rb") as picklefile:
        Quejas = pickle.load(picklefile)
    
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





        
