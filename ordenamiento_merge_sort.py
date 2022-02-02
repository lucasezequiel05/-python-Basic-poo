
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

def merge_sort(lista):

    #PRIMERA ETAPA:
    # + Recibir una lista, obtener su punto medio y crear dos sublistas
    # + La función recursiva divide las listas hasta que quede en un elemento
    
    if len(lista)>1:
        middle_point = len(lista)//2
        left = lista[:middle_point] #retorna una lista con los valores desde el inicio, excluyendo el indice indicado.
        right = lista[middle_point:] #retorna una lista con los valores del indice incluido hasta el final.
        
        print('*'*5,left,'*'*5,right,'*'*5)

    # Etapa recursiva se ejecutarà hasta que los elementos no puedan dividirse y comiencen a retornar un elemento individual.    
        value_left = merge_sort(left) 
        value_right = merge_sort(right)

    #SEGUNDA ETAPA: Unir los bloques
    # + Cada bloque unido y ordenado lo retorno como una lista nueva.
    # + A esta lista temporal se le irán insertando los valores ordenados.
    # + Necesito dos iteradores para leer valor a valor y comparar dos listas a la vez.
    
        i = 0
        j = 0    

        temp_lista = lista() 

        #Se recorren ambas listas accediendo a cada valor con el indice e incrementandolo al
        #siguiente valor para seguir comparando.
        # La condición es que ambas listas tengan aún elementos por recorrer. 
        while i < len(value_left) and j < len(value_right): 

            if value_left[i] <= value_right[j]:
                temp_lista.append(value_left[i])
                i += 1
            else:
                temp_lista.append(value_right[j])
                j += 1
        
        #Cuando quedan elementos solo en una de las listas, esta se recorre hasta agregar todos los elementos restantes
        # a la lista armada.
        while i < len(value_left):
            temp_lista.append(value_left[i])
            i += 1

        while j < len(value_right):
            temp_lista.append(value_right[j])
            j += 1

        print('-'*3,temp_lista,'-'*3)
        return temp_lista

    #Cuando las sublistas lleguen a contar con un elemento retorna una lista de un valor.
    if len(lista)<=1:
        print('Retorna:','*'*5,lista,'*'*5)
        return lista 

if __name__ == '__main__':

    lista_pri = create_random_lista()
    
    nueva_lista = merge_sort(lista_pri)

    print('\n', lista_pri)
    print('\n', nueva_lista)
    