from bokeh.plotting import figure, output_file, show

#De bokeh.plotting ("graficado") se importan 3 funciones
# + figure = La ventana donde vamos a graficar y determinar las caracteristicas de la figura.
# + output_file = Permite determinar el nombre del archivo que generaremos como output (.html para visualiza desde el buscador)
# + show = Permite generar un servidor que al encenderlo muestra nuestro archivo.

if __name__ == '__main__':

    output_file('graficado_simple.html')    #Se declara el nombre del archivo de salida
    fig = figure()         #Para instanciar figura donde se generarán los gráficos

    #Se pregunta al usuario cuando valores graficar x, y:
    #Lista de valores
    total_vals = int(input("¿Cúantos valores quieres graficar?"))
    x_vals = list(range(total_vals)) 
    y_vals = []

    for i in x_vals:
        val = int(input(f'Ingrese el valor Y para X:'))
        y_vals.append(val)

#Cada grafica tiene ciertos requisitos para su graficado:
# En este caso dos arrays.
# La propiedad line_width es el espesor de la línea
# El método .line() recibe los valores para la figura.

    fig.line(x_vals, y_vals, line_width=2)

# show( ) muestra la figur 
    show(fig)

#PARA EJECUTAR:
# Desde la terminal, se ingresa y ubica en la carpeta donde se generó el entorno, 
# se activa con source env/bin/activate
# Se ejecuta el programa a través del comando python3.8 nombre_archivo.py
