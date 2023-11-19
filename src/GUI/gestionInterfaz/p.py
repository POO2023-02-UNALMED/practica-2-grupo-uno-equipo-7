import tkinter as tk
from tkinter import ttk


class k:
    def __init__(self, ventana):
        self.ventana = ventana
        

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

        self.lbl_informacion = ttk.Label(self.ventana, text="Información del inventario", padding="10")
        self.lbl_informacion.pack(side="top", fill="x")

    def mostrar_inventario(self):
        self.lbl_informacion.config(text="Información del inventario")

    def precio_articulo_inventario(self):
        self.lbl_informacion.config(text="Precio del artículo en el inventario")

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


