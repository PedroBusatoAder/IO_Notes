import picos

p = picos.Problem()

# 1) Variables de decision
x = picos.IntegerVariable('x', 3, lower = 0)
y = picos.BinaryVariable('y', 3)                    # Variables de activacion de costos fijos

# 2) Funcion Objetivo
p.set_objective('min', x[0]*20 + y[0] * 80000 + x[1]*25 + y[1] * 40000 + x[2]*30 + y[2] * 30000)

# 3) Restricciones
# Demanda --> Igualdad estricta '=='
p.add_constraint(x[0] + x[1] + x[2] == 12000)

#Oferta --> Desigualdad
p.add_constraint(x[0] <= 6000)
p.add_constraint(x[1] <= 7000)
p.add_constraint(x[2] <= 6000)

# Restricciones especiales
p.add_constraint(x[0] <= 1000000*y[0]) # 2000 <= 1000000 * 1
p.add_constraint(x[1] <= 1000000*y[1]) # 0    <= 1000000 * 0
p.add_constraint(x[2] <= 1000000*y[2])

# print(p)

p.solve()

print('Las cantidades a producir por fabrica son: \n', x)
print()
print('Activamos los costos fijos de las fabrica \n', y)