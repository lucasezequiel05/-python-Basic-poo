#BUBBLE SORT: Itera una lista de n elementos por n veces cada elemento.

import random

#Crear una lista con numeros aleatorios con "import random"
def create_random_lista():
    tamano_lista = int(input("Tamano de la lista:\n "))
    lista = []

    for i in range(0,tamano_lista):
        lista.append(random.randint(0,100))    #Inserta al final

    print(f'lista creada:\n{lista}\n')
    return lista

def bubble_sort(lista):
    
    lista_len = len(lista)
    print(f'len = {lista_len}')

    #for - range inicia iterando en 0 pero se detiene al llegar al valor máximo. No saliendo del indice permitido.
    for i in range(lista_len):
        print(f'i = {i}')

    #Voy a iterar hasta el último índice permitido pero le resto uno para poder comparar la posición j+1 sin salir del límite de la lista.
    #A su vez resto i para dejar fuera de comparación los últimos elementos ya ordenados. En el primer ciclo i = 0, ya en el segundo es i = 1 y así sucesivamente.
        for j in range(lista_len -1 -i):

            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista

if __name__ == '__main__':

    lista = create_random_lista()
    print(lista)
    lista_ordenada = bubble_sort(lista)
    print(lista_ordenada)
