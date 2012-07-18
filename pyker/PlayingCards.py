#******************************************************************************
# PlayingCards.py                               Author: Curtis Smith
# Written in Python 3.2
#
# Contains classes to represent a deck of playing cards.
#******************************************************************************

import random

class Deck:
    ''' Represents a deck (array) of card objects. '''
    def __init__(self, acesLow = False):
        ''' Initializes the deck of cards with card objects. '''
        self.deck = []
        self.discards = []
        lowAce = 0 # set to 1 if aces are low
        if acesLow:
            lowAce = 1
        i = 1 # suit value
        while i <= 4:
            j = 2 - lowAce # rank value
            while j <= 14 - lowAce:
                card = Card(j, i)
                self.deck.append(card)
                j += 1
            i += 1
    
    def shuffle(self):
        '''	Shuffles whatever is left in deck '''
        random.shuffle(self.deck)
    
    def reShuffle(self):
        ''' Shuffles the discards back into the deck '''
        self.deck += self.discards
        self.discards = []
        self.shuffle()
    
    def deal(self):
        ''' Reshuffles the deck if it's empty, otherwise
            it returns the first item from the deck '''
        if len(self.deck) == 0:
            self.reShuffle()
        try:
            return self.deck.pop(0)
        except IndexError:
            return False
            
    def reset(self):
        ''' Resets the deck and shuffles it '''
        self.deck += self.discards
        self.discards = []
        self.shuffle()
        
    def discard(self, card):
        ''' Takes an array of cards and adds them to the discard pile '''
        self.discards.append(card)

class Card:
    ''' Create a card object with the card's rank and suit. '''
    
    rank_descs = {  1:"A",  2:"2",  3:"3",  4:"4",  5:"5",  6:"6",  7:"7",
                    8:"8",  9:"9", 10:"T", 11:"J", 12:"Q", 13:"K", 14:"A"   }
    suit_descs = {  1:"c",  2:"s",  3:"d",  4:"h"   }   
    
    def __init__(self, rank, suit):
        ''' Creates a card object initializing the rank and suit objects
            with the values passed.'''
        self.rank = Rank(rank)
        self.suit = Suit(suit)
    
    #--------------------------------------------------------------------------
    # Comparison operators: Defines the special object comparison methods as
    # follows:
    # eq - Checks equivalency of suits.
    # ne - Defined only because eq is defined.
    # gt - True if this card's rank is greater than the compared card's rank
    # lt - True if this card's rank is less than the compared card's rank
    # ge/le - Not used because these comparisons are incomprehensible for cards
    # 
    # Rationale for eq/ne: Since we never need to check to see if two cards are
    # the exact same card, it makes sense to use these operators to check
    # equivalency of suits instead.
    #--------------------------------------------------------------------------
    
    def __eq__(self, other):
        if self.suit == other.suit:
            return True
        else:
            return False
    
    def __ne__(self, other):
        if self.suit != other.suit:
            return True
        else:
            return False
    
    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        else:
            return False
    
    def __lt__(self, other):
        if self.rank < other.rank:
            return True
        else:
            return False
            
    #--------------------------------------------------------------------------
    # Returns a long and short string representation of the card using the
    # rank/suit's str methods or the descs class variables for a short
    # description.
    #--------------------------------------------------------------------------
    def __str__(self):
        ''' Returns the short description representation of the card. '''
        return self.rank_descs[self.rank.rank] + self.suit_descs[self.suit.suit]
    
    def longDesc(self):
        ''' Returns the long description representation of the card. '''
        return str(self.rank) + " of " + str(self.suit)

class Rank:
    ''' Represents the rank of a playing card. Holds a number value
        from 1-14 (Corresponding to A23456789TJQKA respectively. '''
    
    descs = {   1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
                6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
                11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
    
    def __init__(self, rank):
        ''' Initializes the object's rank variable '''
        self.rank = rank
    
    def __lt__(self, other):
        if self.rank < other.rank:
            return True
        else:
            return False
    
    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        else:
            return False
    
    def __eq__(self, other):
        if self.rank == other.rank:
            return True
        else:
            return False
    
    def __ne__(self, other):
        if self.rank != other.rank:
            return True
        else:
            return False
    
    def __str__(self):
        return self.descs[self.rank]

class Suit:
    ''' Represents the suit of a playing card with the integer values
        1, 2, 3, 4 representing clubs, spades, diamonds, and hearts
        respectively. '''
    descs = {1: "Clubs", 2: "Spades", 3: "Diamonds", 4: "Hearts"}
    
    def __init__(self, suit):
        ''' Initializes the suit variable to the value passed. '''
        self.suit = suit
    
    def __eq__(self, other):
        if self.suit == other.suit:
            return True
        else:
            return False
    
    def __ne__(self, other):
        if self.suit != other.suit:
            return True
        else:
            return False
    
    def __str__(self):
        return self.descs[self.suit]