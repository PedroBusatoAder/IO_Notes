import picos
import numpy as np
from scipy import optimize

def ejercicio5():
    P = picos.Problem()
    
    x = picos.BinaryVariable('x', 25)
    y = picos.BinaryVariable('y', 5)

    c = np.array([5,12,30,20,15,20,4,15,10,25,15,20,6,15,12,25,15,25,4,10,10,25,15,12,5])

    P.set_objective('min', x[0]*c[0] + x[1]*c[1] + x[2]*c[2] + x[3]*c[3] + x[4]*c[4] + x[5]*c[5] + x[6]*c[6] + x[7]*c[7]+ x[8]*c[8] + x[9]*c[9] + x[10]*c[10]+ x[11]*c[11] + x[12]*c[12] + x[13]*c[13] + x[14]*c[14] + x[15]*c[15] + x[16]*c[16] + x[17]*c[17] + x[18]*c[18] + x[19]*c[19] + x[20]*c[20] + x[21]*c[21] + x[22]*c[22] + x[23]*c[23] + x[24]*c[24])    

    P.add_constraint(x[0] + x[6] + x[12] + x[18] + x[24] == 2)
    
    P.add_constraint(x[0] + x[1] + x[2] + x[3] + x[4] <= 10000 * y[0])
    P.add_constraint(x[5] + x[6] + x[7] + x[8] + x[9] <= 10000 * y[1])
    P.add_constraint(x[10] + x[11] + x[12] + x[13] + x[14] <= 10000 * y[2])
    P.add_constraint(x[15] + x[16] + x[17] + x[18] + x[19] <= 10000 * y[3])
    P.add_constraint(x[20] + x[21] + x[22] + x[23] + x[24] <= 10000 * y[4])
    
    P.add_constraint(sum(x) == 5) #Con esto obligo a que todas las variables queden asociadas a una ciudad! Sino el problema de optimizacion solo asocia las ciudades a donde se construye, ya que minimizamos tiempo
    
    P.solve()

    print(y)
    for i in range(len(x)):
        print('El x' + str(i), 'es:', x[i])   
#ejercicio5()

def ejercicio6():
    
    def objFun(x):
        return ( (x[0]-2)**2 + (x[0]-1)*(x[1]-1) + (x[1]-3)**2 )

    def r1(x):
        return (x[1] - 2*x[0])

    res1 = optimize.NonlinearConstraint(fun=r1 ,lb = 2, ub = 2)
    
    '''
    #Intente cambiar la forma de declarar las restricciones lineales de igualdad pero me cambio el resultado --> No se cual es el correcto
    A = [[1,-2]]
    res1 = optimize.LinearConstraint(A=A, lb=2, ub=2)
    '''
    
    def r2(x):
        return(x[0]**2 + x[1]**2)

    res2 = optimize.NonlinearConstraint(fun=r2, lb=0, ub=8)

    constraints = (res1,res2)
    seeds = [3,3]


    opt = optimize.minimize(fun = objFun, x0 = seeds, constraints = constraints)
    
    if (opt.success):
        print('Los valores de x encontrados que minimzan la funcion son:' )
        print('Para x[0]:', opt.x[0])
        print('Para x[1]:', opt.x[1], '\n')
        print('La funcion en el optimo es:', opt.fun, '\n')

    print('El ejercicio 6 es un problema de optimizacion convexo ya que el espacio factible es convexo y estamos minimizando una funcion convexa')
    print('Esto nos dice que el minimo hallado sera global')
#ejercicio6()

def ejercicio6RandomSeeds(): #Preguntar a Lucas si las semillas generadas tienen que respetar las condiciones
    def objFun(x):
        return ( (x[0] - 2)**2 + (x[0]-1)*(x[1]-1) + (x[1] - 3)**2 )

    def r1(x):
        return( x[1] - 2*x[0] )
    res1 = optimize.NonlinearConstraint(fun=r1, lb=2, ub=2)

    def r2(x):
        return( x[0]**2 + x[1]**2 )
    res2 = optimize.NonlinearConstraint(fun=r2, lb=0, ub=8)

    constrains = (res1, res2)

    iterations = 15
    xopt = []
    fopt =[]

    for x in range (iterations):
        numRandom = np.random.randint(0,10001)/100      #Numeros entre 1 y 100 con decimales
        seed = ([numRandom, numRandom])                 #Las semillas generadas deben respetar las resricciones?

        opt = optimize.minimize(fun = objFun, x0 = seed,constraints = constrains)
        if (opt.success):
            xopt.append(opt.x)
            fopt.append(opt.fun)

        print('Semilla: ' + str(seed) + ' --> x_opt: ' + str(opt.x) + ' --> ' + str(opt.fun)) #Vemos que efectivamente para todas las semillas llegamos a los mismos valores de 'x' y de la imagen de funcion
