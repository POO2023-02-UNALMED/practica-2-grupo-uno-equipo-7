from .Factura import Factura
from .Plato import Plato
from .Item import Item
class Pedido:
    listado_pedidos = []

    def __init__(self, numeroOrden: int, estadoPedido: str, direccionPedido: str, tipoPedido: str, cantidadPlatos: int, direccionPedido2: str):
        self._numeroOrden = numeroOrden
        self._estadoPedido = estadoPedido 
        self._direccionPedido  = direccionPedido 
        self._tipoPedido = tipoPedido
        self._cantidadPlatos =  cantidadPlatos
        self._direccionPedido2 =  direccionPedido2
        Pedido._listado_pedidos.append(self)

    def MostrarNumOrden(self):
        return self._numeroOrden
    def mostrarEstPedido(self):
        return self._estadoPedido
    def mostrarDirPedido(self):
        return self._direccionPedido
    def mostrarCantPlatos(self):
        return self._cantidadPlatos
    def mostrarListPedidos(self):
        return 
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
    
    def MostrarRegistroPedidos(self):
        print("Numero del pedido: ", self.numeroOrden)
        print("Estado del pedido: ", self.estadoPedido)
        print("direccion del pedido: ", self.direccionPedido)
        print("tipo de pedido: ", self.tipoPedido)