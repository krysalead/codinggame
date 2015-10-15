import sys
import math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# ---------------------- VARS
player_count = int(raw_input())
my_id = int(raw_input())

# History format:
# X for empty Cell
# id for player for the lastest position
# [A, B, C, D] for trail of respective players
# example:
# . A . . C . . .
# . 0 . . 3 . . .
# . . B B + B B 1

X_MAX = 30
Y_MAX = 15

# GLOBAL FUNC
def debug(message):
    print >> sys.stderr, message



history = [["." for x in range(15)] for x in range(30)]
playerTrail = {0 : "A", 1: "B", 2: "C", 3: "D"}

def print_history():
    for i in range(15):
        for col in history:
            sys.stderr.write(str(col[i]))
            sys.stderr.write(" ")
        debug("")


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



players = {}
for n in range(player_count):
    players[n] = Player(Position(0,0), n, 0)
holes = {}

def cellAtPosition(x, y):
  return history[x % 30][y % 15]

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


def next_move():
    me = players[my_id]
    if cellAtPosition(me.position.x, me.position.y - 1) != ".":
        print "RIGHT"
    print 'UP'


# game loop
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
    next_move()
