from gestorAplicacion import ServiciosClientes
from gestorAplicacion import Plato
from gestorAplicacion import Empleado
from gestorAplicacion import Restaurante

class Queja(ServiciosClientes):

    Quejas = []
    QuejasMenu = []
    QuejasEmpleados = []
    QuejasSedes = []
    QuejasOtros = []


    def __init__(self, name, tipe, algo, text):
        super._nombre = name
        super._razon = text
        
        if tipe == "Menu":
            plate = Plato.buscarPlato(algo) #Recordatorio: Asegurarse de que exista el metodo en la clase Plato :D

            self._plato = plate
            Queja.QuejasMenu.append(self)
        
        elif tipe == "Empleado":
            worker = Empleado.existeEmpleado(algo) #Recordatorio: Asegurarse de que exista el metodo en la clase Empleado :D SE SUPONE QUE SI XD
            Empleado.nuevaAmonestacion(worker) #CHECK

            self._empleado = worker
            Queja.QuejasEmpleados.append(self)
        
        elif tipe == "Sedes":
            se = Restaurante.buscarSedeXUbicacion(algo) #Recordatorio: Asegurarse de que exista el metodo en la clase Restaurante :D

            self._sede = se
            Queja.QuejasSedes.append(self)

        else: 
            Queja.QuejasOtros.append(self)
        
        Queja.Quejas.append(self)
    
    def setTipo(self, tipe):
        self.tipo = tipe
    
    def getTipo(self):
        return self.tipo
    
    def __str__(self):
        if self.tipo == "Menu":
            return "Nombre: " + super.cliente.getNombre() + "\n" + "Realizo una queja sobre el platillo: " + self._plato.getNombre() + "\n" + "'" + super.getRazon() + "'"

        elif self.tipo == "Empleado":
            return "Nombre: " + super.cliente.getNombre() + "\n" + "Realizo una queja sobre el empleado: " + self._empleado.getNombre() + "\n" + "'" + super.getRazon() + "'"
        
        elif self.tipo == "Sede":
            return "Nombre: " + super.cliente.getNombre() + "\n" + "Realizo una queja sobre la " + self.Restaurante.getUbicacion() + "\n"  + "'" + super.getRazon() + "'"
        else:
            return "Nombre: " + super.cliente.getNombre() + "\n"  + "Realizo una queja: " + "'" + super.getRazon() + "'"
    
    @classmethod
    def getAllQuejas(cls):
        return cls.Quejas

    @classmethod
    def getQuejasMenu(cls):
        return cls.QuejasMenu
    
    @classmethod
    def getQuejasEmpleados(cls):
        return cls.QuejasEmpleados
    
    @classmethod
    def getQuejasOtros(cls):
        return cls.QuejasOtros
    
    @classmethod
    def cantidadQuejas(cls):
        countQuejas = len(cls.Quejas)

        if countQuejas == 0:
            return "No hay quejas que mostrar"
        else:
            return "Hay un total de (" + countQuejas + ") quejas."
    
    @classmethod
    def cantidadQuejasMenu(cls):
        countQuejasMenu = len(cls.QuejasMenu)

        if countQuejasMenu == 0:
            return "No hay quejas que mostrar"
        else:
            return "Hay un total de (" + countQuejasMenu + ") quejas del tipo: MENU."
    
    @classmethod
    def cantidadQuejasEmpleados(cls):
        countQuejasEmpleados = len(cls.QuejasEmpleados)
        
        if countQuejasEmpleados == 0:
            return "No hay quejas que mostrar"
        else:
            return "Hay un total de (" + countQuejasEmpleados + ") quejas del tipo: EMPLEADO."
    
    @classmethod
    def cantidadQuejasSedes(cls):
        countQuejasSedes = len(cls.QuejasSedes)

        if countQuejasSedes == 0:
            return "No hay quejas que mostrar"
        else:
            return "Hay un total de (" + countQuejasSedes + ") quejas del tipo: SEDE."
    
    @classmethod
    def cantidadQuejasOtros(cls):
        countQuejasOtros = len(cls.QuejasOtros)
        if countQuejasOtros == 0:
            return "No hay quejas que mostrar"
        else:
            return "Hay un total de (" + countQuejasOtros + ") quejas del tipo: OTRO."
    
    @classmethod
    def cantidadAmonestaciones(self, empleado):
         return "Nombre empleado: " + empleado.getNombre() + " tiene (" + empleado.cantidadAmonestaciones() + ")" #Revisar metodo en la clase Empleado