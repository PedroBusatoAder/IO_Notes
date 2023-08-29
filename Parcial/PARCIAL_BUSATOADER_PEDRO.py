import picos
import numpy as np
from scipy import optimize

def ejercicio1(): 
    P = picos.Problem()

    x = picos.IntegerVariable('x', 3, lower = 0) #Cantidad de producto 1 producido en la planta i
    y = picos.IntegerVariable('y', 3, lower = 0)
    z = picos.IntegerVariable('z', 3, lower = 0)
    s = picos.IntegerVariable('s', 3, lower = 0) #Cantidad de producto i que queda sin satisfacer

    #Definimos nuestros costos de produccion --> Costos definidos por producto
    cp1 = np.array([31,29,32])
    cp2 = np.array([45,41,46])
    cp3 = np.array([38,35,40])
    cs = np.array([150,200,300])

    P.set_objective('min', cp1.T * x + cp2.T * y + cp3.T * z + cs.T * s)

    #Restricciones de demanda --> Demanda de cada producto
    P.add_constraint(x[0] + x[1] + x[2] + s[0] == 1000) #Debemos satisfacer la demanda restante mediante slack variables, que tendra un costo extra
    P.add_constraint(y[0] + y[1] + y[2] + s[1] == 1500)
    P.add_constraint(z[0] + z[1] + z[2] + s[2]== 900)

    #Restricciones de oferta --> Oferta de cada planta de produccion
    P.add_constraint(x[0] + y[0] + z[0] <= 1000)  
    P.add_constraint(x[1] + y[1] + z[1] <= 600)
    P.add_constraint(x[2] + y[2] + z[2] <= 400)

    P.solve()
    
    for i in range(len(x)):
        print('La cantidad a producir de producto 1 en la fabrica', i+1, 'sera:', x[i])
    for i in range(len(y)):
        print('La cantidad a producir de producto 2 en la fabrica', i+1, 'sera:', y[i])
    for i in range(len(z)):
        print('La cantidad a producir de producto 3 en la fabrica', i+1, 'sera:', z[i])
    for i in range(len(s)):
        print('La cantidad de demanda insatisfecha del producto', i+1, 'es:', s[i])
   
    print('El costo total de produccion es de:', P.value)

ejercicio1()

"""
def ejercicio3():
    def funObj(x):
        d1c = np.sqrt( ((x[0] - 0)**2) + ((x[1] - 10)**2) )
        d2c = np.sqrt( ((x[0] - 2)**2) + ((x[1] - 1)**2) )
        d3c = np.sqrt( ((x[0] - 3)**2) + ((x[1] - 7)**2) )
        return (300*d1c + 400*d2c + 200*d3c)

    bounds = [(None, None), (None, None)] #En principio el centro de distribucion podria esta en los 'x' e 'y' negativos del plano, pero la funcion al minimizar, no los va a tomar en cuenta probablemente

    funOpt = np.inf
    xOpt = 0
    iterations = 15
    for x in range(iterations):
        numRandom1 = np.random.randint(0,101)/10  #Generamos numeros aleatorios entre 0 y 10 (incluido), con un decimal     
        numRandom2 = np.random.randint(0,101)/10    
        seed = [numRandom1, numRandom2]
        opt = optimize.minimize(fun = funObj, bounds = bounds, x0 = seed, constraints = None)

        print('Seed:', str(seed) + ' --> x: ' + str(opt.x) + ' --> fun: ' + str(opt.fun))
        print('La distancia tota')

        if (opt.success and opt.fun < funOpt):
            funOpt = opt.fun
            xOpt = opt.x
    print('El centro de distribucion se encontrara en: ' + str(xOpt) + 'y la distancia minima sera: ' + str(funOpt))
ejercicio3()
"""