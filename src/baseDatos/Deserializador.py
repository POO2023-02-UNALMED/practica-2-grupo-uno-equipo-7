import pickle

if __name__ == "__main__":
    # Lectura del archivo serializado
    picklefile = open("src/baseDatos/Prueba.pkl", "rb")

    #Deserializacion del archivo
    s = pickle.load(picklefile)

    #Cierre del archivo serializado
    picklefile.close()

    #Ejecucion metodos para comporbar deserializacion
    print(type(s))
    s[1].details()