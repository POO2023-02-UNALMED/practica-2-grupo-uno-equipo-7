# -*- coding: utf-8 -*-
class Resena():
    
    count = 1
    countCalificaciones = 0
    Recopilatorio = []

    def __init__(self, name, texto, cal):
        self._nombre = name
        self._texto = texto
        self._codigoReferencia = Resena.count
        Resena.count += 1
        self._calificacion = cal
        Resena.countCalificaciones += cal
        Resena.Recopilatorio.append(self)
    
    def getNombre(self):
        return self._nombre
    
    def getTexto(self):
        return self._texto

    def getCodigoReferencia(self):
        return self._codigoReferencia

    def setCalificacion(self, cal):
        self._calificacion = cal
    
    def getCalificacion(self):
        return self._calificacion
    
    def __str__(self):
        if self.getNombre() != "Anonimo":
            return "Reseña Numero: " + str(self.getCodigoReferencia()) + "\n" + "Nombre: " + self.getNombre() + "\n" + "Calificacion: " + str(self.getCalificacion()) + "\n" + "'" + self.getTexto() + "'"
        else:
            return "Reseña Numero: " + str(self.getCodigoReferencia()) + "\n" + "Anonimo" + "\n" + "Calificacion: " + str(self.getCalificacion()) + "\n" + "'" + self.getTexto() + "'"
        
    @classmethod
    def getRecopilatorio(cls):
        return cls.Recopilatorio

    @classmethod
    def cantidadResenas(cls):
        countResenas = len(cls.Recopilatorio)
        return countResenas
    
    @classmethod
    def sumCalificaciones(cls):
        return cls.countCalificaciones

    @classmethod
    def PromedioCalificaciones(cls):
        promedio = cls.sumCalificaciones() / cls.cantidadResenas()

        S = "El promedio de calificaciones es --> " + str(promedio)
        
        if promedio >= 3 and promedio < 4:
            S += "\nLa satisfacción general de los clientes es regular :/"
            
        elif promedio < 3:
            S += "\nLa satisfacción general de los clientes es mala :c"
            
        else:
            S += "\nLa satisfacción general de los clientes es buena :D"

        return S
    
