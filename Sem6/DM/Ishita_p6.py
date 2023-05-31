V=4
c = [
    [0,0,0,0, 0],
    [0,0, 10, 15, 20],
    [0,10, 0, 35, 25],
    [0,15, 35, 0, 30],
    [0,20, 25, 30, 0]]

graph=[[0 for column in range(V)]for row in range(V)]
for i in range(1,len(c)):
    for j in range(1,len(c)):
        if c[i][j]!=0:
            graph[i-1][j-1]=1
        else:
            graph[i-1][j-1]=0
print(graph)

def isSafe(v, pos, path):
    if graph[ path[pos-1] ][v] == 0:
        return False

    for vertex in path:
        if vertex == v:
            return False

    return True

def hamCycleUtil(path, pos):
    if pos == V:
        if graph[path[pos-1]][path[0]] == 1:
            return True
        else:
            return False
    for v in range(1,V):

        if isSafe(v,pos,path) == True:

            path[pos] = v

            if hamCycleUtil(path,pos+1) == True:
                return True
            path[pos] = -1

    return False

def hamCycle():
    path = [-1] * V
    path[0] = 0

    if hamCycleUtil(path,1) == False:
        print ("Solution does not exist\n")
        return False

    print ("Solution Exists: Following is one Hamiltonian Cycle")
    for vertex in path:
        print (vertex,end = " ")
    print (path[0], "\n")
    return True



hamCycle()


def tsp(c,path, start,cities):
    temp = [0,0,0,0,0]
    minDist=999
    optimumPath = [0,0,0,0,0]
    if start == cities-1 :
        return (c[path[cities-1]][path[cities]] + c[path[cities]][1])
    for i in range(start+1,cities+1):
        for j in range (1,cities+1):
            temp[j]=path[j]

        temp[start+1] = path[i]

        temp[i] = path[start+1]
        ccost = tsp(c,temp,start+1,cities)

        if ((c[path[start]][path[i]]+ccost)<minDist ):
            minDist = c[path[start]][path[i]] + ccost

            for k in range(1,cities+1):
                optimumPath[k]=temp[k]


    for i in range(1,cities+1):
        path[i] = optimumPath[i]

    return minDist


cities=4
path = [0,0,0,0,0]
if(cities==1) :
    print("Path Not Possible!")
    exit(0)
'''
c = [
[0,0,0,0,0],
[0,0, 20, 30, 10, 11],
[0,15, 0, 16, 4, 2],
[0,3, 5, 0, 2, 4],
[0,19, 6, 18, 0, 3],
[0,16, 4, 7, 16, 0]]
'''


for i in range (1,cities+1):
    path[i]=i
cost = tsp(c,path,1,cities)
print("The Optimal Path is: ")
for i in range (1,cities+1):
    print(path[i], end=" -> ")
print("1")
print("Minimum Cost: ",cost)
