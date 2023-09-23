from scipy import optimize
import numpy as np
# import picos
# P = picos.Problem()
# x = picos.RealVariable('x', 2, lower = 0)

def objFun(x):
    dC1 = np.sqrt((x[0] - 5)**2 + (x[1] - 10)**2)
    dC2 = np.sqrt((x[0] - 10)**2 + (x[1] - 5)**2)
    dC3 = np.sqrt((x[0] - 0)**2 + (x[1] - 12)**2)
    dC4 = np.sqrt((x[0] - 12)**2 + (x[1] - 0)**2)
    return(200 * dC1 + 150 * dC2 + 200 * dC3 + 300 * dC4)

# Simula ser una de nuestras restricciones!
limitesX = [(0, None), (0, None)]

iterations = 10

# Adentro del for() metemos unicamente aquellas cosas que van a cambiar en cada iteracion
for i in range(iterations):
    seed = []
    s1 = np.random.randint(0,1000)
    s2 = np.random.randint(0,1000)
    print(s1)
    print(s2)
    seed.append(s1)
    seed.append(s2)

    opt = optimize.minimize(fun = objFun, x0 = seed, bounds = limitesX)
    print('Las coordenadas del centro de distribucion son:\n', opt.x)