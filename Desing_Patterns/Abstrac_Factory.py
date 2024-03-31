from abc import ABC, abstractmethod

# Creacion de instancias de satelites distintos 
# usando el patron de diseño abstract factory

# Clase abstracta y clases para generar 
# familias de productos

class AbstractFactory(ABC):
    @abstractmethod
    def createSat(self):
        pass

# Satelites factories
    
class CubeSatFactory(AbstractFactory):
    def createSat(self):
        return CubeSat()
    
class CanSatFactory(AbstractFactory):
    def createSat(self):
        return CanSat()
    
# Productos o familia de productos
    
class Sat(ABC):
    @abstractmethod
    def operation(self):
        pass

class CubeSat(Sat):
    def operation(self):
        return "{Creando un cube sat}"
class CanSat(Sat):
    def operation(self):
        return "{Creando un cansat}"


# Peticiones del usuario

def user_code(factory):
    print(factory.createSat().operation())

if __name__=='__main__':
    print("\nTesting fabrica de pico Satelites...")
    user_code(CubeSatFactory())

    print("\nTesting fabrica de cansats...")
    user_code(CanSatFactory())