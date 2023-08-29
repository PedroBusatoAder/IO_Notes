# instalo librerias en caso que sea necesario
# pip install picos
# pip install swiglpk

# importo librerias
import numpy as np
import picos
import swiglpk
from scipy import optimize


######################## PICOS ########################
######################## PICOS ########################
######################## PICOS ########################

P = picos.Problem() # declarar el problema
x = picos.BinaryVariable('x', 2) # variables de decision ej 2 variables binarias
x = picos.IntegerVariable('x', 2 ) # variables de decision ej 2 variables enteras
x = picos.RealVariable('x', 2 , lower=0) # variables de decision ej 2 variables reales

d = picos.Constant('d', []) # si necesitas un vector de constantes

P.set_objective('min', ... ) # determinar la funcion objetivo
P.add_constraint( ... >= .. ) # restriccion >= 

P.solve() # en programacion lineal
P.solve(solver = 'glpk') # si necesitas resolver en ENTERA

print(P) # imprimir todo el problema
print(x) # imprimir variables de decision

P.value # imprimir el valor de la func. objetivo 



######################## SCIPY ########################
######################## SCIPY ########################
######################## SCIPY ########################

# Defino una funcion para la funcion objetivo
def f(x):
  x1 = x[0]
  x2 = x[1]
  ...
  ...
  xn = x[n] # listar las variables de entrada
  return # detallar la funcion 

# Defino una funcion para una restriccion
def con1(x):
  x1 = x[0]
  x2 = x[1]
  ...
  ...
  xn = x[n] # listar las variables de entrada
  return # detallar la funcion 

# declaro la restriccion en formato scipy
con1_scipy = optimize.NonlinearConstraint(fun = con1, lb = ... , ub =  ... )

constraints  = (con1, con2) # si queres agrupar muchas restricciones


x0 = [. , . , . ] # defino la semilla

# Busco el mínimo de f partiendo desde x0
opt = optimize.minimize(fun = ... , x0 = x0, constraints = ..., bounds = [(.. , ... ),(..., ...)])
opt.x # imprimo las variables de decision luego de la optimizacion
opt.fun # imprimo la funcion objetivo luego de la optimizacion