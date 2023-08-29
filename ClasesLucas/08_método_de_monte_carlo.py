"""
## Acumulación de autos en un semáforo
"""
import matplotlib.pyplot as plt
import numpy as np
# Defino lista vacía
cantidad_autos_semaforo = []

# Defino la cantidad de veces que voy a simular
N = 1000 # 10, 100 y 1000

for i in range(N):
  # En este caso el arange va de 0 a 5 porque tengo de 0 a 4 autos
  cantidad_autos_semaforo.append( np.random.choice(np.arange(0, 5), p=[0.15, 0.2, 0.35, 0.23, 0.07]) )

x = cantidad_autos_semaforo
#Genero el histograma
Y, bins = np.histogram(x, bins=np.arange(0, 6)) #El histograma retorna dos valores, por lo que la variable donde almacenamos es doble!
#Grafico el histograma
plt.bar(bins[:-1], Y / np.sum(Y), width=0.7, alpha = 0.5)

# Label del eje x
plt.xlabel('x', fontsize = 18)
# Label del eje y
plt.ylabel('Frecuencia', fontsize = 18)
# Defino un titulo
plt.title('Proba de tener X autos en el semáforo esperando')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

"""## 2 dados que suman 5"""

import numpy as np

# Defino el número de veces que voy a tirar los dados
N = 10000
# Contador, va a sumar 1 cada vez que el resultado de la suma sea 5
count = 0
for i in range(N):
    # El + 1 está porque randint empieza en 0
    d_1 = np.random.randint(6) + 1
    d_2 = np.random.randint(6) + 1
    if d_1 + d_2 == 5:
        count = count + 1

# La probabilidad de que la suma sea 5 es la cantidad de éxitos sobre el total.
proba_empirica = count / N
print('La probabilidad empirica es: p =', proba_empirica)

"""## Dos dados, uno con 8 caras otro con 5, suman 7."""

import numpy as np

N = 100000

count = 0

for i in range(N):
  d_1 = np.random.randint(8) + 1
  d_2 = np.random.randint(5) + 1
  if d_1 + d_2 == 7:
    count += 1

"""## Cálculo de Pi

### Cálculo del área
"""

import numpy as np
import matplotlib.pyplot as plt

# Defino el número de veces que voy a samplear x e y
N_it = 50

# Contador para saber la cantidad de veces que el punto cayó dentro de la circ.
N_acepto = 0
# Guardo las coordenadas del punto aceptado
X_acepto = []
Y_acepto = []

# Contador para saber la cantidad de veces que el punto cayó fuera de la circ.
N_rechazo = 0
# Guardo las coordenadas del punto rechazado
X_rechazo = []
Y_rechazo = []


for i in range(N_it):
    #genero un valor de x e y random entre 0 y 1
    x = np.random.rand(1)
    y = np.random.rand(1)

    # Acepto el punto si cae dentro de la circ.
    if x**2 + y**2 <= 1:
        N_acepto = N_acepto + 1
        X_acepto.append(x)
        Y_acepto.append(y)
    # Rechazo el punto si cae fuera de la circ.
    else:
        N_rechazo = N_rechazo + 1
        X_rechazo.append(x)
        Y_rechazo.append(y)

# Exitos sobre total de tiros
proporcion = N_acepto / N_it

print('cantidad de exitos sobre el total de intentos =',proporcion, '\n')

# Calculo pi considerando los 4 cuadrantes
valor_de_pi = 4 * N_acepto / N_it

print('pi calculado =',valor_de_pi, '\n')


plt.figure(figsize=(6,6))
# Plot de puntos
plt.scatter(X_acepto, Y_acepto) # Azul
plt.scatter(X_rechazo, Y_rechazo) # Naranja

# Genero este conjunto de puntos para plotear la circunferencia
x_aux = np.linspace(0,1,100)
plt.plot(x_aux, np.sqrt(1 - x_aux**2), color = 'r')

# Label del eje x
plt.xlabel('x', fontsize = 18)
# Label del eje y
plt.ylabel('y', fontsize = 18)
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

"""### Cálculo del área en función del número de iteraciones"""

import numpy as np
from math import pi
import matplotlib.pyplot as plt

# Defino el número de veces que voy a samplear x e y
# Esto es lo mismo que arriba pero variando la cantidad de iteraciones
N_it = np.linspace(1, 500, 50)

# Voy a guardar sólo el valor de pi obtenido en cada pasada.
# Cada pasada tiene más número de intentos que la anterior.
valor_de_pi = []

