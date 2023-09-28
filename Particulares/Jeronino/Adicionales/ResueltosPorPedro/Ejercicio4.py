import picos

p = picos.Problem()

# 1) Variables de decision
x = picos.RealVariable('x', 3, lower = 0) 
y = picos.BinaryVariable('y', 3)

# 2) Funcion objetivo
p.set_objective('max', x[0] * 2000000 + x[1] * 3000000 + x[2] * 800000 - y[0] * 3000000 - y[1] * 2000000 - y[2] * 0)

# 3) Restricciones
p.add_constraint(x[0] * 0.2 + x[1] * 0.4 + x[2] * 0.2 == 1)

p.add_constraint(x[0] <= 3)
p.add_constraint(x[1] <= 2)
p.add_constraint(x[2] <= 5)

p.add_constraint(x[0] <= 1000000 * y[0])
p.add_constraint(x[1] <= 1000000 * y[1])
p.add_constraint(x[2] <= 1000000 * y[2])
p.solve()

print('Las cantidades a producir de cada avion son:\n', x)
print('Esto implica que se activan los costos fijos de las fabricas:\n', y)