#ejercicio6RandomSeeds()

def ejercicio7():

    def objFun(x):
        dC1 = np.sqrt((x[0]-5)**2 + (x[1]-10)**2)
        dC2 = np.sqrt((x[0]-10)**2 + (x[1]-5)**2)
        dC3 = np.sqrt((x[0]-0)**2 + (x[1]-12)**2)
        dC4 = np.sqrt((x[0]-12)**2 + (x[1]-0)**2)
        return(200*dC1 + 150*dC2 + 200*dC3 + 300*dC4)

    numIteraciones = 15
    funEnMin = np.inf   #Guardamos infinito positivo ya que buscamos un minimo

    for i in range (numIteraciones):
        randomNum = np.random.randint(0,2001)/100               #Semillas entre 0 y 20 con valores decimales
        seed = [randomNum, randomNum]

        opt = optimize.minimize(fun=objFun, x0=seed)

        if(opt.success):
            print('Seed: ' + str(seed) + ' --> x_opt: ' + str(opt.x) + ' --> ' + str(opt.fun))
            if(opt.fun < funEnMin):
                funEnMin = opt.fun
    
    if(opt.success): #Sino encontro el minimo, imprimira el infinito, por eso ponemos el condicional
        print('Para las', numIteraciones, 'semillas planteadas, el minimo de la funcion sera: ', funEnMin)
#ejercicio7()

def ejercicio8(): #Trabajamos con unidades equivalentes a unidad de millon --> 1 = 1.000.000
    def funObj(x):
        return(50 * x[0] + 100 * x[1])

    def r1(x): #Cantidad de hombres como minimo que vean sus publicidades
        return(0.5 * 1000000 * np.sqrt(x[0]) + 1.7 * 1000000 * np.sqrt(x[1]))
    res1 = optimize.NonlinearConstraint(fun = r1, lb = 40 * 1000000, ub = np.inf)

    def r2(x):
        return( 2 * 1000000 * np.sqrt(x[0]) + 0.7 * 1000000 * np.sqrt(x[1]))
    res2 = optimize.NonlinearConstraint(fun = r2, lb = 60 * 1000000, ub = np.inf)

    contraints = (res1, res2)
    bounds = [(0, None), (0, None)]

    minAbs = np.inf
    xMinoAbs = 0 

    iterations = 15
    for i in range(iterations):
        numRandom = np.random.randint(0,10001)/100 #Genero semillas entre 0 y 100 con deccimales
        seed = [numRandom, numRandom]
        opt = optimize.minimize(fun = funObj, bounds=bounds, x0=seed, constraints=contraints)
        if(opt.success):
            print('Seed: '+ str(seed)+ ' --> x: ', str(opt.x) + 'funOpt: ' + str(opt.fun))
    #if (opt.success and opt.fun < minAbs):
ejercicio8()

def ejercicio9():
    def f(x): 
        return (50*x[0] + 100*x[1])

    def hombre(x): 
        return ( 500000*(x[0]**(1/2)) + 1700000*(x[1]**1/2) )
    Rhombre = optimize.NonlinearConstraint(fun=hombre, lb=40000000, ub=np.inf)

    def mujer(x): 
        return ( 2000000*(x[0]**(1/2)) + 700000*(x[1]**(1/2)) )
    Rmujer = optimize.NonlinearConstraint(fun=mujer, lb=60000000, ub=np.inf)

#    bounds= [(0,None),(0,None)]

    restricciones = (Rhombre, Rmujer)

    x0 = [0,0]


    Resolucion= optimize.minimize(fun=f, constraints=restricciones, x0=x0)

    print(Resolucion)

ejercicio9()