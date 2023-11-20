import tkinter as tk
from tkinter import ttk
from gestorAplicacion.Restaurante import Restaurante
from gestorAplicacion.Item import Item

class k:
    def __init__(self, ventana, num):
        
        self.ventana = ventana
        self.num=num
        

        self.tool_bar = ttk.Frame(self.ventana, padding="10")
        self.tool_bar.pack(side="top", fill="x")

        self.btn_1 = ttk.Button(self.tool_bar, text="1. Mostrar inventario", command=self.mostrar_inventario)
        self.btn_1.pack(side="left")

        self.btn_2 = ttk.Button(self.tool_bar, text="2. Precio articulo inventario", command=self.precio_articulo_inventario)
        self.btn_2.pack(side="left")

        self.btn_3 = ttk.Button(self.tool_bar, text="3. Revisar niveles de Stock", command=self.revisar_niveles_de_stock)
        self.btn_3.pack(side="left")

        self.btn_4 = ttk.Button(self.tool_bar, text="4. Registrar artículo en inventario", command=self.registrar_articulo_en_inventario)
        self.btn_4.pack(side="left")

        self.btn_5 = ttk.Button(self.tool_bar, text="5. Renovar inventario", command=self.renovar_inventario)
        self.btn_5.pack(side="left")

        self.btn_6 = ttk.Button(self.tool_bar, text="6. Valor del inventario total", command=self.valor_del_inventario_total)
        self.btn_6.pack(side="left")

        self.btn_7 = ttk.Button(self.tool_bar, text="7. Salir", command=self.salir)
        self.btn_7.pack(side="left")
        self.lbl_descripcion=ttk.Label(self.ventana, text="Descripcion", padding="10",font=("Arial", 28, "bold") )
        self.lbl_descripcion.pack(side="top",  fill="x", pady=20, padx=200)

        self.lbl_informacion = ttk.Label(self.ventana, text="Información del inventario", padding="10")
        self.lbl_informacion.pack(side="top", fill="x")
        ## new frame
        self.frame_inf=ttk.Frame(self.ventana,padding="10")
        self.frame_inf.pack(side="top", fill="x", pady="0", anchor="n")
        
        

    def mostrar_inventario(self):
        self.lbl_descripcion.config(text="Acá se muestra el inventario actualizado y listo")
        listaRepetidos=[]
        text1=Restaurante.get_sedes()[self.num].ubicacion
        for i in Restaurante.get_sedes()[self.num].inventario.listado_items:
            listaRepetidos.append(i)
            text1+="\n"+ i.nombre +" "+ " "+str(i.cantidad)+" " + " " + str(i.fecha_vencimiento)
            
        self.lbl_informacion.config(text=text1)
        

    def precio_articulo_inventario(self):
        self.lbl_descripcion.config(text="Busqueda de precio de articulo especifico")
        
   # crear etiquetas 
        etiqueta_criterio = ttk.Label(self.frame_inf, text="Criterio")
        etiqueta_valor = ttk.Label(self.frame_inf, text="Valor")
        etiqueta_numero = ttk.Label(self.frame_inf, text="Código")
        etiqueta_nombre = ttk.Label(self.frame_inf, text="Nombre")

# Crear barras de texto
        codigo_entry = ttk.Entry(self.frame_inf, width=100)
        nombre_entry = ttk.Entry(self.frame_inf, width=100)
        codigo_entry.place(x=10, y=40, width=200, height=100)


# Crear botones
        boton_aceptar = ttk.Button(self.frame_inf, text="Aceptar", command= self.show_articulo(codigo_entry.get(), nombre_entry.get(), Restaurante.sedes[self.num].inventario.listado_items))
        boton_borrar = ttk.Button(self.frame_inf, text="Borrar")
    

# Organizar widgets usando grid
        etiqueta_criterio.grid(row=0, column=2, pady=5, sticky="w")
        etiqueta_valor.grid(row=0, column=3, pady=5, sticky="w")
        codigo_entry.grid(row=1, column=3, padx=5, pady=5, sticky="ew")
        nombre_entry.grid(row=2, column=3, padx=5, pady=5, sticky="ew")
        boton_aceptar.grid(row=5, column=2, columnspan=1, pady=10, sticky="ew")
        boton_borrar.grid(row=5, column=3, columnspan=1, pady=5, sticky="ew")
        etiqueta_numero.grid(row=1, column=2, pady=5, sticky="w")
        etiqueta_nombre.grid(row=2, column=2, pady=5, sticky="w")
        self.lbl_informacion.config(text="Precio del artículo en el inventario")
        
        
        
    def show_articulo(self, num, nombre,listaItems):
        item=Item.buscar_item(nombre, listaItems)
        
        if item==None:
            label_precio= ttk.Label( self.frame_inf, text= "Items no encontrados" )
            label_precio.grid(row=0, column=4, rowspan= 3, columnspan=2)
            
        else:
            label_precio= ttk.Label(self.frame_inf,text= item.nombre + " "+ "Precio"+ str(item.cantidad)+ " X "+ str(num)+ "  =  "+  str(item.cantidad*num) )
            label_precio.grid(row=0, column=4, rowspan= 3, columnspan=2)
            
        
        
        
        

    def revisar_niveles_de_stock(self):
        self.lbl_informacion.config(text="Niveles de stock del inventario")

    def registrar_articulo_en_inventario(self):
        self.lbl_informacion.config(text="Registrar artículo en el inventario")

    def renovar_inventario(self):
        self.lbl_informacion.config(text="Renovar inventario")

    def valor_del_inventario_total(self):
        self.lbl_informacion.config(text="Valor total del inventario")

    def salir(self):
        self.ventana.destroy()

# Iniciar la aplicación


