from gestorAplicacion.Sugerencia import Sugerencia
import pickle

def main():
    #Objetos creados 
    s1 = Sugerencia("Otro","En general creo que las sillas deberian ser más comodas")
    s2 = Sugerencia("Empleado","La atencion fue muy buena pero no habian muchos menseros y eso hizo que el tiempo de espera fuera mayor, para mejorar deberian agregar contratar más meseros")
    s3 = Sugerencia("Menu","Me gustaría que vedieran hamburguesas, seguro que les quedan deliciosas")
   
    s = [s1,s2,s3]
   #Creacion del archivo pickle
   
    with open("src/baseDatos/Prueba.pkl","wb") as picklefile:
        pickle.dump(s, picklefile)
