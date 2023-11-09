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
            worker = Empleado.existeEmpleado(algo) #Recordatorio: Asegurarse de que exista el metodo en la clase Empleado :D
            Empleado.nuevaAmonestacion(worker)

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
            return "Nombre: " + super.cliente.getNombre(self) + "\n" + "Realizo una queja sobre el platillo: " + self._plato.getNombre(self) + "\n" + "'" + super.getRazon(self) + "'"

        elif self.tipo == "Empleado":
            return "Nombre: " + super.cliente.getNombre(self) + "\n" + "Realizo una queja sobre el empleado: " + self._empleado.getNombre(self) + "\n" + "'" + super.getRazon(self) + "'"
        
        elif self.tipo == "Sede":
            return "Nombre: " + super.cliente.getNombre(self) + "\n" + "Realizo una queja sobre la " + self.Restaurante.getUbicacion(self) + "\n"  + "'" + super.getRazon(self) + "'"
        else:
            return "Nombre: " + super.cliente.getNombre(self) + "\n"  + "Realizo una queja: " + "'" + super.getRazon(self) + "'"
    
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
        return countQuejas
    
    @classmethod
    def cantidadQuejasMenu(cls):
        countQuejasMenu = len(cls.QuejasMenu)
        return countQuejasMenu
    
    @classmethod
    def cantidadQuejasEmpleados(cls):
        countQuejasEmpleados = len(cls.QuejasEmpleados)
        return countQuejasEmpleados
    
    @classmethod
    def cantidadQuejasSedes(cls):
        countQuejasSedes = len(cls.QuejasSedes)
        return countQuejasSedes
    
    @classmethod
    def cantidadQuejasOtros(cls):
        countQuejasOtros = len(cls.QuejasOtros)
        return countQuejasOtros
    
    @classmethod
    def cantidadAmonestaciones(self, empleado):
         return "Nombre empleado: " + empleado.getNombre(self) + " tiene (" + empleado.cantidadAmonestaciones(self) + ")" #Revisar metodo en la clase Empleado