#******************************************************************************
# PokerTable.py                                     Author: Curtis Smith
# Written in Python 3.2
#
# Represents a player's hand of playing cards.
#******************************************************************************

import PlayingCards

class Table:
    ''' Represents a poker table with seats, a deck of cards, and a poker game.
        '''
    def __init__(self, totalSeats, tableNum = 1, cashTable = False):
        ''' Initialize variables specific to a poker table:
            seats: (Seat[]) initialized with totalSeats Seat objects.
            deck: (Deck) deck object.
            board: (Card[]) holds any community cards that the table has.
            button: (int) indicates the index of the dealer button.
            tableNum: (int) holds the table id number
            pot: (double) holds the number of chips in the pot currently
            cashTable: (bool) describes whether or not this is a cash table '''
        i = 0
        self.seats = []
        while i < totalSeats:
            seats.append(Seat(i + 1))
            i += 1
        self.deck = PlayingCards.Deck()
        self.board = []
        self.button = 0
        self.tableNum = tableNum
        self.pot = 0.0
        self.cashTable = cashTable
    
    def playersInHand(self):
        ''' Returns a count of the number of players that haven't yet folded.
            '''
        count = 0
        for seat in self.seats:
            if not seat.folded:
                count += 1
        return count
    
    def moveButton(self):
        ''' Moves the button a position to the right. If the game is a cash
            game, the button skips seats that are sitting out. '''
        if self.cashTable:
            
    def resetState(self):
    

class Seat:
    ''' Represents a seat at the poker table. Has a player if occupied (None if
        empty). Each seat has a hand as well. Has methods to be called when it
        is the seat's turn to act. '''
    def __init__(self, seatNum):
        ''' Variables describing the state of the seat:
            seatNumber : (int) The seat's number at the table.
            player : (Player/None) Holds the player currently in the seat.
            hand : (Hand) Holds the hand object corresponding to the seat.
            sittingOut : (bool) True if the player is sitting out.
            folded : (bool) True if the player's hand has been folded.
            chips : (double) Represents the chips at this seat.
            wagered : (double) Represents the chips wagered in the current hand
        '''
        self.seatNumber = seatNum
        self.player = None
        self.hand = Hand()
        self.sittingOut = False
        self.folded = True
        self.chips = 0
        self.wagered = 0
    
    def addPlayer(self, player, chips):
        ''' Adds a player with a given amount of chips to the seat. '''
        self.player = player
        self.chips = chips
        self.folded = True
    
    def resetState(self, deck):
        self.hand.reset(deck)
        self.folded = False
    
    

class Hand:
    ''' Represents a hand. Holds cards, and has methods to discard cards from
        the hand as well as a method to reset the hand to an empty array. '''
    def __init__(self):
        self.cards = []
        self.hiHandRank = None
        self.lowHandRank = None
    
    def discard(self, locations, deck):
        ''' Takes a str describing the locations of the cards that the player
            wants to discard from the hand (0 if they don't want to discard).
            ie. 135 -> discards card 1, 3, and 5.
            It then iterates through the values	discarding the card at that
            location. '''
        if int(locations) > 0:
            discards = []
            i = len(locations) - 1
            while i >= 0:
                discards.append(self.cards.pop(int(locations[i]) - 1))
            deck.discard(discards)
    
    def reset(self, deck):
        ''' Discards the hand back into the deck. Resets the handRank
            variables.'''
        while len(self.cards) > 0:
            deck.discard(self.cards.pop(0))
        self.hiHandRank = None
        self.lowHandRank = None
    
    #--------------------------------------------------------------------------
    # Comparison methods for comparing two hands.
    #--------------------------------------------------------------------------
    def __lt__(self, other):
        if self.hiHandRank < other.hiHandRank:
            return True
        else:
            return False
    
    def __gt__(self, other):
        if self.hiHandRank > other.hiHandRank:
            return True
        else:
            return False
    
    def __eq__(self, other):
        if self.hiHandRank == other.hiHandRank:
            return True
        else:
            return False
    
    def __ne__(self, other):
        if self.hiHandRank != other.hiHandRank:
            return True
        else:
            return False
    
    def __str__(self):
        result = "\tHand ["
        i = 0
        while i < len(self.cards):
            result += str(self.cards[i])
            if i != len(self.cards) - 1:
                result += ", "
            i += 1
        result += "]\t Hand rank: " + str(self.hiHandRank)
        return result

