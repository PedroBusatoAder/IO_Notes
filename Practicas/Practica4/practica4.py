# Practica 4 - Metodo Monte Carlo y cadenas de Markov
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def ejercicio1():
    n = 1000
    numbers = []

    # Distribution parameters
    mu = 10
    sigma = 1
    
    for i in range (n):
        numbers.append(np.random.normal(mu, sigma))

    print('The mean observed from generating', n, 'numbers with normal distribution is', np.mean(numbers))
    print('The standard deviation observed from generating', n, 'numbers with normal distribution is', np.std(numbers))
    print('Observe how the empirical mean and standard deviation are almost the same as the computed ones')

    plt.hist(numbers, density = True, bins=10)
    plt.show()

def ejercicio2():
    n = int(input('How many iterations are you willing to see?'))
    numbers = []

    #Distribution parameters
    a = 0
    b = 1
    for i in range(n):
        numbers.append(np.random.uniform(a,b))

    print('The mean observed from generating', n, 'numbers with normal distribution is', np.mean(numbers))
    print('The standard deviation observed from generating', n, 'numbers with normal distribution is', np.std(numbers))
    print('Observe how the empirical mean and standard deviation are almost the same as the computed ones')

    plt.hist(numbers)
    plt.show()


def ejercicio3():
    n = int(input('How many iterations are you willing to see?'))
    sumDices = []
    for i in range(n):
        dice1 = np.random.choice(np.arange(1,7), p=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
        dice2 = np.random.choice(np.arange(1,7), p=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
        sumDices.append(dice1 + dice2)

    plt.hist(sumDices, bins = 11)
    plt.show()


def ejercicio5():
    n = 15000
    carsEachIteration = []
    for i in range(n):
        cars = np.random.choice(np.arange(0,6), p=[0.1, 0.13, 0.21, 0.23, 0.22, 0.11])
        carsEachIteration.append(cars)
    
    plt.hist(carsEachIteration, bins = 6, density=True) #Nunca comprendo como escoger la cantidad de bins
    plt.grid()
    plt.show()



def ejercicio6():
    iterations = 15
    wins = []
    loses = []
    gameMode = int(input('Ingrese la modalidad que desea jugar (1,2 o 3): '))

    for i in range (iterations):
        dice1 = np.random.randint(1,6)
        dice2 = np.random.randint(1,5)
        sumDices = dice1 + dice2
        print(sumDices)
        if(sumDices > 6 and gameMode == 3):
            wins.append(1)
        elif(sumDices > 5 and gameMode == 2):
            wins.append(1)
        elif(sumDices > 4 and gameMode ==1):
            wins.append(1)
        else:
            loses.append(1)
    
    print('Se ha seleccionado la modalidad', gameMode, 'con un total de', iterations, 'iteraciones')
    print('Se han ganado un total de', sum(wins), 'fichas -->', str(sum(wins)/iterations * 100) + '%')
    print('Se han perdido un total de', sum(loses), 'fichas -->', str(sum(loses)/iterations * 100) + '%')
    print('De esta manera, el balance final de fichas es de:', sum(wins)-sum(loses), 'fichas')


def ejercicio7():
    iterations = 1000
    asistance = []

    for i in range(iterations):
        dailyAsistance = np.random.choice(np.arange(1,6), p=[0.1, 0.15, 0.25, 0.35, 0.15])
        asistance.append(dailyAsistance)

    plt.hist(asistance, bins=6, density = True) #Me dan problemas los bins
    plt.xlabel('Cantidad trabajadores que asistieron ese dia')
    plt.ylabel('Frecuencia de asistencia')
    plt.show()

def ejercicio8():
    iterations = 10000
    sum = []
    for i in range(iterations):
        normal1 = np.random.normal(loc = 100, scale = 3)
        normal2 = np.random.normal(loc = 30, scale = 1)
        sum.append(normal1 + normal2)
    
    plt.hist(sum, density = True, bins = 10)
    plt.xlabel('Suma de las dos Normales')
    plt.ylabel('Frecuencia de la suma')
    plt.show()



def ejercicio9():

    trans1 = np.array([[0.9,0.1],[0.2,0.8]])               #Inicialmente las matrices de transicion son iguales
    transM = np.array([[0.9,0.1],[0.2,0.8]])

    initialState = np.array([1,0])                          #Decimos a la simulacion que el dia de hoy esta soleado

    possibleStates = np.shape(trans1)[0]                    #Sabemos que hay dos estados posibles --> Nublado o soleado
    iterations = 50

    results = np.zeros((iterations, possibleStates))        #Matriz de 'iterations' filas y dos columnas para almacenar en cada fila el estado en dicho tiempo 't'

    for i in range(iterations):
        followingState = np.dot(initialState, transM)
        results[i] = followingState
        transM = np.dot(trans1, transM)

    print(results)

    sns.set_context(context = 'talk', font_scale = 0.8)
    plt.title('Vector de probabilidad del estado M')
    plt.plot(results[:,0], marker = 'o', label = 'soleado')
    plt.plot(results[:,1], marker = 'o', label = 'nublado')
    plt.xlabel('Cantidad de pasos')
    plt.ylabel('Probabilidad de estado')
    plt.show()
    






def ejercicio10():
    period = 4
    transition1 = np.array([[0.3,0.5,0.2],[0.2,0.4,0.4],[0.3,0.5,0.2]])             #Matriz de transicion
    transitionM = np.array([[0.3,0.5,0.2],[0.2,0.4,0.4],[0.3,0.5,0.2]])             #En un primer momento las matrices de transicion son iguales
    initialState = np.array([1,0,0])                                                #Tenemos la certeza de que hoy el sistema se encuentra en demanda baja

    possibleStates = (np.shape(initialState)[0])
    allStates = np.zeros((period, possibleStates))

    for i in range(period):
        finalState = np.dot(initialState, transitionM)
        allStates[i] = finalState

        transitionM = np.dot(transition1, transitionM)

    print('La probabilidad de que el data center luego de', period, 'dias se encuentre en alta es de:', round(allStates[period-1][2], 2))
    sns.set_context(context = 'talk', font_scale = 0.8)
    plt.title('Vector de probabilidad del estado M')
    plt.plot(allStates[:,0], marker = 'o', label = 'Baja')
    plt.plot(allStates[:,1], marker = 'o', label = 'Media')
    plt.plot(allStates[:,2], marker = 'o', label = 'Alta')
    
    plt.xlabel('Cantidad de dias')
    plt.ylabel('Probabilidad de estado')
    plt.show()

def ejercicio11():
    iterations = 50                                                   # Cantidad de dias que simularemos el modelo de Markov

    transition1 = np.array([[0.1,0.3,0.6],[0.2,0.2,0.6],[0.2,0.4,0.4]])
    transitionM = np.array([[0.1,0.3,0.6],[0.2,0.2,0.6],[0.2,0.4,0.4]])
    
    initialState = np.array([0,0,1])                                    # Inicialmente nos encontramos en la ciudad C
    possibleStates = np.shape(initialState)[0]

    allStates = np.zeros((iterations, possibleStates))                  #Guardara las probabilidades de estado para cada una de las iteraciones --> Cada fila representa una probabilidad de estado

    for i in range(iterations):
        followingState = np.dot(initialState, transitionM)
        transitionM = np.dot(transition1, transitionM)                  # Vamos actualizando la matriz de transicion
        allStates[i] = followingState
    
    print('La probabilidad de que al cabo de dos dias el ingeniero se encuentre en la ciudad C es de:', allStates[2][2])
    print('A continuacion vemos graficamente las probabilidades al largo plazo (' + str(iterations) + ' iteraciones):')
   
    sns.set_context(context = 'talk', font_scale = 0.8)
    plt.title('Vector de probabilidad del estado M')
    plt.plot(allStates[:,0], marker = 'o', label = 'Ciudad A')
    plt.plot(allStates[:,1], marker = 'o', label = 'Ciudad B')
    plt.plot(allStates[:,2], marker = 'o', label = 'Ciudad C')
    
    plt.xlabel('Cantidad de dias')
    plt.ylabel('Probabilidad de Estado')
    plt.show()
ejercicio11()
