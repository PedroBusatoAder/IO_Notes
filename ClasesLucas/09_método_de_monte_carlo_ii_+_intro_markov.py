"""## Tiempo de llegada de un avión"""

#Podemos usar Monte Carlo en casos donde queremos calcular cierta probabilidad de un outcome, en situaciones donde sumamos por ejemplo variables de distirbuciones distintas o de las cuales ni sabemos su distribucion
#De esta manera podemos simular procesos donde hacer las matematicas a mano podria resultar muy dificultoso o seria simplemente imposible
#Lucas dio el ejemplo de lanzar un foton a un espejo, atravesando un panel --> Probabilidad del foton de salir tiene cierta distribucion, la probabilidad de atravesar el panel otra distribucion y la de llegar al espejo otra distribucion distinta
#Asi Monte Carlo nos soluciona todos los problemas de sumar distribuciones distintas


import matplotlib.pyplot as plt
import numpy as np

### Forma 1
# Defino lista vacía
tiempo_vuelo = []
# Defino la cantidad de veces que voy a simular
N = 1000
for i in range(N):
  tiempo_vuelo.append( np.random.normal( loc = 300, scale = 20 ) )

### Forma 2

# Defino array de 1000 ceros
tiempo_vuelo = np.zeros(1000)
# Defino la cantidad de veces que voy a simular
N = 1000
for i in range(len(tiempo_vuelo)):
  tiempo_vuelo[i] = np.random.normal( loc = 300, scale = 20 )

### Forma 3
tiempo_vuelo = np.random.normal( loc = 300, scale = 20, size = 1000 )

# Calculo el promedio y el desvío estándar
print('Promedio: ', np.mean(tiempo_vuelo))
print('Desvío estándar: ', np.std(tiempo_vuelo), '\n')

# Grafico el histograma de cuentas
y = plt.hist(tiempo_vuelo, bins = 15,
             range = (220, 370), density = True, edgecolor='black')
# Label del eje x
plt.xlabel('tiempo de vuelo', fontsize = 18)
# Label del eje y
plt.ylabel('Densidad', fontsize = 18)
# Defino un titulo
plt.title('Probabilidad empírica de ocurrencia')
# Muestro el plot
plt.show()

# Calculo la probabilidad de tardar más de 320 minutos
print('y: ', y, '\n')
print('y[0]: ', y[0], '\n') # Alturas de las barras
print('y[1]: ', y[1], '\n') # Posiciones de los bordes de los bins
print('Ancho de cada bin: ', np.diff(y[1]), '\n') # Ancho de los bins

# Área bajo la curva cuando t > 320 min
# Ponemos -6 en el ultimo corchete para matchear los tamaños
print('Proba de que t > 320: ', np.sum(y[0][-5:]*np.diff(y[1][-6:])), '\n')

"""## Tiempo de fabricación con etapas

### Dibujo de las distribuciones
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
from scipy.stats import expon
from scipy.stats import triang

fig, ax = plt.subplots(1, 3, figsize=(15,4))
x = np.linspace(0,2,100)
ax[0].plot(x, uniform.pdf(x, loc = 0, scale = 2),
       'r-', alpha=0.6, label='uniform pdf')

# Label del eje x
ax[0].set_xlabel('Tiempo', fontsize = 18)
# Label del eje y
ax[0].set_ylabel('Probabilidad', fontsize = 18)
# Defino un titulo
ax[0].set_title('Etapa 1', fontsize = 18)
# Agrego una grilla
ax[0].grid()

x = np.linspace(0,4,100)
ax[1].plot(x, expon.pdf(x, scale = 1),
       'r-', alpha=0.6, label='uniform pdf')

# Label del eje x
ax[1].set_xlabel('Tiempo', fontsize = 18)
# Defino un titulo
ax[1].set_title('Etapa 2', fontsize = 18)
# Agrego una grilla
ax[1].grid()

x = np.linspace(0,4,100)
ax[2].plot(x, triang.pdf(x, c = .75, scale = 4 ),
       'r-', alpha=0.6, label='uniform pdf')

# Label del eje x
ax[2].set_xlabel('Tiempo', fontsize = 18)
# Defino un titulo
ax[2].set_title('Etapa 3', fontsize = 18)
# Agrego una grilla
ax[2].grid()

"""### Tiempo de producción"""

import numpy as np
import matplotlib.pyplot as plt

# Defino array de 100 ceros
tiempo_produccion = np.zeros(100)
# Defino la cantidad de veces que voy a simular
for i in range(len(tiempo_produccion)):
  t_etapa_1 = np.random.uniform( low = 0, high = 2 )
  t_etapa_2 = np.random.exponential( scale = 1 )
  t_etapa_3 = np.random.triangular( left = 0, mode = 3, right = 4 )
  tiempo_produccion[i] = t_etapa_1 + t_etapa_2 + t_etapa_3

