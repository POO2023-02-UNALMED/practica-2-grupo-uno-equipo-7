import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gestorAplicacion.inventarioaply import Inventarioaply
from gestorAplicacion.Restaurante import Restaurante
dic= {"envigado":0, "sandiego":1, "La America": 2, "Belen":3}




class inventarioapp(tk.Frame):
    text=""
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.configure(background="white")

        label1 = tk.Label(self, text="Inventario", font=("Arial", 40), fg="pink")
        label1.grid(row=0, column=2, columnspan=2, pady=10)

        valor_defecto = tk.StringVar(value="Sedes")
        combo_style = ttk.Style()

        # Crea un nuevo estilo personalizado (My.TCombobox) y ajusta la altura (padding)
        combo_style.configure('My.TCombobox', padding=[20, 5, 90, 5])
        combo = ttk.Combobox(self, values=["envigado", "sandiego", "La America", "belen"], textvariable=valor_defecto,
                             style='My.TCombobox')
        combo.grid(row=1, column=1, padx=2, pady=10, sticky="w")

        otro_label = tk.Label(self, text="Seleccionar sede ", font=("Arial", 20), bg="white")
        otro_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        boton = tk.Button(self, text="Select", height=1, command=lambda: (self.inventario2(dic[combo.get()]), self.show(combo.get())))
        boton.grid(row=1, column=2, padx=2, sticky="w")
        nuevo_frame = tk.Frame(self)
        nuevo_frame.grid(row=2, column=0, columnspan=4, pady=10)
        

        # Agrega una etiqueta con el nombre de la sede
        
        
        # Crea un nuevo Frame para mostrar el nombre de la sede seleccionada
        
        
       
        
        

    def inventario2(self,  number):
        var1=Restaurante.get_sedes()[number].inventario.obtener_items_sin_stock()

        if len(Restaurante.get_sedes()[number].inventario.obtener_items_sin_stock()) == 0:
            message = "no hay items vencidos"
        else:
            message = ""
            for i in var1:
                message += var1.nombre
                
                
        inventarioapp.text = message
        
    
                
                
            
    def show(self, nombre_sede2):   
         messagebox.showinfo("Sede items", f"Sede seleccionada: {nombre_sede2} - {inventarioapp.text}")
       
        
        
        # Crea un nuevo Frame para mostrar el nombre de la sede seleccionada
        
        
    
        
        
        
        
        
        
        
        
       
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
    
    