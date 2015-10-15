import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

player_count = int(raw_input())
my_id = int(raw_input())

#olivier

#class player:
#	position
#	id
#	missile


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

    # print >> sys.stderr, "history: ", history
    print "up"
