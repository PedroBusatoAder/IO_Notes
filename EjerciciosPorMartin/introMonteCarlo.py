#Ver si la suma de uniformes es una uniforme
import numpy as np
import matplotlib.pyplot as plt

iterations = 10000

totalIterations = np.zeros(iterations)
print(totalIterations)
for x in range(iterations):
    restaurantTime = np.random.uniform(0,21)
    deliveryTime = np.random.uniform(20,41)
    totalIterations[x] = deliveryTime + restaurantTime

#Queremos saber la cantidad de elementos en los que el tiempo total sean mayores a 40
mayores40 = np.sum(totalIterations > 40) #Devuelve un array con true o false dependiendo de si se cumple la condicion o no

print('La probabilidad empirica de que el tiempo total sea mayor a 40 es:', mayores40/len(totalIterations))


print(totalIterations)
plt.hist(totalIterations, bins = 20)
plt.show()





