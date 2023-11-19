from gestorAplicacion.ServiciosClientes import ServiciosClientes

class Reseña(ServiciosClientes):
    
    count = 1
    countCalificaciones = 0
    Recopilatorio = []

    def __init__(self, nombre, texto, cal):
        super().__init__(nombre,texto)
        self._codigoReferencia = Reseña.count
        Reseña.count += 1
        self._calificacion = cal
        countCalificaciones += cal
        Reseña.Recopilatorio.append(self)

    def __str__(self):
        if super().getCliente().getNombre() != "Anonimo":
            return "Reseña Numero: " + str(self.getCodigoReferencia()) + "\n" + "Nombre: " + super().getCliente().getNombre() + "\n" + "Calificacion: " + self.getCalificacion() + "\n" + "'" + self.getReseña() + "'"
        else:
            return "Reseña Numero: " + str(self.getCodigoReferencia()) + "\n" + "Anonimo" + "\n" + "Calificacion: " + self.getCalificacion() + "\n" + "'" + self.getReseña() + "'"

    def getCodigoReferencia(self):
        return self._codigoReferencia

    def setCalificacion(self,cal):
        self._calificacion = cal
    
    def getCalificacion(self):
        return self._calificacion
    
    def setReseña(self, texto):
        super().setRazon(texto)

    def getReseña(self):
        return super().getRazon()

    @classmethod
    def getRecopilatorio(cls):
        return cls.Recopilatorio

    @classmethod
    def cantidadReseñas(cls):
        countReseñas = len(cls.Recopilatorio)
        return countReseñas
    @classmethod
    def sumCalificaciones(cls):
        return cls.countCalificaciones

    @classmethod
    def PromedioCalificaciones(cls):
        promedio = cls.sumCalificaciones()/cls.cantidadReseñas()

        S = "El promedio de calificaciones es --> " + promedio
        
        if promedio >=3 and promedio <4:
            S += "\nLa satisfacion general de los clientes es regular :/"
            
        elif promedio <3:
            S += "\nLa satisfacion general de los clientes es mala :c"
            
        else:
            S += "\nLa satisfacion general  de los clientes es buena :D"

        return S
    


