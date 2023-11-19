import pickle

def main():
    # Lectura del archivo serializado
   
    with open("src/baseDatos/Prueba.pkl","rb") as picklefile:
        s = pickle.load(picklefile)

    #Ejecucion metodos para comporbar deserializacion
    for a in s:
        print(a)
        print("\n")
