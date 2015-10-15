import sys
import math
import random
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# ---------------------- GAME VARS
player_count = int(raw_input())
my_id = int(raw_input())

X_MAX = 30
Y_MAX = 15

# GLOBAL FUNC
history = [["." for x in range(Y_MAX)] for x in range(X_MAX)]
playerTrail = {
    0 : {"HEAD" : "A", "TAIL" : "a"},
    1 : {"HEAD" : "B", "TAIL" : "b"},
    2 : {"HEAD" : "C", "TAIL" : "c"},
    3 : {"HEAD" : "D", "TAIL" : "d"}
}
OK_CELL = [".", "X"]

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
def cellAtPosition(x, y):
  return history[x % X_MAX][y % Y_MAX]

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
def generateNeighbourPositions(loc):
    x, y = loc
    offsets = ((0, 1), (1, 0), (0, -1), (-1, 0))
    return [(x + dx, y + dy) for dx, dy in offsets]

def transform(pos,dest_list):
    x, y = pos
    return [(dx-x, dy-y) for dx, dy in dest_list]

#start calculation
def checkNeighbour(x,y):
    #check direct ones
    positions =[]
    for pX,pY in generateNeighbourPositions((x,y)):
        #check the first level
        if(cellAtPosition(pX,pY) in OK_CELL):
            #check the second level
            for ppX,ppY in generateNeighbourPositions((pX,pY)):
                if(cellAtPosition(pX,pY) in OK_CELL):
                    #it is clean on 2 level we can go this direction
                    if (pX,pY) not in positions:
                        positions.append((pX % X_MAX, pY % Y_MAX))
    return positions

def directions(list):
  directions = []
  for tpl in list:
    if(tpl == (1,0)):
      directions.append('LEFT')
    if(tpl == (0,1)):
      directions.append('DOWN')
    if(tpl == (-1,0)):
      directions.append('RIGHT')
    if(tpl == (0,-1)):
      directions.append('UP')
  return directions

# ---------------------- NEXT MOVE
def next_move():
    me = players[my_id]

    if turn > 1 and me.missiles > 0 and random.randint(1, 10) > 8:
        return "DEPLOY"

    if cellAtPosition(me.position.x, me.position.y - 1) not in OK_CELL:
        return "RIGHT"
    return 'UP'

def longestPath(current_x, current_y):
  queue = [[(current_x, current_y)]]
  visited = []
  paths = []

  while queue != []:
    current = queue.pop(0) # current is an array of cords [(x, y), ...]
    if possible_moves(current[-1][0], current[-1][1]) == []:
      # end of options, append to the paths
      paths.append(current)
    else:
      # move is the new (x, y)
      for move in possible_moves(current[-1][0], current[-1][1]):
        if move not in visited:
          # append new path to the queue
          queue.append(current + [move])
          visited.append(move)
  # at this point we have all possible paths
  # return the longest
  return max(paths, key=len)

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

def distra():
    pass

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
    print next_move()
