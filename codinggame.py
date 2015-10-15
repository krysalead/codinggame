import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

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

history = [["." for x in range(15)] for x in range(30)]
players = {0 : "A", 1: "B", 2: "C", 3: "D"}

def updateHistory(player, x, y):
  # 1 replace all heads with trails
  for XXX in history:
    XXX = [players[player] for xxx in XXX if xxx == player]
  # 2 add new head
  history[x][y] = player


# game loop
while 1:
    helper_bots = int(raw_input())
    for i in xrange(player_count):
        x, y = [int(j) for j in raw_input().split()]
        # save in history
        updateHistory(i, x, y)

    removal_count = int(raw_input())
    for i in xrange(removal_count):
        remove_x, remove_y = [int(j) for j in raw_input().split()]

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    print >> sys.stderr, "history: ", history
    print "up"