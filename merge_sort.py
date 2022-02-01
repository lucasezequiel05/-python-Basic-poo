
import random

def create_random_list():
    tamano_lista = int(input("Tamano de la lista:\n "))
    lista = []

    #Mientras que la longitud no alcanzo el tamano indicado
    #ramdon.randrange genera valores de 0 al doble del tamano de la lista para no generar números consecutivos. 
    #Si el valor no esta ya ingresado en la lista se ingresa al final.
    while len(lista) < tamano_lista:
            
        number = random.randint(0,tamano_lista*2)

        if number not in lista:
            lista.append(number)    #Inserta al final

    print(f'Lista creada:\n{lista}\n')
    return lista

def create_another_list(list):

    tamano_list = len(list) 
    new_list = []

    while tamano_list > 0:

        new_value = random.randint(0,100)
        if new_value not in list:
            new_list.append(new_value)
            tamano_list -=1

    return new_list


def delete_list(lista):
    del lista

def empty_list(lista):
    lista = []

#Suponemos dos listas ordenadas.
def fusion_list(lista_pri, lista_sec):
    #Necesito dos iteradores: uno para cada lista, iniciando en 0.
    i = 0
    j = 0

    #Declarar una nueva lista la cual recibira los elementos a través del método append().
    
    nueva_lista = list()

    """Explicación Lectura de dos listas a la vez:
    + Mientras ninguna de las dos listas haya alcanzado su longitud límite,
    se compara cada elemento i, j de cada lista.
    + Después de realizar la operación ( en este caso añadir el menor a una nueva lista)
    se incrementa el índice de una lista para pasar al siguiente elemento.
    
    + Cuando una lista no pueda seguir iterando se pasa al bloque correspondiente a la lista que tiene elementos.
    Este bloque inserta los elementos restantes uno a uno.
    También puedo utilizar el método extend()
    """
    while i < len(lista_pri) and j < len(lista_sec):

        if lista_pri[i] <= lista_sec[j]:
            nueva_lista.append(lista_pri[i])
            i += 1
        else:
            nueva_lista.append(lista_sec[j])
            j += 1

        print(nueva_lista)

    while i < len(lista_pri):
        nueva_lista.append(lista_pri[i])
        i += 1
    
    while j < len(lista_sec):
        nueva_lista.append(lista_sec[j])
        j += 1

    return nueva_lista

# def sort_and_merge(izquierda, derecha):

#     # Iteradores para recorrer las dos sublistas
#     i = 0
#     j = 0
#     # Iterador para la lista principal
#     k = 0
#     lista = []

#     while i < len(izquierda) and j < len(derecha):
#         print(f'****{izquierda[i]}***{derecha[j]}')
#         if izquierda[i] < derecha[j]:
#             lista.append(izquierda[i])
#             i += 1
#         else:
#             lista.append(derecha[j])
#             j += 1

#         k += 1

#     while i < len(izquierda):
#         lista.append(izquierda[i])
#         i += 1
#         k +=1

#     while j < len(derecha):
#         lista.append(derecha[j])
#         j += 1
#         k += 1
    
#     return lista

if __name__ == '__main__':

    lista_pri = create_random_list()

    lista_sec = create_another_list(lista_pri)

    lista_pri.sort()
    lista_sec.sort()

    nueva_lista = fusion_list(lista_pri, lista_sec)

    print(nueva_lista)


    print(nueva_lista)

    #Se puede sustituir un elemento accediendo a su indice, pero
    #No se puede ingresar un elemento nuevo incluso indicando un indice de espacio disponible.
    # k = 0
    # lista = [1,2,3,4,5]
    # lista[k] = 20
    # print(lista)