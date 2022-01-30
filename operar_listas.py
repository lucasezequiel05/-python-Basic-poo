#Clase Para Listar Las Personas
class List_Persona_for_country:

    #Se declara una lista dentro de la estructura
    def __init__(self):
        self._list = []

    #Crea un objeto con los parámetros recibidos y los almacena en la lista
    def add_persona(self, name, country):
        self._list.append({'name':name, 'country': country})

    #Itera la lista y toma los datos de cada elemento para mostrarlos por pantalla
    def view_list(self):
        for element in self._list:
            name = element['name']
            country = element['country']
            print(f'Nombre = {name} => Country = {country}')
        print('\n')

    #Ordenar una lista de objetos
    #Muestra la lista ordenada por el campo Country
    def view_sorted_by_country(self):

        #Sorted(lista, key_function)
        #Recibe el elemento de cada iteración de la lista y un campo clave para comparar
        new_list = sorted(self._list, key= lambda element : element['country'])
        
        for element in new_list:
            name = element['name']
            country = element['country']
            print(f'Nombre = {name} => Country = {country}')
        print('\n')

    #Buscar la posición de un nombre
    #Iteracion por indice: for i in range (0,len(lista))
    def _search_index_name(self, value):

        position = -1
        #Longitud de la lista len( ):
        for index in range(0, len(self._list)):

            #Acceder al elemento y campo de un diccionario
            if (self._list[index]['name'] == value):
                position = index

        return position    

    #Quitar elemento de la lista
    def remove_persona_for_name(self,value):

        element = None
        position = self._search_index_name(value)
        
        if position >= 0:
            element = self._list.pop(position)
        
        return element

if __name__ == '__main__':
    
    