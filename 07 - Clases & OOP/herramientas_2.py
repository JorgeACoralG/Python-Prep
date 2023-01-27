class Herramientas:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def __factorial (self, numero):
        if (type(numero) != int):
            return 'El dato debe ser un entero'
        elif (numero < 0):
            return 'El numero debe ser positivo'
        elif (numero == 0):
            return 1
        elif (numero > 1):
            numero = numero * self.__factorial (numero - 1)
        return numero
  
    def factorial (self):
        for i in self.lista:
            print ('El factorial de ', i, 'es: ', self.__factorial(i))

    
    
    def validar_primo (self):
        for i in self.lista:
            if (self.__validar_primo(i)):
                print('El numero almacenado en ', i, 'si es un numero primo')
            else:
                print('El numero almacenado en ', i, 'no es un numero primo')
        
    def __validar_primo (self, numero):
        primo = True
        for i in range (2, numero):
            if numero % i == 0:
                primo = False
                break
        return primo

    

    def convertir_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__convertir_grados(i, origen, destino), 'grados', destino)

    
    def __convertir_grados (self, valor, origen, destino):
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheith'):
                valor_destino = (valor * 9/5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print ('paramero de destino es incorrecto')
        elif (origen == 'farenheith'):
            if (destino == 'farenheith'):
                valor_destino = valor
            elif (destino == 'celsius'):
                valor_destino = (valor - 32) * 5/9
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print ('parametro de destino es incorrecto')    
        elif (origen == 'kelvin'):
            if (destino == 'kelvin'):
                valor_destino = valor
            if ( destino == 'farenheith'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            if (destino == 'celsius'):
                valor_destino = (valor - 273.15)
            else:
                print ('parametro de destino incorrecto')
        else:
            print ('parametro de origen incorrecto')
        return valor_destino


    def Func_Num_Mas_Repite (self):
    
        Lis_Num_Unicos = []
        Lis_Num_Repetidos = []
        
        if len(self.lista) == 0:
            return None     
               
        for Num_A_Evaluar in self.lista: 
            if Num_A_Evaluar in Lis_Num_Unicos: 
                i = Lis_Num_Unicos.index(Num_A_Evaluar) 
                Lis_Num_Repetidos [i] += 1 
            else:
                Lis_Num_Unicos.append (Num_A_Evaluar) 
                Lis_Num_Repetidos.append(1) 

        moda = Lis_Num_Unicos [0] 
        maximo = Lis_Num_Repetidos [0]

        for i, Num_A_Evaluar in enumerate(Lis_Num_Unicos): 
            if Lis_Num_Repetidos[i] > maximo: 
                
                moda = Lis_Num_Unicos[i]
                maximo = Lis_Num_Repetidos[i]
        
        return moda, maximo