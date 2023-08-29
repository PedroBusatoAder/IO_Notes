import picos
import numpy as np
from scipy import optimize

def ejercicioEntera():
    P = picos.Problem()

    x = picos.BinaryVariable('x', 12)

    cd = np.array([5,2,4,1,4,1,2,5,3,3,5,3]) #Costos que representan distancias

    P.set_objective('min', cd.T * x)

    #Restriccion nodo origen
    P.add_constraint(x[0] + x[1] + x[2] == 1)

    #Restriccion nodo llegada
    P.add_constraint(x[9] + x[10] + x[11] == 1)

    #Restricciones de flujo --> Aseguramos que el programa efectivamente escoja un camino
    P.add_constraint(x[1] == x[4] + x[5])               #Nodo B
    P.add_constraint(x[2] == x[6] + x[8])               #Nodo C
    P.add_constraint(x[0] == x[3])                      #Nodo D
    P.add_constraint(x[5] + x[6] == x[7] + x[10])       #Nodo E
    P.add_constraint(x[3] + x[4] + x[7] == x[9])        #Nodo F
    P.add_constraint(x[8] == x[11])                     #Nodo G

    P.solve()
    distanciaTotal = 0
    print('Los caminos escogidos para minimizar la distancia son: ')
    for i in range(len(x)):
        if (int(x[i]) == 1):
            print('El camino: ', i)
    
    for i in range(len(x)):
        distanciaTotal += cd[i] * x[i]
    print('El costo total del recorrido sera:', distanciaTotal)
#ejercicioEntera()

def ejericioNoLineal1():
    def funObj(x):
        return -( -(1/5)*(x-3)**6 + (3/2)*(x-3)**4 - 2*(x-3)**2 + x - 4 )
        
    iteraciones = 15

    xMax = 0
    funMax = -np.inf

    for i in range(iteraciones):
        numRandom = np.random.randint(0,10001) / 100 #Semillas entre 0 y 10, con decimales
        seed = numRandom
        opt = optimize.minimize(fun = funObj, x0=seed, constraints = None)
        if(opt.success):
            print('Seed: ' + str(seed) + ' --> x = ' + str(opt.x) + ' --> function in opt: ' + str(-opt.fun)) #Debemos agregar un signo '-' al realizar los prints!
            if(-opt.fun >= funMax):
                xMax = opt.x 
                funMax = -opt.fun
    print('El maximo encontrado tras las', iteraciones, 'iteraciones es:', funMax, 'para el valor de X =', xMax)   
#ejericioNoLineal1()   

def ejercicioNoLineal2():
    def funObj(x):
        return -(-2 * (x[0]**2) - (x[1]**2) + x[0]*x[1] + 8 * x[0] + 3*x[1])

    def r1(x):
        return(3000 * x[0] + 1000 * x[1])
    res1 = optimize.NonlinearConstraint(fun = r1, lb=10000, ub=10000) #Lower y upper bound iguales para que la funcion resrticcion sea igualdad estricta

    bounds = [(0,None),(0,None)]

    xOpt = 0
    funOpt = -np.inf #Como queremos maximizar comenzamos por el infinito negativo

    iterations = 15
    for i in range(iterations):
        randomNum1 = np.random.randint(0,10001)/100
        randomNum2 = np.random.randint(0,10001)/100
        seeds=[randomNum1, randomNum2]

        opt = optimize.minimize(fun = funObj, x0=seeds,bounds = bounds, constraints = res1)
        if(opt.success):
            print('Seed: ' + str(seeds) + ' --> x: ' + str(opt.x) + ' --> fun_opt: ' + str(-opt.fun))
            if(-opt.fun > funOpt):
                funOpt = -opt.fun
                xOpt = opt.x
        print('')
ejercicioNoLineal2()


def ejercicioNoLineal2Alejo():
    def funObj(x):
        return -(-2 * (x[0]**2) - (x[1]**2) + x[0]*x[1] + 8 * x[0] + 3*x[1])

    def r1(x):
        return(3000 * x[0] + 1000 * x[1])
    res1 = optimize.NonlinearConstraint(fun = r1, lb=10000, ub=10000) #Lower y upper bound iguales para que la funcion resrticcion sea igualdad estricta

    bounds = [(0,None),(0,None)]

    seeds = [[0,0], [1,1], [5,5], [10,10], [7,7], [-10,5]]
    for i in range(len(seeds)):
        opt = optimize.minimize(fun = funObj, x0=seeds[i], bounds = bounds, constraints = res1)
        print('Seed: ' + str(seeds[i]) + ' ---> x: ' + str(opt.x) + ' --> fun: ' + str(-opt.fun)) #Cuando me pida MAXIMIZAR pongo un menos delante del 'opt.fun'

#ejercicioNoLineal2Alejo()
