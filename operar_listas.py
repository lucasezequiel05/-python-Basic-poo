#Clase Para listar Las Personas
class lista_Persona_for_country:

    #Se declara una lista dentro de la estructura
    def __init__(self):
        self._lista = []

    #Crea un objeto con los parámetros recibidos y los almacena al final de la lista
    def add_persona(self, name, country):
        self._lista.append({'name':name, 'country': country})

    #Ver el contenido de la lista
    #Itera la lista y toma los datos de cada elemento para mostrarlos por pantalla
    def view_lista(self):
        for element in self._lista:
            name = element['name']
            country = element['country']
            print(f'Nombre = {name} => Country = {country}')
        print('\n')

    #Ordenar una lista de objetos
    #Muestra la lista ordenada por el campo Country
    def view_sorted_by_country(self):

        #Sorted(lista, key_function)
        #Recibe el elemento de cada iteración de la lista y un campo clave para comparar
        new_lista = sorted(self._lista, key= lambda element : element['country'])
        
        for element in new_lista:
            name = element['name']
            country = element['country']
            print(f'Nombre = {name} => Country = {country}')
        print('\n')

    #Mediante BÚSQUEDA LINEAL:
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

    #Quitar elemento de la lista y retornarlo.
    def remove_persona_for_name(self,value):

        element = None
        position = self._search_index_name(value)
        
        if position >= 0:
            element = self._lista.pop(position)
        
        return element

if __name__ == '__main__':
    
    pass