#Caso ideal para usar Monte Carlo --> Suma de tres variables con distribucion diferentes, lo cual sumarlas a mano dificultaria muchisimo la cuestion --> Usamos Monte Carlo



# Calculo el promedio y el desvío estándar
print('Promedio: ', np.mean(tiempo_produccion))
print('Desvío estándar: ', np.std(tiempo_produccion), '\n')

# Grafico el histograma de cuentas
y = plt.hist(tiempo_produccion,
             bins = 10, range = (0, 10),
             density = True, edgecolor='black')
# Label del eje x
plt.xlabel('tiempo de fabricacion', fontsize = 18)
# Label del eje y
plt.ylabel('Densidad', fontsize = 18)
# Defino un titulo
plt.title('Probabilidad empírica de ocurrencia')
# Muestro el plot
plt.show()

# Calculo la probabilidad de tardar menos de 3 minutos
print('y: ', y, '\n')
print('y[0]: ', y[0], '\n') # Alturas de las barras
print('y[1]: ', y[1], '\n') # Posiciones de los bordes de los bins
print('Ancho de cada bin: ', np.diff(y[1]), '\n') # Ancho de los bins

# Área bajo la curva cuando t < 3 min
print('Proba de que t < 3: ', np.sum(y[0][:3]*np.diff(y[1][:4])), '\n')

"""## Competencia petrolera"""

import numpy as np

# Estado inicial
E_ini = np.array([80, 20])

# Matriz de Transicion de 1 paso
P = np.array([[0.85,0.15],
              [0.25,0.75]])

E_final_semana_1 = E_ini @ P

print('Repartición del mercado total luego de 1 semana:', E_final_semana_1, '\n')

# Calculo la matriz de 3 pasos de transicion:
P3 = np.linalg.matrix_power(P, 3)

E_final_semana_3 = E_ini @ P3

print('Repartición del mercado total luego de 3 semanas:', E_final_semana_3, '\n')

## Calculo matriz de transicion (aproximado)
n = 100
T = np.linalg.matrix_power(P, n)

E_largo_plazo = E_ini @ T

print('Matriz de transición estacionaria:')
print(T, '\n')
print('Repartición del mercado total luego de n semanas:', E_largo_plazo, '\n')

"""### Predicción para varias semanas"""

import numpy as np
import matplotlib.pyplot as plt

# Estado inicial
E_ini = np.array([80, 20])

# Matriz de Transicion de 1 paso
P = np.array([[0.85,0.15],
              [0.25,0.75]])

pasos = np.arange(1, 15, 1, dtype=int)

Estados_vec = []
Proporcion_petrobras = []
Proporcion_axion = []

for i in range(len(pasos)):
    P_i = np.linalg.matrix_power(P, i)
    E_i = E_ini @ P_i
    Estados_vec.append(E_i)
    Proporcion_petrobras.append(E_i[0])
    Proporcion_axion.append(E_i[1])


# Hago los plots para cada empresa
plt.plot(pasos-1, Proporcion_petrobras, marker = 'o', label='Petrobras')
plt.plot(pasos-1, Proporcion_axion, marker = 'o', label='Axion')

# Label del eje x
plt.xlabel('pasos', fontsize = 16)
# Label del eje y
plt.ylabel('Proporción', fontsize = 16)
# Defino un titulo
plt.title('Vector de proba de estado para distintos pasos', fontsize = 16)
# Agrego una grilla
plt.grid()
# Agrego una leyenda
plt.legend()

"""## Ejemplo Markov: Viaje de clientes en una web"""

import numpy as np

# Estado inicial
E_ini = np.array([0.19,0.38,0.43])

# Matriz de Transicion de 1 paso
P = np.array([[0.32,0.47,0.21],
              [0.18,0.61,0.21],
              [0.22,0.29,0.49]])

# Calculo la matriz de 3 pasos de transicion:
P3 = np.linalg.matrix_power(P, 3)

print('La matriz de transición de 3 pasos es:\n', P3, '\n')

E_45_minutos = E_ini @ P3

print('La distribución de los jugadores a los 45 minutos es:', E_45_minutos, '\n')

## Calculo matriz de transicion (aproximado)
n = 100
T = np.linalg.matrix_power(P, n)

E_largo_plazo = E_ini @ T

print('Matriz de transición estacionaria:\n', T, '\n')
print('Distribución de jugadores a largo plazo:', E_largo_plazo, '\n')

## Calculo matriz de transicion de 12 pasos, es decir 3 horas.
n = 12
T = np.linalg.matrix_power(P, n)

## La probabilidad de volver a estar en el mismo juego son las diagonales
P_volver_3_horas = np.array([T[0,0], T[1,1], T[2,2]])

print('Matriz de transición de 12 pasos:\n', T, '\n')
print('Probabilidad de volver a estar en el mismo juego a las 3 horas:', P_volver_3_horas, '\n')