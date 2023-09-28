import picos

p = picos.Problem()

# 1) Variables de decision
x = picos.IntegerVariable('x', 3, lower = 0)    # Cantidad a producir para cada minorista
y = picos.BinaryVariable('y', 3)                # Variable de activacion de costos fijos/iniciales

# 2) Funcion objetivo --> Maximizar ganancias totales
p.set_objective('max', 3000 * x[0] + 4000 * x[1] + 2500 * x[2] - y[0] * 40000 - y[1] * 60000 - y[2] * 20000)

# 3) Restricciones

# i) De produccion
#p.add_constraint(0.2 * x[0] + 0.3 * x[1] + 0.1 * x[2] <= 1)
#p.add_constraint(x[0] <= 5)
#p.add_constraint(x[1] <= 4)
#p.add_constraint(x[2] <= 6)

p.add_constraint(0.2 * x[0] <= 5)
p.add_constraint(0.3 * x[1] <= 4)
p.add_constraint(0.1 * x[2] <= 6)

# ii) Especiales
p.add_constraint(x[0]<= 100000* y[0])
p.add_constraint(x[1]<= 100000* y[1])
p.add_constraint(x[2]<= 100000* y[2])


p.solve()

print('Las cantidades a producir en cada una de las plantas son:\n', x)
print('Lo cual implica que se activaron los costos iniciales de las siguientes plantas:\n', y)