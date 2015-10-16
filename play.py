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
NOT_HEAD_CELL = [".", "X", "a", "b", "c", "d"]
# ----------------------  GLOBAL PRINT FUNC
def debug(message):
    print >> sys.stderr, message

def print_history():
    for i in range(Y_MAX):
        for col in history:
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
    offsets = ((0, 1), (1, 0), (0, -1), (-1, 0))
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




#history[0][0] = "A"
paths = sorted(possiblePaths((1,1), history), key=len ,reverse=True)


def draw_path(path, symbol="X"):

    for x,y in path:

        history[x][y] = symbol


def draw_path_c(path, symbol="X"):
    count = 1
    for x,y in path:

        history[x][y] = count
        count = count + 1


#for i, path in enumerate(paths):
#    draw_path(path, i)

draw_path_c(paths[0])

print_history()