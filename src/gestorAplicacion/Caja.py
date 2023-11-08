from typing import List
class Caja:
    listado_cajas: List[Caja] = []  # Lista para llevar un registro de todas las cajas

    def __init__(self, dinero_caja:int, numero_de_serie:int):
        self.dinero_caja = dinero_caja
        self.numero_de_serie = numero_de_serie
        self.total_egresos = 0
        self.total_ingresos = 0
        Caja.listado_cajas.append(self)

    def compra(self, objeto, precio, cantidad, restaurante_asociado):
        costo_total = precio * cantidad

        if self.dinero_caja >= costo_total:
            self.dinero_caja -= costo_total
            self.total_egresos += costo_total
            restaurante_asociado.inventario.añadir_items(objeto.get_nombre(), cantidad)
            return "Compra exitosa"
        else:
            return "No hay suficiente dinero en la caja para realizar la compra. Debe ingresar dinero en caja para hacer posible la compra."

    def agregar_dinero_caja(self, monto):
        self.total_ingresos += monto
        self.dinero_caja += monto

    def obtener_resumen_caja(self):
        print("Número de Serie:", self.numero_de_serie)
        print("Dinero en Caja:", self.dinero_caja)
        print("Total de Ingresos:", self.total_ingresos)
        print("Total de Egresos:", self.total_egresos)
        print("Saldo Actual:", self.dinero_caja)

    def cerrar_caja(self):
        self.total_ingresos = 0
        self.total_egresos = 0
        self.dinero_caja = 0

    def registrar_egreso(self, monto):
        if monto <= self.dinero_caja:
            self.total_egresos += monto
            self.dinero_caja -= monto
        else:
            print("Fondos insuficientes en la caja para realizar el egreso.")

    def transferir_dinero_a_caja(self, otra_caja, monto):
        if self.dinero_caja >= monto:
            self.registrar_egreso(monto)
            otra_caja.agregar_dinero_caja(monto)
            print(f"Transferencia exitosa de ${monto} a la caja {otra_caja.numero_de_serie}")
        else:
            print("Fondos insuficientes para realizar la transferencia.")

    def ver_registro_transacciones(self):
        print("Registro de Transacciones de la Caja", self.numero_de_serie)
        print("Ingresos totales:", self.total_ingresos)
        print("Egresos totales:", self.total_egresos)

    def generar_informe_cierre_diario(self):
        print("Informe de Cierre Diario de la Caja", self.numero_de_serie)
        saldo_inicial = self.dinero_caja + self.total_egresos - self.total_ingresos
        print("Saldo Inicial:", saldo_inicial)
        print("Ingresos del Día:", self.total_ingresos)
        print("Egresos del Día:", self.total_egresos)
        print("Saldo Actual:", self.dinero_caja)

    def registrar_propina(self, monto):
        if monto > 0:
            self.dinero_caja += monto
            print(f"Propina registrada exitosamente de ${monto}")
        else:
            print("Sin propina.")