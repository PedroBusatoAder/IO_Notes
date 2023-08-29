import numpy as np
import picos 
import matplotlib.pyplot as plt

def ejercicio1():
    iteraciones = 10
    clicksSeleccion = np.zeros(4)                                       # Necesitamos 4 clicks en el proceso de seleccion
    clicksPago = np.zeros(7)                                            # Necesitamos 7 clicks en el proceso de pago 
    tiemposTotales = np.zeros(10)                                       # Almacenamos todos los tiempos totales que nos lleva hacer el proceos de compra completo

    for i in range(iteraciones):
        
        for x in range(4):                                              # Simulamos como una variable aleatoria los 4 clicks necesarios  
            clicksSeleccion[x] = np.random.exponential(1/30)
        
        for y in range(7):  
            clicksPago[y] = np.random.exponential(1/20)                 # Simulamos de igual manera los 7 clicks necesarios para el proceso de pago
        
        suma = sum(clicksPago) + sum(clicksSeleccion)
        tiemposTotales[i] = suma

    print('El tiempo promedio de compra luego de las', iteraciones, 'iteraciones es: ', np.mean(tiemposTotales))

ejercicio1()

def ejercicio2():
    print(
    # Estado del sistema --> "Presupuesto mensual de la compañía"

    # Eventos que modifican el estado del sistema
    # 1) Gastos mensuales de la compañía en sueldos, servicios e impuestos
    # 2) Ingresos mensuales de la compañía de la venta de servicios y consultorias

    # Funcion de transicion
    # presupuesto[tiempo i] = presupuesto[tiempo i - 1] - gastos mensuales de la compañía[tiempo i] + ingresos mensuales de la compañía[tiempo i]
    )
ejercicio2()


def ejercicio3():
    print(
    # A la hora de simular sistemas de filas de espera, las variables de aleatoria son dos:
    # "Cantidad de personas que arriban al modelo en un tiempo t" --> Tendra distribucion de Poisson(lamba = promedio de personas que arriban en tiempo t)
    # "Tiempo que se tarda en despachar a las personas del modelo" --> Tendra distribucion de Exponencial(lamba = 1/promedio de personas que se despachan en tiempo t)
    )
ejercicio3()