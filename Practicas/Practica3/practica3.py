import numpy as np
import picos       # Siempre recordemos cambiar el interprete! Llevarlo a 3.10.10

def ejercicio1():
    
    P = picos.Problem()

    #Declaramos nuestras variables
    x = picos.IntegerVariable('x', 3, lower = 0)
    y = picos.BinaryVariable("y", 4)        #No es muy necesario indicar el lower ya que son binarias!

    #Vectores de costos y restricciones
    c = np.array([5,7,3])                   #Se declaran los arrays en forma columna
    b1 = np.array([7,5,9])
    
    #c = picos.Constant('c', c) 
    
    P.set_objective('max', c.T * x)

    #Determinamos las restricciones
    P.add_constraint(x <= b1)
    for i in range(3):
        P.add_constraint(x[i] <= 1000*y[i])

    P.add_constraint(y[0] + y[1] + y[2] <= 2)
    P.add_constraint(3*x[0] + 4*x[1] + 2*x[2] - 30 <= 1000*y[3])
    P.add_constraint(4*x[0] + 6*x[1] + 2*x[2] - 40 + 1000*y[3] <= 1000)

    P.solve()
    solutionsX = x
    solutionsY = y

    for i in range(len(solutionsX)):
        print("El valor de x" + str(i) + " es: " + str(solutionsX[i]))
    
    print('')
    
    for i in range(len(solutionsY)):
        print("El valor de y" + str(i) + " es: " + str(solutionsY[i]))

#ejercicio1()

def ejercicio2(): #Problema de asigacion

    P = picos.Problem()

    x = picos.BinaryVariable('x', 4)
    y = picos.BinaryVariable('y', 4)

    #Costos para Eve
    cEve = np.array([4.5, 7.8, 3.6, 2.9])  # Recordemos que los determina como vector columna
    #Costos para Steven
    cSteven = np.array([4.9, 7.2, 4.3, 3.1])

    P.set_objective('min', (cEve.T * x) + (cSteven.T * y))

    #Declaramos nuestras restricciones
    P.add_constraint(x.sum == 2)  # --> x[0] + x[1] + x[2] + x[3] == 2
    P.add_constraint(y.sum == 2)

    for i in range(4):
        P.add_constraint(x[i] + y[i] == 1) #Cada tarea sera realizada unicamente por uno de los dos

    #print(P)

    P.solve()

    tareas = ['Compras', 'Cocinar', 'Lavar platos', 'Lavar ropa']

    for i in range (len(tareas)):
        if int(x[i]) == 1:
            print('Eve realizara la tarea de', tareas[i], '\n')
        else:
            print('Steven realizara la tarea de', tareas[i], '\n')
        
#ejercicio2()

def ejercicio3(): #Problema de set covering --> Pedir ayuda a Martin/Lucas
    P = picos.Problem()

    x = picos.BinaryVariable('x', 7) # x = 'el jugador es parte de la formacion inicial'
    
    y = picos.BinaryVariable('y', 1) #Variable para restricciones especiales 

    g = picos.BinaryVariable('g', 7) # g = 'el jugador juega en la posicion guard'
    f = picos.BinaryVariable('f', 7) # f = 'el jugador juega en la posicion forward'
    c = picos.BinaryVariable('c', 7) # c = 'el jugador juega en la posicion center' 
    
    defence = np.array([3,2,2,1,3,3,1]) # Puntaje personal de cada jugador en 'defence'
    ballHandling = np.array([3,2,2,1,3,3,3])
    shooting = np.array([3,1,3,3,3,1,2])
    rebound = np.array([1,3,2,3,3,2,2])

    P.set_objective('max', (defence.T * x)/len(x))
    
    #Restricciones
    P.add_constraint(x.sum == 5) #La formacion titular puede estar compuesta unicamente por 5 jugadores

    P.add_constraint(g.sum >= 4) #Por lo menos 4 jugadores deben jugar en la posicion 'guard'
    P.add_constraint(f.sum >= 2) #Por los menos 2 jugadores deben jugar en la posicion 'forward'
    P.add_constraint(c.sum >= 1) #Por lo menos 1 jugador debe jugar en la posicion 'center'

    P.add_constraint((ballHandling.T * x)/len(ballHandling) >= 2) #El score promedio de la formacion titual en ball handling es al menos 2
    P.add_constraint((shooting.T * x)/len(shooting) >= 2)         #El score promedio de la formacion titual en shooting es al menos 2
    P.add_constraint((rebound.T * x)/len(rebound) >= 2)           #El score promedio de la formacion titual en rebounding es al menos 2

    P.add_constraint(x[2] <= (1 - x[5])) #Si el jugador 3 es titular, el jugador 6 no puede ser titular, pero si vale la inversa
    P.add_constraint(1 <= x[1] + x[2] <= 2) #Debe estar alguno de los dos jugadores, o ambos de ellos

    P.solve()

