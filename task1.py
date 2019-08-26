import sys
import math
with open("samplein.txt.", "r") as sys.stdin:
    while True:
        dimensions = sys.stdin.readline().strip().split()
        if dimensions == ['0', '0']:
            break
        n = int(dimensions[1]) # n is the number of columns
        m = int(dimensions[0]) # m is the number of rows
        z = dimensions #changes for 280 part 2
        costs = [[] for i in range(m)]
        for i in range(0,m):
            costs[i] = sys.stdin.readline().strip().split()
        costs.reverse()
        costs = [[row[i] for row in costs] for i in range(len(costs[0]))]


        # Sets up the distance dictionary
        dictDist = {}

        # Function to get the neighbours of a particular node
        def getNeighbours(i,j):
            neighbours = []
            for inc1 in range(-1, 2):
                for inc2 in range(-1, 2):
                    x = i + inc1
                    y = j + inc2
                    if x >= 0 and x <= n and y >= 0 and y <= m:
                        if not ((x,y) in visited):
                            neighbours.append((x,y))
            return neighbours

        # Function to get the cost of travelling to a particular node
        def getCost(i1,j1,i2,j2):
            dX = i2 - i1
            dY = j2 - j1

            # Diagonal move
            if abs(dX) == abs(dY) == 1:
                xCost = i1 if dX == 1 else i2
                yCost = j1 if dY == 1 else j2
                return costs[xCost][yCost]

            # Horizontal Move
            elif abs(dX) == 1:
                if j1 != 0 and j1 != m:
                    return min(costs[min(i1,i2)][j1 - 1], costs[min(i1,i2)][j1])
                elif j1 == 0:
                    return costs[min(i1,i2)][j1]
                else:
                    return costs[min(i1, i2)][j1-1]

            # Vertical Move
            elif abs(dY) == 1:
                if i1 != 0 and i1 != n:
                    return min(costs[i1 - 1][min(j1,j2)], costs[i1][min(j1,j2)])
                elif i1 == 0:
                    return costs[i1][min(j1,j2)]
                else:
                    return costs[i1-1][min(j1, j2)]

        currNode = [0,0]
        currDist = 0
        visited = [(0,0)]
        i = j = 0
        while(not (i == n and j == m)):
            neighbours = getNeighbours(currNode[0],currNode[1])
            for neigh in neighbours:
                neighCost = int(getCost(currNode[0], currNode[1], neigh[0], neigh[1]))
                if not (neigh in dictDist):
                    dictDist[neigh] = neighCost + currDist
                else:
                    if neighCost + currDist <= dictDist[neigh]:
                        dictDist[neigh] = neighCost + currDist

            # Select the minimum distance, remove from the distance dictionary, updates i/j
            currNode = min(dictDist, key=dictDist.get)
            currDist = dictDist[currNode]
            visited.append(currNode)
            del dictDist[currNode]
            i = currNode[0]
            j = currNode[1]

        sys.stdout.write(str(int(currDist)) + '\n')
