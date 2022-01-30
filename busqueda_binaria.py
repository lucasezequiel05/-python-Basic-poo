import random

"""
+ BÚSQUEDA BINARIA: Retorna la posición del elemento encontrado. De no hacerlo -1.

+ Condición necesaria que la lista este ordenada. Método sort( )
+ De necesitar varias busquedas se recomienda ordenar la lista y almacenarla ( sorted ())

+ Inicia en la pos 0 y el final es en la posición longitud de la lista-1 evitando salir del alcance de la misma.
+ El valor medio es la suma de los extremos dividido por enteros en 2
+ El loop itera mientras los puntos de referencia no se crucen y la posición permanezca con su valor por defecto.
En el peor de los casos los puntos de referencia apuntaran a la misma posición por lo que es necesario indicar que pueden ser iguales.

+ Si el valor buscado es menor al valor encontrado en el punto medio. Se modifican los puntos de referencia, se
Se desestima el bloque de la derecha y se toma como punto final el punto medio-1.
+Si por el contrario el valor del punto medio es menor al valor buscado, Se modifica el punto de inicio en medio+1.
"""

def busqueda_binaria(lista_ordenada,valor):

    position = -1 #Retorna -1 en caso de no hayar el elemento

    inicio = 0
    fin = len(lista_ordenada)-1
    medio = (inicio + fin) // 2
    num_paso = 0 #Contador de pasos
    
    while inicio <= fin and position == -1:

        num_paso+=1
        print(f'Paso numero: {num_paso}\n Se busca entre pos.inicio {inicio} y pos.fin {fin}\n Posicion medio: {medio}, Valor[medio] = {lista_ordenada[medio]}\n')
        
        if lista_ordenada[medio] == valor:
            position = medio
            
        elif lista_ordenada[medio] < valor:
            inicio = medio+1
            medio = (inicio + fin)//2

        elif lista_ordenada[medio] > valor:
            fin = medio-1
            medio = (inicio + fin)//2        
    
    return position

#---------------------------------------------------------------------------------

#Crear una lista con numeros aleatorios con "import random"
def create_random_list():
    tamano_lista = int(input("Tamano de la lista:\n "))
    lista = []

    for i in range(0,tamano_lista):
        lista.append(random.randint(0,100))    #Inserta al final
        #lista.insert(0,random.randint(0,100))    #Inserta en el indice

    print(f'Lista creada:\n{lista}\n')
    return lista

def create_list():
    tamano_lista = int(input("Tamano de la lista:\n "))
    lista = []

    for i in range(0,tamano_lista):
        lista.append(i+1)    
    
    print(f'Lista creada:\n{lista}\n')
    return lista

if __name__ == '__main__':

    lista = create_random_list()
    #lista = create_list()

    #Retornar una lista ordenada sorted(lista):
    lista_ordenada = sorted(lista)
    print(f'Lista ordenada:\n{lista_ordenada}\n')
    
    valor = int(input('Que valor desea encontrar: '))

    position = busqueda_binaria(lista_ordenada, valor)
    print(f'El valor se encuentra en la posición {position}')
