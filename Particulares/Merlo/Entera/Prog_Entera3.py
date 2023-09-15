import picos

P = picos.Problem()

x = picos.IntegerVariable('x', 3, lower = 0)    # x[i] es la cantidad producida en cada una de las plantas
y = picos.BinaryVariable('y', 3)                # Variables de activacion de los costos fijos

# c = np.array([20,25,30])
# fc = np.array([80000, 40000, 30000])

P.set_objective('min', x[0] * 20 + x[1] * 25 + x[2] * 30 + y[0] * 80000 + y[1] * 40000 + y[2] * 30000)

#Restricciones

#Restriccion de demanda --> Igual estricta
P.add_constraint(x[0] + x[1] + x[2] == 12000)

#Restricciones de oferta --> Una restriccion por cada planta
P.add_constraint(x[0] <= 6000)
P.add_constraint(x[1] <= 7000)
P.add_constraint(x[2] <= 6000)

#Restricciones de activacion
P.add_constraint(x[0] <= 10000000*y[0])
P.add_constraint(x[1] <= 10000000*y[1])
P.add_constraint(x[2] <= 10000000*y[2])


'''
for i in range(len(y)):
    P.add_constraint(x[i] <= 10000*(y[i]))
'''

# Podemos verificar que este bien
print(P)

P.solve()

print(x)
print(y)
