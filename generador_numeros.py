"""
Objetivo de la clase es generar números de identificación aleatorios
para cada Persona.
+ la clase se convierte en un objeto dentro de otra clase.
+ el módulo random permite generar números aleatorios con random.randint(inicio,hasta)
+ El ciclo for permite generar 6 números utilizando range(desde, hasta)
los cuales seran parseados a string con str( ) y luego contatenados.
"""

import random

class Dni:
  
    def __init__(self):
        self.number = self.dni_create_number()


    def dni_create_number(self):

        dni_number = "30"        
        for n in range(0,6):
            number = random.randint(0,9)
            dni_number = dni_number + str(number)

        return dni_number

if __name__ == '__main__':
    
    carlos = Dni()
    print(carlos.number)
