import picos as picos
import numpy as np

def ejercicio1():
    P = picos.Problem() #Iniciamos el problema en picos

    x = picos.RealVariable('x', 2, lower = 0) #Cantidades producidas en la planta 1
    y = picos.RealVariable('y', 2, lower = 0) #Cantidades producidas en la planta 2

    ct1 = np.array([80,90]) #Costos de transporte de la planta 1
    ct2 = np.array([70,70]) #Costos de transporte de la planta 2

    P.set_objective('min', ct1.T * x + ct2.T * y + x[0] * 50 + x[1] * 50 + y[0] * 80 + y[1] * 80)

    #Restricciones de demanda --> Por mercado
    P.add_constraint(x[0] + y[0] == 1000)
    P.add_constraint(x[1] + y[1] == 500)

    #Restricciones de oferta --> Por planta
    P.add_constraint(x[0] + x[1] <= 200)
    P.add_constraint(y[0] + y[1] >= 200)
    P.add_constraint(x[1] >= 50) #De P1 a B se envian al menos 50 unidades


    print(P)
    P.solve()
    print(x, '\n')
    
    print('La cantidades a producir en la fabrica P1 son:')
    for i in range(len(x)):
        if i==0:
            print(x[i], 'unidades para el Mercado A')
        else:
            print(x[i], 'unidades para el Mercado B')
    
    print('')

    print('La cantidades a producir en la fabrica P2 son:')
    for i in range(len(y)):
        if i==0:
            print(y[i], 'unidades para el Mercado A')
        else:
            print(y[i], 'unidades para el Mercado B')

    print('Asi, la minimizacion del costos para las cantidades producidas es:', P.value)
ejercicio1()

def ejericio2(): #Hecho para verificar el correcto planteo del ejercicio unicamente
    P = picos.Problem()

    x = picos.BinaryVariable('x', 4)

    P.set_objective('min', x[0] + x[1] + x[2] + x[3])

    P.add_constraint(x[0] + x[1] + x[3] >= 1) #'Al menos' una estacion --> Desigualdad en vez de igualdad estricta
    P.add_constraint(x[0] + x[1] >= 1)
    P.add_constraint(x[2] + x[3] >= 1)
    P.add_constraint(x[0] + x[2] + x[3] >= 1)

    P.solve()

    print(x)
ejericio2()

