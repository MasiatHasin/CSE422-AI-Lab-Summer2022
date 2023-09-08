import math
import random

def generatePoints(n):
    randPoints = []
    for i in range(n):
        randPoints.append(random.randint(minimum, maximum))
    return randPoints

def minimax(points, b, node, depth, player, alpha, beta):
    if depth == 0:
        return points[node]
    if player == 'MAX':
        maxVal = -1000
        for i in range(0, b):
            val = minimax(points, b, (node*2)+i, depth-1, 'MIN', alpha, beta)
            maxVal = max(val, maxVal)
            alpha = max(alpha, maxVal)
        return maxVal
    else:
        minVal = 1000
        for i in range(0, b):
            val = minimax(points, b, (node*2)+i, depth-1, 'MAX', alpha, beta)
            minVal = min(val, minVal)
            beta = max(beta, minVal)
        return minVal

id = str(input("Enter your student ID: "))
if (id.find('0') != -1):
    id = id.replace('0', '8')

minimum = int(id[4])
tot2win = int(id[len(id)-1]+id[len(id)-2])
maximum = math.ceil(tot2win*1.5)
shuffleNum = int(id[3])

alpha = -1000
beta = 1000

branchingFactor = 2
depth = 3
terminalNodes = pow(branchingFactor, depth)

points = generatePoints(terminalNodes)

# Task 1
result = minimax(points, branchingFactor, 0, depth, 'MAX', alpha, beta)
print("Generated 8 random points between the minimum and maximum point limits:", points)
print("Total points to win:", tot2win)
print("Achieved point by applying alpha-beta pruning:", result)
if result > tot2win:
    print("Ther winner is Optimus Prime")
else:
    print("The winner is Megatron")

# Task 2
results = []
for i in range(shuffleNum):
    random.shuffle(points)
    result = minimax(points, branchingFactor, 0, depth, 'MAX', alpha, beta)
    results.append(result)
print("After the shuffle:")
print("List of all points values from each shuffles:", results)
maxRes = max(results)
print("The maximum value of all shuffles:", maxRes)
count = 0
for i in range(len(results)):
    if results[i]>tot2win:
        count+=1
print("won", count, "times out of", terminalNodes, "number of shuffles")