import numpy as np
import matplotlib.pyplot as plt

#Ejercicio 5
#Los posibles estados --> cantidad de autos acumulados en cada semaforo --> 0,1,2,3,4,5 autos
def ejercicio5():
    iterations = 1000
    eachLight = []           #Guardamos la cantidad de autos acumulados en cada semaforo
    for i in range (iterations):
        cars = np.random.choice(np.arange(0,6), p=[0.1, 0.13, 0.21, 0.23, 0.22, 0.11])
        eachLight.append(cars) 
    
    plt.hist(eachLight, bins = 6 ,density = True)
    plt.xlabel('Cantidad de autos')
    plt.ylabel('Frecuencia')
    plt.show()

#Ejercicio6
#Posibles estados --> Suma de los dos dados --> 1,2,3,4,5,6,7,8,9
def ejercicio6():
    iterations = 1000
    coinsEachGame = []
    for x in range(3):
        coins = []                                  # Cada vez que se cambia la modalidad del juego se reinicia la cantidad de monedas conseguidas
        for i in range(iterations):
            dice1 = np.random.randint(1,6)
            dice2 = np.random.randint(1,5)
            sumDices = dice1 + dice2
            if  x == 0 and sumDices > 4:                             #Primera modalidad de juego
                coins.append(1)
            elif x == 1 and sumDices > 5:
                coins.append(1)
            elif x == 2 and sumDices > 6:
                coins.append(1)
            else:
                coins.append(0)
        coinsEachGame.append(sum(coins))
        print('La cantidad de monedas conseguidas para el juego', x+1 ,'fueron:', sum(coins)) 
    
    plt.hist(coinsEachGame, bins=5)
    plt.xlabel('Numero de juego')
    plt.ylabel('Frecuencia de ocurrencia')
    plt.show()

ejercicio6()
