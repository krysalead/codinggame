import sys
import math
import random
from copy import copy, deepcopy
import pdb

c = 0
threshold = 5
X_MAX = 30
Y_MAX = 15

memoves = []

# GLOBAL FUNC
history = [["." for x in range(Y_MAX)] for x in range(X_MAX)]
playerTrail = {
    0 : {"HEAD" : "A", "TAIL" : "a"},
    1 : {"HEAD" : "B", "TAIL" : "b"},
    2 : {"HEAD" : "C", "TAIL" : "c"},
    3 : {"HEAD" : "D", "TAIL" : "d"}
}
OK_CELL = [".", "X"]

for i in range(10000):
    OK_CELL.append(str(i))

NOT_HEAD_CELL = [".", "X", "a", "b", "c", "d"]
# ----------------------  GLOBAL PRINT FUNC
def debug(message):
    print >> sys.stderr, message

def print_history(matrix):
    for i in range(Y_MAX):
        for col in matrix:
            letter = str(col[i])
            if len(letter) == 1:
                l = "  " + letter
            if len(letter) == 2:
                l = " " + letter
            if len(letter) == 3:
                l = letter

            sys.stderr.write(l)
            sys.stderr.write(" ")
        debug("")


def generateNeighbourPositions(loc):
    x, y = loc
    offsets = ((1, 0),(0, 1), (0, -1), (-1, 0))
    return [((x + dx) % X_MAX, (y + dy) % Y_MAX) for dx, dy in offsets]

def checkNeighbour(x,y, matrix=history):
    positions =[]
    for pX,pY in generateNeighbourPositions((x,y)):
        if(cellAtPosition(pX,pY, matrix) in OK_CELL):
            positions.append((pX, pY))
    return positions

def cellAtPosition(x, y, matrix = history):
  # print "cell at position", x % X_MAX, y % Y_MAX
  # print  matrix[x % X_MAX][y % Y_MAX]
  return matrix[x % X_MAX][y % Y_MAX]

def possible_moves(x, y, visited, matrix):
  nbs = checkNeighbour(x, y, matrix)
  return [x for x in nbs if x not in visited]


def possiblePaths(position, matrix):
  queue = [[(position)]]
  visited = []
  paths = []
  c = 0
  while queue != []:
    c = c + 1
    current = queue.pop() # current is an array of cords [(x, y), ...]

    if False:
        print current
        print ""
        print visited
        print
        print queue
        print "-"*80
        if c == 11:
            exit()


    nbs = possible_moves(current[-1][0], current[-1][1], visited, matrix)
    if len(nbs) == 0:
      # end of options, append to the paths
      paths.append(current)

    else:
      # move is the new (x, y)
      visited.append(current[-1])
      for move in nbs:
          # append new path to the queue
          queue.append(current + [move])

  # at this point we have all possible paths

  return paths




for i in range(8,20):
    for j in range(4,15):
        pass
        #history[i][j] = "@"

#history[8][1] = "@"
#history[8][2] = "@"
#history[8][3] = "@"

paths = sorted(possiblePaths((1,1), history), key=len ,reverse=True)


def draw_path(path, symbol="X"):
    print ""
    print path
    for x, y in path:
        #print x, y
        history[x][y] = symbol


def draw_path_c(path, symbol="X"):
    count = 1
    for x,y in path:

        history[x][y] = count
        count = count + 1


#for i, path in enumerate(paths):
#    draw_path(path, i)
# print len(paths)
# for i in range(451, 0):
#     draw_path_c(paths[0])
#     print
#print len(paths)
#print paths[0]

#print draw_path_c(paths[0])


def distances(matrix, points, count):
    new_neighbours = []
    for x,y  in points:
        neighbours = checkNeighbour(x,y, matrix)
        for cx, cy in neighbours:
            matrix[cx][cy] = count
        new_neighbours.extend(neighbours)

    #raw_input()
    #print_history()

    if len(new_neighbours) == 0:
        return count - 1, points
    else:
        return distances(matrix, new_neighbours, count + 1)

def checkNeighbourNumbers(x,y, visited, matrix=history):
    positions =[]
    for pX,pY in generateNeighbourPositions((x,y)):
        if(str(cellAtPosition(pX,pY, matrix)) in OK_CELL and (pX,pY) not in visited):
            positions.append((pX, pY))
    return positions

def possible_movesNumbers(x, y, visited, matrix):
  #pdb.set_trace()
  nbs = checkNeighbourNumbers(x, y, visited, matrix)
  if nbs == []:
    return nbs

  max_value = max([cellAtPosition(x, y, matrix) for x,y in nbs])
  max_nodes = [x for x in nbs if cellAtPosition(x[0], x[1], matrix) == max_value]

  return [x for x in max_nodes if x not in visited]

def possiblePathsNumbers(start_position, end_position, matrix):
    queue = [[(start_position)]]
    visited = []
    paths = []
    count = 0

    while queue != []:
        count = count + 1
        current = queue.pop() # current is an array of cords [(x, y), ...]

        nbs = possible_movesNumbers(current[-1][0], current[-1][1], current, matrix)
        
        print "Start node", start_position
        print "Iteration", count
        print "current location", current[-1][0], current[-1][1]
        print "neighbours", nbs
        print "queue", queue
        print ""
        print ""

        if (current[-1][0], current[-1][1]) == start:
          # found the start, append to the paths
          paths.append(current)
        elif len(nbs) == 0:
          continue
        else:
          # move is the new (x, y)
          visited.append(current[-1])
          for move in nbs:
              # append new path to the queue
              queue.append(current + [move])

        # at this point we have all possible paths
    return paths

start = (0,0)

matrx = deepcopy(history)
matrx[start[0]][start[1]] = 0

max_distance, max_nodes = distances(matrx, [start], 1)

print "max_distance", max_distance
print "max_nodes", max_nodes

max_paths = []
## VALID ^^^
print_history(matrx)

for node in max_nodes:
    ## returns all possible paths not the max ones
    max_paths.extend(possiblePathsNumbers(node, start, matrx))


#draw_path_c(sorted(max_paths, key=len, reverse=True)[0])

print("max paths")
print len(max_paths)
print(sorted(max_paths, key=len, reverse=True)[0])

# prints nubers on matrix
print_history(matrx)