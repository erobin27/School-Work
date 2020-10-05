# **NODE CLASS**

import queue as q


class Node:
    def __init__(self, value, parent, g, huer, searchOption):
        self.parent = parent
        self.value = value
        if parent is not None:
            self.g = parent.g + g
        else:
            self.g = g
        self.h = huer
        if (searchOption == "A*"):
            self.f = self.g + self.h
            print(value, "A* :", self.f)
        else:
            self.f = self.h
            print(value, "Greedy :", self.f)

    def getValue(self):
        return self.value

    def __lt__(self, other):
        if self.f < other.f:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.f == other.f:
            return True
        else:
            return False

    def __ge__(self, other):
        in1 = self.f
        in2 = other.ft
        if in1 >= in2:
            return True
        else:
            return False


"""# **Get Neighbors**"""


def getNeighbors(location, grid):
    maxRow = len(grid)
    maxCol = len(grid[0])
    row = location[0]
    col = location[1]
    neighborList = [[row, col + 1],[row + 1, col], [row, col - 1], [row - 1, col],
                    ]  #Right,Down, Left, Up
    nlist = []
    #Out of Bounds Check
    for k in neighborList:  #Loop through Coordinate pairs in neighborlist
        if (k[0] < 0) or (k[0] >= maxRow) or (k[1] < 0) or (
                k[1] >= maxCol):  #if out of bounds remove it
            #print([k[0]],[k[1]],"Out Of Bounds")
            continue
        if (grid[k[0]][k[1]] == 0):  #if the grid value is 0 don't traverse
            continue
        else:
            nlist.append(k)
    return nlist


def gVal(value, grid):
    return grid[value[0]][value[1]]


#EXPAND NODE
""" Returns list of unexplored nodes """


def expandNode(node, grid, openList, closedList, goal, choice):

    newOpen = []
    neighbor = getNeighbors(node.getValue(), grid)

    for i in neighbor:
        cont = False
        node1 = Node(i, node, gVal(i, grid), heuristic(i, goal), choice)

        for n in list(openList.queue):
            if n.getValue() == i:
                cont = True
        for m in closedList:
            if m.getValue() == i:
                cont = True

        if cont is True:
            continue
        else:
            openList.put(node1)


#readGrid & outputGrid
""" Returns grid from a .txt file & outputs a grid path.txt """


# The grid values must be separated by spaces, e.g.
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
# Returns a 2D list of 1s and 0s
def readGrid(filename):
    #print('In readGrid')
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])

    f.close()
    #print 'Exiting readGrid'
    return grid


# Writes a 2D list of 1s and 0s with spaces in between each character
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
def outputGrid(grid, start, goal, path):
    #print('In outputGrid')
    filenameStr = 'path.txt'

    # Open filename
    f = open(filenameStr, 'w')

    # Mark the start and goal points
    grid[start[0]][start[1]] = 'S'
    grid[goal[0]][goal[1]] = 'G'

    # Mark intermediate points with *
    for i, p in enumerate(path):
        if i > 0 and i < len(path) - 1:
            grid[p[0]][p[1]] = '*'

    # Write the grid to a file
    for r, row in enumerate(grid):
        for c, col in enumerate(row):

            # Don't add a ' ' at the end of a line
            if c < len(row) - 1:
                f.write(str(col) + ' ')
            else:
                f.write(str(col))

        # Don't add a '\n' after the last line
        if r < len(grid) - 1:
            f.write("\n")

    # Close file
    f.close()
    #print('Exiting outputGrid')


#HEURISTIC
""" Returns the manhattan distance of 2 nodes """


def heuristic(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])


"""# **Informed Search**"""


def informedSearch(grid, start, goal, choice):

    current = Node(start, None, gVal(start, grid), heuristic(start, goal),
                   choice)
    cList = []
    oList = q.PriorityQueue()
    oList.put(current)

    while True:
        current = oList.get()
        print(grid[current.getValue()[0]][current.getValue()[1]])
        if current.value == goal:
            path = []
            setPath(current, path)
            print("GOAL REACHED")
            return path

        #Node has been searched so add it to the closedList
        cList.append(current)

        #clear nodes that are not beside the current
        oList.queue.clear()
        expandNode(current, grid, oList, cList, goal, choice)

        #if path runs into wall of 0s or noniterable poits back out to an iterable point
        if (oList.empty()):
            oList.put(current.parent)


def setPath(current, path):
    path.append(current.value)
    if current.parent is not None:
        setPath(current.parent, path)
    else:
        return path


"""#**MAIN FUNCTION**"""


def main(grid, startAndEnd, choice):
    path = informedSearch(grid, startAndEnd[0], startAndEnd[1], choice)
    print("PATH\n------------------------")
    print(path)
    outputGrid(grid, startAndEnd[0], startAndEnd[1],
               path)  #outputs to path.txt file


def start():
    grid = readGrid("GRID.txt")
    validS = False
    validG = False
    validChoice = False

    while validS is False:
        start = input("Enter Start State as Row,Col ie. 1,1 : ")
        start = start.replace(" ", "").split(",")
        start = [int(start[0]), int(start[1])]
        start

        if grid[start[0]][start[1]] != 0:
            validS = True
        else:
            print(start, ' contains a 0 on the grid and is nonreachable')

    while validG is False:
        goalS = input("Enter Goal State as Row,Col ie. 4,4 : ")
        goalS = goalS.replace(" ", "").split(",")
        goalS = [int(goalS[0]), int(goalS[1])]
        goalS

        if grid[goalS[0]][goalS[1]] != 0:
            validG = True
        else:
            print(goalS, 'contains a 0 on the grid and is nonreachable')

    choice = input(
        "Enter your algorithm choice as A* or Greedy \n\t(Case Se): ")
    choice = choice.replace(" ", "")
    startAndGoal = [start, goalS]
    main(grid, startAndGoal, choice)


start()
