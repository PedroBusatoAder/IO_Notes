from scipy import optimize # No usamos mas picos
import picos
import numpy as np

p = picos.Problem()

# x = picos.RealVariable('x', 5)
# p.set_objective('min')


# Declaramos variables de decision y funcion objetivo en el mismo paso
def objFun(x):
    return((x[0] - 2)**2 + (x[0] - 1)*(x[1] - 1) + (x[1] - 3)**2)

# 3) Restricciones
def r1(x):
    return(x[1] - 2*x[0])

# p.add_constraint(0 <= x[0] <= 10) #up = 0 y lb = 10
res1 = optimize.NonlinearConstraint(fun = r1, lb = 2, ub = 2) # Le decimos a optimize que la funcion r1 es efectivamente una restriccion

def r2(x):
    return(x[0]**2 + x[1]**2)

res2 = optimize.NonlinearConstraint(fun = r2, lb = 0, ub = 8)

restricciones = (res1, res2) # Exige guardar las restricciones en tuplas --> Array pero inmutable

seed = []
s1 = np.random.randint(0,10001) # Generamos nuestras seeds random!
s2 = np.random.randint(0,10001)

seed.append(s1)
seed.append(s2)

# seed = [3,3] # Especificamos la semilla

# Optimize solamente permite minimizar!  
opt = optimize.minimize(fun = objFun, x0 = seed, constraints = restricciones)

print(opt.x)


# 2 <= x[1] <= 2 --> x[1] == 2