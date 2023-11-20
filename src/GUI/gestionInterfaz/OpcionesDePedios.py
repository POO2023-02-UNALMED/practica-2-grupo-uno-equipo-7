from tkinter import *
from GUI.estilos.style import *
from tkinter import messagebox
from gestorAplicacion.Pedido import Pedido
from gestorAplicacion.Empleado import Empleado
from gestorAplicacion.Plato import Plato
from baseDatos import Deserializador
from baseDatos import Serializador



##Ventanas Finales
class MostrarVentanaFinal(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Ventana de confirmación")
        self.configure(background=BACKGROUND_CONTENEDOR)
        labelInicial = Label(self, justify=CENTER, text="Pedido Confirmado", bg=BACKGROUND_FRAMES, font=FONT2, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)
    
        labelInicial = Label(self, justify=CENTER, text="Su pedido esta en camino o lo espera para ser recogido", bg=BACKGROUND_FRAMES, font=FONT2, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        labelInicial = Label(self, justify=CENTER, text="Gracias por comprar en el restaurante de Toño", bg=BACKGROUND_FRAMES, font=FONT2, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)

##Ventanas semifinales
class VentanaConfir(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Ventana de confirmación")
        self.configure(background=BACKGROUND_CONTENEDOR)
        labelInicial = Label(self, justify=CENTER, text="¿Desea confirmar su pedido?", bg=BACKGROUND_FRAMES, font=FONT2, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        # Botón para confirmar el pedido
        boton_guardar = Button(self, text="Confirmar", command=self.VentanaFin,bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        boton_guardar.pack(side=TOP, pady=10)

        # Botón para no confirmar el pedido
        boton_guardar = Button(self, text="No confirmar", command=self.MostrarMenu,bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        boton_guardar.pack(side=TOP, pady=10)

    def MostrarMenu(self):
        ventana = VentanadePedidos(self)
    def VentanaFin(self):
        ventana = MostrarVentanaFinal(self)

##Ventanas terciarias
class VentanadePedidos(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Menu Disponible")
        self.configure(background=BACKGROUND_CONTENEDOR)
        labelInicial = Label(self, justify=CENTER, text="Menu Disponible", bg=BACKGROUND_FRAMES, font=FONT2, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    # Definir el menú de platillos con códigos, nombres y precios
        
        plato1 = Label(self,justify=CENTER, text="Taco 1000", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        plato1.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        #precio1 = Label(self, justify=CENTER, text="1000", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        #precio1.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        plato2 = Label(self, justify=CENTER, text="Tostada 1000", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        plato2.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        #precio2 = Label(self, justify=CENTER, text="2000", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        #precio2.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        plato3 = Label(self, justify=CENTER, text="Sope 1000", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        plato3.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        #precio3 = Label(self, justify=CENTER,text="3000", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        #precio3.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        plato4 = Label(self, justify=CENTER, text="Enchilada 1000", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        plato4.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        #precio4 = Label(self, justify=CENTER, text="4000", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        #precio4.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        plato5 = Label(self, justify=CENTER, text="Quesadilla 1000", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        plato5.pack(side=TOP, fill=BOTH, padx=5, pady=5)
        #precio5 =Label(self, justify=CENTER, text="5000", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        #precio5.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        # Aquí van los espacios de respuesta

        labelFinal = Label(self, justify=CENTER, text="¿Cuantos platos desea ordenar?", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelFinal.pack(side=TOP, pady=5)
        self.entry_Cantidad_Platos = Entry(self, width=30)
        self.entry_Cantidad_Platos.pack(side=TOP, pady=5)

        labelFinal2 = Label(self, justify=CENTER, text="¿Que desea ordenar?", bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        labelFinal2.pack(side=TOP, pady=5)
        self.entry_Nombres_platos = Entry(self, width=30)
        self.entry_Nombres_platos.pack(side=TOP, pady=5)

        # Botón para guardar la sugerencia
        boton_guardar = Button(self, text="Guardar", command=self.ventanaconfir,bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        boton_guardar.pack(side=TOP, pady=10)

    def ventanaconfir(self):
        ventana = VentanaConfir(self)
class VentanaDeOpcionesAdmin(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Opciones de Administrador")
        self.configure(background=BACKGROUND_CONTENEDOR)
        labelInicial = Label(self, justify=CENTER, text="Apartado de opciones de administrador", bg=BACKGROUND_FRAMES, font=FONT2, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
    #Metodo para mostrar los datos de los pedidos actuales
        labelInicial = Label(self, justify=CENTER, text="Las ventas totales por pedidos son: ", bg=BACKGROUND_FRAMES, font=FONT2, fg=FG)
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
        Button(self, text="Mostrar Pedidos Totales", command=self.mostrarPedidosTotales, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a").pack()
        self.resultado_text = Text(self, height=10, width=50, wrap='word', bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        self.resultado_text.pack(side='top', fill='both', padx=10, pady=10)
    
    def mostrarPedidosTotales(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        a = Deserializador.PedidosT()
        for resultado in a:
            self.mostrar_resultado(str(resultado))
            self.mostrar_resultado("\n")

    def mostrar_resultado(self, resultado):
        # Insertar el resultado en la última línea del área de texto
        self.resultado_text.insert('end', resultado + '\n')
        # Desplazar la vista de la caja de texto para mostrar la última línea
        self.resultado_text.see('end')
    #

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
        label_Usuario = Label(self, text="Usuario: ", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        label_Usuario.pack(side=TOP, pady=5)

        self.entry_Usuario = Entry(self, width=30)
        self.entry_Usuario.pack(side=TOP, pady=5)

        label_Contraseña = Label(self, text="Contraseña:", bg=BACKGROUND_CONTENEDOR, font=FONT2, fg=FG)
        label_Contraseña.pack(side=TOP, pady=5)
        

        self.entry_Contraseña = Entry(self, width=30)
        self.entry_Contraseña.pack(side=TOP, pady=5)    
        

        # Botón para verificar el código
        Button(self, text="Verificar", command=self.verificar_codigo, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a").pack()

    def verificar_codigo(self):
        codigo_empleado = self.entry_Usuario.get()
        contr = self.entry_Contraseña.get()
        ver = Empleado.buscarEmpleadoXCodigo(codigo_empleado)
        # Verificar aquí si el código de empleado es válido
        if ver != None and contr == "Admin":  
            ventana = VentanaDeOpcionesAdmin(self)

        else:
            # Muestra un mensaje de error o realiza alguna acción según tu lógica
            print("Los datos no estan registrados")
            
    
    def MostrarVentanaAdmin(self):
        ventana = VentanaDeOpcionesAdmin(self)
        #nombre = self.entry_U.get()
        #Identificacion = self.entry_Iden.get()
        #direccion = self.entry_Direccion.get()
        #tipo = self.var_tipo.get()
        # Aquí puedes realizar acciones con el tipo y la sugerencia, como guardar en una base de datos, etc.
        ##print(pedido)
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

    def registropedido(self):
        nombre = self.entry_Nombre
        Identificacion = self.entry_Iden
        direccion = self.entry_Direccion
        tipo = self.var_tipo.get()
        try: 
            nombre == " "
            Identificacion == ""
            direccion == " "
        
        except:
            messagebox.showerror("Error", "Por favor, rellene todos los campos requeridos")
            return
        
    
    
    def MostrarMenu(self):
        ventana = VentanadePedidos(self)
    def registropedido(self):
        nombre = self.entry_Nombre.get()
        Identificacion = self.entry_Iden.get()
        direccion = self.entry_Direccion.get()
        tipo = self.var_tipo.get()
        # Aquí puedes realizar acciones con el tipo y la sugerencia, como guardar en una base de datos, etc.
        pedido = Pedido(nombre, Identificacion, direccion, tipo)
        Serializador.AgregarNuevoPedido(pedido)
        
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
