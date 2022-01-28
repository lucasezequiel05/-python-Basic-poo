import random

class Persona:

    def __init__(self,name, last_name, age, country):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.__number = 40 #Solo se accede desde la clase. No desde la instancia
        self._color = 'blue' #Se accede desde la instancia y cualquier subclase
        self._dni = Dni()

    def __view_info(self):
        print(f'{self.name}\n{self.last_name}\n{self.age}\n{self.country}\n')

    @property
    def get_info(self):
        return self.__view_info()

    @property
    def get_dni_number(self):
        return print(f'{self.name} = dni {self._dni.number}')

# Clase Dni es una clase dentro de Persona.
# Genera una secuencia de números aleatorios, concatenando los enteros a un string mediante el pareo de str()
# Mediante range genero un ciclo que itera hasta 6 veces para adicionar los números a las cadenas que comenzaran con 30.

class Dni:
  
    def dni_create_number(self):

        dni_number = "30"        
        for n in range(0,6):
            number = random.randint(0,9)
            dni_number = dni_number + str(number)

        return dni_number

    def __init__(self):
        self.number = self.dni_create_number()

class Employer(Persona):

    def __init__(self, name, last_name, age, country):
        super().__init__(name, last_name, age, country)

class User(Persona):

    def __init__(self, name, last_name, age, country):
        super().__init__(name, last_name, age, country)

class Others(User):

    def __init__(self, name, last_name, age, country):
        super().__init__(name, last_name, age, country)
    
if __name__ == '__main__':

    david = Employer('david', 'ottamendi', 33, 'Argentina')
    jessica = User('jessica','cardinal',25,'Uruguay')

    #jessica.__view_info()  No accede al metodo privado.
    david.get_info

    sech = Persona('sech', 'armstrong', 40, 'USA')
    sech.get_info
    
    
    #print(david._color+'\n') #Accede al atributo protegido.
    #print(david.__number) No accede al atributo privado.

    regina = Others('regina', 'cambridge', 30, 'New Zeland')
    regina.get_info

    print(regina._color)

    david.get_dni_number
    jessica.get_dni_number
    sech.get_dni_number
    regina.get_dni_number
