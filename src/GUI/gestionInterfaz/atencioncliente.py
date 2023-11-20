from tkinter import *
from tkinter import messagebox
from gestorAplicacion.Sugerencia import Sugerencia
from gestorAplicacion.Empleado import Empleado
from baseDatos import Deserializador

#Inicio Sugerencias

class ReportesSugerencia(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Reporte de Sugerencias")
        self.configure(background="#72a18b")

        botonSugerencias = Button(self, text="Reporte de todas las sugerencias", command=self.reporte_todas_sugerencias, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        botonSugerencias.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        botonSugerenciaM = Button(self, text="Reporte de sugerencias del menu", command=self.reporte_sugerencias_menu, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        botonSugerenciaM.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        botonSugerenciaE = Button(self, text="Reporte de sugerencias sobre empleados", command=self.reporte_sugerencias_empleados, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        botonSugerenciaE.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        botonSugerenciaS = Button(self, text="Reporte de sugerencias de sede", command=self.reporte_sugerencias_sede, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        botonSugerenciaS.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        botonSugerenciaO = Button(self, text="Reporte de sugerencias otros", command=self.reporte_sugerencias_otros, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        botonSugerenciaO.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        self.resultado_text = Text(self, height=10, width=50, wrap='word', bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        self.resultado_text.pack(side='top', fill='both', padx=10, pady=10)

    def reporte_todas_sugerencias(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        # Lógica para el reporte de todas las sugerencias
        a = Deserializador.SugerenciasT()
        for resultado in a:
            self.mostrar_resultado(resultado)
            self.mostrar_resultado("\n")



    def reporte_sugerencias_menu(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        a = Deserializador.SugerenciaXTipo("Menu")
        for resultado in a:   # Aquí deberías generar el contenido del reporte
            self.mostrar_resultado(str(resultado))
            self.mostrar_resultado("\n")

    def reporte_sugerencias_empleados(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        a = Deserializador.SugerenciaXTipo("Empleado")
        # Lógica para el reporte de sugerencias sobre empleados
        for resultado in a:  # Aquí deberías generar el contenido del reporte
            self.mostrar_resultado(str(resultado))
            self.mostrar_resultado("\n")

    def reporte_sugerencias_sede(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        a = Deserializador.SugerenciaXTipo("Sede")
        # Lógica para el reporte de sugerencias de sede
        for resultado in a: # Aquí deberías generar el contenido del reporte
            self.mostrar_resultado(str(resultado))
            self.mostrar_resultado("\n")

    def reporte_sugerencias_otros(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        a = Deserializador.SugerenciaXTipo("Otro")
        # Lógica para el reporte de sugerencias otros
        for resultado in a:  # Aquí deberías generar el contenido del reporte
            self.mostrar_resultado(str(resultado))

    def mostrar_resultado(self, resultado):
        # Insertar el resultado en la última línea del área de texto
        self.resultado_text.insert('end', resultado + '\n')
        # Desplazar la vista de la caja de texto para mostrar la última línea
        self.resultado_text.see('end')

class VentanaVerificacionSugerencia(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Acesso Empleados")
        self.configure(background="#72a18b")
        
        # Etiqueta de instrucción
        Label(self, text="Necesita un código de empleado para acceder a esta funcion",bg = "#72a18b", font=("Roboto", 12), fg="#0a0a0a").pack()

        # Entry para ingresar el código
        label_sugerencia = Label(self, text="Codigo:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_sugerencia.pack(side=TOP, pady=5)
        self.entry_codigo = Entry(self)
        self.entry_codigo.pack()

        # Botón para verificar el código
        Button(self, text="Verificar", command=self.verificar_codigo, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a").pack()

    def verificar_codigo(self):
        codigo_empleado = self.entry_codigo.get()

        ver = Empleado.buscarEmpleadoXCodigo(codigo_empleado)
        # Verificar aquí si el código de empleado es válido
        if ver != None:  
            self.abrir_ReportesSugerencia()

            print("Si funciona")
        else:
            # Muestra un mensaje de error o realiza alguna acción según tu lógica
            print("Código de empleado no válido")
    def abrir_ReportesSugerencia(self):
        ventana = ReportesSugerencia(self)

class NuevaSugerencia(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Nueva Sugerencia")
        self.configure(background="#72a18b")

        # Etiqueta y menú desplegable
        label_tipo = Label(self, text="Tipo:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_tipo.pack(side=TOP, pady=5)

        opciones_tipo = ["Menu", "Empleado", "Sedes", "Otros"]
        self.var_tipo = StringVar(self)
        self.var_tipo.set(opciones_tipo[3])  # Establecer el valor predeterminado
        menu_tipo = OptionMenu(self, self.var_tipo, *opciones_tipo)
        menu_tipo.pack(side=TOP, pady=5)

        # Etiqueta y entrada para la sugerencia
        label_sugerencia = Label(self, text="Sugerencia:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_sugerencia.pack(side=TOP, pady=5)

        self.entry_sugerencia = Entry(self, width=30)
        self.entry_sugerencia.pack(side=TOP, pady=5)

        # Botón para guardar la sugerencia
        boton_guardar = Button(self, text="Guardar", command=self.confirmar_guardar_sugerencia, bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        boton_guardar.pack(side=TOP, pady=10)

        self.resultado_text = Text(self, height=10, width=50, wrap='word', bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        self.resultado_text.pack(side='top', fill='both', padx=10, pady=10)

    def mostrar_resultado(self, resultado):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        # Insertar el resultado en el área de texto
        self.resultado_text.insert('end', resultado)

    def confirmar_guardar_sugerencia(self):
        tipo = self.var_tipo.get()
        sugerencia_texto = self.entry_sugerencia.get()

        # Crear un mensaje de confirmación
        mensaje_confirmacion = f"¿Está seguro que desea enviar esta sugerencia?\n\nTipo: {tipo}\nSugerencia: {sugerencia_texto}"

        # Mostrar el cuadro de diálogo de confirmación
        confirmacion = messagebox.askokcancel("Confirmación", mensaje_confirmacion)

        if confirmacion:
            sug = Sugerencia(tipo, sugerencia_texto)
            # Mostrar el objeto sugerencia en el área de texto
            self.mostrar_resultado(str(sug))
        else:
            resultado = "La sugerencia no fue guardada"
            self.mostrar_resultado(resultado)
            
        
          
        
class VentanaSugerencia(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Opciones de Sugerencia")
        self.configure(background="#72a18b")

        boton_crear_sugerencia = Button(self, text="Crear nueva sugerencia", command=self.crear_nueva_sugerencia, bg="#a19f9f",font=("Roboto", 12), fg="#0a0a0a")
        boton_crear_sugerencia.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        boton_reportes = Button(self, text="Reportes", command=self.mostrar_reportes, bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        boton_reportes.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def crear_nueva_sugerencia(self):
        ventana_nueva_sugerencia = NuevaSugerencia(self)
    

    def mostrar_reportes(self):
        ventana = VentanaVerificacionSugerencia(self)
    
#Fin de sugerencias

    

#Lo que va a importar el main
class AtencionCliente(Frame):

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self._controlador = controlador
        self.configure(background="#72a18b")

        self._mostrarTitulo()
        self._botonSugerencia()
        self._botonQueja()
        self._botonReseña()
        self._botonDevolucion()

    def _mostrarTitulo(self):
        label1 = Label(self, text="Bienvenido al centro de Atencion al cliente\n¿Que desea realizar?", bg="#72a18b", font=("Roboto", 20), fg="#0a0a0a")
        label1.pack(side=TOP, fill=BOTH, pady=10)

    def _botonSugerencia(self):
        botonSugerencia = Button(self, text="Sugerencia", command=self._crear_ventana_sugerencia, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        botonSugerencia.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _botonQueja(self):
        botonQueja = Button(self, text="Queja", command=self.mostrar, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        botonQueja.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _botonReseña(self):
        botonReseña = Button(self, text="Reseña", command=self.mostrar, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        botonReseña.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _botonDevolucion(self):
        botonDevolucion = Button(self, text="Devolución", command=self.mostrar, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        botonDevolucion.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _crear_ventana_sugerencia(self):
        ventana_sugerencia = VentanaSugerencia(self)
        

    def mostrar(self):
        print("Prueba")

    