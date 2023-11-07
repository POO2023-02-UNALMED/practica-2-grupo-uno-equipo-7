from gestorAplicacion import ServiciosClientes

class Sugerencia(ServiciosClientes):

    Sugerencias = []
    SugerenciasMenu = []
    SugerenciasEmpleados = []
    SugerenciasSedes = []
    SugerenciasOtros = []

    def __init__(self,tipe = "Otro",text = None):
        super._razon = text
        self._tipo = tipe

        if tipe == "Menu":
            Sugerencia.SugerenciasMenu.append(self)
        
        elif tipe == "Empleado":
            Sugerencia.SugerenciasEmpleados.append(self)

        elif tipe == "Sede":
            Sugerencia.SugerenciasSedes.append(self)

        else:
            Sugerencia.SugerenciasOtros.append(self)
        
        Sugerencia.Sugerencias.append(self)

    def setTipo(self, tipe):
        self._tipo = tipe
    
    def getTipo(self):
        return self._tipo
    
    def __str__(self):
        return "N° Referencia: " + super.getCodigoReferencia(self)   + "\nSugerencia tipo: " + self.getTipo(self) + "\n" + "''" + super.getRazon(self) + "''";

    @classmethod
    def getTAllSugerences(cls):
        return cls.Sugerencias
    
    @classmethod
    def getSugerenciasMenu(cls):
        return cls.SugerenciasMenu
    
    @classmethod
    def getSugerenciasEmpleados(cls):
        return cls.SugerenciasEmpleados
    
    @classmethod
    def getSugerenciasSedes(cls):
        return cls.SugerenciasSedes
    
    @classmethod
    def getSugerenciasOtros(cls):
        return cls.getSugerenciasOtrosS
    
    @classmethod
    def cantidadSugerencias(cls):
        countSugerencias = len(cls.Sugerencias)
        return countSugerencias





