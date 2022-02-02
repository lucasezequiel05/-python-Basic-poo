import random

def create_random_lista():
    tamano_lista = int(input("Tamano de la lista:\n "))
    lista = []

    #Mientras que la longitud no alcanzo el tamano indicado
    #ramdon.randrange genera valores de 0 al doble del tamano de la lista para no generar números consecutivos. 
    #Si el valor no esta ya ingresado en la lista se ingresa al final.
    while len(lista) < tamano_lista:
            
        number = random.randint(0,tamano_lista*2)

        if number not in lista:
            lista.append(number)    #Inserta al final

    print(f'lista creada:\n{lista}\n')
    return lista

# Crear una lista con valores que no se encuentran en otra lista ya existente
def create_another_lista(lista):

    tamano_lista = len(lista) 
    new_lista = list()

    for i in range(0, tamano_lista):

        new_value = random.randint(0,100)
        if new_value not in lista:
            new_lista.append(new_value)
            tamano_lista -=1

    print(f'lista creada:\n{new_lista}\n')
    return new_lista

#Función para unir el contenido de dos listas en valores ordenados.
#Se deben recibir ambas listas ordenadas.
def fusion_lista(lista_pri, lista_sec):
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

if __name__ == '__main__':

    lista_pri = create_random_lista()
    lista_sec = create_another_lista(lista_pri)

    lista_pri.sort()
    lista_sec.sort()

    print('\n Primer Lista: ', lista_pri,'\n')
    print('\n Segunda Lista: ', lista_sec,'\n')

    nueva_lista = fusion_lista(lista_pri, lista_sec)

    print('\n', nueva_lista)
    