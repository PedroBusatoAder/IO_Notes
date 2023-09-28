import picos
import numpy as np

p = picos.Problem()

# 1) Variables de decision
# x = picos.RealVariable('x', 30, lower = 0)
x = picos.RealVariable('x', (5,6), lower = 0) # 5 filas x 6 columnas

# Matriz de costos
costos = np.array([[13,10,22,29,18,0],
                  [14,13,16,21,1000,0],
                  [3,0,1000,11,6,0],
                  [18,9,19,23,11,0],
                  [30,24,34,36,28,0] ])


# 2) Funcion objetivo
p.set_objective('min', picos.sum(costos^x))

# 3) Restricciones
# i) Oferta --> Desigualdades
p.add_constraint(picos.sum(x[0,:]) <= 5)
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


# Resolveme el problema
p.solve()

# Los valores de x son su valores optimo
print(x)

# Es costo total --> Lo que pedimos en la funcion objetivo
print(p.value)

# Lo usamos para imprimir el problema y ver como
# print(p)
