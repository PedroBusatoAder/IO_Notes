# Ejercicio 5 --> Transhipment
import picos

p = picos.Problem()

# 1) Variables de decision
x = picos.RealVariable('x', 3, lower = 0) # x[i] es 'Cantidad producidas por mes en horas regulares
y = picos.RealVariable('y', 3, lower = 0) # y[i] es 'Cantidad producidas por mes en horas extras
z = picos.RealVariable('z', 3, lower = 0) # z[i] es 'Cantidad almacenada en el mes i'

# 2) Funcion objetivo
p.set_objective('min', x[0]*31 + x[1]*32 + x[2]*36 + y[0]*38 +  y[1]*38 + y[2]*48 + z[0]*3 + z[1]*3 + z[2]*3) # Minimizamos el costo total de produccion y almacenamiento

# 3) Restriccion
# i) Restricciones de oferta
p.add_constraint(x[0] <= 10)
p.add_constraint(x[1] <= 8)
p.add_constraint(x[2] <= 10)

p.add_constraint(y[0] <= 3)
p.add_constraint(y[1] <= 2)
p.add_constraint(y[2] <= 3)

# ii) Restricciones de almacenamiento --> Podes almacenar unicamente si producis mas que la demanda de ese mes!
p.add_constraint(z[0] == x[0] + y[0] - 8) # x[0] = 9, y[0] = 2, demanda = 8
p.add_constraint(z[1] == x[1] + y[1] + z[0] - 10)
p.add_constraint(z[2] == x[2] + y[2] + z[1] - 16)

# iii) Restricciones de demanda
p.add_constraint(x[0]+ y[0] == 8 + z[0])
p.add_constraint(x[1] + y[1] + z[0] == 10 + z[1])
p.add_constraint(x[2] + y[2] + z[1] == 16)

p.solve()
print('Las cantidades producidas en horas regulares son:')
print(x)

print('Las cantidades producidas en horas extra son:')
print(y)

print('Las cantidades almacenadas son:')
print(z)
