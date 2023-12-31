from tkinter import *
from tkinter import messagebox
from gestorAplicacion.Sugerencia import Sugerencia
from gestorAplicacion.Queja import Queja
from gestorAplicacion.Resena import Resena
from gestorAplicacion.Empleado import Empleado
from gestorAplicacion.Devolucion import Devolucion
from baseDatos import Deserializador,Serializador

#Inicio clases para la opcion Devolucion
class VerMisSolicitudes(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Buscar mis solicitude")
        self.configure(background="#72a18b")
        labelInicial = Label(self, justify=CENTER, text="Bienvenid@ para continuar por favor ingrese su nombre y luego\npresione 'Mostrar Solicitudes' para ver todas sus solicitudes", bg = "#72a18b", font=("Roboto", 12), fg="#0a0a0a")
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        label_Nombre = Label(self, text="Nombre:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_Nombre.pack(side="top", pady=5)
        self.entry_Nombre = Entry(self, width=30)
        self.entry_Nombre.pack(side="top", pady=5)
        
        boton_mostrar = Button(self, text="Mostrar Solicitudes", command=self.mostrarRepositorio, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        boton_mostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        self.resultado_text = Text(self, height=10, width=50, wrap='word', bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        self.resultado_text.pack(side='top', fill='both', padx=10, pady=10)
    
    def mostrarRepositorio(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        nombre = self.entry_Nombre.get()
        a = Deserializador.DelXTipo(nombre)
        for resultado in a:
            self.mostrar_resultado(str(resultado))
            self.mostrar_resultado("\n")

    def mostrar_resultado(self, resultado):
        # Insertar el resultado en la última línea del área de texto
        self.resultado_text.insert('end', resultado + '\n')
        # Desplazar la vista de la caja de texto para mostrar la última línea
        self.resultado_text.see('end')

class SolicitudesDevolucion(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Todas las Solicitudes")
        self.configure(background="#72a18b")
        labelInicial = Label(self, justify=CENTER, text="Bienvenid@ al repositorio de solicitudes\nPresione 'Mostrar Repositorio' para ver todas las solicitudes", bg = "#72a18b", font=("Roboto", 12), fg="#0a0a0a")
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
        boton_mostrar = Button(self, text="Mostrar repositorio", command=self.mostrarRepositorio, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        boton_mostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        self.resultado_text = Text(self, height=10, width=50, wrap='word', bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        self.resultado_text.pack(side='top', fill='both', padx=10, pady=10)
    
    def mostrarRepositorio(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        a = Deserializador.DevolucionesT()
        for resultado in a:
            self.mostrar_resultado(str(resultado))
            self.mostrar_resultado("\n")

    def mostrar_resultado(self, resultado):
        # Insertar el resultado en la última línea del área de texto
        self.resultado_text.insert('end', resultado + '\n')
        # Desplazar la vista de la caja de texto para mostrar la última línea
        self.resultado_text.see('end')

class VentanaVerificacionDevolucion(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Acesso Empleados")
        self.configure(background="#72a18b")
        
        # Etiqueta de instrucción
        Label(self, text="\nNecesita un código de empleado\npara poder acceder a esta funcion\n",bg = "#72a18b", font=("Roboto", 12), fg="#0a0a0a").pack()

        # Entry para ingresar el código
        label_Queja = Label(self, text="Codigo:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_Queja.pack(side=TOP, pady=5)
        self.entry_codigo = Entry(self)
        self.entry_codigo.pack()

        # Botón para verificar el código
        Button(self, text="Verificar", command=self.verificar_codigo, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a").pack()

    def verificar_codigo(self):
        codigo_empleado = self.entry_codigo.get()

        ver = Empleado.buscarEmpleadoXCodigo(codigo_empleado)
        # Verificar aquí si el código de empleado es válido
        if ver != None:  
            self.abrir_solicitudes()

        else:
            # Muestra un mensaje de error o realiza alguna acción según tu lógica
            print("Código de empleado no válido")
    def abrir_solicitudes(self):
        ventana = SolicitudesDevolucion(self)

class NuevaSolucitud(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Nueva Solucitud")
        self.configure(background="#72a18b")
        self.geometry("900x1000")

        label_Nombre = Label(self, text="Nombre:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_Nombre.pack(side="top", pady=5)
        self.entry_Nombre = Entry(self, width=30)
        self.entry_Nombre.pack(side="top", pady=5)

        label_Cedula = Label(self, text="Cedula:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_Cedula.pack(side="top", pady=5)
        self.entry_Cedula = Entry(self, width=30)
        self.entry_Cedula.pack(side="top", pady=5)

        label_Correo = Label(self, text="Correo:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_Correo.pack(side="top", pady=5)
        self.entry_Correo = Entry(self, width=30)
        self.entry_Correo.pack(side="top", pady=5)

        label_NFactura = Label(self, text="No. Factura:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_NFactura.pack(side="top", pady=5)
        self.entry_NFactura = Entry(self, width=30)
        self.entry_NFactura.pack(side="top", pady=5)

        label_Texto = Label(self, text="Razon de su solicitud:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_Texto.pack(side="top", pady=5)
        self.entry_Texto = Entry(self, width=30)
        self.entry_Texto.pack(side="top", pady=5)

        # Botón para guardar la queja
        boton_guardar = Button(self, text="Guardar", command=self.confirmar_guardar_solicitud, bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        boton_guardar.pack(side="top", pady=10)

        self.resultado_text = Text(self, height=10, width=50, wrap='word', bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        self.resultado_text.pack(side="top", fill="both", padx=10, pady=10)
    
    def mostrar_resultado(self, resultado):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        # Insertar el resultado en el área de texto
        self.resultado_text.insert('end', resultado)
    
    def confirmar_guardar_solicitud(self):
        nombreIngreso = self.entry_Nombre.get()
        nombre = nombreIngreso.upper()
        cedula = self.entry_Cedula.get()
        correo = self.entry_Correo.get()
        factura = self.entry_NFactura.get()
        texto_texto = self.entry_Texto.get()

        # Crear un mensaje de confirmación
        mensaje_confirmacion = f"¿Está seguro que desea enviar esta solicitud?\nNombre: {nombreIngreso}\nCedula: {cedula}\nCorreo: {correo}\nNo. Factura: {factura}\nRazon de solicitud: {texto_texto}"

        # Mostrar el cuadro de diálogo de confirmación
        confirmacion = messagebox.askokcancel("Confirmación", mensaje_confirmacion)

        if confirmacion:
            dlv = Devolucion(nombre, cedula, correo, factura, texto_texto)
            # Agregar a la serialización
            Serializador.agregarSolicitudNueva(dlv)
            # Mostrar el objeto sugerencia en el área de texto
            self.mostrar_resultado(dlv)

        else:
            resultado = "La solicitud no fue guardada"
            self.mostrar_resultado(resultado)

class VentanaDevolucion(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Opciones de Devolucion")
        self.configure(background="#72a18b")

        boton_solucitudes = Button(self, text="Ver las solicitudes de Devoluciones", command=self.mostrar_solicitudes, bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        boton_solucitudes.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        boton_crear_solicitud = Button(self, text="Realizar una nueva solicitud", command=self.crear_nueva_solicitud, bg="#a19f9f",font=("Roboto", 12), fg="#0a0a0a")
        boton_crear_solicitud.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        boton_estado = Button(self, text="Revisar el estado de mi solicitud", command=self.mostrar_estados, bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        boton_estado.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def mostrar_estados(self):
        ventana = VerMisSolicitudes(self)

    def crear_nueva_solicitud(self):
        ventana = NuevaSolucitud(self)
    

    def mostrar_solicitudes(self):
        ventana = VentanaVerificacionDevolucion(self)

#Fin clases para la opcion Devolucion

#Inicio clases para la opcion Reseña
class ReporteCalificaciones(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Reporte de calificaciones")
        self.configure(background="#72a18b")
        labelInicial = Label(self, justify=CENTER, text="Bienvenid@ al reporte de calificaciones\nPresione 'Mostrar reporte' para el reporte", bg = "#72a18b", font=("Roboto", 12), fg="#0a0a0a")
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
        boton_mostrar = Button(self, text="Mostrar reporte", command=self.mostrarReporte, bg = "#72a18b", font=("Roboto", 12), fg="#0a0a0a")
        boton_mostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        self.resultado_text = Text(self, height=10, width=50, wrap='word', bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        self.resultado_text.pack(side='bottom', fill='both', padx=10, pady=10)
    
    def mostrarReporte(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        resultado =  Deserializador.countCalificacionResenas()
        self.mostrar_resultado(str(resultado))

    def mostrar_resultado(self, resultado):
        # Insertar el resultado en la última línea del área de texto
        self.resultado_text.insert('end', resultado + '\n')
        # Desplazar la vista de la caja de texto para mostrar la última línea
        self.resultado_text.see('end')

class VentanaVerificacionResena(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Acesso Empleados")
        self.configure(background="#72a18b")
        
        # Etiqueta de instrucción
        Label(self, text="\nNecesita un código de empleado\npara poder acceder a esta funcion\n",bg = "#72a18b", font=("Roboto", 12), fg="#0a0a0a").pack()

        # Entry para ingresar el código
        label_Queja = Label(self, text="Codigo:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_Queja.pack(side=TOP, pady=5)
        self.entry_codigo = Entry(self)
        self.entry_codigo.pack()

        # Botón para verificar el código
        Button(self, text="Verificar", command=self.verificar_codigo, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a").pack()

    def verificar_codigo(self):
        codigo_empleado = self.entry_codigo.get()

        ver = Empleado.buscarEmpleadoXCodigo(codigo_empleado)
        # Verificar aquí si el código de empleado es válido
        if ver != None:  
            self.abrir_ReporteCalificaciones()

        else:
            # Muestra un mensaje de error o realiza alguna acción según tu lógica
            print("Código de empleado no válido")
    def abrir_ReporteCalificaciones(self):
        ventana = ReporteCalificaciones(self)

class NuevaResena(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Reseña")
        self.configure(background="#72a18b")
        self.geometry("900x1000")

        label_Nombre = Label(self, text="Nombre:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_Nombre.pack(side="top", pady=5)
        self.entry_Nombre = Entry(self, width=30)
        self.entry_Nombre.pack(side="top", pady=5)

        self.otro_text = Text(self, height=10, width=50, wrap='word', bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        self.otro_text.pack(side="top", fill="both", padx=10, pady=10)
        self.otro_text.insert('end', "Por favor, si desea que su reseña sea anonima en el apartado nombre escriba: 'Anonimo'")

        # Etiqueta y menú desplegable
        label_calificacion = Label(self, text="Calificacion:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_calificacion.pack(side="top", pady=5)

        opciones_tipo = [1,2,3,4,5]
        self.var_tipo = IntVar(self)
        self.var_tipo.set(opciones_tipo[3])  # Establecer el valor predeterminado
        menu_tipo = OptionMenu(self, self.var_tipo, *opciones_tipo)
        menu_tipo.pack(side=TOP, pady=5)

    
        # Etiqueta y entrada para la queja
        label_resena = Label(self, text="Reseña:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_resena.pack(side="top", pady=5)

        self.entry_resena = Entry(self, width=30)
        self.entry_resena.pack(side="top", pady=5)

        # Botón para guardar la queja
        boton_guardar = Button(self, text="Guardar", command=self.confirmar_guardar_resena, bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        boton_guardar.pack(side="top", pady=10)

        self.resultado_text = Text(self, height=10, width=50, wrap='word', bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        self.resultado_text.pack(side="top", fill="both", padx=10, pady=10)

    def mostrar_resultado(self, resultado):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        # Insertar el resultado en el área de texto
        self.resultado_text.insert('end', resultado)

    def confirmar_guardar_resena(self):
        nombre = self.entry_Nombre.get()
        cal = self.var_tipo.get()
        a = int(cal)
        resena_texto = self.entry_resena.get()

        # Crear un mensaje de confirmación
        mensaje_confirmacion = f"¿Está seguro que desea enviar esta reseña?\nNombre: {nombre}\nCalificacion: {cal}\nReseña: {resena_texto}"

        # Mostrar el cuadro de diálogo de confirmación
        confirmacion = messagebox.askokcancel("Confirmación", mensaje_confirmacion)

        if confirmacion:
            rna = Resena(nombre, resena_texto, a)
            # Agregar a la serialización
            Serializador.agregarResenaNueva(rna)
            # Mostrar el objeto sugerencia en el área de texto
            self.mostrar_resultado(rna)

        else:
            resultado = "La reseña no fue guardada"
            self.mostrar_resultado(resultado)

class RepositorioResenas(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Repositorio de Reseñas")
        self.configure(background="#72a18b")
        labelInicial = Label(self, justify=CENTER, text="Bienvenid@ al repositorio de Reseñas\nPresione 'Mostrar Repositorio' para ver todas las reseñas", bg = "#72a18b", font=("Roboto", 12), fg="#0a0a0a")
        labelInicial.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        
        boton_mostrar = Button(self, text="Mostrar repositorio", command=self.mostrarRepositorio, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        boton_mostrar.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        self.resultado_text = Text(self, height=10, width=50, wrap='word', bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        self.resultado_text.pack(side='top', fill='both', padx=10, pady=10)
    
    def mostrarRepositorio(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        a = Deserializador.ResenasT()
        for resultado in a:
            self.mostrar_resultado(str(resultado))
            self.mostrar_resultado("\n")

    def mostrar_resultado(self, resultado):
        # Insertar el resultado en la última línea del área de texto
        self.resultado_text.insert('end', resultado + '\n')
        # Desplazar la vista de la caja de texto para mostrar la última línea
        self.resultado_text.see('end')

class VentanaResena(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Opciones de Reseña")
        self.configure(background="#72a18b")

        boton_repositorio = Button(self, text="Repositorio de reseñas", command=self.mostrar_repositorio, bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        boton_repositorio.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        boton_crear_Resena = Button(self, text="Crear nueva reseña", command=self.crear_nueva_resena, bg="#a19f9f",font=("Roboto", 12), fg="#0a0a0a")
        boton_crear_Resena.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        boton_cal = Button(self, text="Reporte de calificaciones", command=self.mostrar_reporte_calificaciones, bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        boton_cal.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def mostrar_reporte_calificaciones(self):
        ventana = VentanaVerificacionResena(self)

    def crear_nueva_resena(self):
        ventana = NuevaResena(self)
    

    def mostrar_repositorio(self):
        ventana = RepositorioResenas(self)
#Fin clases para la opcion Reseñas

#Inicio clases para la opcion Queja
class ReportesQuejas(Toplevel):

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Reporte de Sugerencias")
        self.configure(background="#72a18b")

        Label(self, text="\nBienvenid@ de nuevo, por favor,\na continuacion elija una opcion:\n",bg = "#72a18b", font=("Roboto", 12), fg="#0a0a0a").pack()


        botonQuejas = Button(self, text="Reporte de todas las quejas", command=self.reporte_todas_quejas, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        botonQuejas.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        botonQuejaM = Button(self, text="Reporte de quejas del menu", command=self.reporte_quejas_menu, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        botonQuejaM.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        botonQuejaE = Button(self, text="Reporte de quejas sobre empleados", command=self.reporte_quejas_empleados, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        botonQuejaE.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        botonQuejaS = Button(self, text="Reporte de quejas de sede", command=self.reporte_quejas_sede, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        botonQuejaS.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        botonQuejaO = Button(self, text="Reporte de quejas otros", command=self.reporte_quejas_otros, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        botonQuejaO.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        self.resultado_text = Text(self, height=10, width=50, wrap='word', bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        self.resultado_text.pack(side='top', fill='both', padx=10, pady=10)

    def reporte_todas_quejas(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        a = Deserializador.QuejasT()
        for resultado in a:
            self.mostrar_resultado(str(resultado))
            self.mostrar_resultado("\n")

    def reporte_quejas_menu(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        a = Deserializador.QuejasXTipo("Menu")
        for resultado in a:  
            self.mostrar_resultado(str(resultado))
            self.mostrar_resultado("\n")

    def reporte_quejas_empleados(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        a = Deserializador.QuejasXTipo("Empleado")
        for resultado in a: 
            self.mostrar_resultado(str(resultado))
            self.mostrar_resultado("\n")

    def reporte_quejas_sede(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        a = Deserializador.QuejasXTipo("Sede")
        for resultado in a:
            self.mostrar_resultado(str(resultado))
            self.mostrar_resultado("\n")

    def reporte_quejas_otros(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        a = Deserializador.QuejasXTipo("Otro")
        for resultado in a:
            self.mostrar_resultado(str(resultado))
            self.mostrar_resultado("\n")

    def mostrar_resultado(self, resultado):
        # Insertar el resultado en la última línea del área de texto
        self.resultado_text.insert('end', resultado + '\n')
        # Desplazar la vista de la caja de texto para mostrar la última línea
        self.resultado_text.see('end')

class VentanaVerificacionQueja(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Acesso Empleados")
        self.configure(background="#72a18b")
        
        # Etiqueta de instrucción
        Label(self, text="\nNecesita un código de empleado\npara poder acceder a esta funcion\n",bg = "#72a18b", font=("Roboto", 12), fg="#0a0a0a").pack()

        # Entry para ingresar el código
        label_Queja = Label(self, text="Codigo:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_Queja.pack(side=TOP, pady=5)
        self.entry_codigo = Entry(self)
        self.entry_codigo.pack()

        # Botón para verificar el código
        Button(self, text="Verificar", command=self.verificar_codigo, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a").pack()

    def verificar_codigo(self):
        codigo_empleado = self.entry_codigo.get()

        ver = Empleado.buscarEmpleadoXCodigo(codigo_empleado)
        # Verificar aquí si el código de empleado es válido
        if ver != None:  
            self.abrir_ReportesQuejas()

        else:
            # Muestra un mensaje de error o realiza alguna acción según tu lógica
            print("Código de empleado no válido")
    def abrir_ReportesQuejas(self):
        ventana = ReportesQuejas(self)

class NuevaQueja(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Nueva Queja")
        self.configure(background="#72a18b")
        self.geometry("900x1000")

        label_Nombre = Label(self, text="Nombre:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_Nombre.pack(side="top", pady=5)
        self.entry_Nombre = Entry(self, width=30)
        self.entry_Nombre.pack(side="top", pady=5)

        # Etiqueta y menú desplegable
        label_tipo = Label(self, text="Tipo:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_tipo.pack(side="top", pady=5)

        opciones_tipo = ["Menu", "Empleado", "Sede", "Otros"]
        self.var_tipo = StringVar(self)
        self.var_tipo.set(opciones_tipo[3])  # Establecer el valor predeterminado
        menu_tipo = OptionMenu(self, self.var_tipo, *opciones_tipo, command=self.cambiarOtro)
        menu_tipo.pack(side="top", pady=5)

        

        self.otro_text = Text(self, height=10, width=50, wrap='word', bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        self.otro_text.pack(side="top", fill="both", padx=10, pady=10)

        label_Sobre = Label(self, text="Sobre:", bg= "#a19f9f", font =("Roboto", 12), fg ="#0a0a0a")
        label_Sobre.pack(side="top", pady=5)
        self.entry_otro = Entry(self, width=30)
        self.entry_otro.pack(side="top", pady=5)
    

        # Etiqueta y entrada para la queja
        label_Queja = Label(self, text="Queja:", bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        label_Queja.pack(side="top", pady=5)

        self.entry_queja = Entry(self, width=30)
        self.entry_queja.pack(side="top", pady=5)

        # Botón para guardar la queja
        boton_guardar = Button(self, text="Guardar", command=self.confirmar_guardar_queja, bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        boton_guardar.pack(side="top", pady=10)

        self.resultado_text = Text(self, height=10, width=50, wrap='word', bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        self.resultado_text.pack(side="top", fill="both", padx=10, pady=10)

    def cambiarOtro(self, *args):
        resultado = ""
        tipo = self.var_tipo.get()

        # Primero, ocultar/mostrar menú y etiqueta de sede
        if tipo == "Sede":
            resultado = "Por favor, ingrese el nombre de la sede de la cual quiere quejarse en el apartado de 'Sobre:\nConsejo: Escriba 'Sede: ' y luego escriba la sede (Envigado/Sandiego/Belen/La America)"

        elif tipo == "Otros":
            resultado = "Por favor no llene el apartado 'Sobre: ', no es necesario"
        # Luego, mostrar el texto correcto en el área de texto
        elif tipo == "Menu":
            resultado = "Por favor, ingrese el nombre del plato del cual quiere quejarse en el apartado de 'Sobre:'\nConsejo: Si no cuenta con el nombre del plato se le recomienda hacer una queja del tipo 'Otro'."
            
        elif tipo == "Empleado":
            resultado = "Por favor, ingrese el nombre del empleado del cual quiere quejarse en el apartado de 'Sobre:' \nConsejo: Si no cuenta con el nombre del empleado se le recomienda hacer una queja del tipo 'Otro'."
            
        self.mostrar_resultado2(resultado)



    def mostrar_resultado2(self, resultado):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.otro_text.delete(1.0, 'end')
        # Insertar el resultado en el área de texto
        self.otro_text.insert('end', resultado)

    def mostrar_resultado(self, resultado):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        # Insertar el resultado en el área de texto
        self.resultado_text.insert('end', resultado)

    def confirmar_guardar_queja(self):
        nombre = self.entry_Nombre.get()
        tipo = self.var_tipo.get()
        algo = self.entry_otro.get()
        queja_texto = self.entry_queja.get()

        # Crear un mensaje de confirmación
        mensaje_confirmacion = f"¿Está seguro que desea enviar esta queja?\nNombre: {nombre}\nTipo: {tipo}\nSobre: {algo}\nQueja: {queja_texto}"

        # Mostrar el cuadro de diálogo de confirmación
        confirmacion = messagebox.askokcancel("Confirmación", mensaje_confirmacion)

        if confirmacion:
            qja = Queja(nombre, tipo, algo, queja_texto)
            # Agregar a la serialización
            Serializador.agregarQuejaNueva(qja)
            # Mostrar el objeto sugerencia en el área de texto
            self.mostrar_resultado(qja)

        else:
            resultado = "La queja no fue guardada"
            self.mostrar_resultado(resultado)

class VentanaQueja(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Opciones de Queja")
        self.configure(background="#72a18b")

        boton_crear_sugerencia = Button(self, text="Crear nueva queja", command=self.crear_nueva_Queja, bg="#a19f9f",font=("Roboto", 12), fg="#0a0a0a")
        boton_crear_sugerencia.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        boton_reportes = Button(self, text="Reportes", command=self.mostrar_reportes, bg="#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        boton_reportes.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def crear_nueva_Queja(self):
        ventana_nueva_queja = NuevaQueja(self)
    

    def mostrar_reportes(self):
        ventana = VentanaVerificacionQueja(self)

#Fin de clases para la opcion Queja

#Inicio clases para la opcion sugerencias

class ReportesSugerencia(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Reporte de Sugerencias")
        self.configure(background="#72a18b")

        Label(self, text="\nBienvenid@ de nuevo, por favor,\na continuacion elija una opcion:\n",bg = "#72a18b", font=("Roboto", 12), fg="#0a0a0a").pack()


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
        a = Deserializador.SugerenciasT()
        for resultado in a:
            self.mostrar_resultado(str(resultado))
            self.mostrar_resultado("\n")

    def reporte_sugerencias_menu(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        a = Deserializador.SugerenciaXTipo("Menu")
        for resultado in a:  
            self.mostrar_resultado(str(resultado))
            self.mostrar_resultado("\n")

    def reporte_sugerencias_empleados(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        a = Deserializador.SugerenciaXTipo("Empleado")
        for resultado in a: 
            self.mostrar_resultado(str(resultado))
            self.mostrar_resultado("\n")

    def reporte_sugerencias_sede(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        a = Deserializador.SugerenciaXTipo("Sede")
        for resultado in a:
            self.mostrar_resultado(str(resultado))
            self.mostrar_resultado("\n")

    def reporte_sugerencias_otros(self):
        # Limpiar el área de texto antes de mostrar un nuevo resultado
        self.resultado_text.delete(1.0, 'end')
        a = Deserializador.SugerenciaXTipo("Otro")
        for resultado in a:
            self.mostrar_resultado(str(resultado))
            self.mostrar_resultado("\n")

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
        Label(self, text="\nNecesita un código de empleado\npara poder acceder a esta funcion\n",bg = "#72a18b", font=("Roboto", 12), fg="#0a0a0a").pack()

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

        opciones_tipo = ["Menu", "Empleado", "Sede", "Otros"]
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
            # Agregar a la serialización
            Serializador.agregarSugerenciaNueva(sug)
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
    
#Fin de clases para la opcion sugerencias

#clase principal:
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
        botonQueja = Button(self, text="Queja", command=self._crear_ventana_queja, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        botonQueja.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _botonReseña(self):
        botonReseña = Button(self, text="Reseña", command=self._crear_ventana_resena, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        botonReseña.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _botonDevolucion(self):
        botonDevolucion = Button(self, text="Devolución", command=self._crear_ventana_devolucion, bg = "#a19f9f", font=("Roboto", 12), fg="#0a0a0a")
        botonDevolucion.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    def _crear_ventana_sugerencia(self):
        ventana_sugerencia = VentanaSugerencia(self)

    def _crear_ventana_queja(self):
        ventana_sugerencia = VentanaQueja(self)
    
    def _crear_ventana_resena(self):
        ventana_resena = VentanaResena(self)
    
    def _crear_ventana_devolucion(self):
        ventana_devolucion = VentanaDevolucion(self)

    