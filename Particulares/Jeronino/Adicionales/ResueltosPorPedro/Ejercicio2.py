import picos

p = picos.Problem()

# 1) Variables de decision
x = picos.RealVariable('x', 2, lower = 0)

# 2) Funcion objetivo
p.set_objective('max', x[0] + 3*x[1])

# 3) Restricciones
p.add_constraint(x[1] <= -2/3 * x[0] + 2)
p.add_constraint(x[1] >= x[0] - 2)

p.solve()

print('Las soluciones al problema son:\n', x)
print(p.value)