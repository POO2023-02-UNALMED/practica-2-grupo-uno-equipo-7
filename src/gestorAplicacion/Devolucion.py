from gestorAplicacion import ServiciosClientes
from gestorAplicacion import Factura

class Devolucion (ServiciosClientes):

    Devoluciones = []

    def __init__(self, nombre, cedula, correo, numerofactura, texto):
        super._cliente = nombre
        super._razon = texto
        self._cedula.setCedula(cedula) #Pendiente revisar ID
        self._correo.setEmail(correo)#Pendiente revisar Correo
        self._estado = "Pendiente"

        factura = Factura.buscarFactura(numerofactura)
        self._factura = factura
        Devolucion.Devoluciones.append(self)

    def setEstado(self, nuevoEstado):
        self._estado = nuevoEstado

    def getEstado(self):
        return self._estado
    
    @classmethod
    def getDevoluciones(cls):
        return cls.Devoluciones

    @classmethod
    def getCantidadDevoluciones(cls):
        return len(cls.Devoluciones)
    
    @classmethod
    def existeDevolucion(cls, codigo):
        a = False
        b = cls.getDevoluciones()

        for devolucion in b:
            if devolucion.getCodigoReferencia(cls) == codigo:
                a = True
        
        return a
    
    @classmethod
    def buscarDevolucion(cls, codigo):
        b = cls.getDevoluciones()
        for devolucion in b:
            if devolucion.getCodigoReferencia(cls) == codigo:
                return devolucion
        
    
