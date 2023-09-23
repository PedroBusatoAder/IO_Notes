import picos

p = picos.Problem() # Estoy inicializando un problema de picos

# 1) Variables de decision --> 'Cuantas ventanas de cada tipo vendemos'
x = picos.RealVariable('x', 2, lower = 0) # Con variables continuas
# x = picos.IntegerVariable('x', 2) # Con variables enteras

# 2) Funcion objetivo
p.set_objective('max', x[0]*180 + x[1]*90)

# 3) Restricciones
p.add_constraint(x[0] <= 6) # Como mucho puedo producir 6 ventanas de madera
p.add_constraint(x[1] <= 4) # Como mucho puedo producir 4 ventanas de aluminio
p.add_constraint(x[0]*6 + x[1]*8 <= 48)

p.solve()

print(x)
