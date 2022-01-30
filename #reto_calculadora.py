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

    #Decorador: timeis retorna una función wrapper
    #Agrega la funcionalidad de tomar los tiempos y devolver el resultado como el tiempo demorado.
    def _timeis(func):

        def wrapper(*args, **kwargs): #Se indica que recibirá parámetros
            time_start = time.time()
            result = func(*args, **kwargs) #Recibe los argumentos que se pasaron al llamar la funcion.
            time_end = time.time()
            print(f'Result = {result}\n Tiempo de la operación: {time_end-time_start}')

        return wrapper

    @_timeis
    def logarithm(self,n):
        return math.log10(n)

    @_timeis
    def lineal(self,n):
        return n

    @_timeis
    def n_logarithm(self,n):
        return n * math.log10(n)

    @_timeis
    def square(self,n):
        return n**2

    @_timeis
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

    #El bloque compara la opción correcta y ejecuta la operación.
    if option == 1:        
        result = calculadora_math.lineal(number)
        
    elif option == 2:        
        result = calculadora_math.logarithm(number)
        
    elif option == 3:        
        result = calculadora_math.n_logarithm(number)
        
    elif option == 4:        
        result = calculadora_math.square(number)
        
    elif option == 5:
        result = calculadora_math.exponential(number)
        
    else:
        print("Invalid option")
    