import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def debug(message):
    print >> sys.stderr, message

def print_history():
    for row in history:
        for col in row:
            sys.stderr.write(str(col))
            sys.stderr.write(" ")
        debug("")

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

class player(object):
	def __init__(self,position,id,missile):
		self.position = position
		self.id = id
		self.missile = missile
	def updatePosition(self,position):
		self.position=position
class position(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
 history = [["." for x in range(15)] for x in range(30)]
playerTrail = {0 : "A", 1: "B", 2: "C", 3: "D"}

def updateHistory(player, x, y):
  # 1 replace all heads with trails
  for xx, row in enumerate(history):
    for yy, cell in enumerate(row):
      #print >> sys.stderr, "CELL", cell
      if cell == player: # if cell is player head
        #print >> sys.stderr, cell, player
        history[xx][yy] = playerTrail[player] # update with player trail

  # 2 add new head
  history[x][y] = player


# game loop
while 1:
    helper_bots = int(raw_input())
    for i in xrange(player_count):
        col, row = [int(j) for j in raw_input().split()]
        # save in history
        updateHistory(i, row, col)

    removal_count = int(raw_input())
    for i in xrange(removal_count):
        remove_x, remove_y = [int(j) for j in raw_input().split()]

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # print >> sys.stderr, "history: ", history
    print_history()
    print "up"
