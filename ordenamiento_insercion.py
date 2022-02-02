import random

# INSERTION SORT:
"""
+Es un algoritmo que toma un elemento y lo compara con cada elemento a su izquierda, realizando un intercambio cuando este sea mayor.
+La iteración de la lista comienza con un bucle for principal desde la posición 1, no cero.
+Se itera n veces por cada n elementos.
+Para iterar hacia la izquierda  necesito una segunda iteración con un bucle while ayudado por una variable que guarde la posición actual del índice del arreglo, este en cada repetición del ciclo irá descendiendo en -1.
+El segundo bucle se detiene cuando el indice de esta llegue a 0. Ya que no hay un valor a la izquierda de la posición cero.
+Cada vez que el valor en la posición izquierda [j-1], sea mayor a la posición actual [j], se realiza en intercambio de valorescon ayuda del almacenamiento en una variable temporal de un valor a sustituir.
+Como el ordenamiento se basa en empezar desde el inicio e ir acomodando hacia la izquierda, al momento de encontrar un valor a la izquierda que NO sea mayor, significa que el resto ya esta ordenado. Con esta condición podemos detener el bucle secundario.
"""

def insertion_sort(unordered_lista):

    for i in range(1, len(unordered_lista)): #Bucle principal. Inicia desde la posición 1.
        
        #Variable de ayuda para realizar una segunda iteración por cada elemento:
        #Almacena la posición del índice i, para ir disminuyendo en -1 e iterar en reversa hasta la posición 0.
        current_position = i

        #El loop se detiene al alcanzar la posición cero y cuando los valores a la izquierda son menores al elemento actual que se compara.
        while current_position > 0 and unordered_lista[current_position-1] > unordered_lista[current_position]:

        #Cada que el valor a la izquierda es mayor, realiza un intercambio ayudado por una variable temporal.
            temp_storage = unordered_lista[current_position]
            unordered_lista[current_position] = unordered_lista[current_position-1]
            unordered_lista[current_position-1] = temp_storage
            
            current_position -= 1

#Crear una lista con numeros aleatorios con "import random"
#Sin repetir valores.

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

if __name__ == '__main__':
    
    lista = create_random_lista()

    insertion_sort(lista)

    print(lista)
