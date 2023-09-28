import picos
def ejercicio1():
    p = picos.Problem()

    # 1) Variables de decision
    x = picos.IntegerVariable('x', 1, lower = 0) #Cantidad de osos a producir
    y = picos.IntegerVariable('y', 1, lower = 0) #Cantidad de conejos a producir

    # 2) Funcion objetivo
    p.set_objective('max', 10*x[0] + 8*y[0])

    # 3) Restricciones
    p.add_constraint(2*x[0] + y[0] <= 20)
    p.add_constraint(x[0] + 2*y[0] <= 24)

    p.solve()

    print('La cantidad de osos a producir es:\n', x)
    print('La cantidad de conejos a producir es:\n', y)
    print('La ganancia total es de:\n', p.value)

def ejercicio1Sensibilidad():
    p = picos.Problem()

    # 1) Variables de decision
    x = picos.IntegerVariable('x', 1, lower = 0) #Cantidad de osos a producir
    y = picos.IntegerVariable('y', 1, lower = 0) #Cantidad de conejos a producir

    # 2) Funcion objetivo
    p.set_objective('max', 12*x[0] + 8*y[0])

    # 3) Restricciones
    p.add_constraint(2*x[0] + y[0] <= 25)
    p.add_constraint(x[0] + 2*y[0] <= 20)

    p.solve()

    print('La cantidad de osos a producir es:\n', x)
    print('La cantidad de conejos a producir es:\n', y)
    print('La ganancia total es de:\n', p.value)

#ejercicio1()
ejercicio1Sensibilidad()
