from datetime import datetime
from typing import List

class Factura:
    contadorFacturas = 0
    facturas = []

    def __init__(self, codigoCliente: int, codigoEmpleado: int, codigoSede: int, fecha: str, total: int, platos: []):
        self.codigo = Factura.contadorFacturas + 1
        self.codigoCliente = codigoCliente
        self.codigoEmpleado = codigoEmpleado
        self.codigoSede = codigoSede
        self.total = total
        Factura.contadorFacturas += 1
        self.fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
        Factura.facturas.append(self)
        self.platos = platos

    @classmethod
    def init_facturas(cls):
        platos1 = [Plato.buscarPlato("Tacos"), Plato.buscarPlato("Tostadas")]
        platos2 = [Plato.buscarPlato("Sopes"), Plato.buscarPlato("Enchiladas")]
        platos3 = [Plato.buscarPlato("Tamales")]
        factura1 = Factura(1, 1, 1, "2020-01-01", 1000, platos1)
        factura2 = Factura(1, 1, 1, "2020-01-02", 2000, platos1)
        factura3 = Factura(1, 1, 1, "2020-01-03", 3000, platos1)
        factura4 = Factura(1, 1, 1, "2020-01-04", 4000, platos2)
        factura5 = Factura(1, 1, 1, "2020-01-05", 5000, platos2)
        factura6 = Factura(1, 1, 1, "2020-01-06", 6000, platos2)
        factura7 = Factura(1, 2, 1, "2020-01-07", 7000, platos2)
        factura8 = Factura(1, 2, 1, "2020-01-08", 8000, platos2)
        factura9 = Factura(1, 2, 1, "2020-01-09", 9000, platos2)
        factura10 = Factura(1, 2, 1, "2020-01-10", 10000, platos3)
        factura11 = Factura(1, 2, 1, "2020-01-11", 11000, platos2)
        factura12 = Factura(1, 2, 1, "2020-01-12", 12000, platos2)
        factura13 = Factura(1, 2, 1, "2020-01-13", 13000, platos3)
        factura14 = Factura(1, 2, 1, "2020-01-14", 14000, platos1)
        factura15 = Factura(1, 2, 1, "2020-01-15", 15000, platos2)
        factura16 = Factura(1, 2, 1, "2020-01-16", 16000, platos2)
        factura17 = Factura(1, 2, 1, "2020-01-17", 17000, platos2)
        factura18 = Factura(1, 2, 1, "2020-01-18", 18000, platos2)

    def getCodigo(self):
        return self.codigo

    def getCodigoCliente(self):
        return self.codigoCliente

    def getCodigoEmpleado(self):
        return self.codigoEmpleado

    def getCodigoSede(self):
        return self.codigoSede

    def getTotal(self):
        return self.total

    def getFecha(self):
        return self.fecha

    def setTotal(self, total):
        self.total = total

    @staticmethod
    def existeFactura(codigo):
        for factura in Factura.facturas:
            if factura.getCodigo() == codigo:
                return True
        return False

    @staticmethod
    def buscarFactura(codigo):
        for factura in Factura.facturas:
            if factura.getCodigo() == codigo:
                return factura
        return None

    @staticmethod
    def buscarFacturasPorCliente(codigoCliente):
        facturasCliente = []
        for factura in Factura.facturas:
            if factura.getCodigoCliente() == codigoCliente:
                facturasCliente.append(factura)
        return facturasCliente

    @staticmethod
    def buscarFacturasPorEmpleado(codigoEmpleado):
        facturasEmpleado = []
        for factura in Factura.facturas:
            if factura.getCodigoEmpleado() == codigoEmpleado:
                facturasEmpleado.append(factura)
        return facturasEmpleado

    @staticmethod
    def buscarFacturasPorSede(codigoSede):
        facturasSede = []
        for factura in Factura.facturas:
            if factura.getCodigoSede() == codigoSede:
                facturasSede.append(factura)
        return facturasSede

    @staticmethod
    def buscarFacturasPorFecha(fechaInicio, fechaFin):
        facturasFecha = []
        for factura in Factura.facturas:
            if factura.getFecha() > fechaInicio and factura.getFecha() < fechaFin:
                facturasFecha.append(factura)
        return facturasFecha

    @staticmethod
    def buscarFacturasPorFechaycodigo(codigoEmpleado, fechaInicio, fechaFin):
        facturasFecha = []
        for factura in Factura.facturas:
            if factura.getCodigoEmpleado() == codigoEmpleado and factura.getFecha() > fechaInicio and factura.getFecha() < fechaFin:
                facturasFecha.append(factura)
        return facturasFecha

    def getPlatos(self):
        return self.platos
