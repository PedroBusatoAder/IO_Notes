import numpy as np
import picos

def ejercicio1():
    P = picos.Problem()

    x = picos.IntegerVariable('x', 2, lower = 0)
    g = np.array([180, 90])

    P.set_objective('max', g.T * x)

    #Restricciones
    P.add_constraint(0<= x[0] <= 6)
    P.add_constraint(0<= x[1] <= 4)
    P.add_constraint(6*x[0] + 8*x[1] <= 48)

    P.solve()

    for i in range(len(x)):
        if i == 0:
            print('Para maximizar la ganancia total se deberan producir un total de' , x[i], 'ventanas de madera')
        else:
            print('Para maximizar la ganancia total se deberan producir un total de' , x[i], 'ventanas de aluminio')

#ejercicio1()

def ejercicio2():
    demand = 25
    offer = 25
    if demand == offer:

        P =  picos.Problem()
        c = np.array([[13,10,22,29,18,0], [14,13,16,21,1000,0], [3,0,1000,11,6,0], [18,9,19,23,11,0], [30,24,34,36,28,0]])        
        c = picos.Constant('c', c)
        print('Observermos que la matriz de costos es de', c.shape)
        print(len(c))
        x = picos.RealVariable('x', 30, lower = 0)
        objectiveFunction = 0
        
        for i in range(len(c)):
            objectiveFunction += c[i] * x[i]
    
        P.set_objective('min', objectiveFunction)
        
        #Restricciones
        #Restricciones de oferta
        P.add_constraint(x[0] + x[1] + x[2] + x[3] + x[4] + x[5] <= 5)
        P.add_constraint(x[6] + x[7] + x[8] + x[9] + x[10] + x[11] <= 6)
        P.add_constraint(x[12] + x[13] + x[14] + x[15] + x[16] + x[17] <= 7)
        P.add_constraint(x[18] + x[19] + x[20] + x[21] + x[22] + x[23] <= 4)
        P.add_constraint(x[24] + x[25] + x[26] + x[27] + x[28] + x[29] <= 3)

        #Restricciones de demanda
        P.add_constraint(x[0] + x[6] + x[12] + x[18] + x[24] == 3)
        P.add_constraint(x[1] + x[7] + x[13] + x[19] + x[25] == 5)
        P.add_constraint(x[2] + x[8] + x[14] + x[20] + x[26] == 4)
        P.add_constraint(x[3] + x[9] + x[15] + x[21] + x[27] == 5)
        P.add_constraint(x[4] + x[10] + x[16] + x[22] + x[28] == 6)
        P.add_constraint(x[5] + x[11] + x[17] + x[23] + x[29] == 2)

        P.solve()
        for i in range(len(x)):
            print('Las cantidades a enviar en el arco', i, 'son:', round(x[i], 2)) 
ejercicio2()

def ejercicio3():
    P = picos.Problem()

    x = picos.RealVariable('x', 3, lower=0) #Cantidades de cemento extraidas desde North
    y = picos.RealVariable('y', 3, lower=0) #Cantidades de cementos extraidas desde South

    c1 = np.array([100,190,160]) #Costos de transporte de North a las obras 1, 2 y 3
    c2 = np.array([180,110,140]) #Costos de transporte de South a las obras 1, 2 y 3

    P.set_objective('min', c1.T * x + c2.T * y + 300 * (x[0] + x[1] + x[2]) + 420 * (y[0] + y[1] + y[2])) 

    #Restricciones
    #Restricciones de oferta
    P.add_constraint(x[0] + x[1] + x[2] <= 18)
    P.add_constraint(y[0] + y[1] + y[2] <= 14)
    
    #Restricciones de demanda    
    P.add_constraint(x[0] + y[0] == 10)
    P.add_constraint(x[1] + y[1] == 5)
    P.add_constraint(x[2] + y[2] == 10)

    P.solve()

    print('Desde la cantera North se enviaran:')
    for i in range(len(x)):
        print(round(x[i],2), 'toneladas de cemento a la construccion', i+1)
    
    print('Desde la cantera South se enviaran:')
    for i in range(len(y)):
        print(round(y[i],2), 'toneladas de cemento a la construccion', i+1)
#ejercicio3()

