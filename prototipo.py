from pyevolve import G1DList, GSimpleGA, Selectors
from pyevolve import Initializators, Mutators, Consts
from pyevolve import Interaction as it
import math
import numpy as np
import matplotlib.pyplot as pyplot
import argparse

#Definiendo argumentos
ap = argparse.ArgumentParser()
ap.add_argument('-rmin','--rangemin',type=int, required=True,help='help: rango minimo')
ap.add_argument('-rmax','--rangemax',type=int, required=True,help='help: rango maximo')
args = vars(ap.parse_args())

#Rangos para el eje x
rangemin=args["rangemin"]
rangemax=args["rangemax"]


#metodo para graficar la funcion y el punto minimo
def graficar(xmin,ymin):
    x=np.arange(rangemin,rangemax)
    pyplot.plot(x, [f(i) for i in x])
    #pyplot.plot(x, [ElipseEscNgt(i,w,h) for i in x])
    pyplot.plot(xmin,ymin , marker='o', markersize=3, color="red")
    pyplot.xlim(rangemin,rangemax)
    pyplot.ylim(rangemin,rangemax)
    pyplot.show()

#metodo de la funcion (x+1)**2 +1 
def f(x):
	r=math.pow(x+1,2)+1 
	return r 

#funcion fitnnes, evalua el genoma en la funcion
def fit_func(genome):
   score=0
   t1=f(genome[0])
   if t1>-1:
       score=t1
   return score

def run_main():
   # Instancia del genoma
   genome = G1DList.G1DList(2) #tupla de valores iniciales (x,y) para la evolucion
   genome.setParams(rangemin=rangemin, rangemax=rangemax, bestrawscore=0.0000, rounddecimal=4)
   genome.initializator.set(Initializators.G1DListInitializatorReal) #indicar que se utilizan numeros reales
   genome.mutator.set(Mutators.G1DListMutatorRealGaussian) #estableciendo el metodo de mutacion de los genomas hijos

   # Estableciendo la fucion fitnnes al genoma
   genome.evaluator.set(fit_func)

   # Instancia del algoritmo genetico
   ga = GSimpleGA.GSimpleGA(genome)
   ga.selector.set(Selectors.GRouletteWheel)
   #Tipo de optimizacion minimizar
   ga.setMinimax(Consts.minimaxType["minimize"])
   ga.setGenerations(100) #numero de generaciones
   ga.setMutationRate(0.05) #tasa de mutacion
   ga.setPopulationSize(100) #longitud de la poblacion
   ga.terminationCriteria.set(GSimpleGA.RawScoreCriteria)

   # Volcar las estadisticas para la evolucion
   # Frecuencia de 20 generaciones
   ga.evolve(freq_stats=20)

   # Best individual
   best = ga.bestIndividual()
   #pop = ga.getPopulation()
   #it.plotHistPopScore(pop)
   #it.plotPopScore(pop)
   print best
   print "Best individual score: %.2f" % best.getRawScore()
   graficar(best[0],best.getRawScore())

if __name__ == "__main__":
   run_main()




