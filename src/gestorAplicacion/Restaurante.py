from gestorAplicacion import Empleado
class Restaurante:
    incentivos = {
        10: 0.05,
        15: 0.06,
        20: 0.065,
        25: 0.07,
        30: 0.072
    }
    facturas = {}
    sedes = ["envigado", "sandiego","belen","La America"]

    def __init__(self, ubicacion, direccion, inventario, caja, telefono, horario, menu, mesas):
        self.nombre = "La Casa de Toño"
        self.ubicacion = ubicacion
        self.direccion = direccion
        self.telefono = telefono
        self.horario = horario
        self.menu = menu
        self.mesas = mesas
        self.inventario = inventario
        self.caja = caja
        self.codigo_sede = len(Restaurante.sedes)
        Restaurante.sedes.append(self)
        self.disponibilidad = ["2023-10-25 14:00 PM", "2023-10-25 18:00 PM", "2023-10-26 12:00 PM", "2023-10-30 11:00 AM"]

    def get_ubicacion(self):
        return self.ubicacion

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def get_caja(self):
        return self.caja

    def set_caja(self, caja):
        self.caja = caja

    def get_nombre(self):
        return self.nombre

    def get_direccion(self):
        return self.direccion

    def get_telefono(self):
        return self.telefono

    def get_horario(self):
        return self.horario

    def get_menu(self):
        return self.menu

    @classmethod
    def get_menu_by_sede(cls, sede):
        for restaurante in cls.sedes:
            if restaurante.get_ubicacion() == sede:
                return restaurante.get_menu()
        return None

    def get_mesas(self):
        return self.mesas

    @classmethod
    def get_sedes(cls):
        return cls.sedes

    @classmethod
    def set_sedes(cls, sedes):
        cls.sedes = sedes

    def get_disponibilidad(self):
        return self.disponibilidad

    def set_disponibilidad(self, disponibilidad):
        self.disponibilidad = disponibilidad

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_horario(self, horario):
        self.horario = horario

    def set_menu(self, menu):
        self.menu = menu

    def set_mesas(self, mesas):
        self.mesas = mesas

    def set_empleados(self, empleados):
        self.empleados = empleados

    def agregar_plato(self, plato):
        self.menu.append(plato)

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)

    def eliminar_plato(self, plato):
        self.menu.remove(plato)

    def eliminar_mesa(self, mesa):
        self.mesas.remove(mesa)

    def eliminar_empleado(self, empleado):
        self.empleados.remove(empleado)

    def agregar_factura(self, factura):
        Restaurante.facturas[factura.get_codigo()] = self.nombre

    @classmethod
    def get_incentivos(cls):
        return cls.incentivos

    @classmethod
    def set_incentivos(cls, incentivos):
        cls.incentivos = incentivos

    def get_codigo_sede(self):
        return self.codigo_sede

    @classmethod
    def buscar_sede(cls, codigo_sede):
        for sede in cls.sedes:
            if sede.get_codigo_sede() == codigo_sede:
                return sede
        return None

    @classmethod
    def buscar_sede_por_ubicacion(cls, ubicacion):
        for sede in cls.sedes:
            if sede.get_ubicacion() == ubicacion:
                return sede
        return None

    @classmethod
    def calcular_propinas_por_sede(cls, codigo_sede):
        sede = cls.buscar_sede(codigo_sede)
        if sede is None:
            return 0
        total_propinas = 0
        empleados = Empleado.get_empleados(codigo_sede)
        for empleado in empleados:
            total_propinas += empleado.calcular_propinas(empleado.get_codigo())
        return total_propinas

    @classmethod
    def horarios_disponibles(cls, fecha_deseada):
        restaurantes_disponibles = []
        for sede in cls.sedes:
            for disponibilidad in sede.disponibilidad:
                if disponibilidad == fecha_deseada:
                    restaurantes_disponibles.append(sede)
        return restaurantes_disponibles

    @classmethod
    def sedes_disponibles(cls, mi_horario, mi_mesa):
        mesas_encontradas = Mesa.mesas_disponibles(mi_mesa)
        horario_encontrados = cls.horarios_disponibles(mi_horario)
        sedes_disponibles = []
        for restaurante in horario_encontrados:
            for mesa in mesas_encontradas:
                if mesa.get_ubicacion() == restaurante.ubicacion:
                    sedes_disponibles.append(restaurante)
        return sedes_disponibles

    def get_inventario(self):
        return self.inventario

           
