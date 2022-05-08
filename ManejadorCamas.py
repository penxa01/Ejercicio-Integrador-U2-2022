import numpy as np
from ClaseCamas import Cama
import os
import csv

class ManejadorCamas():
    __incremento = 5
    __cantidad = 0
    __dimension = 30
    __camas = None

    def __init__(self,dimension = 30, incremento = 5):
        self.__incremento = incremento
        self.__camas = np.empty(dimension,dtype = Cama)
    
    def agregarCamas(self,C):

        if (self.__cantidad == self.__dimension):
            self.__dimension += self.__incremento
            self.__camas.resize(self.__dimension)
        self.__camas[self.__cantidad] = C
        self.__cantidad += 1
    
    def CargarCamas(self):
        rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
        Archivo = os.path.join(rutaAbsoluta, "camas.csv")
        archivo = open(Archivo)
        reader = csv.reader(archivo,delimiter = ";")
        cabeza = True
        for comp in reader:
            if cabeza:
                cabeza = not cabeza
            else:
                NuevaCama = Cama(int(comp[0]),int(comp[1]),bool(comp[2]),comp[3],comp[4],comp[5])
                print(NuevaCama)
                self.agregarCamas(NuevaCama)
        
        archivo.close()

    def DarAlta(self,Medicamentos):
        print("Funcion sin terminar")
            



    def Listar(self):
        diagnostico = input("Ingrese diagnostico que desea\n")
        os.system("cls")
        print("Pacientes con diagnostico de {}".format(diagnostico))
        for i in range(30):
            if(self.__camas[i] != None):
                if (self.__camas[i].getEstado() == True):
                    if(self.__camas[i].getDiagnostico() == diagnostico):
                        print("".center(20,"-"))
                        print(self.__camas[i])
                        print("".center(20,"-"))


    def __str__(self):
        return ("{}".format(self.__camas))