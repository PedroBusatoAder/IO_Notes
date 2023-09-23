# Ejercicio 6 --> Transhpiment
import picos
import numpy as np

p = picos.Problem()

# 1) Variables de decision
x = picos.RealVariable('x', 2, lower = 0) # x[i] es 'cantidad llevada de P1 a W[i]'
y = picos.RealVariable('y', 2, lower = 0) # y[i] es 'cantidad llevada de P2 a W[i]'
z = picos.RealVariable('z', 3, lower = 0) # z[i] es 'cantidad llevada de W1 a L[i]'
w = picos.RealVariable('w', 3, lower = 0) # w[i] es 'cantidad llevada de W2 a L[i]'

# 2) Funcion objetivo
p.set_objective('min', (425*x[0] + 560*x[1]) + (510*y[0] + 600*y[1]) + (470*z[0] + 505*z[1] + 490*z[2]) + (390*w[0] + 410*w[1] + 440*w[2]))

# 3) Restricciones

# i) Restricciones de la planta 1
# Capacidad de transporte
p.add_constraint(x[0] <= 125)
p.add_constraint(x[1] <= 150)

p.add_constraint(y[0] <= 175)
p.add_constraint(y[1] <= 200)

p.add_constraint(z[0] <= 100)
p.add_constraint(z[1] <= 150)
p.add_constraint(z[2] <= 100)

p.add_constraint(w[0] <= 125)
p.add_constraint(w[1] <= 150)
p.add_constraint(w[2] <= 75)

# Oferta
p.add_constraint(x[0] + x[1] <= 200)
p.add_constraint(y[0] + y[1] <= 300)

# Restricciones de warehouse --> Todo lo que entra tiene que ser igual a todo lo que sale!
p.add_constraint(x[0] + y[0] == z[0] + z[1] + z[2])
p.add_constraint(x[1] + y[1] == w[0] + w[1] + w[2])

# Demanda --> Igualdad estricta!
p.add_constraint(z[0] + w[0] == 150)
p.add_constraint(z[1] + w[1] == 200)
p.add_constraint(z[2] + w[2] == 150)

p.solve()

print('Las cantidades llevadas desde la Planta 1 son:')
print(x)
print('Las cantidades llevadas desde la Planta 2 son:')
print(y)
print('Las cantidades llevadas desde la Warehouse 1 son:')
print(z)
print('Las cantidades llevadas desde la Warehouse 2 son:')
print(w)

# Valor optimo? --> El costo total de tranporte
print(p.value)
