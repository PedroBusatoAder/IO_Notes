import picos

P = picos.Problem()

# Variables de decision --> Integer
x = picos.IntegerVariable('x', 2, lower = 0)

# Funcion objetivo
P.set_objective('max', x[0] * 180 + x[1] * 90)

# Restricciones
P.add_constraint(x[0] <= 6)
P.add_constraint(x[1] <= 4)
P.add_constraint(6*x[0] + 8*x[1] <= 48)

P.solve()

print(x)

