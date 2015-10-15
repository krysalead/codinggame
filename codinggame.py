import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

player_count = int(raw_input())
my_id = int(raw_input())

#olivier

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

# game loop
while 1:
    helper_bots = int(raw_input())
    for i in xrange(player_count):
        x, y = [int(j) for j in raw_input().split()]
    removal_count = int(raw_input())
    for i in xrange(removal_count):
        remove_x, remove_y = [int(j) for j in raw_input().split()]

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    print "up"
