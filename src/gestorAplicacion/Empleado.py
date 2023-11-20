from gestorAplicacion.Persona import Persona

class Empleado(Persona):

    Empleados = []
    

    def __init__(self, nombre, cargo, cod, sueldo, codigoSede):
        
        super().__init__( nombre)
        self._cargo = cargo
        self._sueldo = sueldo
        self._codigoSede = codigoSede
        self._codigo = cod
        self._amonestaciones = 0
        Empleado.Empleados.append(self)

    def setCargo(self, cargo):
        self._cargo = cargo
    
    def getCargo(self):
        return self._cargo
    
    def setSueldo(self, sueldo):
        self._sueldo = sueldo

    def getSueldo(self):
        return self._sueldo
    
    def setCodigoSede(self, codigo):
        self._codigoSede = codigo
    
    def getCodigoSede(self):
        return self._codigoSede
    
    def getCodigo(self):
        return self._codigo
    
    def setAmonestaciones (self):
        self._amonestaciones += 1

    def getAmonestaciones(self):
        return self._amonestaciones
    
    def nuevaAmonestacion(self,empleado):
        empleados = self.Empleados
        for i in empleados:
            if i == empleado:
                empleado.setAmonestaciones()
    
    @classmethod
    def getEmpleados(cls):
        return cls.Empleados
    
    @classmethod
    def existeEmpleado(cls, nombre):
        a = False
        empleados = cls.getEmpleados()
        for empleado in empleados:
            if empleado.getNombre() == nombre:
                a = True
        
        return a
    
    @classmethod
    def buscarEmpleadoXNombre(cls, nombre):
        empleados = cls.Empleados
        for empleado in empleados:
            if empleado.getNombre() == nombre:
                return empleado
            else:
                return None
            
    @classmethod
    def buscarEmpleadoXCodigo(cls, codigo):
        empleados = cls.Empleados
        for empleado in empleados:
            if empleado.getCodigo() == codigo:
                return empleado
        return None

