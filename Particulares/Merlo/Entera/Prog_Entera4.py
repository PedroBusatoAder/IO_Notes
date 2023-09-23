import picos
import numpy as np # Hacemos matrices

p = picos.Problem()

x = picos.BinaryVariable('x', 5)       # Construyo o no construyo en el lugar 'i'
y = picos.BinaryVariable('y', (5,5))   # Variable de decision con forma de matriz

# 'c' es la matriz de costos/tiempos
c = np.array([[5*2,12*1,30*3,20*1,15*3],
              [20*2,4*1,15*3,10*1,25*3],
              [15*2,20*1,6*3,15*1,12*3],
              [25*2,15*1,25*3,4*1,10*3],
              [10*2,25*1,15*3,12*1,5*3]])

"""
Hacemos una matriz de 3x3!
np.array([[1,2,3],
         [4,5,6],
         [7,8,9]])
"""

p.set_objective('min', picos.sum(c^y)/10)     # Tenemos 10 emergencias por dia

# 3) Restricciones
p.add_constraint(picos.sum(x) == 2)           # En total, debemos construir en dos lugares
# p.add_constraint(x[0] + x[1] + x[2] + x[3] + x[4] ==2)

for i in range(5):
  p.add_constraint(picos.sum(y[:,i]) >= 1) 
                                           # "Cada localizacion tiene que estar asignada por lo menos a una estacion" --> Por eso el >=

# Explicacion de la suma de filas y columnas
# Sumo fila --> Una estacion a cuantos lugares atiende
# Sumo columna --> Cuantas estaciones atienden a ese lugar


for i in range(5):    
  for j in range(5):
    p.add_constraint(y[i,j] <= x[i])       # Si x[i] no alverga una estacion, no podemos asignarle ciudades a las que abastecer 


# En Colab exige poner el solver muchas!
p.solve(solver = 'glpk')

print('Las resoluciones de x son:\n', x)
print('Las resoluciones de y son:\n', y)
