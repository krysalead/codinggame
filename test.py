import sys
import math
import random
from copy import copy, deepcopy

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

def possible_movesNumbers(x, y, visited, matrix):
  nbs = checkNeighbour(x, y, matrix)
  #max_value = [max(x) for cellAtPosition(y, matrix) in nbs]
  max_nodes = [x for x in nbs if cellAtPosition(x, matrix) == max_value]
  return [x for x in nbs if x not in visited and x in max_nodes]

def possiblePathsNumbers(position, matrix):

    nbs = checkNeighbour(position[0], position[1], matrix)
    print nbs
    exit()

    queue = [[(position)]]
    visited = []
    paths = []
    c = 0
    while queue != []:
        c = c + 1
        current = queue.pop() # current is an array of cords [(x, y), ...]

        nbs = possible_movesNumbers(current[-1][0], current[-1][1], current, matrix)
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

start = (1,1)
matrx = deepcopy(history)
matrx[start[0]][start[1]] = 0

max_distance, max_nodes = distances(matrx, [(1,1)], 1)

print "max_distance", max_distance
print "max_nodes", max_nodes

max_paths = []
for node in max_nodes:
    max_paths.extend(possiblePathsNumbers(node, matrx))



print_history(matrx)