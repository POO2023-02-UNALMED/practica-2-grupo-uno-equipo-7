import pickle
from baseDatos import Serializador
from gestorAplicacion.Sugerencia import Sugerencia

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

        
