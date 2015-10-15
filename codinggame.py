import sys
import math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# ---------------------- GAME VARS
player_count = int(raw_input())
my_id = int(raw_input())

X_MAX = 30
Y_MAX = 15

# GLOBAL FUNC
history = [["." for x in range(15)] for x in range(30)]
playerTrail = {0 : "A", 1: "B", 2: "C", 3: "D"}
# ----------------------  GLOBAL PRINT FUNC
def debug(message):
    print >> sys.stderr, message

def print_history():
    for i in range(15):
        for col in history:
            sys.stderr.write(str(col[i]))
            sys.stderr.write(" ")
        debug("")

# ---------------------- PLAYER CLASS
class Player(object):
    def __init__(self,position,id,missile):
        self.position = position
        self.id = id
        self.missile = missile

    def updatePosition(self,position):
        self.position=position

class Position(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y

# ---------------------- PLAYER DICTIONARY
players = {}
for n in range(player_count):
    players[n] = Player(Position(0,0), n, 0)
holes = {}

# ---------------------- HISTORY METHODS
def cellAtPosition(x, y):
  return history[x % X_MAX][y % Y_MAX]

def updateHistory(player_id, x, y):
  # 1 replace all heads with trails
  for xx, row in enumerate(history):
    for yy, cell in enumerate(row):
      #print >> sys.stderr, "CELL", cell
      if cell == player_id: # if cell is player_id head
        #print >> sys.stderr, cell, player_id
        history[xx][yy] = playerTrail[player_id] # update with player trail

  # 2 add new head
  history[x][y] = player_id

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
		if(cellAtPosition(pX,pY)=='.'):
			#check the second level
			for ppX,ppY in generateNeighbourPositions((pX,pY)):
				if(cellAtPosition(pX,pY)=='.'):
					#it is clean on 2 level we can go this direction
					if (pX,pY) not in positions:
						positions.append((pX % X_MAX, pY % Y_MAX))
	debug(positions)
	return positions

def directions(list):
	directions = []
	for tpl in list:
		if(tpl == (1,0)):
			directions.append('TOP')
		if(tpl == (0,1)):
			directions.append('RIGHT')
		if(tpl == (-1,0)):
			directions.append('BOTTOM')
		if(tpl == (0,-1)):
			directions.append('LEFT')
	return directions


# ---------------------- NEXT MOVE
def next_move():
    me = players[my_id]
    if cellAtPosition(me.position.x, me.position.y - 1) != ".":
        return "RIGHT"
    return 'UP'

# ----------------------
# ---------------------- GAME LOOP
# ----------------------
while 1:
    helper_bots = int(raw_input())
    for i in xrange(player_count):
        x, y = [int(j) for j in raw_input().split()]
        # save in history
        updateHistory(i, x, y)
        players[i].position.x = x
        players[i].position.y = y

    removal_count = int(raw_input())
    for i in xrange(removal_count):
        remove_x, remove_y = [int(j) for j in raw_input().split()]

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # print >> sys.stderr, "history: ", history
    print_history()
    print next_move()
