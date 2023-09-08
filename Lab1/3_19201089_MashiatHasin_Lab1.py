#Question 1
def DFS(people, start, region):
    visited.append(start)
    infected = []
    region += 1
    
    row = start[0]
    col = start[1]
    
    #top
    if (row-1 >= 0 and people[row-1][col]=="Y"):
        infected.append([row-1,col])
    
    #bottom
    if (row+1 < len(people) and people[row+1][col]=="Y"):
        infected.append([row+1,col])
        
    #left
    if (col-1 >= 0 and people[row][col-1]=="Y"):
        infected.append([row,col-1])
    
    #right
    if (col+1 < len(people[0]) and people[row][col+1]=="Y"):
        infected.append([row,col+1])
    
    #upper left
    if (row-1 >= 0 and col-1 >= 0 and people[row-1][col-1]=="Y"):
        infected.append([row-1,col-1])
        
    #upper right
    if (row-1 >= 0 and col+1 < len(people[0]) and people[row-1][col+1]=="Y"):
        infected.append([row-1,col+1])
        
    #lower left
    if (row+1 < len(people) and col-1 >= 0 and people[row+1][col-1]=="Y"):
        infected.append([row+1,col-1])
    
    #lower right
    if (row+1 < len(people) and col+1 < len(people[0]) and people[row+1][col+1]=="Y"):
        infected.append([row+1,col+1])
        
    for i in infected:
        if i not in visited:
            region = DFS(people, i, region)
    return region


file1 = open('input1.txt', 'r')
people = file1.read()
people = people.replace("\t", "")
people = people.replace(" ", "")
people = people.split("\n")

visited = []
maxRegion = 0

for i in range(len(people)):
    for j in range(len(people[i])):
        region = 0
        if (people[i][j]=="Y" and [i,j] not in visited):
            region = DFS(people, [i,j], region)
            if region > maxRegion:
                maxRegion = region 

print("Output for Question 1:")                  
print(maxRegion)

#-----------------------------------------------------------------------------

#Question 2
def BFS(grid, index, queue, visited):
    row = queue[0][0]
    col = queue[0][1]
    lvl = queue[0][2]
    alienPos[index][2] = lvl
    
    #top
    if (row-1>=0 and grid[row-1][col]=="H"):
        queue.append([row-1,col,lvl+1])
        xcity[row-1]= xcity[row-1][:col] + "A" + xcity[row-1][col+1:]
    #left
    if (col-1>=0 and grid[row][col-1]=="H"):
        queue.append([row,col-1,lvl+1])
        xcity[row]= xcity[row][:col-1] + "A" + xcity[row][col:]
    #down
    if (row+1< len(grid) and grid[row+1][col]=="H"):
        queue.append([row+1,col,lvl+1])
        xcity[row+1]= xcity[row+1][:col] + "A" + xcity[row+1][col+1:]
    #right
    if (col+1< len(grid[0]) and grid[row][col+1]=="H"):
        queue.append([row,col+1,lvl+1])
        xcity[row]= xcity[row][:col+1] + "A" + xcity[row][col+2:]

    visited.append([row,col, lvl])    
    queue.pop(0)
    if(len(queue) != 0 and queue[0] not in visited):
        BFS(grid, index, queue, visited)
        
def findPosition(grid, row, col, elem):
    position = []
    for i in range(row):
        for j in range(col):
            if grid[i][j]==elem:
                position.append([i,j,0]) 
    return position

           
file2 = open('input2.txt', 'r')
xcity = file2.read()
xcity = xcity.replace("\t", "")
xcity = xcity.replace(" ", "")
xcity = xcity.split("\n")

row = int(xcity.pop(0))
col = int(xcity.pop(0))

visited = []

alienPos = findPosition(xcity, row, col, 'A')

for i in range(len(alienPos)):
    BFS(xcity, i, [alienPos[i]], visited)
 
alienPos.sort(key=lambda alienPos:alienPos[2])
time = alienPos[-1][2]
print("Output for Question 2:")    
print("Time: " + str(time) + " minutes")

humanPos = findPosition(xcity, row, col, 'H')
humans = len(humanPos)
if (humans == 0):
    print("No one survived")
else:
    print(str(humans)+ " survived")