# Eventos discretos

## Ejemplo 1: Impresora

"""### Exponencial"""


import numpy as np
import matplotlib.pyplot as plt

N = 100
X_exp = np.zeros(N)

lambda_ = 3 # Llegan 3 trabajos por cada intervalo de 15 minutos en promedio

for i in range(N):
  X_exp[i] = np.random.exponential( 1 / lambda_ )

print('Probabilidad de que el tiempo entre trabajos sea mayor a 15 minutos: ')
print(np.sum(X_exp >= 1)/N) # 1 intervalo de 15 minutos

# Grafico el histograma
plt.hist(X_exp , bins = 40,
             density = True,
             edgecolor='black')
# Label del eje x
plt.xlabel('Tiempo entre trabajos consecutivos / 15 min')
# Label del eje y
plt.ylabel('Probabilidad')
# Defino un titulo
plt.title('Exponencial')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

# Grafico el histograma
plt.hist(X_exp * 15, bins = 40,
             density = True,
             edgecolor='black')
# Label del eje x
plt.xlabel('Tiempo entre trabajos consecutivos')
# Label del eje y
plt.ylabel('Probabilidad')
# Defino un titulo
plt.title('Exponencial')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

"""### Poisson"""

import numpy as np
import matplotlib.pyplot as plt

N = 1000
X_Poi = np.zeros(N)

lambda_ = 3

for i in range(N):
  X_Poi[i] = np.random.poisson( lambda_ )


print('Probabilidad de que lleguen 0 trabajos en 15 minutos: ')
print(np.sum(X_Poi == 0)/N)

print('Probabilidad de que 2 trabajos o menos lleguen en 15 minutos: ')
print(np.sum(X_Poi <= 2)/N)

# Grafico el histograma
plt.hist(X_Poi , bins = np.arange(0, 10)-0.25,
             density = True, width = 0.6,
             edgecolor='black')
# Label del eje x
plt.xlabel('Trabajos recibidos en los 15 minutos')
# Label del eje y
plt.ylabel('Probabilidad')
# Defino un titulo
plt.title('Poisson')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

"""### Exponencial y Poisson"""

import numpy as np
import matplotlib.pyplot as plt

N = 100000
X_Poi = np.zeros(N)
X_exp = np.zeros(N)

lambda_ = 3

for i in range(N):
  X_Poi[i] = np.random.poisson( lambda_ )
  X_exp[i] = np.random.exponential( 1 / lambda_ )

print('Probabilidad de que lleguen 0 trabajos en 15 minutos: ')
print(np.sum(X_Poi == 0)/N)
print('Probabilidad de que el tiempo entre trabajos sea mayor a 15 minutos: ')
print(np.sum(X_exp > 1)/N)

fig, ax = plt.subplots(1, 2, figsize=(12,4))
# Grafico el histograma
ax[0].hist(X_Poi, bins = np.arange(0, 10)-0.25,
           width = 0.6,
             density = True, align='mid',
             edgecolor='black')
# Label del eje x
ax[0].set_xlabel('Trabajos en los próximos 15 minutos')
# Label del eje y
ax[0].set_ylabel('Probabilidad')
# Defino un titulo
ax[0].set_title('Poisson')
# Agrego una grilla
ax[0].grid()

# Grafico el histograma
ax[1].hist(X_exp , bins = 50,
             density = True,
             edgecolor='black')
# Label del eje x
ax[1].set_xlabel('Tiempo entre trabajos consecutivos / 15 min')
# Label del eje y
ax[1].set_ylabel('Probabilidad')
# Defino un titulo
ax[1].set_title('Exponencial')
# Agrego una grilla
ax[1].grid()
# Muestro el plot
plt.show()

"""## Ejemplo 2: Inventario"""

import numpy as np
import matplotlib.pyplot as plt

dias_sim = 50

u_stock = np.zeros(dias_sim)
u_stock[0] = 800

lambda_arribo = 800
lambda_demanda = 790

for i in range(1,dias_sim):
    u_arribo = np.random.poisson( lambda_arribo )
    u_ventas = np.random.poisson( lambda_demanda )

    if i%7==0:
        u_demanda_adic = 40
    else:
        u_demanda_adic = 0

    u_stock[i] = u_stock[i-1] + u_arribo - u_ventas - u_demanda_adic

print('stock promedio: ', np.mean(u_stock), 'unidades\n')
print('Proba de que el stock sea menor a 800 unidades: ', np.sum(u_stock < 800)/dias_sim, '\n')

# Grafico el histograma
plt.plot(u_stock, marker = 'o')
# Label del eje x
plt.xlabel('Días de simulación')
# Label del eje y
plt.ylabel('Stock acumulado')
# Defino un titulo
plt.title('')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

"""### Proba de que el inventario sea menor a 800 unidades luego de los 50 días de simulación"""

import numpy as np
import matplotlib.pyplot as plt

cantidad_de_simulaciones = 1000
u_stock_50_dias = np.zeros(cantidad_de_simulaciones)

lambda_arribo = 800
lambda_demanda = 790

for j in range(cantidad_de_simulaciones):
    dias_sim = 50

    u_stock = np.zeros(dias_sim)
    u_stock[0] = 800
    for i in range(1,dias_sim):
        u_arribo = np.random.poisson( lambda_arribo )
        u_ventas = np.random.poisson( lambda_demanda )

        if i%7==0:
            u_demanda_adic = 40
        else:
            u_demanda_adic = 0

        u_stock[i] = u_stock[i-1] + u_arribo - u_ventas - u_demanda_adic
    u_stock_50_dias[j] = u_stock[-1]

# Grafico el plot
plt.plot(u_stock_50_dias, marker = 'o')
# Label del eje x
plt.xlabel('Número de simulación')
# Label del eje y
plt.ylabel('Stock acumulado a 50 días')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

# Grafico el histograma
plt.hist(u_stock_50_dias , bins = 30,
             density = True,
             edgecolor='black')
# Label del eje x
plt.xlabel('stock acumulado a 50 días')
# Label del eje y
plt.ylabel('Probabilidad')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

# Calculo el promedio y el desvío estándar
print('Promedio: ', np.mean(u_stock_50_dias))
print('Desvío estándar: ', np.std(u_stock_50_dias), '\n')
print('Probabilidad de tener stock mayor a 800 a los 50 días: ', np.sum(u_stock_50_dias > 800)/cantidad_de_simulaciones)