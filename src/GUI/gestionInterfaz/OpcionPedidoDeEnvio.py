from tkinter import *
from GUI.estilos.style import *
from gestorAplicacion.Pedido import Pedido
from tkinter import messagebox

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
        boton_guardar = Button(self, text="Guardar", command=self.confirmar_guardar_sugerencia,bg=BACKGROUND_FRAMES, font=FONT, fg=FG)
        boton_guardar.pack(side=TOP, pady=10)

    
    
    def confirmar_guardar_sugerencia(self):
        nombre = self.entry_Nombre.get()
        Idenificacion = self.entry_Iden.get()
        direccion = self.entry_Direccion.get()
        tipo = self.var_tipo.get()
        # Aquí puedes realizar acciones con el tipo y la sugerencia, como guardar en una base de datos, etc.
        pedido = Pedido(nombre, int(Idenificacion), direccion, tipo)
        print(pedido)





    
