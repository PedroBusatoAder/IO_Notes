import numpy as np
import matplotlib.pyplot as plt

#Generamos numeros aleatorios con distribucion uniforme --> 
print('Numero a:', np.random.uniform(low=0, high=10)) #Todos los numeros tendran la misma probabilidad por ser distribucion normal

num2 = np.random.uniform(low=-3, high=1, size=2)
print(num2)                                           #Me devuelve el array con dos numeros generados aleatoriamente dentro de la distribucion uniforme
print(num2[1])

#3 formas de generar numeros aleatorios
N = 150
#  1)
array1 = np.random.uniform(low=-3, high=1, size=N)

print('El array 1 generado de numeros aleatorios es:', array1, "\n")

#  2)
U = []
for i in range(N):
    U.append(round(np.random.uniform(low=-3, high=1),3))

print('El array 2 generado de numeros aleatorios es:', U, "\n")

#  3)
U2 = np.zeros(N) #Vector tamano 'N' lleno de ceros 
for i in range(N):
    U2[i] = np.random.uniform(low = -3, high = 1)

print('El array 3 generado de numeros aleatorios es:', U2, "\n")


#Como hacer histogramas
plt.hist(U, bins = 10, density = True) #La suma de las areas de los bines debe ser 1 cuando son variables continuas
plt.xlabel('x', fontsize = 18)
plt.xlabel('Cuentas', fontsize = 18)
plt.title('')
# plt.show()


#Histogramas con distintos parametros
a = [0.0, 0.0, 1.0]
b = [1.0, 2.0, 5.0] 

for i in range(len(a)):
  # Grafico el histograma de cuentas
  U = np.random.uniform(low=a[i], high=b[i], size=N)
  plt.hist(U, bins = 10, density = True, label = 'a ='+str(a[i])+', b ='+str(b[i]), alpha = 0.5)

# Label del eje x
plt.xlabel('x', fontsize = 18)
# Label del eje y
plt.ylabel('Cuentas', fontsize = 18)
# Defino un titulo
plt.title('Probabilidad empírica de ocurrencia')
# Agrego una grilla
plt.grid()
# Agrego la leyenda
plt.legend()
# Muestro el plot
plt.show()


#Distribucion Gaussiana --> Como generar valores aleatorios con una distribucion normal
# 1
print('a: ',np.random.normal(0.0, 1.0), '\n')
# 2
print('b: ',np.random.normal(loc=0.0, scale=1.0, size = 2), '\n')
# 5
print('c: ',np.random.normal(loc=0.0, scale=1.0, size = 5), '\n')

# Genero números aleatorios con distribución gaussiana.
# Esperanza -5 (mu = -5), desvío estándar = 0.1 (sigma = 0.1).
print('d: ',np.random.normal(loc=-5.0, scale=0.1, size = 5), '\n')

# Genero números aleatorios con distribución gaussiana.
# Esperanza -5 (mu = -5), desvío estándar = 1 (sigma = 0.1).
print('e: ',np.random.normal(loc=-5.0, scale=1, size = 5), '\n')

# Lo mismo pero usando un for
G = []
for i in range(5):
  G.append( np.random.normal(loc=-5.0, scale=0.1) )
print('f: ',G)

"""
Forma 1 de generar los N números aleatorios
"""
G = np.random.normal(loc=-5.0, scale=0.1, size = N)

"""
Forma 2 de generar los N números aleatorios
"""
G = []
for i in range(N):
  G.append( np.random.normal(loc=-5.0, scale=0.1) )

"""
Forma 3 de generar los N números aleatorios
"""
G = np.zeros(N)
for i in range(N):
  G[i] = np.random.normal(loc=-5.0, scale=0.1)


# Grafico el histograma de cuentas
plt.hist(G, bins = 50)

# Label del eje x
plt.xlabel('x', fontsize = 18)
# Label del eje y
plt.ylabel('Cuentas', fontsize = 18)
# Defino un titulo
plt.title('Probabilidad empírica de ocurrencia')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()


# Grafico el histograma de frecuencias
plt.hist(G, density = True, bins = 50)
# Label del eje x
plt.xlabel('x', fontsize = 18)
# Label del eje y
plt.ylabel('Frecuencia', fontsize = 18)
# Defino un titulo
plt.title('Densidad de probabilidad empírica')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

# Grafico el histograma de probabilidad acumulada
plt.hist(G, density = True, cumulative = True, bins = 50)
# Label del eje x
plt.xlabel('x', fontsize = 18)
# Label del eje y
plt.ylabel('Acumulada', fontsize = 18)
# Defino un titulo
plt.title('Probabilidad acumulada')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

