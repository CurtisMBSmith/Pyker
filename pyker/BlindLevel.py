#******************************************************************************
# BlindLevel.py                                     Author: Curtis Smith
# Written in Python 3.2
#
# Represents a blind level in a poker game.
#******************************************************************************

class BlindLevel:
    ''' Represents a blind level. Contains 4 instance variables - one for 
        the big blind, small blind, ante, and bring in (if required). '''
    def __init__(self, bblind, sblind, ante, bringIn):
        self.bigBlind = bblind
        self.smallBlind = sblind
        self.ante = ante
        self.bringIn = bringIn