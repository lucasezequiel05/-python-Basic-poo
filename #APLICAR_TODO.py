from curses import wrapper
import random

#Aplica para mediro el tiempo del programa en segundos mediante time.time()
import time

class Persona:

    def __init__(self,name, last_name, age, country):
        self._name = name.lower()
        self._last_name = last_name.lower()
        self._age = age
        self._country = country.lower()
        self.__number = 40 #Solo se accede desde la clase. No desde la instancia
        self._color = 'blue' #Se accede desde la instancia y cualquier subclase
        self._dni = Dni()

    #Por ser un método privado solo la clase Persona accede a él.
    #Pero al decorar la función get_info se permite el acceso desde sus instancias.
    def __view_info(self):
        print(f'{self._name}\n{self._last_name}\n{self._age}\n{self._country}\n')

    @property
    def get_info(self):
        return self.__view_info()

    @property
    def get_dni_number(self):
        return print(f'{self._name} = dni {self._dni.number}')

    @property
    def get_name(self):
        return self._name

    @property
    def get_country(self):
        return self._country

# Clase Dni es una clase dentro de Persona.
# Genera una secuencia de números aleatorios, concatenando los enteros a un string mediante el pareo de str()
# Mediante range genero un ciclo que itera hasta 6 veces para adicionar los números a las cadenas que comenzaran con 30.

class Dni:
  
    def dni_create_number(self):

        dni_number = "30"        
        for n in range(0,6):
            #Se generan los números desde cero a nueve inclusive.
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

#Clase Para listar Las Personas
class lista_Persona_for_country:

    #Se declara una lista dentro de la estructura
    def __init__(self):
        self._lista = []

    #Crea un objeto con los parámetros recibidos y los almacena en la lista
    def add_persona(self, name, country):
        self._lista.append({'name':name, 'country': country})

    #Itera la lista y toma los datos de cada elemento para mostrarlos por pantalla
    def view_lista(self):
        for element in self._lista:
            name = element['name']
            country = element['country']
            print(f'Nombre = {name} => Country = {country}')
        print('\n')
    
    #Vaciar contenido de la lista
    def clear_lista(self):
        self._lista.clear()
        print('-'*5, ' The lista is empty ','-'*5)

    #Ordena la lista de objetos y la almacena en memoria.
    #Muestra la lista ordenada por el campo Country
    def sorted_lista_by_country(self):

        #Sorted(lista, key_function)
        #Recibe el elemento de cada iteración de la lista y un campo clave para comparar
        new_lista = sorted(self._lista, key= lambda element : element['country'])
        self._lista = new_lista #Reemplazo lista en memoria

        for element in new_lista:
            name = element['name']
            country = element['country']
            print(f'Nombre = {name} => Country = {country}')
        print('\n')

    #Buscar la posición de un nombre
    #Iteracion por indice: for i in range (0,len(lista))
    def _search_index_name(self, value):

        position = -1
        #Longitud de la lista len( ):
        for index in range(0, len(self._lista)):

            #Acceder al elemento y campo de un diccionario
            if (self._lista[index]['name'] == value):
                position = index

        return position    

    #Quitar elemento de la lista
    def remove_persona_for_name(self,value):

        element = None
        position = self._search_index_name(value)
        
        if position >= 0:
            element = self._lista.pop(position)
        
        return element

    def get_persona_by_position(self, position_persona):
        return self._lista[position_persona]    

    #Realizar Búsqueda binaria por país
    def binary_search_by_country(self, value_country):
        
        value_country = value_country.lower() #Convierte a minúscula
        position = -1

        start_point = 0
        end_point = len(self._lista)-1
        mid_point = (start_point+end_point)//2

        while start_point <= end_point and position == -1:
            
            if value_country == self._lista[mid_point]['country']:
                position = mid_point
            elif value_country < self._lista[mid_point]['country']:
                end_point = mid_point -1
                mid_point = (start_point + end_point)//2
            elif value_country > self._lista[mid_point]['country']:
                start_point = mid_point +1
                mid_point = (start_point + end_point)//2
        
        return position

if __name__ == '__main__':

    tiempo_inicio = time.time()

    david = Employer('david', 'ottamendi', 33, 'Argentina')
    jessica = User('jessica','cardinal',25,'Uruguay')

    #jessica.__view_info()  No accede al metodo privado.
    david.get_info

    sech = Persona('sech', 'armstrong', 40, 'USA')
    sech.get_info
    
    anastasia = Persona('anastasia', 'romanof', 33, 'Rusia')

    #print(david._color+'\n') #Accede al atributo protegido.
    #print(david.__number) No accede al atributo privado.

    regina = Others('regina', 'cambridge', 30, 'New Zeland')
    regina.get_info

    oswald = Others('oswald', 'wellington', 31, 'Canada')

    print(regina._color)

    david.get_dni_number
    jessica.get_dni_number
    sech.get_dni_number
    regina.get_dni_number

    tiempo_fin = time.time()
    print(f'Se demoró {tiempo_fin-tiempo_inicio} segundos.')

    #listar las personas

    lista_personas = lista_Persona_for_country()

    lista_personas.add_persona(david.get_name,david.get_country)
    lista_personas.add_persona(jessica.get_name,jessica.get_country)
    lista_personas.add_persona(sech.get_name,sech.get_country)
    lista_personas.add_persona(regina.get_name,regina.get_country)
    lista_personas.add_persona(anastasia.get_name,anastasia.get_country)
    lista_personas.add_persona(oswald.get_name,oswald.get_country)

    lista_personas.sorted_lista_by_country()

    elem_position = lista_personas.binary_search_by_country('new ZEland')
    print(elem_position)
    print(lista_personas.get_persona_by_position(elem_position))

    out = lista_personas.remove_persona_for_name('david')
    print(out)
  