"""#### Histogramas con distintos parámetros"""

N = 10000

mu = [0.0, -3.0, -3.0]
sigma = [1.0, 1.0, 0.4] 

for i in range(len(mu)):
  # Grafico el histograma de cuentas
  G = np.random.normal(loc=mu[i], scale=sigma[i], size = N)
  plt.hist(G, density = True, bins = 50, label = '$\mu$ ='+str(mu[i])+', $\sigma$ ='+str(sigma[i]), alpha = 0.4)

# Label del eje x
plt.xlabel('x', fontsize = 18)
# Label del eje y
plt.ylabel('Cuentas', fontsize = 18)
# Defino un titulo
plt.title('Probabilidad empírica de ocurrencia')
# Agrego una grilla
plt.grid()
# Agrego la leyenda
plt.legend()
# Muestro el plot
plt.show()

"""## Distribución Exponencial

### Muestreo

#### Generación de N números aleatorios con distribución exponencial para distintos lambda
"""

import numpy as np

# Genero números aleatorios con distribución exponencial.
# frecuencia de ocurrencia media 1 (lambda = 1).
# 1
print('a: ',np.random.exponential(scale=1.0), '\n') #'Scale' es el valor de nuestro lambda
# 2
print('b: ',np.random.exponential(scale=1.0, size = 2), '\n')
# 5
print('c: ',np.random.exponential(scale=1.0, size = 5), '\n')

# Genero números aleatorios con distribución exponencial.
# frecuencia de ocurrencia media 4 (lambda = 4).
print('d: ',np.random.exponential(scale=4.0, size = 5), '\n')

# Lo mismo pero usando un for
E = []
for i in range(5):
  E.append( np.random.exponential(scale=4.0) )
print('e: ',E)

"""#### Generación de N números aleatorios con distribución exponencial para distintos lambda. Histograma de frecuencias. Densidad de probabilidad empírica. Probabilidad acumulada de ocurrencia."""

import matplotlib.pyplot as plt
import numpy as np

N = 10000

"""
Forma 1 de generar los N números aleatorios
"""
E = np.random.exponential(scale=1.0, size = N)

"""
Forma 2 de generar los N números aleatorios
"""
E = []
for i in range(N):
  E.append( np.random.exponential(scale=1.0) )

"""
Forma 3 de generar los N números aleatorios
"""
E = np.zeros(N)
for i in range(N):
  E[i] = np.random.exponential(scale=1.0)


# Grafico el histograma de cuentas
plt.hist(E, bins = 50)

# Label del eje x
plt.xlabel('x', fontsize = 18)
# Label del eje y
plt.ylabel('Cuentas', fontsize = 18)
# Defino un titulo
plt.title('Probabilidad empírica de ocurrencia')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()


# Grafico el histograma de frecuencias
plt.hist(E, density = True, bins = 50)
# Label del eje x
plt.xlabel('x', fontsize = 18)
# Label del eje y
plt.ylabel('Frecuencia', fontsize = 18)
# Defino un titulo
plt.title('Densidad de probabilidad empírica')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

# Grafico el histograma de probabilidad acumulada
plt.hist(E, density = True, cumulative = True, bins = 50)
# Label del eje x
plt.xlabel('x', fontsize = 18)
# Label del eje y
plt.ylabel('Acumulada', fontsize = 18)
# Defino un titulo
plt.title('Probabilidad acumulada')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

"""#### Histogramas con distintos parámetros"""

N = 10000

lambda_ = [1.0, 3.0, 5.0]

for i in range(len(lambda_)):
  # Grafico el histograma de cuentas
  E = np.random.exponential(scale = lambda_[i], size = N)
  plt.hist(E, density = True, bins = 50, label = '$\lambda$ ='+str(lambda_[i]), alpha = 0.5)

# Limite al eje x para que se vea mejor
plt.xlim(-1,20)
# Label del eje x
plt.xlabel('x', fontsize = 18)
# Label del eje y
plt.ylabel('Cuentas', fontsize = 18)
# Defino un titulo
plt.title('Probabilidad empírica de ocurrencia')
# Agrego una grilla
plt.grid()
# Agrego la leyenda
plt.legend()
# Muestro el plot
plt.show()

"""## Distribución de Poisson

### Muestreo

##### Parámetro fijo, único valor.
"""

