from gestorAplicacion.ServiciosClientes import ServiciosClientes
from gestorAplicacion.Factura import Factura

class Devolucion (ServiciosClientes):

    count = 1
    Devoluciones = []

    

    def __init__(self, nombre, cedula, correo, numerofactura, texto):
        super().__init__(nombre,texto)
        super().getCliente().setId(cedula) #Pendiente revisar ID
        super().getCliente().setEmail(correo)#Pendiente revisar Correo
        self._codigoReferencia = Devolucion.count
        Devolucion.count += 1
        self._estado = "Pendiente"
        self._motivo = None
        self._factura = numerofactura
        Devolucion.Devoluciones.append(self)

    def getNombre(self):
        return super().getCliente().getNombre()

    def getCodigoReferencia(self):
        return self._codigoReferencia    

    def setEstado(self, nuevoEstado):
        self._estado = nuevoEstado

    def getEstado(self):
        return self._estado
    
    def setMotivo(self, texto):
        self._motivo = texto

    def getMotivo(self):
         return self._motivo
    
    def setFactura(self, codigo):
        factura = Factura.buscarFactura(codigo)
        self._factura = factura
    
    def getFactura(self):
        return self._factura
    
   
    def __str__(self):
        a = None

        if self.getEstado() == "Denegado": 
            a = "N° Solicitud: " + str(self.getCodigoReferencia()) + "\n" + "Cliente: " + super().getCliente().getNombre() + " - CC. " + super().getCliente().getId() + " - Email: " + super().getCliente().getEmail() + "\n" + "Estado de la solicitud:  " + self.getEstado()+ "\n" + "Motivo de rechazo: " + self.getMotivo() + "\n" + "La solicitud fue denegada, se enviara un correo al cliente con la decision tomada"
        
        elif self.getEstado() == "Aprobado":
            a = "N° Solicitud: " + str(self.getCodigoReferencia()) + "\n" + "Cliente: " + super().getCliente().getNombre() + " - CC. " + super().getCliente().getId() + " - Email: " + super().getCliente().getEmail() + "\n" + "Estado de la solicitud:  " + self.getEstado()+ "\n" + "La solicitud fue aprobada, se enviara un correo al cliente con la decision tomada y los pasos a seguir para hacer efectiva su solicitud"
        
        else: 
            a = "N° Solicitud: " + str(self.getCodigoReferencia()) + "\n" + "Cliente: " + super().getCliente().getNombre() + " - CC. " + super().getCliente().getId() + " - Email: " + super().getCliente().getEmail() + "\n" + "Codigo de Factura: " + str(self.getFactura()) + "\n" + "Estado de la solicitud:  " + self.getEstado()+ "\n" + "Motivo de la solicitud: " + super().getRazon()
        return a


    @classmethod
    def DenegarDevolucion(cls, codigo, motivo):
        a = cls.buscarDevolucion(codigo)
        a.setEstado("Denegado")
        a.setMotivo(motivo)

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
            if devolucion.getCodigoReferencia() == codigo:
                a = True
        
        return a
    
    @classmethod
    def buscarDevolucion(cls, codigo):
        c = cls.existeDevolucion(codigo)
        if c == True:
            b = cls.getDevoluciones()
            for devolucion in b:
                if devolucion.getCodigoReferencia() == codigo:
                    return devolucion
        else:
            return None
        
    