#ejercicio3()

def ejercicio4():
    P = picos.Problem()

    x = picos.IntegerVariable('x', 3, lower = 0)    #x[i] es la cantidad producida en cada una de las plantas
    y = picos.BinaryVariable('y', 3)                #Variables de activacion de los costos fijos

    c = np.array([20,25,30])
    fc = np.array([80000, 40000, 30000])

    P.set_objective('min', c.T * x + fc.T * y)

    #Restricciones

    #Restriccion de demanda
    P.add_constraint(x[0] + x[1] + x[2] == 12000) 

    #Restricciones de oferta
    P.add_constraint(x[0] <= 6000)
    P.add_constraint(x[1] <= 7000)
    P.add_constraint(x[2] <= 6000)

    #Restricciones de activacion
    for i in range(len(y)):
        P.add_constraint(x[i] <= 10000*(y[i]))

    P.solve()

    print(x)

    for i in range(len(x)):
        print('En la planta', i+1, 'se produjo una cantidad total de', x[i])

#ejercicio4()

def ejercicio5(): #Problema de set covering --> Pedir ayuda a Martin/Lucas

    P = picos.Problem()

    x = picos.BinaryVariable('x', 25) 
    
    c = np.array([[5,12,30,20,15], [20,4,15,10,25], [15,20,6,15,12], [25,15,25,4,10], [10,25,15,12,5]])
    c = picos.Constant('c', c)
    print(len(c))
    
    
    P.set_objective('min', 5 * x[0] + 12 * x[0] + 30 * x[0] + 20 * x[0] + 15 * x[0] + 20 * x[1] + 4 * x[1] + 15 * x[1] + 10 * x[1] + 25 * x[1] + 15 * x[2] + 20 * x[2] + 6 * x[2] + 15 * x[2] + 12 * x[2] + 25 * x[3] + 15 * x[3] + 25 * x[3] + 4 * x[3] + 10 * x[3] + 10 * x[4] + 25 * x[4] + 15 * x[4] + 12 * x[4] + 5 * x[4]) 

    P.add_constraint(x.sum == 2) #Se deben colocar dos estaciones de bomberos --> Cambiar (seria la suma de la diagonal de la matriz)

    for i in range(len(x)):
        P.add_constraint(x[i] <= 1) #No es muy necesario de aclarar ya que son variables binarias
    
    #Variables de la diagonal de la matriz dicen si tenemos la estacion


    print(P)

#ejercicio5()

def ejercicio7():
    P = picos.Problem()

    x = picos.BinaryVariable('x', 7)
    c = np.array([2,8,5,6,4,12,10])

    P.set_objective('min', c.T * x)

    #Restricciones de flujo
    P.add_constraint(x[0] + x[1] == 1)            #Nodo origen
    P.add_constraint(x[0] == x[2] + x[4] + x[5])  #Nodo 2
    P.add_constraint(x[1] + x[2] == x[3])         #Nodo 3
    P.add_constraint(x[3] + x[4] == x[6])         #Nodo 4
    P.add_constraint(x[5] + x[6] == 1)            #Nodo llegada
    
    print(P)
    P.solve()
    print('Los arcos escogidos para minimizar el camino son:')
    for i in range(len(x)):
        if int(x[i]) == int(1.0): #Me obliga a convertir a int para que se respete el condicional
            print('El nodo', i)

#ejercicio7()

'''objectiveFunction = 0
    for i in range(len(c)):
        print(c[i])
    '''
    

def escogerFuncion(): # Terminarlo
    funToExcecute = 'ejercicio'

    while True:
        try:
            funChosen = int(input("Buenas! Bienvenido a la practica 3. Escoja que funcion le gustaria ejectuar: "))
            break
        except ValueError:
            print("Debe ingresar un numero. Intente nuevamente: ")
    
    funToExcecute = funToExcecute + str(funChosen)

#escogerFuncion()

cons1 = 'Juan'
cons2 = 'Pedro'

x = (cons1, cons2)
print(type(x))
