from gestorAplicacion.Sugerencia import Sugerencia
import pickle

TodasSugerencias = []
TodasSugerencias = Sugerencia.getTAllSugerences()

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

