# Ejercicio 6 - Practica 3
from scipy import optimize # Ya no usamos picos
import picos
import numpy as np

def objFun(x):                                                      # Definimos aqui mismo las variables de decision --> Se definen como array!
    return((x[0] - 2)**2 + (x[0] - 1)*(x[1] - 1) + (x[1]-3)**2)     # Aqui definimos la funcion objetivo como tal

# En picos hubiera sido:
# x = picos.RealVariable('x', 2)
# P.set_objective('min', x[0] * 12 + x[1] * 20)

# x[1] = 2*x[0] + 2 --> x[1] - 2*x[0] = 2
def r1(x):
    return(x[1] - 2*x[0])
res1 = optimize.NonlinearConstraint(fun=r1, lb=2, ub=2)             # Restriccion de igualdad 

def r2(x):
    return(x[0]**2 + x[1]**2)
res2 = optimize.NonlinearConstraint(fun=r2, lb=0 , ub=8)            # Restriccion de desigualdad

bounds = [(None, None), (None, None)]                               # Restricciones para nuestras variables de decision
constraints = (res1, res2)                                          # Guardamos los elementos en una tupla 
iterations = 5
seeds = [3,3]

for i in range(iterations):
    numrandom = np.random.randint(0,1000)
    seeds = [numrandom,numrandom]

    opt = optimize.minimize(fun = objFun, bounds = bounds, x0 = seeds)
    if (opt.success):
        print(opt.x)


#opt = optimize.minimize(fun = objFun, x0 = seeds, constraints = constraints)

#if (opt.success):
#   print(opt.x)


