import sys
import math
from random import randint as rand

file1 = open('input.txt', 'r')
batsmen = file1.read()
batsmen = batsmen.split("\n")

prop =  batsmen[0].split(" ")
N = int(prop[0])
T = int(prop[1])

batsmen.pop(0)
name = []
R = []

threshold = sys.getrecursionlimit()

for i in range(len(batsmen)):
    info = batsmen[i].split(" ")
    name.append(info[0])
    R.append(int(info[1]))

def fitness(pattern):
    score = 0
    for i in range(len(pattern)):
        if pattern[i]=="1":
            score+= R[i]
    return score

def crossover(parent1 , parent2):
    midpoint = int(math.ceil(N/2.0))
    x = parent1[:midpoint]+parent2[midpoint:]
    y = parent2[:midpoint]+parent1[midpoint:]
    return x,y

def mutation(parent):
    index = int(str(rand(0, N-1)))
    if parent[index]=="1":
        change = "0"
    else:
        change = "1"
    mutant = parent[:index]+change+parent[index+1:]
    return mutant
    
def randPopulation(size):
    string = ""
    for i in range(size):
        string+=str(rand(0, 1))
    return(string)
    
def geneticAlgo(parent1, parent2, threshold):
    x, y = crossover(parent1,parent2)
    if (fitness(x)==T):
        return x
    elif (fitness(y)==T):
        return y
    elif (threshold==0):
        return -1
    else:
        threshold-=1
        x = mutation(x)
        y = mutation(y)
        return geneticAlgo(x,y,threshold)

x = randPopulation(N)
y = randPopulation(N)
print(name)
result = geneticAlgo(x, y, threshold)
print(result)
