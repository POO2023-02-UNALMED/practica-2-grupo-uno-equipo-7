# Se importan las librería a utilizar
from distutils import command
from tkinter import *
from tkinter import messagebox
#from gestionInterfaz.inventario import Inventario


class MenuPrincipal(Menu):
    
    #Se crea el método constructor
    def __init__(self, padre, controlador):
        # Se llama al padre (Menu), para que inicialice
        super().__init__(padre)
        
        # Atributos
        self._padre = padre
        self._controlador = controlador
        
        # Se crea la barra del menu con los submenus
        menuArchivos = Menu(self, tearoff=0)
        menuProcesos = Menu(self, tearoff=0)
        menuAyuda = Menu(self, tearoff=0)
        
        # se añaden los submenus a la barra del menu
        self.add_cascade(label="Archivo", menu=menuArchivos)
        self.add_cascade(label="Procesos y Consultas", menu=menuProcesos)
        self.add_cascade(label="Ayuda", menu=menuAyuda)
       
        
        self._values = {"tituloCriterios":"Atributos", "tituloValores":"Valores"}
        # Se crean los opciones de cada submenu
        
        # Para el caso del submenu Archivos
        menuArchivos.add_command(label="Aplicacion", command=self.informacionAplicativo)
        menuArchivos.add_command(label="Salir", command=self.salir)

        # Para el caso del submenu Procesos y Consultas
        menuProcesos.add_command(label="Gestionar Productos", command= self._gestionarVendedores)
        menuAyuda.add_command(label="Acerca de", command=self.quienesSomos)### Acá estoy, Andrés.....
        #menuProcesos.add_command(label="Gestion inventario", comnad= )## ya lo relleno- Andrés
        menuProcesos.add_command(label="gestion inventario", command= self.abrirInventario)
        
    def salir(self):
        self._controlador.deiconify()
        self._padre.destroy()
        
    def informacionAplicativo(self):
        messagebox.showinfo(
                title="Información Básica",
                message="Restaurante"
            )
        
    def quienesSomos(self):
        messagebox.showinfo(
                title="Autores",
                message="David \nManuel \n Andrés \n camila\nluan"
            )
        
    def _gestionarVendedores(self):
        self._values["criterios"] = ["ID","Nombre","Email","Fecha Registro", "Direccion"]
        self._values["habilitado"] = ["ID"]
        self._values["nombreProceso"] = "Plato mas vendido"
        self._values["descripcionProceso"] = "Muestra el plato preferido para el cliente basado en sus compras"
        from gestorAplicacion.Cliente import Cliente
        # obtener los IDs de los clientes y agregarlos a una lista de valores
        valores = []
        for cliente in Cliente.clientes:
            valores.append(cliente.id)
        self._values["objeto"] = Cliente
        self._values["valores"] = valores + [None]*(len(self._values["criterios"]) - len(self._values['habilitado']))
        self._values["atributos"] = ["ID","Nombre","Email","Fecha Registro", "Direccion"]
        self._padre.showFieldFrame(self._values)

        
    def abrirInventario(self):
        valores2=[]
        self._values["criterios"]=["Sedes"]

        from gestorAplicacion.Inventario import Inventario
        from gestorAplicacion.Restaurante import Restaurante 
        for i in range (4):
            valores2.append(Restaurante.sedes(i))
        
        
        
        self._values["objeto"]=Inventario
        self._padre.showFieldFrame(self._values)
        self._values["valores"]=valores2

        
        
    
