from datetime import datetime
from typing import List
from .Plato import Plato

class Factura:
    contadorFacturas = 0
    facturas = []
    # Obtener los platos que queremos agregar a las facturas
    

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

