import random

def busqueda_lineal(lista, valor):
    match = False
    for i in lista:
        if i == valor:
            match = True
            break
    return match    

#Crear una lista con numeros aleatorios:
tamano_lista = int(input("Tamano de la lista:\n "))
lista = []

for i in range(0,tamano_lista):
    lista.append(random.randint(0,100))    #Inserta al final
#lista.insert(0,random.randint(0,100))    #Inserta en el indice

print(f'Lista creada:\n {lista}\n')

lista.sort() #Ordena de menor a mayor
lista.sort(reverse=True) #Ordena de mayor a menor
lista_ordenada = sorted(lista) # Retorna una lista ordenada
lista_mayor_a_menor = sorted(lista, reverse=True) #Retorna una lista de mayor a menor

print(f'Lista ordenada:\n {lista}')
print(lista_ordenada)
print(lista_mayor_a_menor)

valor = int(input('Que valor desea encontrar: '))

if(busqueda_lineal(lista, valor)):
    print('El valor fue encontrado')

else:
    print("El valor no se encuentra")

    
#Eliminar último elemento.Retorna.
numero = lista.pop()

#Eliminar por índice. Retorna.
numero = lista.pop(0)

#Eliminar por valor. No retorna.
lista.remove(valor)

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