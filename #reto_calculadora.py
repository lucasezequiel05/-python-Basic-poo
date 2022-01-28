"""
Created 28-January-2021
by lucasezequiel05
"""
"""
+Se importan time para la toma de tiempos de la operación
+Se importa math para realizar las operaciones logarítmicas.
+El programa solicita el ingreso de un número y una opción,
 mostrando por pantalla resultado y el tiempo utilizado.
"""

import time
import math

class Calculadora:

    def __init__(self):
        pass

    def logarithm(self,n):
        return math.log10(n)

    def lineal(self,n):
        return n

    def n_logarithm(self,n):
        return n * math.log10(n)

    def square(self,n):
        return n**2

    def exponential(self,n):
        return 2**n


if __name__ == "__main__":

    #Crea instancia
    calculadora_math = Calculadora()

    #Se ingresan los valores convirtiendolos a enteros.
    number = int(input("Enter a number:\n"))
    print(f'You have entered: {number}\n')

    print("Select a operation (indicate the number):\n 1)lineal\n 2)logarithm\n 3)n_logarithm\n 4)square\n 5)exponential\n")
    option = int(input("\n"))

    #El bloque compara la opción correcta, toma los tiempos y muestra resultados.
    if option == 1:
        time_start = time.time()
        result = calculadora_math.lineal(number)
        time_end = time.time()
        print(f'Result = {result}\n Tiempo de la operación: {time_end-time_start}')        

    elif option == 2:
        time_start = time.time()
        result = calculadora_math.logarithm(number)
        time_end = time.time()
        print(f'Result = {result}\n Tiempo de la operación: {time_end-time_start}')        
    
    elif option == 3:
        time_start = time.time()
        result = calculadora_math.n_logarithm(number)
        time_end = time.time()
        print(f'Result = {result}\n Tiempo de la operación: {time_end-time_start}')        
    
    elif option == 4:
        time_start = time.time()
        result = calculadora_math.square(number)
        time_end = time.time()
        print(f'Result = {result}\n Tiempo de la operación: {time_end-time_start}')        
      
    elif option == 5:
        time_start = time.time()
        result = calculadora_math.exponential(number)
        time_end = time.time()
        print(f'Result = {result}\n Tiempo de la operación: {time_end-time_start}')        

    else:
        print("Invalid option")
    