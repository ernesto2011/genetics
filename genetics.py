
# el genset es de donde se obtienen los caractres  y letras para poder crear una ṕoblación aleatoria
geneSet = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ,.! '
#el target es el texto objetivo a encontrar mediante un algoritmo genetico 
target = input("ingrese el texto a encontrar:  ")

#importación de la librerias
import datetime
import random
random.seed(2)

#cuando se ejecuta el programa aqui se toma el tiempo cuando inicia
startTime = datetime.datetime.now()

#Funcion para generar de manera aleatoria una muestra de genes y este será el padres
def generate_parent(length):
    genes = [] #Lista donde se almacenan las secuencia aleatoria
    while len(genes) < length: 
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet,sampleSize)) #Obtención de la muestra aleatoria
    return ''.join(genes) #Regresamos una cadena 
    
#Funcion de optimización, si el nuestra muestra aleatoria tiene un caracter igual a nuestro target
#en el cual la optimización se sumara 1 si en la muestra aleatoria coinside en lugar y en caracter
def get_fitness(guess):
    return sum(1 for expected, actual in zip(target,guess) if expected == actual)

#Funcion para mutar a nuestra cadena original o padre
def mutate(parent):
    index = random.randrange(0,len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet,2) #se hace una muestra aleatoria, se agrega y se itera en este proceso
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    return ''.join(childGenes)#regresamos una cadena

#Funcion para imprimir en pantalla los resultados
def display(guess):
    timeDiff = datetime.datetime.now() - startTime#se resta el tiempo inicial - el final para obtener el resultado
    fitness = get_fitness(guess)
    print('{}\t{}\t{}'.format(guess,fitness,timeDiff))#imprimos el guess, la generacíon y el tiempo que le tomo


#Inicializamos nuestros parametros
bestParent = generate_parent(len(target))#aqui se inicializa al padre con la logitud de tarhet como mejor padre
bestFitness = get_fitness(bestParent)#despues con la función de aptitud vemos que tanto coincide con la cadena original
display(bestParent)#aqui mostramos al padre

#Creamos un ciclo para iterar nuestras funciones
#Hasta obtener nuestro target

while True:
    #empeamos a mutar al padre y a crear hijos del padre
    child = mutate(bestParent)
    #obtenemos su aptitud del hijo
    childFitness = get_fitness(child)
    #si se cumple esta condicion de el mejor fitness el mayor igual al childfitness
    if bestFitness >= childFitness:
        continue
    display(child) #mostramos el hijo
    if childFitness >= len(bestParent):#si se cumple esta condicion se termina el ciclo iterativo
        break
    bestFitness = childFitness #aqui gardamos el mejor fitness del hijo 
    bestParent = child #igual se aguarda al mejor hijo que se paresca al target
