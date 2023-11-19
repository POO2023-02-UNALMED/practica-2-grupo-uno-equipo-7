from gestorAplicacion.Sugerencia import Sugerencia
import pickle

def main():
    #Objetos creados 
    s1 = Sugerencia("Otro","En general creo que las sillas deberian ser más comodas")
    s2 = Sugerencia("Empleado","La atencion fue muy buena pero no habian muchos menseros y eso hizo que el tiempo de espera fuera mayor, para mejorar deberian agregar contratar más meseros")
    s3 = Sugerencia("Menu","Me gustaria que vedieran hamburguesas, seguro que les quedan deliciosas")
    s4 = Sugerencia("Sedes",  "Seria muy bueno que agregen mas mesas para reservar en la sede de Envigado, siempre hay muchas personas y es dificil que se pueda acceder a ese servicio")
    s5 = Sugerencia("Menu", "Vendan salchipapas")
    s6 = Sugerencia("Empleado", "Contraten a mi primo, se llama Hernesto Garcia")

    s = [s1,s2,s3,s4,s5,s6]
   #Creacion del archivo pickle
   
    with open("src/baseDatos/Sugerencias.pkl","wb") as picklefile:
        pickle.dump(s, picklefile)
