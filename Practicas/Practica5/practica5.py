# -- Guia de Ejercicios 5 - Simulacion de Eventos Discretos y Sistemas de Filas -- ##
import numpy as np
import matplotlib.pyplot as plt
def ejercicio1():
    n = 100                                                                             #Cantidad de dias de operaciones que se simulan
    inventarioDiario = np.zeros(n)
    inventarioDiario[0] = 200

    for i in range(1,n):
        arriboPallets = np.random.poisson(lam = 170)
        DespachoPallets = np.random.poisson(lam = 160)
        inventarioDiario[i] = inventarioDiario[i-1] + arriboPallets - DespachoPallets   #Esta es nuestra funcion de transicion

    print('La probabilidad de que el inventario sea menor a 200 en los dias transcurridos es de:', sum(inventarioDiario < 200)/n)
    print('El inventario promedio en los', n, 'dias fue:', np.mean(inventarioDiario))

    plt.bar(np.arange(n), inventarioDiario)
    plt.xlabel('Dias')
    plt.ylabel('Cantidad Stock')
    plt.xlim(0,n)
    plt.axhline(y= np.mean(inventarioDiario), color='r', linestyle='--')
    plt.show()

def ejercicio2(): #No entendi lo que pide en el inciso d)
    n = 1000
    totalArribos = np.zeros(n)
    for i in range(n):
        arribo = np.random.exponential(scale = 1/7)  #Estamos trabajando con el tiempo en horas! --> Siete clientes por hora
        totalArribos[i] = round(arribo, 2)
    print('La probabilidad de que el tiempo entre dos arribos sea mayor a 10 minutos es:', sum(totalArribos > (1/6))/n)  #Debemos colocar los minutos en horas ya que el parametro lambda esta expresado en horas!
    print('La probabilidad de que el tiempo entre dos arribos sea menor a 5 minutos es:', sum(totalArribos < (1/12))/n)  

    #Ploteamos los 1000 tiempos de llegada
    plt.bar(np.arange(0,n), totalArribos)
    plt.xlabel('Numero de arribo')
    plt.ylabel('Tiempo entre arribos (en horas)')
    plt.show()

def ejercicio3():
    n = 10000
    clientesAtendidos = np.zeros(n)
    clientesLlegados = np.zeros(n)
    for i in range(n):
        clienteLlega = np.random.exponential(1/3)
        clienteAtendido = np.random.exponential(1/2)

ejercicio3()
