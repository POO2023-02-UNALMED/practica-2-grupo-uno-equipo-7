
class Pedido:
    listado_pedidos = []

    def __init__(self, numeroOrden: int, estadoPedido: str, direccionPedido: str, tipoPedido: str, cantidadPlatos: int, direccionPedido2: str):
        self.numeroOrden = numeroOrden
        self.estadoPedido = estadoPedido 
        self.direccionPedido  = direccionPedido 
        self.tipoPedido = tipoPedido
        self.cantidadPlatos =  cantidadPlatos
        self.direccionPedido2 =  direccionPedido2
        Pedido.listado_pedidos.append(self)

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

    def direccion(self, calle: str, casa: str, piso: int):
        self._casa = casa
        self._calle = calle
        self._piso = piso

    def MostrarRegistroPedidos(self):
        print("Numero del pedido: ", self.numeroOrden)
        print("Estado del pedido: ", self.estadoPedido)
        print("direccion del pedido: ", self.direccionPedido)
        print("tipo de pedido: ", self.tipoPedido)