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
        self._motivo = None

        factura = Factura.buscarFactura(numerofactura)
        self._factura = factura
        Devolucion.Devoluciones.append(self)

    def setEstado(self, nuevoEstado):
        self._estado = nuevoEstado

    def getEstado(self):
        return self._estado
    
    def setMotivo(self, texto):
        self._motivo = texto
    
    def getMotivo(self):
         return self._motivo
    
    def __str__(self):
        a = None

        if self.getEstado() == "Denegado": 
            a = "N° Solicitud: " + self.getCodigoReferencia() + "\n" + "Cliente: " + self._cliente.getNombre() + " - CC. " + self._cliente.getCedula() + " - Email: " + self._cliente.getEmail() + "\n" + "Estado de la solicitud:  " + self.getEstado()+ "\n" + "Motivo de rechazo: " + self.getMotivo() + "\n" + "La solicitud fue denegada, se enviara un correo al cliente con la decision tomada"
        
        elif self.getEstado() == "Aprobado":
            a = "N° Solicitud: " + self.getCodigoReferencia() + "\n" + "Cliente: " + self._cliente.getNombre() + " - CC. " + self._cliente.getId() + " - Email: " + self._cliente.getEmail() + "\n" + "Estado de la solicitud:  " + self.getEstado()+ "\n" + "La solicitud fue aprobada, se enviara un correo al cliente con la decision tomada y los pasos a seguir para hacer efectiva su solicitud"
        
        else: 
            a = "N° Solicitud: " + self.getCodigoReferencia() + "\n" + "Cliente: " + self._cliente.getNombre() + " - CC. " + self._cliente.getId() + " - Email: " + self._cliente.getEmail() + "\n" + "Codigo de Factura: " + self._factura.getCodigo() + "\n" + "Estado de la solicitud:  " + self.getEstado()+ "\n" + "Motivo de la solicitud: " + self.getTexto()
        
    @classmethod
    def DenegarDevolucion(cls, codigo):
        a = cls.buscarDevolucion(codigo)
        a.setEstado("Denegado")

    @classmethod
    def AprobarDevolucion(cls, codigo):
        a = cls.buscarDevolucion(codigo)
        a.setEstado("Aprobado")
        
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
        
    
