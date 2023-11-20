from baseDatos import Serializador, Deserializador
from gestorAplicacion.Sugerencia import Sugerencia

#NO LO BORREN AUN Oswaldo lo creo para ayudar a que probemos la serializacion

if __name__ == "__main__":
    # sug = Sugerencia("Otro", "Este es el mensaje")}
   #Deserializador.imprimirAllSugerencias()
   a = Deserializador.QuejasT()
   #c = Deserializador.QuejasXTipo("Sede")
   #Serializador.main2()
   #Deserializador.imprimirAllQuejas()
   for b in a: print(str(b))
   #for d in c: print(str(d))