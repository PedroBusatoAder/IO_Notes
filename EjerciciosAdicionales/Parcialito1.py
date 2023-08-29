'''

<-- Ejercicios adicionales de las clases tutoriales de Lucas -->

'''

import picos
import numpy as np

def ejercicio1(): #Problema de Transhipment
    P = picos.Problem()
    
    c1 = np.array([10000, 10000])                    #Costos de productir los autos en cada una de las plantas
    c2 = np.array([1253, 637, 1398, 841])            #Costos de envio de las plantas a los warehouse
    c3 = np.array([1059, 996, 1691, 2786, 802, 100]) #Costos de envio de los warehouse a los clientes

    x = picos.IntegerVariable('x', 2, lower = 0)
    y = picos.IntegerVariable('y', 4, lower = 0)     #Cantidad de autos enviados a cada uno de los warehouse
    z = picos.IntegerVariable('z', 6, lower = 0)     #Cantidad de autos enviados a cada uno de los consumidores finales

    P.set_objective('min', c1.T * x + c2.T * y + c3.T * z)

    #Restricciones de oferta
    P.add_constraint(x[0] <= 150) #Detroir puede producir hasta 150 autos a la semana
    P.add_constraint(x[1] <= 100) #Atlanta puede producir hasta 100 autos a la semana

    #Restricciones de demanda
    P.add_constraint(z[0] + z[3] == 80)
    P.add_constraint(z[1] + z[4] == 70)
    P.add_constraint(z[2] + z[5] == 60)

    #Restricciones de control de flujo
    P.add_constraint(x[0] == y[0] + y[1])               #Lo que se manda desde Detroir debe ser igual a lo producido alli
    P.add_constraint(x[1] == y[2] + y[3])               #Lo que se manda desde Atlanta debe ser igual a los producido alli
    P.add_constraint(y[0] + y[2] == z[0] + z[1] + z[2]) #Lo que sale de Denver es igual a lo que llega alli
    P.add_constraint(y[1] + y[3] == z[3] + z[4] + z[5]) #Lo que sale de Nueva York es igual a lo que llega all

    print(P)

    P.solve()

    print('\nPara satisfacer la demanda de Ford al precio minimo debemos producir: ')
    for i in range(len(x)):
        if i == 0:   
            print(x[i], 'autos en la planta de Detroit')
        else:
            print(x[i], 'autos en la planta de Atlanta')
    
    recibidosDenver = 0
    recibidosNY = 0
    
    print('\nDe los cuales:')
    for i in range(len(y)):
        if(i == 0 or i == 2):
            recibidosDenver += y[i]
        else:
            recibidosNY += y[i]
    print(recibidosDenver, 'son recibidos por Denver')
    print(recibidosNY, 'son recibidos por Nueva York')

    recibidosLA = 0
    recibidosChicago = 0
    recibidosPhili = 0

    print('\nY de alli son enviados a: ')
    for i in range(len(z)):
        if(i == 0 or i == 3):
            recibidosLA += z[i]
        elif(i == 1 or i == 4):
            recibidosChicago += z[i]
        else:
            recibidosPhili += z[i]
    print('Los Angeles en', recibidosLA, 'unidades')
    print('Chicago en', recibidosChicago, 'unidades')
    print('Philadelphia en', recibidosPhili, 'unidades')
    
#ejercicio1()

