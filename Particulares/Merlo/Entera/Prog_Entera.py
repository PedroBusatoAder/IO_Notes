import picos 

P = picos.Problem()

#Seteamos variables binarias
x = picos.BinaryVariable('x', 4) # [x1, x2, x3, x4]

# Funcion objetivo
P.set_objective('max', x[0] * 16000 + x[1] * 22000 + x[2] * 12000 + x[3] * 8000)

# Restricciones
P.add_constraint( x[0] * 5000 + x[1] * 7000 + x[2] * 4000 + x[3] * 3000 <= 14000)

P.solve()

print(x)