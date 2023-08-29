### Universidad de San Andres
### Investigacion Operativa
### Template Monte Carlo


import numpy as np
import matplotlib.pyplot as plt


######## Variables aleatorias #########
######## Variables aleatorias #########
######## Variables aleatorias #########

np.random.choice(np.arange(0, n), p=[p1, p2, p3, p4, ... , pn]) # distribucion custom discreta
np.random.normal( loc , scale ) # distribucion normal
np.random.uniform( low , high ) # distribucion uniforme continua
np.random.exponential( scale ) # distribucion exponencial
np.random.triangular( left , mode , right ) # distribucion triangular

######### Operaciones con Variables Aleatorias ######### 
######### Operaciones con Variables Aleatorias ######### 
######### Operaciones con Variables Aleatorias ######### 

# Suma de variables aleatorias X = X_1 + X_2. Ejemplo Uniforme + Exponencial
X = np.zeros(N)
for i in range(len(X)):
  X_1 = np.random.uniform( low , high )
  X_2 = np.random.exponential( scale )
  X[i] = X_1 + X_2

# Promedio y el desvío estándar de X
Promedio: np.mean(X)
Desvío estándar: np.std(X)


####### Vector de resultados ###########
####### Vector de resultados ###########
####### Vector de resultados ###########

### Formas de generar un vector de resultados ###
     ### Ejemplo con distribucion normal ###

###### Forma 1 #

# Defino lista vacía
datos = []
# Defino la cantidad de veces que voy a simular
N = 1000
for i in range(N):
  datos.append( np.random.normal( loc , scale ) )

###### Forma 2 #

N = 1000
# Defino array de N ceros
datos = np.zeros(N)

for i in range(len(datos)):
  datos[i] = np.random.normal( loc , scale )

###### Forma 3 #

datos = np.random.normal( loc , scale , size )


###### Explorar los valores de los datos generados
np.sum(datos > valor) # contar cuantas veces un valor es mayor a otro

###### Visualizacion #######
###### Visualizacion #######
###### Visualizacion #######

### Histogramas ###

x = datos_generados

# Grafico el histograma de cuentas
y = plt.hist(x,
             bins , range ,
             density = True,
             edgecolor='black')
# Label del eje x
plt.xlabel('x')
# Label del eje y
plt.ylabel('y')
# Defino un titulo
plt.title('Título')
# Agrego una grilla
plt.grid()
# Muestro el plot
plt.show()

y[0] # Alturas de las barras
y[1] # Posiciones de los bordes de los bins
np.diff(y[1]) # Ancho de los bins

# Área bajo la curva hasta t
Proba de que variable < t: np.sum(y[0][:t]*np.diff(y[1][:t+1]))

# Área bajo la curva de t en adelante
Proba de que variable > t: np.sum(y[0][t:]*np.diff(y[1][t-1:]))