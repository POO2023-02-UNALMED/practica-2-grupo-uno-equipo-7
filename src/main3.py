from baseDatos import Serializador, Deserializador
from gestorAplicacion.Sugerencia import Sugerencia

#NO LO BORREN AUN Oswaldo lo creo para ayudar a que probemos la serializacion

if __name__ == "__main__":
   
   # Serializador.main4()
   # a = Deserializador.ResenasT()
   # for b in a: print(b)
   a = Deserializador.deserializador_reservas()
   for b in a: print(b)

