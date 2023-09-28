import picos

#Ejercicio 2 --> Asignacion

p = picos.Problem()

# 1) Variables de decision
st = picos.BinaryVariable('st', 4)
eve = picos.BinaryVariable('eve', 4)

# 2) Funcion objetivo
p.set_objective('min', eve[0] * 4.5 + eve[1] + 7.8 + eve[2] * 3.6 + eve[3] * 2.9 + st[0]*4.9 + st[1] * 7.8 + st[2] *3.6 + st[3]*2.9)

# 3) Restricciones
p.add_constraint(st[0] + st[1] + st[2] + st[3] == 2)
p.add_constraint(eve[0] + eve[1] + eve[2] + eve[3] == 2)

p.add_constraint(st[0] + eve[0] == 1)
p.add_constraint(st[1] + eve[1] == 1)
p.add_constraint(st[2] + eve[2] == 1)
p.add_constraint(st[3] + eve[3] == 1)

p.solve()

print('Las tareas que realiza Steve son: \n', st)
print()
print('Las tareas que realiza Eve son: \n', eve)