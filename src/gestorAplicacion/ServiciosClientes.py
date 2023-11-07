from gestorAplicacion import Cliente

class ServiciosClientes:
    count =  0

    def __init__ (self, nombre = "Anonimo" , text = None):
        self._cliente = nombre # Recuerda: debes cambiar esto despues, cuando este la clase de cliente :D
        self._razon = text
        self._codigoReferencia += count
        count += 1

    def setCliente(self, cliente):
        self._cliente = cliente
    
    def getCliente(self):
        return self._cliente
    
    def setRazon(self, text):
        self._razon = text
    
    def getRazon(self):
        return self._razon
    
    def getCodigoRerencia(self):
        return self._codigoReferencia
    

    
