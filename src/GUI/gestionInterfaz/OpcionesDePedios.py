from tkinter import *
from GUI.estilos.style import *
from tkinter import messagebox
from gestorAplicacion.Pedido import Pedido








##Ventanas terciarias
class VentanadePedidos(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Nuevo Pedido")
        self.configure(background=BACKGROUND_CONTENEDOR)


    def mostrar_detalle_platillo(codigo):
        # Esta función se llama cuando se selecciona un platillo en el menú
        platillo = menu_platillos[codigo]
        detalle = f"Código: {codigo}\nPlatillo: {platillo['nombre']}\nPrecio: ${platillo['precio']:.2f}"

        # Actualizar la etiqueta de detalles con la información del platillo seleccionado
        etiqueta_detalles.config(text=detalle)

    # Definir el menú de platillos con códigos, nombres y precios
    menu_platillos = {
        '001': {'nombre': 'Hamburguesa', 'precio': 8.99},
        '002': {'nombre': 'Pizza', 'precio': 10.50},
        '003': {'nombre': 'Ensalada', 'precio': 5.99},}
        # Agrega más platillos según sea necesario

class VentanaDeOpcionesAdmin(Toplevel):
    def __init__(self, ventana, pedidos):
        self.ventana = ventana
        self.ventana.title("Reporte de Pedidos")

        # Crear una etiqueta para mostrar el reporte de pedidos
        self.etiqueta_reporte = tk.Label(ventana, text="Reporte de Pedidos", font=("Helvetica", 16))
        self.etiqueta_reporte.pack(pady=10)

        # Crear un cuadro de texto para mostrar los detalles de los pedidos
        self.texto_pedidos = tk.Text(ventana, height=10, width=40)
        self.texto_pedidos.pack()

        # Mostrar los detalles de los pedidos en el cuadro de texto
        self.mostrar_reporte_pedidos(pedidos)

    def mostrar_reporte_pedidos(self, pedidos):
        for pedido in pedidos:
            detalle_pedido = f"Pedido #{pedido['numero']}\n"
            for platillo, cantidad in pedido['detalle'].items():
                detalle_pedido += f"{platillo}: {cantidad} unidades\n"
            detalle_pedido += f"Total: ${pedido['total']:.2f}\n\n"
            self.texto_pedidos.insert(tk.END, detalle_pedido)

##Ventanas secundarias
class OpcionesdeAdmin(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Nuevo Pedido")
        self.configure(background=BACKGROUND_CONTENEDOR)
        
                             
        # Etiqueta y entrada para la sugerencia
        label_Nombre = Label(self, text="Usuario: ", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        label_Nombre.pack(side=TOP, pady=5)

        self.entry_Nombre = Entry(self, width=30)
        self.entry_Nombre.pack(side=TOP, pady=5)

        label_Iden = Label(self, text="Contraseña:", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        label_Iden.pack(side=TOP, pady=5)

        self.entry_Iden = Entry(self, width=30)
        self.entry_Iden.pack(side=TOP, pady=5)

        opciones_tipo = ["De envio", "Para recoger"]
        self.var_tipo = StringVar(self)
        self.var_tipo.set(opciones_tipo[1])  # Establecer el valor predeterminado
        menu_tipo = OptionMenu(self, self.var_tipo, *opciones_tipo)
        menu_tipo.pack(side=TOP, pady=5)
    
        

        # Botón para guardar la sugerencia
        boton_guardar = Button(self, text="Guardar", command=self.MostrarVentanaAdmin,bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        boton_guardar.pack(side=TOP, pady=10)

    def MostrarVentanaAdmin(self):
        ventana = VentanaDeOpcionesAdmin(self)
        nombre = self.entry_Nombre.get()
        Identificacion = self.entry_Iden.get()
        direccion = self.entry_Direccion.get()
        tipo = self.var_tipo.get()
        # Aquí puedes realizar acciones con el tipo y la sugerencia, como guardar en una base de datos, etc.
        pedido = Pedido(nombre, Identificacion, direccion, tipo)
        print(pedido)
class NuevoPedido(Toplevel):

    
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Nuevo Pedido")
        self.configure(background=BACKGROUND_CONTENEDOR)
        
                             
        # Etiqueta y entrada para la sugerencia
        label_Nombre = Label(self, text="Nombre: ", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        label_Nombre.pack(side=TOP, pady=5)

        self.entry_Nombre = Entry(self, width=30)
        self.entry_Nombre.pack(side=TOP, pady=5)

        label_Iden = Label(self, text="Identificación:", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        label_Iden.pack(side=TOP, pady=5)

        self.entry_Iden = Entry(self, width=30)
        self.entry_Iden.pack(side=TOP, pady=5)

        label_Direccion = Label(self, text="Direccion:", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        label_Direccion.pack(side=TOP, pady=5)

        self.entry_Direccion = Entry(self, width=30)
        self.entry_Direccion.pack(side=TOP, pady=5)

        opciones_tipo = ["De envio", "Para recoger"]
        self.var_tipo = StringVar(self)
        self.var_tipo.set(opciones_tipo[1])  # Establecer el valor predeterminado
        menu_tipo = OptionMenu(self, self.var_tipo, *opciones_tipo)
        menu_tipo.pack(side=TOP, pady=5)
    
        

        # Botón para guardar la sugerencia
        boton_guardar = Button(self, text="Guardar", command=self.MostrarMenu,bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        boton_guardar.pack(side=TOP, pady=10)

    
    
    def MostrarMenu(self):
        ventana = VentanadePedidos(self)
        nombre = self.entry_Nombre.get()
        Identificacion = self.entry_Iden.get()
        direccion = self.entry_Direccion.get()
        tipo = self.var_tipo.get()
        # Aquí puedes realizar acciones con el tipo y la sugerencia, como guardar en una base de datos, etc.
        pedido = Pedido(nombre, Identificacion, direccion, tipo)
        print(pedido)

    
#Ventana Inicial
class OpcionesDePedidos(Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.configure(background=BACKGROUND_CONTENEDOR)
        self._controlador = controlador
        
        self._inicializarTitulo()
        self._Boton1()
        self._Boton2()
        
        
        
    def _inicializarTitulo(self):    
        # Se inicializa el título  que va a estar en la parte superior de la ventana
        labelInicial = Label(self, justify=CENTER, text="Bienvenido al apartado de pedidos", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        labelFinal = Label(self, justify=CENTER, text="¿Que desea hacer?", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelFinal.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
    def _Boton1(self):
        # Se inicializa el botón para mostrar el nombre y plato preferido del cliente
        botonMostrar = Button(self, text="Ordenar un Pedido", command= self.nPedido, font=FONT2, fg="green")
        botonMostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _Boton2(self):
        # Se inicializa el botón para mostrar el nombre y plato preferido del cliente
        botonMostrar = Button(self, text="Opciones de administrador", command=self.mostrar, font=FONT2, fg="green")
        botonMostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def nPedido(self):
        ventana = NuevoPedido(self)
    
    def mostrar(self):
        ventana = OpcionesdeAdmin(self)
    

#terminado de momento..... faltan los comands
