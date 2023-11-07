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

    @classmethod
    def cantidadReseñas(cls):
        return cls.countReseñas
    @classmethod
    def sumCalificaciones(cls):
        return cls.countCalificaciones

    @classmethod
    def PromedioCalificaciones(cls):
        return cls.sumCalificaciones()/cls.cantidadReseñas()
    


