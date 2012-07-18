#******************************************************************************
# Levels.py									Author: Curtis Smith
# Written in Python 3.2
#
# Represents the blind levels of a poker game.
#******************************************************************************

class Levels:
	''' Holds an array of BlindLevel objects and keeps track of the current
		level. Also contains a method that takes the time elapsed and 
		increments the level if sufficient time has elapsed. '''
		
	def __init__(self, levelTime, cashGame):
		''' Prepares the level array, takes the time of each level, sets the
			current level to 1, and takes a boolean value for whether or not
			this is a cash game. '''
		self.levels = []
		self.levelTime = levelTime
		self.currentLevel = 0
		self.cashGame = cashGame
		
	def setLevel(self, timeElapsed):
		''' Converts the time elapsed to minutes, then divides by the
			length of a blind level to see if it's time for a new level. '''
		if int((timeElapsed / 60) / self.levelTime) > self.currentLevel:
			currentLevel += 1
	
	def addLevel(self, newLevel):
		''' Appends the passed level to the level array. '''
		self.levels.append(newLevel)