import random

def confirmation_message(func):

    def wrapper(*args, **kwargs):
        if(func(*args, **kwargs)):
            print('El valor se encuentra dentro de la lista')
        else:
            print("El valor no se encuentra")

    return wrapper

@confirmation_message
def busqueda_lineal(lista, valor):
    match = False
    for i in lista:
        if i == valor:
            match = True
            break
    return match    

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

if __name__ == '__main__':

    lista = create_random_list()

#Métodos para ordenamiento

    #Ordenar de menor a mayor la lista sin retornar una nueva sort():
    lista.sort()
    #Retornar una lista ordenada sorted(lista):
    lista_ordenada = sorted(lista)

    print(f'Lista ordenada:\n{lista}\n')
    
    #Ordenar de mayor a menor con parámetro reverse=True 
    lista.sort(reverse=True)
    lista_mayor_a_menor = sorted(lista, reverse=True)

    print(f'Lista ordenada de Mayor a Menor:\n{lista_mayor_a_menor}\n')

    valor = int(input('Que valor desea encontrar: '))

    busqueda_lineal(lista, valor)

#Métodos para eliminar elementos:

    #Quitar el último elemento y lo Retorna.
    # numero = lista.pop()

    #Quitar elementos por índice y lo Retorna.
    # numero = lista.pop(0)

    #Eliminar por valor. No retorna.
    # lista.remove(valor)

#Ordenar Lista de Objetos por campos:

#Sorted puede recibir el parámetro key el cual recibe una función que se ejecuta en cada elemento iterado.
#Esta función recibe un parámetro y retorna una clave para tener en cuenta en la comparación

    lista_objetos = [
        {'color':'negro',
        'numero':20},
        {'color':'azul',
        'numero':55},
        {'color':'fucsia',
        'numero':5},
        {'color':'blanco',
        'numero':17}
        ]
"""
#En el caso de diccionarios se define la palabra del campo
lista_objetos_ordenada = sorted(lista_objetos, key=lambda elemento : elemento['numero'])
print(lista_objetos_ordenada)

#Para las listas o tuplas el indice
lista_objetos_ordenada = sorted(lista_objetos, key=lambda elemento : elemento[indice])
print(lista_objetos_ordenada)

#Para los objetos instanciados el campo
lista_objetos_ordenada = sorted(lista_objetos, key=lambda elemento : elemento.campo)
print(lista_objetos_ordenada)
"""