# For que recorre los números de iteraciones
for i in range(len(N_it)):
    N_acepto = 0
    X_acepto = []
    Y_acepto = []

    N_rechazo = 0
    X_rechazo = []
    Y_rechazo = []

    # For para calcular pi para este número de iteración
    for j in range(int(N_it[i])):
        x = np.random.rand(1)
        y = np.random.rand(1)

        if x**2 + y**2 <= 1:
            N_acepto = N_acepto + 1
            X_acepto.append(x)
            Y_acepto.append(y)
        else:
            N_rechazo = N_rechazo + 1
            X_rechazo.append(x)
            Y_rechazo.append(y)

    valor_de_pi.append( 4 * N_acepto / N_it[i] )

# Plot de lineas
plt.scatter(N_it, valor_de_pi)
# Label del eje x
plt.xlabel('Cantidad de iteraciones', fontsize = 18)
# Label del eje y
plt.ylabel('Valor de $\pi$ estimado', fontsize = 18)
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

"""## Juego de dados modificado"""

import numpy as np

# Cantidad de veces que pretendo jugar
nro_juegos = 10
# Contador de la cantidad de veces que gano
ganados = 0
# Contador de las tiradas necesarias para ganar.
# Va a ser un vector con las tiradas necesarias para ganar en cada
# uno de los juegos
tiradas = []

# Voy a iterar (jugar) nro_juegos veces
for i in range(nro_juegos):
    # state es una variable auxiliar que indica:
    # Si es 0: no gané ni perdí. Si es -1 perdí. Si es 1 gané.
    state = 0
    # Contador de tiros en cada juego individual
    tiros = 0
    # Va a iterar mientras state = 0, es decir si no gano ni pierdo
    # puede seguir infinitamente
    while state == 0:
        # tiro dos dados aleatorios. Cae entre 1 y 6. Entero.
        dados = np.random.randint(1,7,2)
        # sumo los resultados de la tirada de los dos dados
        suma = np.sum(dados)
        # agrego el tiro al contador
        tiros = tiros + 1
        # si entro acá es que salió 7 u 11 y gané
        if suma == 7 or suma == 11:
            # sumo uno al contador de ganados
            ganados +=1
            # paso el estado a 1 para indicarle al while que deje de iterar
            state = 1
            # guardo la cantidad de tiradas necesaria para ganar
            tiradas.append(tiros)
        # si entro acá es que salió 2, 3 o 12 y perdí
        elif suma == 2 or suma == 3 or suma == 12:
            # paso el estado a -1 para indicarle al while que deje de iterar
            state = -1
        # Si no gano ni pierdo indico "pass" para decirle que siga nomás.
        else:
            pass
        

print('cantidad de juegos ganados =', ganados)
print('cantidad de juegos totales =', nro_juegos)
print('proporcion de juegos ganados =', ganados/nro_juegos, '\n')

print('cantidad de tiradas para ganar promedio', np.mean(tiradas))

"""### Proporcion de juegos ganados en función del número de intentos"""

import numpy as np

# Esto es lo mismo que arriba pero variando la cantidad de iteraciones
nro_juegos = np.linspace(10, 500, 50)

# Voy a almacenar los ganados y las tiradas para cada una de las veces que juegue
ganados_vec = []
tiradas_vec = []

# For que recorre los números de iteraciones,  es decir la cantidad de juegos
# total por corrida
for i in range(len(nro_juegos)):
    ganados = 0
    tiradas = []
    # Voy a iterar (jugar) nro_juegos veces
    for j in range(int(nro_juegos[i])):
        state = 0
        tiros = 0
        while state == 0:
            dados = np.random.randint(1,7,2)
            suma = np.sum(dados)
            tiros = tiros + 1
            if suma == 7 or suma == 11:
                ganados +=1
                state = 1
                tiradas.append(tiros)
            elif suma == 2 or suma == 3 or suma == 12:
                state = -1
            else:
                pass
    tiradas_vec.append(np.mean(tiradas))
    ganados_vec.append(ganados)


# Plot de lineas
plt.plot(nro_juegos, ganados_vec/nro_juegos)
# Label del eje x
plt.xlabel('Cantidad de iteraciones', fontsize = 18)
# Label del eje y
plt.ylabel('Proporcion de victorias', fontsize = 18)
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

# Plot de lineas
plt.plot(nro_juegos, tiradas_vec)
# Label del eje x
plt.xlabel('Cantidad de iteraciones', fontsize = 18)
# Label del eje y
plt.ylabel('Número de tiradas estimado', fontsize = 18)
# Título
plt.title('Número de tiradas necesarios para ganar estimado', fontsize = 18)
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()