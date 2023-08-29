### Universidad de San Andres
### Licenciatura en Negocios Digitales
### Investigacion Operativa
### Autor: Martin Palazzo


####################### Importamos librerias #######################
####################### Importamos librerias #######################
####################### Importamos librerias #######################

# Importamos Numpy para hacer cuentas con vectores, matrices
import numpy as np
# Importamos Matplotlib para visualizar
import matplotlib.pyplot as plt
# importamos seaborn
import seaborn as sns

# definimos una funcion que simula la cantidad de clientes en el sistema en base a eventos de arribos y despachos que suceden

def simular_fila_1canal(mins, n_eventos, lambda_arribos, lambda_despachos):

  # generamos eventos aleatorios de arribos y despachos utilizando distribucion exponencial
  arribos = np.random.exponential(1/lambda_arribos,n_eventos)*60
  despachos = np.random.exponential(1/lambda_despachos,n_eventos)*60

  # acumulamos los eventos en el tiempo
  arribos_cum = np.cumsum(arribos)*60
  despachos_cum = np.cumsum(despachos)*60

  # el vector clientes guardara el N de clientes que se encuentren en el sistema a cada minuto
  clientes = np.zeros((mins))

  # guardamos la cantidad de arribos y despachos que suceden en toda la simulacion
  num_arribos = 0
  num_despachos = 0

  # guardamos en que instante sucedio un evento de arribo o despacho
  tiempo_arribos = np.zeros((n_eventos))
  tiempo_despachos = np.zeros((n_eventos))

  counter = 1

  # for loop por la cantidad de minutos
  for i in range(1,mins):

    # preguntamos si hubo un arribo en el minuto actual
    if i > arribos_cum[num_arribos]:
      clientes[counter] = clientes[counter-1]+1
      tiempo_arribos[num_arribos] = i
      num_arribos += 1 

    # preguntamos si hubo un despacho en el minuto actual
    elif i > despachos_cum[num_despachos]: 
      if clientes[counter-1] > 0:
        tiempo_despachos[num_despachos] = i
        clientes[counter] = clientes[counter-1] - 1
        num_despachos += 1

    # si no hubo eventos dejamos todo igual
    else:
      clientes[counter] = clientes[counter-1]

    counter += 1

  return num_despachos, num_arribos, tiempo_despachos, tiempo_arribos, clientes

# definimos parametros de la simulacion
n_eventos = 10000
lambda_arribos = 8
lambda_despachos = 8.3

# corremos la simulacion con los parametros determinados
num_despachos, num_arribos, t_despachos, t_arribos, clientes = simular_fila_1canal(50000, n_eventos, lambda_arribos, lambda_despachos)


sns.set_context("talk")
plt.figure(figsize=(10,4))
plt.plot(clientes)
plt.title("Lambda arribos = " + str(lambda_arribos) + ". lambda despachos = " + str(lambda_despachos))
plt.xlabel("Minutos")
plt.ylabel("Estado del sistema")
plt.show()

plt.figure(figsize=(10,4))
#plt.hist(clientes, bins = 11)
sns.histplot(clientes, bins = 12)
plt.title("Lambda arribos = " + str(lambda_arribos) + ". lambda despachos = " + str(lambda_despachos))
plt.xlabel("estado del sistema")
plt.ylabel("frecuencia")
plt.plot()


# definimos parametros de la simulacion
n_eventos = 10000
lambda_arribos = 8.2
lambda_despachos = 8.3

# corremos la simulacion con los parametros determinados
num_despachos, num_arribos, t_despachos, t_arribos, clientes = simular_fila_1canal(50000, n_eventos, lambda_arribos, lambda_despachos)

sns.set_context("talk")
plt.figure(figsize=(10,4))
plt.plot(clientes)
plt.title("Lambda arribos = " + str(lambda_arribos) + ". lambda despachos = " + str(lambda_despachos))
plt.xlabel("Minutos")
plt.ylabel("Estado del sistema")
plt.show()


plt.figure(figsize=(10,4))
#plt.hist(clientes, bins = 11)
sns.histplot(clientes, bins = 12)
plt.title("Lambda arribos = " + str(lambda_arribos) + ". lambda despachos = " + str(lambda_despachos))
plt.xlabel("estado del sistema")
plt.ylabel("frecuencia")
plt.plot()


# definimos parametros de la simulacion
n_eventos = 10000
lambda_arribos = 10
lambda_despachos = 8.3


# corremos la simulacion con los parametros determinados
num_despachos, num_arribos, t_despachos, t_arribos, clientes = simular_fila_1canal(50000, n_eventos, lambda_arribos, lambda_despachos)

sns.set_context("talk")
plt.figure(figsize=(10,4))
plt.plot(clientes)
plt.title("Lambda arribos = " + str(lambda_arribos) + ". lambda despachos = " + str(lambda_despachos))
plt.xlabel("Minutos")
plt.ylabel("Estado del sistema")
plt.show()


plt.figure(figsize=(10,4))
#plt.hist(clientes, bins = 11)
sns.histplot(clientes, bins = 12)
plt.title("Lambda arribos = " + str(lambda_arribos) + ". lambda despachos = " + str(lambda_despachos))
plt.xlabel("estado del sistema")
plt.ylabel("frecuencia")
plt.plot()



