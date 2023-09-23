# El ejercicio 2) es un problema de asignacion!
import picos

p = picos.Problem()

# 1) Variables de decision --> Son variables binarias
x = picos.BinaryVariable('x', 4) # Variables para Steve --> xi es 'Steve realiza o no la tarea numero i'
y = picos.BinaryVariable('y', 4) # Variables para Eve --> yi es 'Eve realiza o no la tarea numero i'

# 2) Funcion objetivo --> Siempre tenes un unica funcion objetivo!
p.set_objective('min', (x[0]*4.9 + x[1]*7.2 + x[2]*4.3 + x[3]*3.1) + (y[0]*4.5 + y[1]*7.8 + y[2]*3.6 + y[3]*2.9))

# 3) Restricciones
p.add_constraint(x[0] + x[1] + x[2] + x[3] == 2) # Aseguramos que Steve haga dos tareas
p.add_constraint(y[0] + y[1] + y[2] + y[3] == 2) # Aseguramos que Eve haga dos tareas

# Necesitamos que Steve y Eve no repitan las mismas tareas
p.add_constraint(x[0] + y[0] == 1)
p.add_constraint(x[1] + y[1] == 1)
p.add_constraint(x[2] + y[2] == 1)
p.add_constraint(x[3] + y[3] == 1)

p.solve()

print('Steve hace las tareas:')
print(x)
print()
print('Eve hace las tareas:')
print(y)