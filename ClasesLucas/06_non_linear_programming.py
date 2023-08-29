from scipy import optimize

# Defino una funcion
def f(x):
  return x**2 +1

# Le doy un valor inicial a optimize.minimize para que empiece a buscar
# el mínimo a partir de ahí
x0 = 2

# Busco el mínimo de f partiendo desde x0
opt = optimize.minimize(fun = f, x0 = x0)
print('Sin restricciones','\n')
print(opt,'\n')

# Busco el mínimo de f partiendo desde x0
# Restrinjo los límites de la solucion posible
opt = optimize.minimize(fun = f, x0 = x0, bounds = [(1.1, 1.5)])
print('Con restricciones','\n')
print(opt)

"""# Ubicación de aeropuerto"""

from scipy import optimize
import numpy as np

# Defino que L como un número que va a estar fijo
L = 1

# Defino la función objetivo a minimizar
def f(x):
  return (x[0] - L/2)**2 + x[1]**2 + (x[0] + L/2)**2 + x[1]**2 + x[0]**2 + (x[1] + - np.sqrt(3)/2*L)**2

# optimize.minimize necesita que ingresemos a mano un valor inicial
x0 = [0,0]
# optimizo la funcion objetivo. Busco el valor optimo para la ubicación
# del aeropuerto
opt = optimize.minimize(fun = f, x0 = x0)

print(opt)
print('Poniendo opt.x[0] obtenemos: ', opt.x[0])
print('Poniendo opt.x[1] obtenemos: ', opt.x[1])


# Lo siguiente es solamente para realizar el grafico
import matplotlib.pyplot as plt
import matplotlib.tri as tri
x_vec = [0, -L/2, L/2, round(opt.x[0],3)]
y_vec = [np.sqrt(3) * L / 2, 0, 0, round(opt.x[1],3)]
leg_ = ['Ciudad 1', 'Ciudad 2', 'Ciudad 3', 'Aeropuerto: (%.2f, %.2f)'%(x_vec[3],y_vec[3])]

triangles = [[0, 1, 2]]
triang = tri.Triangulation(x_vec, y_vec, triangles)

for i in range(len(x_vec)):
  plt.scatter(x_vec[i], y_vec[i], label = leg_[i])

plt.triplot(triang, lw=1, zorder=0) # draw the outlines of the triangles

plt.xlabel('x')
plt.ylabel('y')
plt.title('Ubicación del aeropuerto y las ciudades')
plt.legend()
plt.tight_layout()
plt.show()

"""# Candy bar pricing"""

from scipy import optimize
import numpy as np


# Demanda en funcion del precio de la unidad (x) para la region 1
def f1(x):
  if x <= 1.3:
    return (32 - 35) / (1.3 - 1.1) * (x - 1.1) + 35
  else:
    return (22 - 32) / (1.5 - 1.3) * (x - 1.3) + 32

# Demanda en funcion del precio de la unidad (x) para la region 2
def f2(x):
  if x <= 1.3:
    return (27 - 32) / (1.3 - 1.1) * (x - 1.1) + 32
  else:
    return (16 - 27) / (1.5 - 1.3) * (x - 1.3) + 27

# Demanda en funcion del precio de la unidad (x) para la region 3
def f3(x):
  if x <= 1.3:
    return (17 - 24) / (1.3 - 1.1) * (x - 1.1) + 24
  else:
    return (9 - 17) / (1.5 - 1.3) * (x - 1.3) + 17

# Funcion objetivo, tengo que poner un menos porque busco maximizar
# usando la funcion minimizar y: max(f(x)) = - min(- f(x))
def f(x):
  return -x * (f1(x) + f2(x) + f3(x))

opt = optimize.minimize(fun = f, x0 = 0, bounds = [(1.1, 1.5)])

print(opt)
print('Poniendo opt.x obtenemos: ', opt.x)
print('Poniendo opt.x[0] obtenemos: ', opt.x[0])

# Lo siguiente es solamente para realizar el grafico
import matplotlib.pyplot as plt

x_plot = np.linspace(1.1, 1.5, 100)
f_plot = np.zeros(len(x_plot))
for i in range(len(x_plot)):
  f_plot[i] = -f(x_plot[i])
plt.plot(x_plot, f_plot)
plt.scatter(round(opt.x[0],3), -f(round(opt.x[0],3)),
            label = 'Óptimo: (%.2f, %.2f)'%(round(opt.x[0],3), -f(round(opt.x[0],3))),
            color = 'r')
plt.vlines(round(opt.x[0],3), 70, 99, linestyles = 'dashed', color = 'r')

plt.xlabel('precio del producto')
plt.ylabel('Facturación')
plt.title('Facturaciónesperada según el precio asignado al producto')
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()

"""# Semillas randomizadas"""

from scipy import optimize
import numpy as np

# Defino una función de dos variables
def f(X):
    x = X[0]
    y = X[1]
    z = 0.22*x**6 - 1.25 * x**4 + 2 * x**2 + 0.22*y**6 - 1.25 * y**4 + 2 * y**2
    return z

# Defino un número de iteraciones
N = 10

for i in range(N):
    # Esta función da un vector de dimensión 2 formado por dos números
    # aleatorios que siguen una distribución uniforme entre -2 y 2.
    x0 = np.random.uniform(-2,2,2)
    # Cada vez que el for pase por acá va a tener una nueva semilla.
    # Busco el mínimo de la función
    opt = optimize.minimize(fun = f, x0 = x0)
    # Printeo la semilla cada vez
    print('seed = {},{}'.format(round(x0[0],2), round(x0[1],2)))
    # Printeo el valor óptimo encontrado cada vez
    print('optimal value = {},{}'.format(round(opt.x[0],2), round(opt.x[1],2)))


# Defino un número de iteraciones
N = 100

# Defino esta variable como infinito, ahora vamos a ver por qué
optimal_value = np.Inf

for i in range(N):
    # Esta función da un vector de dimensión 2 formado por dos números
    # aleatorios que siguen una distribución uniforme entre -20 y 20.
    x0 = np.random.uniform(-20,20,2)
    # Cada vez que el for pase por acá va a tener una nueva semilla.
    # Busco el mínimo de la función
    opt = optimize.minimize(fun = f, x0 = x0)
    # Si efectivamente encuentra un mínimo Y si ese mínimo es menor al valor
    # guardado en la variable "optimal_value" (inicialmente "infinito")
    if opt.success is True and opt.fun < optimal_value:
        # Reemplazo el valor de la variable valor óptimo
        optimal_value = opt.fun
        # Defino un nuevo punto (x,y) en que se encuentra el óptimo
        optimal_point = opt.x
        # Printeo el nuevo mínimo encoontrado y sus coordenadas
        print('Found new minimum!  Iteration: {}, Opt point: {}, Opt val: {}'.format(i,
                                                                                   (round(x0[0],2), round(x0[1],2)),
                                                                                   (opt.x[0], opt.x[1])))