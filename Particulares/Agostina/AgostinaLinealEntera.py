# Programacion lineal y entera
import picos

# Paso 1 --> Iniciamos el problema en picos
P = picos.Problem()

# Empezamos a plantear el problema

# 1) Variables de decision
x = picos.RealVariable('x', 2, lower = 0) # xi = "Cantidad de ventanas madera/aluminio producidas"
# x = picos.IntegerVariable('x', 2, lower = 0) # xi = "Cantidad de ventanas madera/aluminio producidas"

# 2) Funcion objetivo
P.set_objective('max', x[0] * 90 + x[1] * 180) 

# 3) Restricciones --> Restricciones de oferta
P.add_constraint(x[0] <= 4)
P.add_constraint(x[1] <= 6)  
P.add_constraint(x[0] * 8 + x[1] * 8 <= 48) 

# Resolvemos el problema
P.solve()

# Imprimimos las resoluciones
print("Las resoluciones de mi problema son:", x)

