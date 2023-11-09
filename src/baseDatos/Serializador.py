from gestorAplicacion import Sugerencia, Queja, Reseña, Devolucion
import pickle

if __name__ == "__main__":
    #Objetos creados 
    s1 = Sugerencia("Otro","En general creo que las sillas deberian ser más comodas")
    s2 = Sugerencia("Empleado","La atencion fue muy buena pero no habian muchos menseros y eso hizo que el tiempo de espera fuera mayor, para mejorar deberian agregar contratar más meseros")
    s3 = Sugerencia("Menu","Me gustaría que vedieran hamburguesas, seguro que les quedan deliciosas")
   
   #Creacion del archivo pickle
    picklefile = open("src/baseDatos/Prueba.pkl","wb")

    #Serializacion de los objetos creados
    s = [s1,s2,s3]
    pickle.dump(s,picklefile)

    #Cierre archivo serializado
    picklefile.close()