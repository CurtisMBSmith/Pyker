#******************************************************************************
# PokerPlayer.py                                    Author: Curtis Smith
# Written in Python 3.2
#
# Represents a poker player.
#******************************************************************************

class PokerPlayer:
    ''' Creates a poker player with a name and money '''
    counter = 1
    
    def __init__(self, name, money = 0):
        ''' Initialize the player. Default values that can be passed are:
            Name: Anonymous
            Money: 200 '''
        self.name = name
        self.money = money
        self.id = self.counter
        counter += 1