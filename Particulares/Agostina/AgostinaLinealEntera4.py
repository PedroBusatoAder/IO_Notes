import picos

P = picos.Problem()

x = picos.IntegerVariable('x', 3, lower = 0)    #x[i] es la cantidad producida en cada una de las plantas
y = picos.BinaryVariable('y', 3)                #Variables de activacion de los costos fijos


P.set_objective('min', x[0]*20 + x[1]*25 + x[2]*30 + y[0]*80000 + y[1]*40000 + y[2]*30000)

#Restricciones

#Restriccion de demanda
P.add_constraint(x[0] + x[1] + x[2] == 12000) 

#Restricciones de oferta
P.add_constraint(x[0] <= 6000)
P.add_constraint(x[1] <= 7000)
P.add_constraint(x[2] <= 6000)

#Restricciones de activacion

P.add_constraint(x[0] <= 10000*(y[0]))
P.add_constraint(x[1] <= 10000*(y[1]))
P.add_constraint(x[2] <= 10000*(y[2]))
P.solve()

print(x)
