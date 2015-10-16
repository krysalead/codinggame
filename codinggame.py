import sys
import math
import random
from copy import copy, deepcopy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# ---------------------- GAME VARS
player_count = int(raw_input())
my_id = int(raw_input())

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
            sys.stderr.write(str(col[i]))
            sys.stderr.write(" ")
        debug("")
# ---------------------- PLAYER CLASS
class Player(object):
    def __init__(self,position,id,missiles):
        self.position = position
        self.id = id
        self.missiles = missiles

    def updatePosition(self,position):
        self.position=position

class Position(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
# ---------------------- PLAYER DICTIONARY

holes_turn = []
holes_history = []

players = {}
for n in range(player_count):
    players[n] = Player(Position(0,0), n, 3)
# ---------------------- HISTORY METHODS
def cellAtPosition(x, y, matrix = history):
  return matrix[x % X_MAX][y % Y_MAX]

def updateHistory(player_id, x, y):
  # 1 replace all heads with trails
  for xx, row in enumerate(history):
    for yy, cell in enumerate(row):
      #print >> sys.stderr, "CELL", cell
      if cell == playerTrail[player_id]["HEAD"]: # if cell is player_id head
        #print >> sys.stderr, cell, player_id
        history[xx][yy] = playerTrail[player_id]["TAIL"] # update with player trail

  # 2 add new head
  history[x][y] = playerTrail[player_id]["HEAD"]

# ---------------------- Player Methods
def updatePlayerPositionAndMissiles(i, x, y, helper_bots):
    players[i].position.x = x
    players[i].position.y = y
    if i == my_id:
        players[i].missiles = helper_bots

# ---------------------- Neighbour

# def transform(pos,dest_list):
#     return [vector(pos, x) for x in dest_list]

def vector(p1, p2):
    vx = p2[0] - p1[0]
    vy = p2[1] - p1[1]

    vx = vx if vx < 2 else -1
    vx = vx if vx > -2 else 1

    vy = vy if vy < 2 else -1
    vy = vy if vy > -2 else 1

    return (vx, vy)

def generateNeighbourPositions(loc):
    x, y = loc
    offsets = ((0, 1), (1, 0), (0, -1), (-1, 0))
    return [((x + dx) % X_MAX, (y + dy) % Y_MAX) for dx, dy in offsets]

#start calculation
def checkNeighbour(x,y, matrix=history):

    #check direct ones
    positions =[]
    for pX,pY in generateNeighbourPositions((x,y)):
        #check the first level
        if(cellAtPosition(pX,pY, matrix) in OK_CELL):
            positions.append((pX, pY))
            # #check the second level
            #for ppX,ppY in generateNeighbourPositions((pX,pY)):
            #    if(cellAtPosition(pX,pY) in OK_CELL):
            #         #it is clean on 2 level we can go this direction
            #        if (pX,pY) not in positions:
            #            positions.append((pX, pY))
    return positions

def moveFromCoordinates((x,y)):
    me = players[my_id]
    v = vector((me.position.x, me.position.y), (x,y))
    if(v == (1,0)):
      return 'RIGHT'
    if(v == (0,1)):
      return 'DOWN'
    if(v == (-1,0)):
      return 'LEFT'
    if(v == (0,-1)):
      return 'UP'


def isNextMoveValid(current, next):
    #return True
    valid_cells = generateNeighbourPositions(next)
    heads = ["A","B","C","D"]
    heads.remove(playerTrail[my_id]["HEAD"])
    debug(heads)
    for x,y in valid_cells:
        if cellAtPosition(x,y) in heads:
            return False
    return True

def future():
    me = players[my_id]

    if (len(memoves)) == 0 or me.missiles == 0:
        return history

    future_map = deepcopy(history)

    mex = me.position.x
    mey = me.position.y
    last_move = memoves[-1]


    stuff_ahead = []
    if last_move == "UP":
        stuff_ahead = [(mex, (mey - i)% Y_MAX)  for i in range(threshold)]
    if last_move == "DOWN":
        stuff_ahead = [(mex, (mey + i)% Y_MAX)  for i in range(threshold)]
    if last_move == "LEFT":
        stuff_ahead = [((mex - i ) % X_MAX, mey )  for i in range(threshold)]
    if last_move == "RIGHT":
        stuff_ahead = [((mex + i ) % X_MAX, mey )  for i in range(threshold)]

    debug(stuff_ahead)

    count_missiles = me.missiles
    for cell in stuff_ahead:
        trail = ["a","b","c","d"]
        if cellAtPosition(cell[0], cell[1]) in trail:
            if count_missiles > 0:
                future_map[cell[0]][cell[1]] = "."
                count_missiles = count_missiles - 1

    return future_map



# ---------------------- NEXT MOVE
def next_move():

    me = players[my_id]

    current_pos = (me.position.x, me.position.y)


    future_map = future()
    future_paths = [[]]
    #future_paths = possiblePaths(current_pos, future_map)
    #future_paths = sorted(future_paths, key=len, reverse=True)

    paths = possiblePaths(current_pos, history)
    paths = sorted(paths, key=len, reverse=True)

    #for path in paths:
    #    sys.stderr.write(" " + str(len(path)))

    debug("")
    debug(len(paths[0]))
    debug(len(future_paths[0]))

    chosenOne = future_paths if len(future_paths[0]) > len(paths[0]) + threshold else paths

    forceShoot = True if len(future_paths[0]) > len(paths[0]) + threshold else False
    if forceShoot:
        return "DEPLOY"

    for path in chosenOne:
        if len(path) > 1:
            next_cell = path[1]
            if isNextMoveValid(current_pos, next_cell):
                return moveFromCoordinates(next_cell)

    for path in chosenOne:
        if len(path) > 1:
            x,y = path[0]
            moves = checkNeighbour(x,y)
            if len(moves) == 1:
                return moveFromCoordinates(moves[0])

    return "DEPLOY"

def possible_moves(x, y, visited, matrix):
  nbs = checkNeighbour(x, y, matrix)
  return [x for x in nbs if x not in visited]

def possiblePaths(position, matrix):
  queue = [[(position)]]
  visited = []
  paths = []

  while queue != []:
    current = queue.pop(0) # current is an array of cords [(x, y), ...]
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

# --------------------- Missiles
def adjust_missiles_count():
    pass

def print_players():
    for id in players:
        debug("")
        debug("Player ID: " + str(players[id].id))
        if players[id].position.x != -1:
            debug("Player Missiles: " + str(players[id].missiles))
            debug("Player Coordinates: " + str(players[id].position.x) + " - " + str(players[id].position.y))
        else:
            debug("Player Destroyed")
        debug("")


# ----------------------
# ---------------------- GAME LOOP
# ----------------------
turn = 0

while 1:



    helper_bots = int(raw_input())
    turn = turn + 1
    debug("# ----- TURN " + str(turn) + "------------------ #")
    debug("Player ID:" + str(my_id))
    debug("Helper Bots:" + str(helper_bots))

    debug("")

    for i in xrange(player_count):
        x, y = [int(j) for j in raw_input().split()]
        # save in history
        updateHistory(i, x, y)
        updatePlayerPositionAndMissiles(i, x, y, helper_bots)

    removal_count = int(raw_input())
    debug("-- Removal Count:" + str(removal_count))

    holes_turn = []
    for i in xrange(removal_count):
        remove_x, remove_y = [int(j) for j in raw_input().split()]
        if (players[my_id].position.x != remove_x and players[my_id].position.y != remove_y):
            history[remove_x][remove_y] = "X"
            holes_turn.append((remove_x, remove_y))
        holes_history.append((remove_x, remove_y))
    debug("-- Turn Removal Coordinates:")
    debug(holes_turn)
    debug("-- History of Removal Coordinates:")
    debug(holes_history)

    # Printing Players status
    print_players()


    debug("# ----------------------- #")
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # print >> sys.stderr, "history: ", history
    print_history()
    next = next_move()
    memoves.append(next)
    print next

