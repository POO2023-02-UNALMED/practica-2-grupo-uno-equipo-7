import tkinter as tk
from tkinter import messagebox

class inventario:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.inventario = {}  # Puedes usar un diccionario para el inventario

class RestauranteApp:
    def __init__(self, root):
        self.root = root
        root.title("Restaurante App")

        self.sedes = []  # Lista de sedes
        self.selected_sede = tk.StringVar()

        self.create_ui()

    def create_ui(self):
        self.label_sede = tk.Label(self.root, text="Seleccione una sede:")
        self.label_sede.pack()

        sede_options = [sede.nombre for sede in self.sedes]
        self.selected_sede.set(sede_options[0])  # Establece el valor predeterminado del menú desplegable
        self.sede_combobox = tk.OptionMenu(self.root, self.selected_sede, *sede_options)
        self.sede_combobox.pack()

        self.label_option = tk.Label(self.root, text="Seleccione una opción:")
        self.label_option.pack()

        self.opciones = tk.StringVar()
        self.opcion_combobox = tk.OptionMenu(self.root, self.opciones, "1. Mostrar inventario", "2. Precio artículo inventario", "3. Revisar niveles de Stock", "4. Registrar artículo en inventario", "5. Renovar inventario", "6. Valor del inventario total", "7. Salir")
        self.opcion_combobox.pack()

        self.continuar_button = tk.Button(self.root, text="Continuar", command=self.continuar_click)
        self.continuar_button.pack()

        self.output_text = tk.Text(self.root, height=10, width=40)
        self.output_text.pack()

    def continuar_click(self):
        selected_sede = self.selected_sede.get()
        selected_option = self.opciones.get()
        self.output_text.delete(1.0, tk.END)  # Borra el texto anterior

        if selected_option == "":
            messagebox.showinfo("Advertencia", "Selecciona una opción válida.")
            return

        # Encuentra la sede seleccionada en la lista de sedes
        sede = None
        for s in self.sedes:
            if s.nombre == selected_sede:
                sede = s
                break

        if not sede:
            messagebox.showinfo("Error", "Sede no encontrada.")
            return

        if selected_option == "1. Mostrar inventario":
            # Lógica para mostrar el inventario
            self.output_text.insert(tk.END, f"Inventario de {sede.nombre} ubicado en {sede.ubicacion}:\n")
            for item, cantidad in sede.inventario.items():
                self.output_text.insert(tk.END, f"{item}: {cantidad}\n")
        elif selected_option == "2. Precio artículo inventario":
            # Lógica para obtener el precio de un artículo
            self.output_text.insert(tk.END, "Implementa la lógica para obtener el precio de un artículo aquí.\n")
        # Agrega casos para las otras opciones
        elif selected_option == "3. Revisar niveles de Stock":
            # Lógica para revisar los niveles de stock
            self.output_text.insert(tk.END, "Implementa la lógica para revisar niveles de stock aquí.\n")
        elif selected_option == "4. Registrar artículo en inventario":
            # Lógica para registrar un artículo en el inventario
            self.output_text.insert(tk.END, "Implementa la lógica para registrar un artículo en el inventario aquí.\n")
        elif selected_option == "5. Renovar inventario":
            # Lógica para renovar el inventario
            self.output_text.insert(tk.END, "Implementa la lógica para renovar el inventario aquí.\n")
        elif selected_option == "6. Valor del inventario total":
            # Lógica para calcular el valor del inventario total
            self.output_text.insert(tk.END, "Implementa la lógica para calcular el valor del inventario total aquí.\n")
        elif selected_option == "7. Salir":
            # Lógica para salir de la aplicación
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RestauranteApp(root)

    # Agregar las sedes de ejemplo
    sede1 = RestauranteSede("Envigado", "Medellin")
    sede2 = RestauranteSede("Sandiego", "Medellin")
    sede3 = RestauranteSede("Belen", "Medellin")
    sede4 = RestauranteSede("La America", "Medellin")
    app.sedes.extend([sede1, sede2, sede3, sede4])

    root.mainloop()


