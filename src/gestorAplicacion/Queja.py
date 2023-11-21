
class Queja():

    count = 1

    Quejas = []
    QuejasMenu = []
    QuejasEmpleados = []
    QuejasSedes = []
    QuejasOtros = []


    def __init__(self, name, tipe = "Otros", algo= "", text=""):
        self._nombre = name
        self._tipo = tipe
        self._codigoReferencia = Queja.count
        Queja.count += 1
        self._otro = algo
        self._texto = text

        if tipe == "Menu":
            Queja.QuejasMenu.append(self)
        elif tipe == "Empleado":
            Queja.QuejasEmpleados.append(self)

        elif tipe == "Sede":
            Queja.QuejasSedes.append(self)
        elif tipe == "Otros":
            Queja.QuejasOtros.append(self)

        Queja.Quejas.append(self)

    def getCodigoReferencia(self):
        return self._codigoReferencia

    def setTipo(self, tipe):
        self._tipo = tipe
    
    def getTipo(self):
        return self._tipo
    
    def getNombre(self):
        return self._nombre
    
    def getOtro(self):
        return self._otro
    
    def getTexto(self):
        return self._texto
    
    
    def __str__(self):
        
        if self._tipo == "Otros":
            return "N. Referencia: " + str(self.getCodigoReferencia()) + "\nNombre: " + self.getNombre()  + "\n"  + "Realizo una queja: " + "'" + self.getTexto() + "'"

        elif self._tipo == "Sede":
            return "N. Referencia: " + str(self.getCodigoReferencia()) + "\nNombre: " + self.getNombre()  + "\n" + "Realizo una queja sobre: " + self.getOtro() + "\n"  + "'" + self.getTexto()+ "'"
        
        elif self._tipo == "Menu":
            return "N. Referencia: " + str(self.getCodigoReferencia()) + "\nNombre: " + self.getNombre()  + "\n" + "Realizo una queja sobre: " + self.getOtro() + "\n"  + "'" + self.getTexto()+ "'"
        
        elif self._tipo == "Empleado":
            return "N. Referencia: " + str(self.getCodigoReferencia()) + "\nNombre: " + self.getNombre()  + "\n" + "Realizo una queja sobre: " + self.getOtro() + "\n"  + "'" + self.getTexto()+ "'"
        
    
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
    
    @staticmethod
    def init_quejas():
        q1 = Queja("Juan Perez", "Empleado", "Camilo Palacio", "Me cobro propina sin dar la autorización")
        q2 = Queja("Juan Perez", "Empleado", "Camilo Palacio", "Es muy grosero, me insulto por dejar, segun él, poca propina")
        q3 = Queja("Maria Lopez", "Sede", "Sede: Envigado", "No quisieron hacerme un domicilio")
        