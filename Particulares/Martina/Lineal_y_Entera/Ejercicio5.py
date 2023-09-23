import picos

p = picos.Problem()

# 1) Variables de decision
x = picos.RealVariable('x', 3, lower = 0) # xi es la 'Cantidad de produccion (mensual) en horas regulares'
y = picos.RealVariable('y', 3, lower = 0) # yi es la 'Cantidad de produccion (mensual) en horas extras
z = picos.RealVariable('z', 3, lower = 0) # zi es la 'Cantidad almacenada en el mes i'

# 2) Funcion objetivo --> Minimizar los costos totales
p.set_objective('min', (x[0]*31 + x[1]*32 + x[2]*36) + (y[0]*38 + y[1]*38 + y[2]*44) + (z[0]*3 + z[1]*3 + z[2]*3))

# 3) Restricciones
# i) Oferta --> Desigualdades
p.add_constraint(x[0] <= 10)
p.add_constraint(x[1] <= 8)
p.add_constraint(x[2] <= 10)

# ii) Almacenamiento --> Todo lo que sobra, hay que almacenarlo
p.add_constraint(z[0] == (x[0] + y[0]) - 8)  # Por que ponemos ==? De esta manera, le decimos al picos que TODO el exceso de produccion lo tiene que almacenar obligatoriamente
p.add_constraint(z[1] == (x[1] + y[1] + z[0]) - 10)
p.add_constraint(z[2] == (x[2] + y[2] + z[1]) - 16)

# iii) Demanda --> Igualdad estricta
p.add_constraint(x[0] + y[0] == 8 + z[0])
p.add_constraint(x[1] + y[1] + z[0] == 10 + z[1])
p.add_constraint(x[2] + y[2] + z[1] == 16) # Podemos ahorrarnos el + z[2] ya que no tiene sentido almacenar para el mes 4 que no forma parte del problema!

p.solve()
print(x)
print(y)
print(z)