def ejercicio4():
    P = picos.Problem()

    x = picos.RealVariable('x', 5, lower = 0) #Cantidad de producto 1 producido en la planta i
    y = picos.RealVariable('y', 5, lower = 0) #Cantidad de producto 2 producido en la planta i
    z = picos.RealVariable('z', 3, lower = 0) #Cantidad de producto 3 producido en la planta i

    c1 = np.array([31,19,32,28,20])
    c2 = np.array([45,41,46,42,43])
    c3 = np.array([38,35,40])

    P.set_objective('min', c1.T * x + c2.T * y + c3.T * z)

    #Restricciones
    #Cantidades demandadas de cada producto
    P.add_constraint(x.sum == 600) 
    P.add_constraint(y.sum == 1000)
    P.add_constraint(z.sum == 800)  

    #Cantidades de oferta posibles por planta
    P.add_constraint(x[0] + y[0] + z[0] <= 400) #Planta 1
    P.add_constraint(x[1] + y[1] + z[1] <= 600) #Planta 2
    P.add_constraint(x[2] + y[2] + z[2] <= 400) #Planta 3
    P.add_constraint(x[3] + y[3] <= 600)        #Planta 4
    P.add_constraint(x[4] + y[4] <= 1000)       #Planta 5    

    print(P)

    P.solve()
    for i in range(len(x)):
        print('La cantidad de producto 1 a producir en la fabrica', i+1, 'es:', round(x[i]))
    
    print('')
    
    for i in range(len(y)):
        print('La cantidad de producto 2 a producir en la fabrica', i+1, 'es:', round(y[i]))

    print('')
    
    for i in range(len(z)):
        print('La cantidad de producto 3 a producir en la fabrica', i+1, 'es:', round(z[i]))
#ejercicio4()

def ejercicio5():
    
    P = picos.Problem()

    x = picos.RealVariable('x', 3, lower = 0) #Cantidades producidas en horas regulares
    y = picos.RealVariable('y', 3, lower = 0) #Cantidades producidas en horas extra
    z = picos.RealVariable('z', 3, lower = 0) #Cantidades almacenadas --> Por el momento declaramos tres variables pero no nos interesa mucho la tercera

    #Nuestros costos de produccion y almacenamiento
    cr = np.array([31,32,36])
    ce = np.array([38,38,44])
    ca = np.array([3,3,3])

    P.set_objective('min', cr.T * x + ce.T * y + ca.T * z)

    #Restricciones
    #Restricciones de oferta/capacidad de produccion
    P.add_constraint(x[0] <= 10)
    P.add_constraint(x[1] <= 8)
    P.add_constraint(x[2] <= 10)
    
    P.add_constraint(y[0] <= 3)
    P.add_constraint(y[1] <= 2)
    P.add_constraint(y[2] <= 3)

    #Restricciones de almacenamiento --> La cantidad almacenada puede estar entre 0 y la diferencia entre la maxima produccion y la demanda
    P.add_constraint(0 <= z[0] <= x[0] + y[0] - 8)          #x=6 y=3 z=1
    P.add_constraint(0 <= z[1] <= x[1] + y[1] + z[0] - 10)  #x=8 y=2 z[0]=1
    P.add_constraint(0 <= z[2] <= x[2] + y[2] + z[1] - 16)
    
    #Restricciones de demanda
    P.add_constraint(x[0] + y[0] == 8 + z[0])
    P.add_constraint(x[1] + y[1] + z[0] == 10 + z[1])
    P.add_constraint(x[2] + y[2] + z[1] == 16)          #No agregamos '16 + z[2]' ya que no seria lo optimo! Estariamos almacenando sin consumir a futuro

    print(P)
    
    P.solve()
    
    print("<--- Cantidades de producto en horas regulares a producir en el mes: -->")
    for i in range(len(x)):
        print(i+1, "es: ", round(x[i], 2))
    
    print("")
    
    print("<--- Cantidades de producto en horas extra a producir en el mes: -->")
    for i in range(len(y)):
        print(i+1, "es: ", round(y[i], 2))
    
    print("")
    
    
    print("<--- Cantidades de producto a almacenar en el mes: -->")
    for i in range(len(z)):
        print(i+1, "es: ",round(z[i], 2))
#ejercicio5()

def ejercicio7():
    
    P = picos.Problem()

    w = np.array([9,7,7,2,4,6,6,3,9])
    x = picos.IntegerVariable('x', 9, lower = 0)

    P.set_objective('max', x[6] + x[8])

    #Restricciones --> Restricciones de maxima capacidad
    for i in range (len(x)):
        P.add_constraint(x[i] <= w[i])
        
    #Restricciones --> Control de flujo en nodos intermedios
    P.add_constraint(x[0] == x[2] + x[3])           #Flujo del nodo B
    P.add_constraint(x[1] == x[4] + x[5])           #Flujo del nodo C
    P.add_constraint(x[2] + x[4] == x[6] + x[7])    #Flujo del nodo D
    P.add_constraint(x[3] + x[5] + x[7] == x[8])    #Flujo del nodo E
    
    #print(P)

    P.solve()
    print('Para poder maximizar la cantidad de flujo del grafo, se enviaran:')
    for i in range(len(x)):
        print(x[i], 'por el arco', i+1)
    print('\nObservamos asi que la cantidad inyectada en el grafo es igual a la cantidad de llegada -->', x[0] + x[1], '=', x[6] + x[8])
#ejercicio7()
