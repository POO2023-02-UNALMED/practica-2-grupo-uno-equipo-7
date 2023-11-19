# Se importan las librería a utilizar
from distutils import command
from tkinter import *
from tkinter import messagebox
#from gestionInterfaz.inventario import Inventario
from GUI.gestionInterfaz.consultarPlatoPreferido import ConsultarPlatoPreferido
from GUI.gestionInterfaz.inventarioapp import inventarioapp
from GUI.gestionInterfaz.ConsultarPlatoRecomendado import ConsultarPlatoRecomendado
from GUI.gestionInterfaz.atencioncliente import AtencionCliente
from GUI.gestionInterfaz.OpcionesDePedios import OpcionesDePedidos
from GUI.gestionInterfaz.Reservaciones import Reservaciones
from GUI.gestionInterfaz.Fechasreserv import Fechasreserv



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
        menuProcesos.add_command(label="Consultar Plato Preferido", command= self.platoPreferido)
        menuProcesos.add_command(label="Consultar Plato Recomendado", command= self.platoRecomendado)
        menuProcesos.add_command(label="gestion inventario",command=self.abrirInventario)
        menuProcesos.add_command(label="Pedidos",command=self.abrirOpcionesPedidos)
        menuProcesos.add_command(label="Generar Reservaciones", command= self.GenerarReservaciones)
        menuProcesos.add_command(label="Atencion al cliente",command=self.abrirAtencionCliente)
        menuAyuda.add_command(label="Acerca de", command=self.quienesSomos)### Acá estoy, Andrés.....
        #menuProcesos.add_command(label="Gestion inventario", comnad= )## ya lo relleno- Andrés
        
        
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
                message="David \nManuel \nAndrés \nCamila \nMaria"
            )
        
    def _gestionarVendedores(self):
        self._values["criterios"] = ["ID","Nombre","Email","Fecha Registro", "Direccion"]
        self._values["habilitado"] = ["Nombre","Email","Fecha Registro", "Direccion"]
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
        self._padre.mostrarFuncionalidades(inventarioapp)
        
    def abrirAtencionCliente(self):
        self._padre.mostrarFuncionalidades(AtencionCliente)
    
    def abrirOpcionesPedidos(self):
        self._padre.mostrarFuncionalidades(OpcionesDePedidos)

    def platoPreferido(self):
        self._padre.mostrarFuncionalidades(ConsultarPlatoPreferido)

    def platoRecomendado(self):
        self._padre.mostrarFuncionalidades(ConsultarPlatoRecomendado)
        
    def GenerarReservaciones(self):
        self._padre.mostrarFuncionalidades(Fechasreserv)


