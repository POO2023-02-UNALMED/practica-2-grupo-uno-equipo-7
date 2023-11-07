from gestorAplicacion import ServiciosClientes

class Reseña(ServiciosClientes):
    
    countCalificaciones = 0
    countReseñas = 0
    Recopilatorio = []

    def __init__(self, nombre, texto, calificacion):
        super.__init__(nombre,texto)
        self._calificacion = calificacion
        countReseñas += 1
        countCalificaciones += calificacion
        Recopilatorio.append(self)

    def __str__(self):
        if super._cliente.getNombre(self) != "Anonimo":
            return "Reseña Numero: " + super.getCodigoReferencia(self) + "\n" + "Nombre: " + super._cliente.getNombre(self) + "\n" + "Calificacion: " + self.getCalificacion(self) + "\n" + "'" + self.getReseña(self) + "'"
        else:
            return "Reseña Numero: " + super.getCodigoReferencia(self) + "\n" + "Anonimo" + "\n" + "Calificacion: " + self.getCalificacion(self) + "\n" + "'" + self.getReseña(self) + "'"

    def setCalificacion(self,cal):
        self._calificacion = cal
    
    def getCalificacion(self):
        return self._calificacion
    
    def setReseña(self, texto):
        super.setRazon(texto)

    def getReseña(self):
        super.getRazon()

    @classmethod
    def getRecopilatorio(cls):
        return cls.Recopilatorio

    @classmethod
    def cantidadReseñas(cls):
        return cls.countReseñas
    @classmethod
    def sumCalificaciones(cls):
        return cls.countCalificaciones

    @classmethod
    def PromedioCalificaciones(cls):
        return cls.sumCalificaciones()/cls.cantidadReseñas()
    


