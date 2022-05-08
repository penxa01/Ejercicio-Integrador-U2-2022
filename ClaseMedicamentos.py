
class medicamento():
    __idCama = 0
    __idMedicamento = 0
    __nameComercial = " "
    __monodroga = " "
    __presentacion = " "
    __cantidadAplicada = 00
    __precioTotal = 0.0

    def __init__(self,idCama,idMed,nameC,monod,pres,cantApli,precio):
        self.__idCama = idCama
        self.__idMedicamento = idMed
        self.__nameComercial = nameC
        self.__monodroga = monod
        self.__presentacion = pres
        self.__cantidadAplicada = cantApli
        self.__precioTotal = precio
    
    