import numpy as np
from scipy.stats import poisson #No lo importamos desde numpy, sino que de otro lado --> La misma libreria de donde importabamos 'optimize' para problemas de optimizacion no lineal
import matplotlib.pyplot as plt

# Declaro un parámetro mu
mu = 5

# Printeo la probabilidad de que un evento ocurra X veces en el intervalo
# de tiempo propuesto, para este mu en particular.
X = 7
print('P( X =',X,') =',poisson.pmf(X, mu), '\n')

"""#### Parámetro fijo, varios valores a la vez."""

import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

# Declaro un parámetro mu
mu = 5

# Defino array de numeros del 0 al 9
x = np.array([4, 5, 6, 7])
# Array de la probabilidad de que ocurran x eventos en el intervalo
pmf_poisson = poisson.pmf(x, mu)

print('Proba de que X = [4, 5, 6, 7]')
print(pmf_poisson)

"""#### Parámetro fijo, varios valores a la vez. Plot."""

import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

# Declaro un parámetro mu
mu = 5

# Defino array de numeros del 0 al 9
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
# Array de la probabilidad de que ocurran x eventos en el intervalo
pmf_poisson = poisson.pmf(x, mu)

# Plot de puntos
plt.scatter(x, pmf_poisson)
# Label del eje x
plt.xlabel('x', fontsize = 18)
# Label del eje y
plt.ylabel('P(x)', fontsize = 18)
# Defino un titulo
plt.title('Función de probabilidad de Poisson con $\mu$= 5')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

"""#### Parámetro variable, varios valores a la vez. Plot. Sin usar for."""

import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

# Declaro un parámetro mu
mu = 1

# Defino array de numeros del 0 al 9
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
# Array de la probabilidad de que ocurran x eventos en el intervalo
pmf_poisson = poisson.pmf(x, mu)

# Plot de puntos
plt.scatter(x, pmf_poisson, label='mu = '+str(mu))

# Declaro un parámetro mu
mu = 3.4

# Defino array de numeros del 0 al 9
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
# Array de la probabilidad de que ocurran x eventos en el intervalo
pmf_poisson = poisson.pmf(x, mu)

# Plot de puntos
plt.scatter(x, pmf_poisson, label='mu = '+str(mu))

# Declaro un parámetro mu
mu = 7.5

# Defino array de numeros del 0 al 9
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
# Array de la probabilidad de que ocurran x eventos en el intervalo
pmf_poisson = poisson.pmf(x, mu)

# Plot de puntos
plt.scatter(x, pmf_poisson, label='mu = '+str(mu))

# Label del eje x
plt.xlabel('x', fontsize = 18)
# Label del eje y
plt.ylabel('P(x)', fontsize = 18)
# Defino un titulo
plt.title('Función de probabilidad de Poisson con $\mu$= 1, 3.4 y 7.5')
# Agrego una grilla
plt.grid()
# Agrego leyendas
plt.legend()
# Muestro el plot
plt.show()

"""#### Parámetro variable, varios valores a la vez. Plot. Usando for."""

# Declaro varios parámetros mu
mu = np.array([1, 3.4, 7.5])

# Defino array de numeros del 0 al 9
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

for i in range(len(mu)):
    # Array de la probabilidad de que ocurran x eventos en el intervalo
    pmf_poisson = poisson.pmf(x, mu[i])

    # Plot de puntos
    plt.scatter(x, pmf_poisson, label='mu = '+str(mu[i]))

# Label del eje x
plt.xlabel('x', fontsize = 18)
# Label del eje y
plt.ylabel('P(x)', fontsize = 18)
# Defino un titulo
plt.title('Función de probabilidad de Poisson con $\mu$= 1, 3.4 y 7.5')
# Agrego una grilla
plt.grid()
# Agrego leyendas
plt.legend()
# Muestro el plot
plt.show()

"""### Ejemplo: Mantenimiento de impresoras"""

#Cual es la probabilidad de que ocurran dos fallas o menos al mes?
import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

# Parámetros

# 1 falla cada 20 días x 24 días al mes 
mu = 1 / 20 * 24 #Cantidad de fallas al mes promedio
print(mu)
costo = 50

# Calculo las probabilidades

# Proba de que no ocurran eventos (que no haya fallas graves en el mes)
pmf_x_0 = poisson.pmf(0, mu)
print('La proba de que no haya ninguna falla mensual es = P(X = 0) =', pmf_x_0, '\n')

# Proba de que ocurra 1 evento (que haya una única falla graves en el mes)
pmf_x_1 = poisson.pmf(1, mu)
print('La proba de que haya 1 falla mensual es = P(X = 1) =', pmf_x_1, '\n')

