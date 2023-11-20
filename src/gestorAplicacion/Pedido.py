from .Factura import Factura
from .Plato import Plato
from .Item import Item
from .Cliente import Cliente
class Pedido:
    listado_pedidos = []
    count = 1
    def __init__(self, nombre: str, identificacion:int, direccionPedido: str, tipoPedido: str ):
        self._cliente = Cliente(nombre, identificacion, direccionPedido)
        self._nombre = nombre
        self._identificacion = identificacion
        self._estadoPedido = "En espera" 
        self._direccionPedido  = direccionPedido 
        self._tipoPedido = tipoPedido
        self._cantidadPlatos = 1
        self._numeroOrden = Pedido.count
        Pedido.count += 1
        Pedido.listado_pedidos.append(self)

    def getEstatoPedido(self):
        return self._estadoPedido
    def setEstadoPedido(self,estadopedido):
        self._estadoPedido = estadopedido
    def getTipoPedido(self):
        return self._tipoPedido
    def setTipoPedido(self, tipopedido):
        self._tipoPedido = tipopedido
    def getCantidadPlatos(self):
        return self._cantidadPlatos
    def setCantidadPlatos(self, cantidadPlatos):
        self._cantidadPlatos = cantidadPlatos
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    def setDireccion(self, direccion):
        self._direccionPedido = direccion
    def getNumOrden(self):
        return self._numeroOrden
    def getIdentificacion(self):
        return self._identificacion
    def setIdentificacion(self, identificacion):
        self._identificacion = identificacion
    def getDirPedido(self):
        return self._direccionPedido
    
    def mostrarListPedidos(self):
        return Pedido.listado_pedidos
        #aquí se podria mostrar los pedidos anteriores, el estado, su dirección, el codigo del pedido, el monto total, etc.

    
    def GenerarPedido(self):
        if self.tipoPedido == "De envio":
            print("Ha seleccionado la opción de envio, por favor, digite a continuación su nombre y apellido")
            self.tomarNombre
            print("Ha continuación, por favor, digitar su dirección de residensia")
            self.direccion
            print("¿Desea confirmar su dirección de residencia?")
            
        else:
            print("Ha seleccionado la opción de recoger en sede, por favor, digite a continuación su nombre y apellido")
            self.tomarNombre
            print("Ha continuación, por favor, digitar la sede donde desea recoger su pedido")

    def tomarNombre(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    def Direccion(self, calle: str, casa: str, piso: int):
        self._casa = casa
        self._calle = calle
        self._piso = piso

    def PrecioTotal():
        precioTotal = int
        #for plato in platos:
        #    precioTotal = plato.getprecio()
        return precioTotal
    
    def __str__(self):
        return "Numero del pedido: "+ str(self.getNumOrden()) + "\n" + "Estado del pedido: "+ self.getEstatoPedido() +"\n" + "direccion del pedido: "+ self.getDirPedido() + "\n" +"tipo de pedido: "+ self.getTipoPedido()

