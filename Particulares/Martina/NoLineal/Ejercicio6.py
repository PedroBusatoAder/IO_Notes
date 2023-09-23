import picos                        # --> Ya no usamos picos
from scipy import optimize
import numpy as np

p = picos.Problem()


# En picos haciamos...
# 1) x = picos.RealVariable('x', 5)
# 2) p.set_objective('min', )

# En Optimize
# 1) y 2) juntos --> Funcion objetivo y variables de decision juntas
def objFun(x):                                                              # Declaras una funcion en Python junto a tus variables de decision
    return( (x[0] - 2)**2 + (x[0] - 1)*(x[1] - 1) + (x[1] - 3)**2)

# 3) Restricciones
def r1(x):
    return(x[1] - 2*x[0])                                                   # Pasamos del mismo lado de la igualdad los terminos que tenga x[i]

# p.add_constraint() --> Picos
restriccion1 = optimize.NonlinearConstraint(fun = r1, lb = 2, ub = 2)       # 2 <= x[1] - 2*x[0] <= 2

def r2(x):
    return(x[0]**2 + x[1]**2)

restriccion2 = optimize.NonlinearConstraint(fun = r2, lb = 0, ub = 8)       # 0 <= x[0]**2 + x[1]**2 <= 8

restricciones = (restriccion1, restriccion2)                                # Guardar las restricciones entre parentesis --> Tupla

# Randomizamos nuestra semilla --> Usando numpy
random1 = np.random.randint(0,1000)
random2 = np.random.randint(0,1000)
seed = [random1, random2]   # La semilla se crea en forma de array --> Tiene que tener tantos elementos como variables tengas
print(seed)

# En picos --> p.solve()
opt = optimize.minimize(fun = objFun, constraints = restricciones, x0 = seed)

print(opt.x)