# Probabilidad de que haya 2 o más eventos (que haya 2 o más fallas graves en el mes)
pmf_x_2_o_mas = 1 - pmf_x_0 - pmf_x_1 #En definitiva, calculamos el complemento


print('La proba de que haya 2 o más fallas mensuales es = P(X>=2) =', pmf_x_2_o_mas, '\n')
print('Presupuesto necesario esperado = ', pmf_x_2_o_mas*costo, 'USD', '\n') #El presupuesto necesario sera la probabilidad de que se rompa la maquinaria multiplicada por su costo de arreglo

# Plot

# Array de numeros del 0 al 9
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Array de la probabilidad de que ocurran x eventos al mes
pmf_poisson = poisson.pmf(x, mu)

# Plot de puntos
plt.scatter(x, pmf_poisson)
# Label del eje x
plt.xlabel('x', fontsize = 18)
# Label del eje y
plt.ylabel('P(x)', fontsize = 18)
# Defino un titulo
plt.title('Función de probabilidad de Poisson con $\mu$= 1.2')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

"""## Distribución de probabilidad "custom"

### Ejemplo: Dado cargado

#### Print de resultados individuales
"""

import numpy as np
import matplotlib.pyplot as plt

# Tiro el dado común
resultado_tirada_dado = np.random.choice(np.arange(1, 7), p=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6]) #Me creo mi propia distribucion de probabilidad puntual

print(resultado_tirada_dado)

# Tiro el dado cargado
resultado_tirada_dado_cargado = np.random.choice(np.arange(1, 7), p=[0.1, 0.05, 0.05, 0.15, 0.5, 0.15])

print(resultado_tirada_dado_cargado)

"""#### Armado de vectores de tamaño N con los resultados de las tiradas"""

# Defino listas vacías
resultado_tirada_dado = []
resultado_tirada_dado_cargado = []

# Defino el tamaño del vector, es decir la cantidad de tiradas
N = 10

for i in range(N):
  resultado_tirada_dado.append( np.random.choice(np.arange(1, 7), p=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6]) )
  resultado_tirada_dado_cargado.append( np.random.choice(np.arange(1, 7), p=[0.1, 0.05, 0.05, 0.15, 0.5, 0.15]) )

print('Resultado luego de', N,'tiradas con dado comun')
print(resultado_tirada_dado)
print('Resultado luego de', N,'tiradas con dado cargado')
print(resultado_tirada_dado_cargado)

"""#### Histograma de frecuencias"""

import matplotlib.pyplot as plt
# Defino listas vacías
resultado_tirada_dado = []
resultado_tirada_dado_cargado = []

# Defino el tamaño del vector
N = 1000

for i in range(N):
  resultado_tirada_dado.append( np.random.choice(np.arange(1, 7), p=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6]) )
  resultado_tirada_dado_cargado.append( np.random.choice(np.arange(1, 7), p=[0.1, 0.05, 0.05, 0.15, 0.5, 0.15]) )

x = resultado_tirada_dado
#Genero el histograma
Y, bins = np.histogram(x, bins=np.arange(1, 8))
#Grafico el histograma
plt.bar(bins[:-1], Y, width=0.7, alpha = 0.5)


x = resultado_tirada_dado_cargado
#Genero el histograma
Y, bins = np.histogram(x, bins=np.arange(1, 8))
#Grafico el histograma
plt.bar(bins[:-1], Y, width=0.7, alpha = 0.5)

# Label del eje x
plt.xlabel('x', fontsize = 18)
# Label del eje y
plt.ylabel('Cuentas', fontsize = 18)
# Defino un titulo
plt.title('Probabilidad empírica de ocurrencia')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

x = resultado_tirada_dado
#Genero el histograma para discretas!
Y, bins = np.histogram(x, bins=np.arange(1, 8))
#Grafico el histograma
plt.bar(bins[:-1], Y / np.sum(Y), width=0.7, alpha = 0.5)

x = resultado_tirada_dado_cargado
#Genero el histograma
Y, bins = np.histogram(x, bins=np.arange(1, 8))
#Grafico el histograma para frecuencia --> Dividimos por la suma de los valores
plt.bar(bins[:-1], Y / np.sum(Y), width=0.7, alpha = 0.5)

# Label del eje x
plt.xlabel('x', fontsize = 18)
# Label del eje y
plt.ylabel('Frecuencia', fontsize = 18)
# Defino un titulo
plt.title('Frecuencia')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()
