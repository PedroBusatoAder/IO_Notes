import picos
import numpy as np


P = picos.Problem()

# 1) Variables de decision
x = picos.BinaryVariable('x', 4) # Variables de asignacion para Steven
y = picos.BinaryVariable('y', 4) # Variables de asignacion para Eve

# 2) Funcion Objetivo
P.set_objective('min', x[0]*4.9 + x[1]*7.2 + x[2]*4.3 + x[3]*3.1 + y[0]*4.5 + y[1]*7.8 + y[2]*3.6 + y[3]*2.9)

# 3) Restricciones
P.add_constraint(x[0] + x[1] + x[2] + x[3] == 2) # Steve realice dos tarea
P.add_constraint(y[0] + y[1] + y[2] + y[3] == 2) # Steve realice dos tarea

P.add_constraint(x[0] + y[0] == 1)
P.add_constraint(x[1] + y[1] == 1)
P.add_constraint(x[2] + y[2] == 1)
P.add_constraint(x[3] + y[3] == 1)

P.solve()

# Imprimimos los resulados
print(x)
print(y)
