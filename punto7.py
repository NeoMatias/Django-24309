class cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular=titular
        self.__cantidad=float(cantidad)
    
    @property
    def titular(self):
        return self.__titular
        
    @titular.setter
    def titular(self, titular):
        self.__titular=titular
        
    @property
    def cantidad(self):
        return self.__cantidad
    
    
    def mostrar(self):
        print(f"Titular:{self.__titular}")
        print(f"Cantidad:{self.__cantidad}")
        
    def ingresar(self,cantidad):
        if cantidad>0:
            self.__cantidad+=cantidad
        else:
            print("No se puede ingresar una cantidad negativa")
    
    def retirar(self,cantidad):
        self.__cantidad-=cantidad
        if self.__cantidad<0:
            print("Cuenta en numeros rojos")        
            
cuenta1=cuenta("Matias Ramirez", 100.0)
cuenta1.mostrar()

cuenta1.ingresar(50.0)
cuenta1.mostrar()

cuenta1.retirar(200.0)
cuenta1.mostrar()

    
        
