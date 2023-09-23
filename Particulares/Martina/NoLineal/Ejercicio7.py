from scipy import optimize
import numpy as np

# 1) y 2) --> Variables de decision y funcion objetivo juntas
def objFun(x):
    distC1 = np.sqrt( (x[0]-5)**2 + (x[1]-10)**2 ) # En lugar de usar numpy uno puede hacer **(1/2)
    distC2 = np.sqrt( (x[0]-10)**2 + (x[1]-5)**2 )
    distC3 = np.sqrt( (x[0]-0)**2 + (x[1]-12)**2 )
    distC4 = np.sqrt( (x[0]-12)**2 + (x[1]-0)**2 )
    return(200 * distC1 + 150 * distC2 + 200 * distC3 + 300 * distC4)

#Randomizar la semilla --> Neesitamos un valor por cada x[i]
random1 = np.random.randint(0,1000)
random2 = np.random.randint(0,1000)
seed = [random1, random2]

print(seed)

restriccionX = [(0,None) , (0,None)] # Reemplaza lo que en picos era 'lower = 0' --> Necesitamos un bound para cada x[i]

# p.solve()
opt = optimize.minimize(fun = objFun, constraints = None, x0 = seed, bounds = restriccionX)

print(opt.x)