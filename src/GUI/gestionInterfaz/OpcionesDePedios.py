from tkinter import *
from GUI.estilos.style import *
from tkinter import messagebox
from gestorAplicacion.Pedido import Pedido
from gestorAplicacion.Empleado import Empleado
from gestorAplicacion.Plato import Plato






##Ventanas terciarias
class VentanadePedidos(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Menu Disponible")
        self.configure(background=BACKGROUND_CONTENEDOR)
        labelInicial = Label(self, justify=CENTER, text="Menu Disponible", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        labelFinal = Label(self, justify=CENTER, text="¿Que desea Ordenar?", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelFinal.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    # Definir el menú de platillos con códigos, nombres y precios
        
        plato1 = Label(self,justify=CENTER, text="Taco", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        plato1.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        precio1 = Label(self, justify=CENTER, text="1000", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        precio1.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        plato2 = Label(self, justify=CENTER, text="Tostada", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        plato2.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        precio2 = Label(self, justify=CENTER, text="2000", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        precio2.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        plato3 = Label(self, justify=CENTER, text="Sope", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        plato3.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        precio3 = Label(self, justify=CENTER,text="3000", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        precio3.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        plato4 = Label(self, justify=CENTER, text="Enchilada", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        plato4.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        precio4 = Label(self, justify=CENTER, text="4000", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        precio4.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        plato5 = Label(self, justify=CENTER, text="Quesadilla", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        plato5.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        precio5 =Label(self, justify=CENTER, text="5000", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        precio5.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        # Agrega más platillos según sea necesario
class VentanaDeOpcionesAdmin(Toplevel):
    ##Mostrar los pedidos guardados hasta el momento
    def ventanaDePedidosRegistrados(self):
        ventana = Pedido.listado_pedidos(self)

##Ventanas secundarias
class OpcionesdeAdmin(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Opciones de Administrador")
        self.configure(background=BACKGROUND_CONTENEDOR)

        #Bienvenida inicial
        labelInicial = Label(self, justify=CENTER, text="Bienvenido al apartado de Opciones de administrador", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        labelFinal = Label(self, justify=CENTER, text="Por favor, ingrese el usuario y contraseña", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelFinal.pack(side=TOP, fill=BOTH, padx=10, pady=10)
                             
        # Etiqueta y entrada para la sugerencia
        label_Nombre = Label(self, text="Usuario: ", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        label_Nombre.pack(side=TOP, pady=5)

        self.entry_Nombre = Entry(self, width=30)
        self.entry_Nombre.pack(side=TOP, pady=5)

        label_Iden = Label(self, text="Contraseña:", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        label_Iden.pack(side=TOP, pady=5)
        

        self.entry_Iden = Entry(self, width=30)
        self.entry_Iden.pack(side=TOP, pady=5)    
        
        # Botón para guardar la sugerencia
        boton_guardar = Button(self, text="Guardar", command=self.MostrarVentanaAdmin,bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        boton_guardar.pack(side=TOP, pady=10)

    # Botón para verificar el código
        Button(self, text="Verificar", command=self.verificar_codigo, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a").pack()

    def verificar_codigo(self):
        codigo_empleado = self.entry_codigo.get()

        ver = Empleado.buscarEmpleadoXCodigo(codigo_empleado)
        # Verificar aquí si el código de empleado es válido
        if ver != None:  
            self.abrir_ReportesQuejas()

        else:
            # Muestra un mensaje de error o realiza alguna acción según tu lógica
            print("Código de empleado no válido")
    def abrir_ReportesQuejas(self):
        ventana = ReportesQuejas(self)
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
        labelInicial = Label(self, justify=CENTER, text="Nuevo Pedido", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        labelFinal = Label(self, justify=CENTER, text="Por favor, ingrese los datos solicitados", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelFinal.pack(side=TOP, fill=BOTH, padx=10, pady=10)
                             
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
