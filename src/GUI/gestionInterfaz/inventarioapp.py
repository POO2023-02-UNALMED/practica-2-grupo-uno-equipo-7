import tkinter as tk
from tkinter import messagebox
from tkinter import Frame
from tkinter import ttk

class inventarioapp(Frame):
    def __init__(self, padre,  controlador):
        super().__init__(padre)
        self.controlador=controlador
        self.configure(background="white")
        label1=tk.Label(self, text="Inventario", font=("Arial",35),fg="pink")
        label1.pack(side="top", pady=10)
        valor_defecto=tk.StringVar(value="Sedes")
        combo=ttk.Combobox(self, values=["envigado","sandiego","La Amercia", "belen"], textvariable=valor_defecto)
        combo.pack(side="bottom")
        
        
        
        
        
        
    
    