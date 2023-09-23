import picos
import numpy as np # La usamos para trabajar con matrices


# Usar unicamente en caso de programar en colab
# !pip3 install swiglpk


p = picos.Problem()

# 1) Variables de decision
x = picos.RealVariable('x', (5,6), lower = 0) # Matriz de decision en lugar de declarar 30 variables individualmente

costos = np.array([ [13,10,22,29,18,0],
                    [14,13,16,21,1000,0],
                    [3,0,1000,11,6,0],
                    [18,9,19,23,11,0],
                    [30,24,34,36,28,0] ])

# 2) Funcion objetivo
p.set_objective('min', picos.sum(costos^x))

# 3) Restricciones
# i) Oferta --> Desigualdad
p.add_constraint(picos.sum(x[0,:]) <= 5) # Me quedo con la primer fila de mi matriz de decision, sumo su elementos xij y eso tiene que se como mucho 5
p.add_constraint(picos.sum(x[1,:]) <= 6) 
p.add_constraint(picos.sum(x[2,:]) <= 7) 
p.add_constraint(picos.sum(x[3,:]) <= 4)
p.add_constraint(picos.sum(x[4,:]) <= 3) 

# ii) Demanda --> Igualdad estricta
p.add_constraint(picos.sum(x[:,0]) == 3)
p.add_constraint(picos.sum(x[:,1]) == 5)
p.add_constraint(picos.sum(x[:,2]) == 4)
p.add_constraint(picos.sum(x[:,3]) == 5)
p.add_constraint(picos.sum(x[:,4]) == 6)
p.add_constraint(picos.sum(x[:,5]) == 2)

# print(p)
p.solve()

# Usar unicamente en caso de programar en Colab
# p.solve(solver = 'glpk')


print('Las soluciones al problema son:')
print(x)