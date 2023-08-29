import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Ejercicio 1

def ejercicio1():
    iteraciones = 1000
    t_espera_total = []
    probabilidad = []                                                       #Array inicialmente vacio donde vamos a guardar un 1 en casa de que la iteracion sea menor a 32 minutos. Caso contrarios almacenaremos un 0
                                                                            #Luego sumamos todos los 1 y al dividirlo por la cantidad de iteraciones encontramos la probabilidad
    for i in range (iteraciones):
        t_preparacion = np.random.normal(loc = 25, scale = 7)
        t_delivery = np.random.uniform(low = 10, high = 20)
        t_espera_total.append(t_preparacion + t_delivery)
        if (t_preparacion + t_delivery < 32 ):  
            probabilidad.append(1)

    t_promedio = np.mean(t_espera_total)
    desvio = np.std(t_espera_total)

    print('El tiempo promedio de espera luego de las', iteraciones, 'iteraciones es de:', round(t_promedio, 3), 'minutos')
    print('El desvio estandar de es la espera luego de las', iteraciones, 'iteraciones es de:', round(desvio, 3), 'minutos')
    print('Para las', iteraciones, 'iteraciones realizadas, la probabilidad empirica de que el tiempo de espera sea menor a 32 minutos es de', sum(probabilidad)/iteraciones)

def ejercicio2():
    iteraciones = 10000 
    exitos = []                                                             #Por cada suma que cumpla que es mayor a 6, sumamos una unidad de exito para luego calcular la probabilidad total
    for i in range (iteraciones):
        dado1 = np.random.randint(1,5)                                      #Arrojamos dos dados de 4 caras perfectamente equilibrados --> Todas las caras con la misma probabilidad de ocurrencia
        dado2 = np.random.randint(1,5)
        if(dado1 + dado2 > 6):
            exitos.append(1)
    print('La probabilidad empirica de que la suma de ambos dados sea mayor a 6 es de:', sum(exitos)/iteraciones)

def ejercicio3():
    transicion = np.array([[0.7, 0.3],[0.4, 0.6]])
    transicion5 = np.array([[0.7, 0.3],[0.4, 0.6]]) #Inicialmente son iguales
    for i in range(5):
        transicion5 = np.dot(transicion, transicion5) 
        print(transicion5)
    print('La probabilidad de estado Alto en el tiempo 6 dado que en el 5 es baja sera de:', np.dot(np.array([0,1]),transicion5)[0])
    
ejercicio3()
