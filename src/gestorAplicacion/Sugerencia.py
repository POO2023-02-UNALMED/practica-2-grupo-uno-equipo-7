from gestorAplicacion.ServiciosClientes import ServiciosClientes

class Sugerencia(ServiciosClientes):

    count = 1
    Sugerencias = []
    SugerenciasMenu = []
    SugerenciasEmpleados = []
    SugerenciasSedes = []
    SugerenciasOtros = []

    def __init__(self,tipe = "Otro",text = None):
        super().__init__("Anonimo", text)
        self._tipo = tipe
        self._codigoReferencia = Sugerencia.count
        Sugerencia.count += 1

        if tipe == "Menu":
            Sugerencia.SugerenciasMenu.append(self)
        elif tipe == "Empleado":
            Sugerencia.SugerenciasEmpleados.append(self)
        elif tipe == "Sede":
            Sugerencia.SugerenciasSedes.append(self)
        else:
            Sugerencia.SugerenciasOtros.append(self)

        Sugerencia.Sugerencias.append(self)

    def getCodigoReferencia(self):
        return self._codigoReferencia

    def setTipo(self, tipe):
        self._tipo = tipe
    
    def getTipo(self):
        return self._tipo
    
    def __str__(self):
        return "N. Referencia: " + str(self.getCodigoReferencia())   + "\nSugerencia tipo: " + self.getTipo() + "\n" + "''" + super().getRazon() + "''"

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
        cls.SugerenciasOtros
    
    @classmethod
    def cantidadSugerencias(cls):
        countSugerencias = len(cls.Sugerencias)

        if countSugerencias == 0:
            return "No hay sugerencias que mostrar"
        else:
            return "Hay un total de (" + countSugerencias + ") sugerencias."
    
    @classmethod
    def cantidadSugerenciasMenu(cls):
        countSugerenciasMenu = len(cls.SugerenciasMenu)

        if countSugerenciasMenu == 0:
            return "No hay sugerencias que mostrar"
        else:
            return "Hay un total de ("+ countSugerenciasMenu + ") sugerencias del tipo: MENU."
    
    @classmethod
    def cantidadSugerenciasEmpleados(cls):
        countSugerenciasEmpleados = len(cls.SugerenciasEmpleados)

        if countSugerenciasEmpleados == 0:
            return "No hay sugerencias que mostrar"
        else:
            return "Hay un total de (" + countSugerenciasEmpleados + ") sugerencias del tipo: EMPLEADO."
    
    @classmethod
    def cantidadSugerenciasSedes(cls):
        countSugerenciasSedes = len(cls.SugerenciasSedes)

        if countSugerenciasSedes == 0:
            return "No hay sugerencias que mostrar"
        else:
            return "Hay un total de (" + countSugerenciasSedes + ") sugerencias del tipo: SEDE."
    
    @classmethod
    def cantidadSugerenciasOtros(cls):
        countSugerenciasOtros = len(cls.SugerenciasOtros)

        if countSugerenciasOtros == 0:
            return "No hay sugerencias que mostrar"
        else:
            return "Hay un total de (" + countSugerenciasOtros + ") sugerencias del tipo: OTRO."





