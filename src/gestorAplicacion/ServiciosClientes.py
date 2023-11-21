from gestorAplicacion.Cliente import Cliente

class ServiciosClientes:

    def __init__ (self, nombre = "Anonimo" , text = None):
        cliente = Cliente(nombre, "11111111")
        self._cliente = cliente 
        self._razon = text

    def setCliente(self, cliente):
        self._cliente = cliente
    
    def getCliente(self):
        return self._cliente
    
    def setRazon(self, text):
        self._razon = text
    
    def getRazon(self):
        return self._razon
    
    

    
