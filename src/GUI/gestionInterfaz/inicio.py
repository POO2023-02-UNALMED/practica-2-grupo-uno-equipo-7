from tkinter import *
import os
import pathlib
path = os.path.join(pathlib.Path(__file__).parent.absolute())
path = os.path.dirname(path)
from GUI.estilos import style
from PIL import Image, Image, ImageTk
from GUI.gestionInterfaz.principal import Principal

class Inicio(Frame, Tk):
    """ Clase encargada de cargar los frames y widgets que utilizará la ventana de inicio
        """

    # Acá guardamos los datos de los desarrolladores para utilizarlos en la implementación
    VALUES  = [
        {"name": "David Alejandro Silva Uribe", "description":"Amante del fútbol y el arte", "email":"dsilvau@unal.edu.co"},
        {"name": "Andrés Felipe Guido Montoya", "description":"Apasionado por el fútbol y el anime", "email":"aguido@unal.edu.co" },
        {"name":"Maria Camila Rios Mejia", "description":"Apasionada por el baile, los comics y los videojuegos", "email":"mriosm@unal.edu.co"},
        {"name": "Manuel Fernando Menza Perdomo", "description":"Amante de la Formula 1 y el automivilismo", "email":"mmenza@unal.edu.co" },
        {"name":"", "description":"Apasionado por la lectura", "email":"jtobonz@unal.edu.co"}
    ]

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.configure(background = style.BACKGROUND_CONTENEDOR)
        self.controlador = controlador
        # numer inicio para tener referencia y control de los datos de los desarrolladores
        self._numeroInicio = 0
        # numero para tener control de las imagenes que se muestran del sistema
        self._numeroImagenesSistema = 0
        self.inicializarFrames()
    
    def cambiarImagenesSistema(self, e=None):
        """ Función encargada de cambiar las imagenes que se muestran del sistema a momento de mover el mouse
            sobre las imagenes"""

        
        self._numeroImagenesSistema += 1
        # Como solo son 5 imagenes
        self._numeroImagenesSistema %= 5

        # Condiciones para mostrar cada una de las imagenes del sistema
        if self._numeroImagenesSistema == 0:
            imagen_sistema = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/s1.png').resize((300,225), Image.ANTIALIAS))
        elif self._numeroImagenesSistema == 1:
            imagen_sistema = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/sistema1.jpeg').resize((300,225), Image.ANTIALIAS))
        elif self._numeroImagenesSistema == 2:
            imagen_sistema = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/sistema1.jpeg').resize((300,225), Image.ANTIALIAS))
        elif self._numeroImagenesSistema == 3:
            imagen_sistema = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/sistema1.jpeg').resize((300,225), Image.ANTIALIAS))
        else :
            imagen_sistema = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/sistema1.jpeg').resize((300,225), Image.ANTIALIAS))

        # cambiar la imagen en el label
        self.imagenesSistema.image = imagen_sistema
        self.imagenesSistema.configure(image = imagen_sistema)
    
    def cambiarInfoDesarrolladores(self, e=None):
        """ Funcion encargada de cambiar la infomacion y las imagenes de los desarroladors '
            cuando se da click en la información"""

        self._numeroInicio += 1
        # Como solo son 3 desarroladores para se repita en ciclo
        #¿no somos 5?
        self._numeroInicio %= 5

        nuevos_valores = self.VALUES[self._numeroInicio]

        # Se cambian los label con los datos del respectivo desarrollador
        self._nombre.config(text= nuevos_valores["name"])
        self._descripcioncita.config(text=nuevos_valores["description"])
        self._correo.config(text=nuevos_valores["email"])

        # Condicionales para configurar las 4 imagenes de cada desarrollador
        if self._numeroInicio == 0 :
            python_imagen1 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/d1.jpg').resize((300,300), Image.ANTIALIAS))
            self.imagen1.image = python_imagen1
            self.imagen1.configure(image = python_imagen1)

            python_imagen2 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/d2.jpg').resize((300,300), Image.ANTIALIAS))
            self.imagen2.image = python_imagen2
            self.imagen2.configure(image = python_imagen2)

            python_imagen3 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/d3.jpg').resize((300,300), Image.ANTIALIAS))
            self.imagen3.image = python_imagen3
            self.imagen3.configure(image = python_imagen3)

            python_imagen4 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/d4.jpg').resize((300,300), Image.ANTIALIAS))
            self.imagen4.image = python_imagen4
            self.imagen4.configure(image = python_imagen4)

        elif self._numeroInicio == 1:
            python_imagen1 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/maestro.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen1.image = python_imagen1
            self.imagen1.configure(image = python_imagen1)

            python_imagen2 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/maestro.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen2.image = python_imagen2
            self.imagen2.configure(image = python_imagen2)

            python_imagen3 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/maestro.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen3.image = python_imagen3
            self.imagen3.configure(image = python_imagen3)

            python_imagen4 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/maestro.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen4.image = python_imagen4
            self.imagen4.configure(image = python_imagen4)

        elif self._numeroInicio == 2: #Camila
            python_imagen1 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/c1.jpg').resize((300,225), Image.ANTIALIAS))
            self.imagen1.image = python_imagen1
            self.imagen1.configure(image = python_imagen1)

            python_imagen2 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/c2.jpg').resize((300,225), Image.ANTIALIAS))
            self.imagen2.image = python_imagen2
            self.imagen2.configure(image = python_imagen2)

            python_imagen3 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/c3.jpg').resize((300,225), Image.ANTIALIAS))
            self.imagen3.image = python_imagen3
            self.imagen3.configure(image = python_imagen3)

            python_imagen4 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/c4.jpg').resize((300,225), Image.ANTIALIAS))
            self.imagen4.image = python_imagen4
            self.imagen4.configure(image = python_imagen4)
            
        elif self._numeroInicio == 3:
            python_imagen1 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/sistema1.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen1.image = python_imagen1
            self.imagen1.configure(image = python_imagen1)

            python_imagen2 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/sistema1.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen2.image = python_imagen2
            self.imagen2.configure(image = python_imagen2)

            python_imagen3 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/sistema1.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen3.image = python_imagen3
            self.imagen3.configure(image = python_imagen3)

            python_imagen4 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/sistema1.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen4.image = python_imagen4
            self.imagen4.configure(image = python_imagen4)
            
        elif self._numeroInicio == 4:
            python_imagen1 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/sistema1.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen1.image = python_imagen1
            self.imagen1.configure(image = python_imagen1)

            python_imagen2 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/sistema1.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen2.image = python_imagen2
            self.imagen2.configure(image = python_imagen2)

            python_imagen3 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/sistema1.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen3.image = python_imagen3
            self.imagen3.configure(image = python_imagen3)

            python_imagen4 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/sistema1.jpeg').resize((300,225), Image.ANTIALIAS))
            self.imagen4.image = python_imagen4
            self.imagen4.configure(image = python_imagen4)
        


    def inicializarFrames(self):
        """Funcion para inicializar los seis frames anidados en la ventana"""

        self._p1 = Frame(self, bg = style.BACKGROUND_FRAMES)
        self._p1.pack(side = LEFT, fill = BOTH, expand = True, padx = 10, pady = 10)
        
        self._p2 = Frame(self, bg = style.BACKGROUND_FRAMES)
        self._p2.pack(side = LEFT, fill = BOTH, expand = True, padx = 10, pady = 10)

        self._p3 = Frame(self._p1, bg = style.BACKGROUND_FRAMES)
        self._p3.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)

        self._p4 = Frame(self._p1, bg = style.BACKGROUND_FRAMES)
        self._p4.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)

        self._p5 = Frame(self._p2, bg = style.BACKGROUND_FRAMES)
        self._p5.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)

        self._p6 = Frame(self._p2, bg = style.BACKGROUND_FRAMES)
        self._p6.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)

        # Se captura el evento de el frame p5 para cambiar la informacion
        self._p5.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        
        # Se inicializan los demas widgets de las demas ventanas
        self.inicializarWidgetsVentana1()
        self.inicializarWidgetsVentana2()
        self.inicializarWidgetsVentana3()
        self.inicializarWidgetsVentana4()
        
    def inicializarWidgetsVentana1(self):
        """Se inicializa la ventana que da el mensaje de bienvenida"""

        Label(
            self._p3,
            **style.ESTILOS_LABEL_VENTANA_1
        ).pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)
    
    def entrarAVentanaPrincipal(self):
            """Función que ejecuta el botón Ingresar para entrar a la ventana principal"""
            principal = Principal(self.controlador)
            principal.grab_set()
            self.controlador.iconify()
        
    def inicializarWidgetsVentana2(self):
        """Funcion par inicializar los widgets con imagenes del sistema y el boton para ingresar al sistema"""

        imagen_sistema = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/sistema1.jpeg').resize((300,225), Image.ANTIALIAS))
        
        self.imagenesSistema = Label(self._p4, pady=20)
        self.imagenesSistema.image = imagen_sistema
        self.imagenesSistema.configure(image = imagen_sistema)
        self.imagenesSistema.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)
        
        Button(self._p4, text="Ingresar", height=5, width=15, font=("Arial", 24), command=self.entrarAVentanaPrincipal).pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)

        self.imagenesSistema.bind('<Enter>', self.cambiarImagenesSistema)
    
    def inicializarWidgetsVentana3(self):
        """ Inicializar frame con los datos de los desarrolladores"""
        
        labelgeneral = Label(self._p5, justify=CENTER)
        labelgeneral.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)

        self._nombre = Label(labelgeneral, text = self.VALUES[self._numeroInicio]["name"], bg = "gray", justify=CENTER)
        self._nombre.grid(row = 0, column = 0, columnspan = 2, sticky = EW)

        contacto = Label(labelgeneral, text = "Descripción", justify=CENTER)
        contacto.grid(row = 1, column = 0, sticky=EW)

        self._descripcioncita = Label(labelgeneral, text =self.VALUES[self._numeroInicio]["description"], justify=LEFT)
        self._descripcioncita.grid(row=1, column=1, sticky=EW)

        email = Label(labelgeneral, text="Email", justify=CENTER)
        email.grid(row=2, column=0, sticky=EW)

        self._correo = Label(labelgeneral, text=self.VALUES[self._numeroInicio]["email"], justify=LEFT)
        self._correo.grid(row=2, column=1, sticky=EW)

        op = Label(labelgeneral, text="Ocupación", justify=CENTER)
        op.grid(row=3, column=0, sticky=EW)

        self._ocupacion = Label(labelgeneral, text="Estudiante de Ingeniería de Sistemas", justify=LEFT)
        self._ocupacion.grid(row=3, column=1, sticky=EW)

        unal = Label(labelgeneral, text="Universidad", justify=CENTER)
        unal.grid(row=4, column=0, sticky=EW)
        universidad = Label(labelgeneral, text="Universidad Nacional de Colombia", justify=LEFT)
        universidad.grid(row=4, column=1, sticky=EW)
        # Expandimos los labels dentro del frame anidado 3
        labelgeneral.columnconfigure(0, weight=1)

        self._descripcioncita.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        self._correo.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        self._ocupacion.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        self._nombre.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)

        contacto.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        email.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        unal.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        contacto.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        op.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
        universidad.bind('<ButtonPress-1>', self.cambiarInfoDesarrolladores)
    
    def inicializarWidgetsVentana4(self):
        """ Se cargan las imagenes de los desarroladores"""
        
        labelgeneralImagenes = Label(self._p5, justify=CENTER)
        labelgeneralImagenes.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 30)
        
        python_imagen1 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/sistema1.jpeg').resize((300,225), Image.ANTIALIAS))

        self.imagen1 = Label(labelgeneralImagenes)
        self.imagen1.image = python_imagen1
        self.imagen1.configure(image = python_imagen1)
        self.imagen1.grid(row = 0, column=0, sticky=NSEW)

        python_imagen2 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/sistema1.jpeg').resize((300,225), Image.ANTIALIAS))

        self.imagen2 = Label(labelgeneralImagenes)
        self.imagen2.image = python_imagen2
        self.imagen2.configure(image = python_imagen2)
        self.imagen2.grid(row = 0, column=1, sticky=NSEW)

        python_imagen3 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/sistema1.jpeg').resize((300,225), Image.ANTIALIAS))

        self.imagen3 = Label(labelgeneralImagenes)
        self.imagen3.image = python_imagen3
        self.imagen3.configure(image = python_imagen3)
        self.imagen3.grid(row = 1, column=0, sticky=NSEW)

        python_imagen4 = ImageTk.PhotoImage(Image.open(path+'/Imagenes/capturas_pantalla/sistema1.jpeg').resize((300,225), Image.ANTIALIAS))

        self.imagen4 = Label(labelgeneralImagenes)
        self.imagen4.image = python_imagen4
        self.imagen4.configure(image = python_imagen4)
        self.imagen4.grid(row = 1, column=1, sticky=NSEW)
        
        labelgeneralImagenes.columnconfigure(0, weight=1)
        labelgeneralImagenes.rowconfigure(0, weight=1)
        