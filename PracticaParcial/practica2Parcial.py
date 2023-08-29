import picos
import numpy as np

def ejercicio2():
    P = picos.Problem()

    objFun = 0

    x = picos.IntegerVariable('x', 30, lower=0) #'xij' es la cantidad de producto enviada del nodo 'i' al nodo 'j'

    #Forma 1 de hacerlo
    c = np.array([13,10,22,29,18,0,14,13,16,21,1000,0,3,0,1000,11,6,0,18,9,19,23,11,0,30,24,34,36,28,0])
    c = picos.Constant('c', c, (1,30))      #Lo traspongo directo aqui
    print(c.shape)                          #1 fila con 30 columnas

    for i in range(len(x)):
        objFun += c[i] * x[i]

    P.set_objective('min', objFun)

    #Restricciones de oferta
    P.add_constraint(0 <= x[0] + x[1] + x[2] + x[3] + x[4] + x[5] <= 5)
    P.add_constraint(0 <= x[6] + x[7] + x[8] + x[9] + x[10] + x[11] <= 6)
    P.add_constraint(0 <= x[12] + x[13] + x[14] + x[15] + x[16] + x[17] <= 7)
    P.add_constraint(0 <= x[18] + x[19] + x[20] + x[21] + x[22] + x[23] <= 4)
    P.add_constraint(0 <= x[24] + x[25] + x[26] + x[27] + x[28] + x[29] <= 3)
    
    #Restricciones de demanda   
    P.add_constraint(x[0] + x[6] + x[12] + x[18] + x[24] == 3)
    P.add_constraint(x[1] + x[7] + x[13] + x[19] + x[25] == 5)
    P.add_constraint(x[2] + x[8] + x[14] + x[20] + x[26] == 4)
    P.add_constraint(x[3] + x[9] + x[15] + x[21] + x[27] == 5)
    P.add_constraint(x[4] + x[10] + x[16] + x[22] + x[28] == 6)
    P.add_constraint(x[5] + x[11] + x[17] + x[23] + x[29] == 2)

    P.solve()
    print(P)
    for i in range(len(x)):
        print('Las cantidades a enviar por el arco', i, 'son:' , x[i])
#ejercicio2()

def ejercicio5():
    P = picos.Problem()

    x = picos.RealVariable('x', 3, lower=0)
    y = picos.RealVariable('y', 3, lower=0)
    z = picos.RealVariable('z', 3, lower=0)

    #costos
    #En horas regulares
    cr = np.array([31,32,36])
    #En horas extra
    ce = np.array([38,38,44])
    #De almacenaje
    ca = np.array([3,3,3]) 
    
    P.set_objective('min', cr.T * x + ce.T * y + ca.T * z)

    #Restricciones
    #De demanda
    P.add_constraint(x[0] + y[0] == 8 + z[0])
    P.add_constraint(x[1] + y[1] + z[0] == 10 + z[1])
    P.add_constraint(x[2] + y[2] + z[1] == 16 + z[2])

    #De oferta regulares
    P.add_constraint(x[0] <= 10)
    P.add_constraint(x[1] <= 8)
    P.add_constraint(x[2] <= 10)

    #De oferta extras
    P.add_constraint(y[0] <= 3)
    P.add_constraint(y[1] <= 2)
    P.add_constraint(y[2] <= 3)

    #print(P)

    P.solve()
    for i in range(len(x)):
        print('Cantidad de x[' + str(i) +'] producida es:', round(x[i]))
    
    for i in range(len(y)):
        print('Cantidad de y[' + str(i) +'] producida es:', round(y[i]))

    for i in range(len(z)):
        print('Cantidad de z[' + str(i) +'] producida es:', round(z[i]))
#ejercicio5()

def ejercicio7():
    P = picos.Problem()

    x = picos.IntegerVariable('x', 9, lower = 0)

    cantMax = np.array([9,7,7,2,4,6,6,3,9])


    P.set_objective('max', x[0] + x[1])

    for i in range(len(x)):
        P.add_constraint(x[i] <= cantMax[i])

    P.add_constraint(x[0] == x[2] + x[3])        #Nodo B
    P.add_constraint(x[1] == x[4] + x[5])        #Nodo C
    P.add_constraint(x[2] + x[4] == x[6] + x[7]) #Nodo D
    P.add_constraint(x[3] + x[5] + x[7] == x[8]) #Nodo E

    P.solve()
    print(P)
    

    print('Para maximizar el flujo del grafo debemos enviar: ')
    for i in range(len(x)):
        print('En el arco', i, 'un total de:', x[i])
    
    print('\n Vemos ademas que las cantidades de salida', x[0] + x[1], 'son iguales a las de llegada', x[6] + x[8])
#ejercicio7()

def clase6(): #Ejercicio de set-covering
    P = picos.Problem()

    x = picos.BinaryVariable('x', 6)

    P.set_objective('min', sum(x))

    P.add_constraint(x[0] + x[1] >= 1)
    P.add_constraint(x[0] + x[1] + x[5] >= 1)
    P.add_constraint(x[2] + x[3] >= 1)
    P.add_constraint(x[2] + x[3] + x[4] >= 1)
    P.add_constraint(x[3] + x[4] + x[5] >= 1)
    P.add_constraint(x[1] + x[4] + x[5] >= 1)

    P.solve()

    print(x)

    for i in range(len(x)):
        if int(x[i]) == 1:
            print('Las ciudad', i+1, 'contendra una estacion de bomberos.')
clase6()