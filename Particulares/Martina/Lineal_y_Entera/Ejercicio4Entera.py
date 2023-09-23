import picos

p = picos.Problem()

# 1) Variables de decision
x = picos.IntegerVariable('x', 3, lower = 0) # xi = 'Cantidad producida en la fabrica i'
y = picos.BinaryVariable('y', 3)             # Variables de activacion de costos fijos


# 2) Funcion objetivo --> Minimizamos costos totales de produccion
p.set_objective('min', x[0]*20 + x[1]*25 + x[2]*30 + y[0]*80000 + y[1]*40000 + y[2]*30000)

# 3) Restricciones

# i) Demanda --> Igualdad estricta
p.add_constraint(x[0] + x[1] + x[2] == 12000)

# ii) Oferta --> Desigualdad
p.add_constraint(x[0] <= 6000)
p.add_constraint(x[1] <= 7000)
p.add_constraint(x[2] <= 6000)

# iii) Activacion --> Activar el costo fijo de cada planta
p.add_constraint(x[0] <= 1000000 * y[0])
p.add_constraint(x[1]<= 1000000 * y[1])
p.add_constraint(x[2]<= 1000000 * y[2])

# x[0]= 1000 ---> 1000 <= 1000000 * 1
# x[1]= 0 ---> 0 <= 1000000 * 0


p.solve()

print(x)
print()
print(y)