def ejercicio1Forma2():  #Cambiando las variables y consecuentemente las restricciones, llegamos al mismo resultado
    P = picos.Problem()
    y = picos.IntegerVariable('y', 2, lower = 0)  #Cantidad de autos producidos en cada planta
    x = picos.IntegerVariable('x', 10, lower = 0) #Cada variable de decision son los autos transportados entre nodos

    cp = np.array([10000,10000]) #Costos de produccion
    ct = np.array([1253, 637, 1398, 841, 1059, 996, 1691, 2786, 802, 100]) #Costos de transporte entre nodos

    P.set_objective('min', ct.T * x + (x[0] + x[1]) * 1000 + (x[2] + x[3]) * 1000)

    #Restricciones
    P.add_constraint(x[0] + x[1] <= 150)
    P.add_constraint(x[2] + x[3] <= 100)

    P.add_constraint(x[0] + x[2] == x[4] + x[5] + x[6]) #Todo lo que llegar a Denver, debe salir
    P.add_constraint(x[1] + x[3] == x[7] + x[8] + x[9]) #Todo lo que llegar a Nueva York, debe salir

    P.add_constraint(x[4] + x[7] == 80) #Demanda de Los Angeles
    P.add_constraint(x[5] + x[8] == 70) #Demanda de Chicago
    P.add_constraint(x[6] + x[9] == 60) #Demanda Philadelphia

    P.solve()

    print(x)

#ejercicio1Forma2()

def ejercicio2():
    P = picos.Problem()

    c = np.array([400, 650, 200, 350, 550, 700, 300, 500, 300, 600, 400, 450]) #Distancia/2 ya que cada milla cuesta 0.5 centimos
    fc = np.array([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    
    y = picos.BinaryVariable('y', 12) #Variables de activacion del costos fijo de 100$
    x = picos.IntegerVariable('x', 12, lower = 0)

    P.set_objective('min', c.T * x + fc.T * y)

    #Restricciones de Oferta
    P.add_constraint(x[0] + x[1] + x[2] + x[3] <= 12) #Capacidad maxima de produccion de la planta 1
    P.add_constraint(x[4] + x[5] + x[6] + x[7] <= 17) #Capacidad maxima de produccion de la planta 2
    P.add_constraint(x[8] + x[9] + x[10] + x[11] <= 11) #Capacidad maxima de produccion de la planta 3
    
    #Restricciones de Demanda
    P.add_constraint(x[0] + x[4] + x[8] == 10)
    P.add_constraint(x[1] + x[5] + x[9] == 10)
    P.add_constraint(x[2] + x[6] + x[10] == 10)
    P.add_constraint(x[3] + x[7] + x[11] == 10)

    #Restricciones de activacion de costos fijos
    for i in range(len(y)):
        P.add_constraint(x[i] <= 1000*y[i])

    print(P)
    
    P.solve()
    print(x)
    print('La planta 1 produzco:' , x[0] + x[1] + x[2] + x[3])
    print('La planta 2 produzco:' , x[4] + x[5] + x[6] + x[7])
    print('La planta 3 produzco:' , x[8] + x[9] + x[10] + x[11])

    print('')

    print('El centro de distribucion 1 recibio:', x[0] + x[4] + x[8])
    print('El centro de distribucion 2 recibio:', x[1] + x[5] + x[9])
    print('El centro de distribucion 3 recibio:', x[2] + x[6] + x[10])
    print('El centro de distribucion 4 recibio:', x[3] + x[7] + x[11])

#ejercicio2()

def ejercicio3(): #Problema de Shortest Path
    P = picos.Problem()

    x = picos.BinaryVariable('x', 7)
    c = picos.Constant('c', [2, 8, 5, 6, 4, 12, 10])

    P.set_objective('min', c.T * x)

    #Restricciones --> Restricciones de control de flujo
    P.add_constraint(x[0] + x[1] == 1)
    P.add_constraint(x[0] == x[2] + x[4] + x[5])
    P.add_constraint(x[1] + x[2] == x[3])
    P.add_constraint(x[3] + x[4] == x[6])
    P.add_constraint(x[5] + x[6] == 1)

    print(P)
    P.solve()

    print(x)
    print('El camino mas corto entre el nodo de incio y el final fue el compuesto por los arcos correspondientes a:')
    for i in range(len(x)):
        if round(x[i]) == 1:
            print('x[' + str(i) + ']')
ejercicio3()