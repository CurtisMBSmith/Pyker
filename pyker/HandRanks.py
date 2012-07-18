#******************************************************************************
# HandRanking.py                                    Author: Curtis Smith
# Written in Python 3.2
#
# Contains classes that represent the rank of a poker hand.
#******************************************************************************

class HandRank:
    ''' Holds the rank of a hand that contains a rank description as well as
        the cards that make up the hand complete with methods to compare a
        hand rank to another of the same rank. '''
    def __init__(self, cards, rankValue, low = False):
        if len(cards) != 5:		# Ensure that there are exactly 5 cards in the hand
            raise ValueError("Hand must be of length 5.")
        self.cards = cards
        self.rankValue = rankValue
        self.low = low
    
    #--------------------------------------------------------------------------
    # Comparison operators - Compares two HandRank objects by their rankValue.
    #--------------------------------------------------------------------------
    
    def __lt__(self, other):
        if self.rankValue < other.rankValue:
            return True
        else:
            return False
    
    def __gt__(self, other):
        if self.rankValue > other.rankValue:
            return True
        else:
            return False
    
    def __eq__(self, other):
        if self.rankValue == other.rankValue:
            return True
        else:
            return False
    
    def __ne__(self, other):
        if self.rankValue != other.rankValue:
            return True
        else:
            return False

class StraightFlush(HandRank):
    ''' Represents a straight flush ranked hand inheriting from the HandRank
        class. Has methods to compare two straight flushes, as well as an
        appropriately defined __str__ method. '''
    def __init__(self, cards):
        ''' Initializes the rank to have a rank value of 9 (highest possible),
            description of "Straight Flush", and initializes the cards
            involved. '''
        HandRank.__init__(self, cards, 9, False)
    
    #--------------------------------------------------------------------------
    # Comparison operators - Enables use of the operators >, <, !=, == for
    # StraightFlush objects.
    #--------------------------------------------------------------------------
    def __lt__(self, other):
        if HandRank.__lt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[4] < other.cards[4]:
                return True
            else:
                return False
        else:
            return False
    
    def __gt__(self, other):
        if HandRank.__gt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[4] > other.cards[4]:
                return True
            else:
                return False
        else:
            return False
    
    def __eq__(self, other):
        if (HandRank.__eq__(self, other) and
            self.cards[4].rank == other.cards[4].rank):
            return True
        else:
            return False
    
    def __ne__(self, other):
        if (HandRank.__ne__(self, other) or
            self.cards[4].rank != other.cards[4].rank):
            return True
        else:
            return False
    
    #--------------------------------------------------------------------------
    # String operator - Returns a string describing the hand's rank in an
    # appropriate way.
    #--------------------------------------------------------------------------
    def __str__(self):
        if self.cards[0].rank.rank == 10:
            return "A Royal Flush."
        else:
            return  ("A Straight Flush " + str(self.cards[0].rank) + " to " +
                    str(self.cards[4].rank) + ".")

class Quads(HandRank):
    ''' Represents a four-of-a-kind ranked hand inheriting from the HandRank
        class. Has methods to compare two quad-ranked hands, as well as an
        appropriately defined __str__ method. '''
    def __init__(self, cards):
        ''' Initializes the rank to have a rank value of 8 (second highest),
            and initializes the cards involved. '''
        HandRank.__init__(self, cards, 8, False)
    
    #--------------------------------------------------------------------------
    # Comparison operators - Enables use of the operators >, <, !=, == for
    # Quad objects. For these comparisons to work, IT IS IMPERATIVE that the
    # cards object is of the format RRRRK (where R = cards of same rank, and
    # K is the kicker).
    #--------------------------------------------------------------------------
    def __lt__(self, other):
        if HandRank.__lt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[0] < other.cards[0]:
                return True
            elif self.cards[0].rank == other.cards[0].rank:
                if self.cards[4] < other.cards[4]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __gt__(self, other):
        if HandRank.__gt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[0] > other.cards[0]:
                return True
            elif self.cards[0].rank == other.cards[0].rank:
                if self.cards[4] > other.cards[4]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __eq__(self, other):
        if (HandRank.__eq__(self, other) and
            self.cards[0].rank == other.cards[0].rank and
            self.cards[4].rank == other.cards[4].rank):
            return True
        else:
            return False
    
    def __ne__(self, other):
        if (HandRank.__ne__(self, other) or
            self.cards[0].rank != other.cards[0].rank or
            self.cards[4].rank != other.cards[4].rank):
            return True
        else:
            return False
    
    #--------------------------------------------------------------------------
    # String operator - Returns a string describing the hand's rank in an
    # appropriate way.
    #--------------------------------------------------------------------------
    def __str__(self):
        return  ("Four of a Kind " + str(self.cards[0].rank) + "s, " + 
                str(self.cards[4].rank) + " kicker.")

class FullHouse(HandRank):
    ''' Represents a full house ranked hand inheriting from the HandRank
        class. Has methods to compare two full house hands, as well as an
        appropriately defined __str__ method. '''
    def __init__(self, cards):
        ''' Initializes the rank to have a rank value of 7 (third highest),
            and initializes the cards involved. '''
        HandRank.__init__(self, cards, 7, False)
    
    #--------------------------------------------------------------------------
    # Comparison operators - Enables use of the operators >, <, !=, == for
    # Full House objects. For these comparisons to work, IT IS IMPERATIVE that
    # the cards object is of the format TTTPP (where T = triple cards, and
    # P is the pair).
    #--------------------------------------------------------------------------
    def __lt__(self, other):
        if HandRank.__lt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[0] < other.cards[0]:
                return True
            elif self.cards[0].rank == other.cards[0].rank:
                if self.cards[4] < other.cards[4]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __gt__(self, other):
        if HandRank.__gt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[0] > other.cards[0]:
                return True
            elif self.cards[0].rank == other.cards[0].rank:
                if self.cards[4] > other.cards[4]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __eq__(self, other):
        if (HandRank.__eq__(self, other) and
            self.cards[0].rank == other.cards[0].rank and
            self.cards[4].rank == other.cards[4].rank):
            return True
        else:
            return False
    
    def __ne__(self, other):
        if (HandRank.__ne__(self, other) or
            self.cards[0].rank != other.cards[0].rank or
            self.cards[4].rank != other.cards[4].rank):
            return True
        else:
            return False
    
    #--------------------------------------------------------------------------
    # String operator - Returns a string describing the hand's rank in an
    # appropriate way.
    #--------------------------------------------------------------------------
    def __str__(self):
        return  ("Full House, " + str(self.cards[0].rank) + "s, full of " + 
                str(self.cards[4].rank) + "s.")

class Flush(HandRank):
    ''' Represents a flush ranked hand inheriting from the HandRank
        class. Has methods to compare two flushes, as well as an
        appropriately defined __str__ method. '''
    def __init__(self, cards):
        ''' Initializes the rank to have a rank value of 6, and initializes
            the cards involved. '''
        HandRank.__init__(self, cards, 6, False)
    
    #--------------------------------------------------------------------------
    # Comparison operators - Enables use of the operators >, <, !=, == for
    # Straight objects.
    #--------------------------------------------------------------------------
    def __lt__(self, other):
        if HandRank.__lt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[4] < other.cards[4]:
                return True
            elif self.cards[4].rank == other.cards[4].rank:
                if self.cards[3] < other.cards[3]:
                    return True
                elif self.cards[3].rank == other.cards[3].rank:
                    if self.cards[2] < other.cards[2]:
                        return True
                    elif self.cards[2].rank == other.cards[2].rank:
                        if self.cards[1] < other.cards[1]:
                            return True
                        elif self.cards[1].rank == other.cards[1].rank:
                            if self.cards[0] < other.cards[0]:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __gt__(self, other):
        if HandRank.__gt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[4] > other.cards[4]:
                return True
            elif self.cards[4].rank == other.cards[4].rank:
                if self.cards[3] > other.cards[3]:
                    return True
                elif self.cards[3].rank == other.cards[3].rank:
                    if self.cards[2] > other.cards[2]:
                        return True
                    elif self.cards[2].rank == other.cards[2].rank:
                        if self.cards[1] > other.cards[1]:
                            return True
                        elif self.cards[1].rank == other.cards[1].rank:
                            if self.cards[0] > other.cards[0]:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __eq__(self, other):
        if (HandRank.__eq__(self, other) and
            self.cards[4].rank == other.cards[4].rank and
            self.cards[3].rank == other.cards[3].rank and
            self.cards[2].rank == other.cards[2].rank and
            self.cards[1].rank == other.cards[1].rank and
            self.cards[0].rank == other.cards[0].rank):
            return True
        else:
            return False
    
    def __ne__(self, other):
        if (HandRank.__ne__(self, other) or
            self.cards[4].rank != other.cards[4].rank or
            self.cards[3].rank != other.cards[3].rank or
            self.cards[2].rank != other.cards[2].rank or
            self.cards[1].rank != other.cards[1].rank or
            self.cards[0].rank != other.cards[0].rank):
            return True
        else:
            return False
    
    #--------------------------------------------------------------------------
    # String operator - Returns a string describing the hand's rank in an
    # appropriate way.
    #--------------------------------------------------------------------------
    def __str__(self):
        return  ("A Flush, " + str(self.cards[4].rank) + " high, " + 
                str(self.cards[3].rank) + "+" + str(self.cards[2].rank) + "+" +
                str(self.cards[1].rank) + "+" + str(self.cards[0].rank) + " kickers.")

class Straight(HandRank):
    ''' Represents a straight ranked hand inheriting from the HandRank
        class. Has methods to compare two straights, as well as an
        appropriately defined __str__ method. '''
    def __init__(self, cards):
        ''' Initializes the rank to have a rank value of 5, and initializes
            the cards involved. '''
        HandRank.__init__(self, cards, 5, False)
    
    #--------------------------------------------------------------------------
    # Comparison operators - Enables use of the operators >, <, !=, == for
    # Straight objects.
    #--------------------------------------------------------------------------
    def __lt__(self, other):
        if HandRank.__lt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[4] < other.cards[4]:
                return True
            else:
                return False
        else:
            return False
    
    def __gt__(self, other):
        if HandRank.__gt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[4] > other.cards[4]:
                return True
            else:
                return False
        else:
            return False
    
    def __eq__(self, other):
        if (HandRank.__eq__(self, other) and
            self.cards[4].rank == other.cards[4].rank):
            return True
        else:
            return False
    
    def __ne__(self, other):
        if (HandRank.__ne__(self, other) or
            self.cards[4].rank != other.cards[4].rank):
            return True
        else:
            return False
    
    #--------------------------------------------------------------------------
    # String operator - Returns a string describing the hand's rank in an
    # appropriate way.
    #--------------------------------------------------------------------------
    def __str__(self):
        return  ("A Straight, " + str(self.cards[0].rank) + " to " + 
                str(self.cards[4].rank) + ".")

class Trips(HandRank):
    ''' Represents a three-of-a-kind ranked hand inheriting from the HandRank
        class. Has methods to compare two three-of-a-kinds, as well as an
        appropriately defined __str__ method. '''
    def __init__(self, cards):
        ''' Initializes the rank to have a rank value of 4 and initializes the
            cards involved. '''
        HandRank.__init__(self, cards, 4, False)
    
    #--------------------------------------------------------------------------
    # Comparison operators - Enables use of the operators >, <, !=, == for
    # Trips objects. For these comparisons to work, IT IS IMPERATIVE that the
    # cards object is of the format RRRJK (where R = cards of same rank, and
    # J, K are kickers s.t. J > K).
    #--------------------------------------------------------------------------
    def __lt__(self, other):
        if HandRank.__lt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[0] < other.cards[0]:
                return True
            elif self.cards[0].rank == other.cards[0].rank:
                if self.cards[3] < other.cards[3]:
                    return True
                elif self.cards[3].rank == other.cards[3].rank:
                    if self.cards[4] < other.cards[4]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __gt__(self, other):
        if HandRank.__gt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[0] > other.cards[0]:
                return True
            elif self.cards[0].rank == other.cards[0].rank:
                if self.cards[3] > other.cards[3]:
                    return True
                elif self.cards[3].rank == other.cards[3].rank:
                    if self.cards[4] > other.cards[4]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __eq__(self, other):
        if (HandRank.__eq__(self, other) and
            self.cards[0].rank == other.cards[0].rank and
            self.cards[3].rank == other.cards[3].rank and
            self.cards[4].rank == other.cards[4].rank):
            return True
        else:
            return False
    
    def __ne__(self, other):
        if (HandRank.__ne__(self, other) or
            self.cards[0].rank != other.cards[0].rank or
            self.cards[3].rank != other.cards[3].rank or
            self.cards[4].rank != other.cards[4].rank):
            return True
        else:
            return False
    
    #--------------------------------------------------------------------------
    # String operator - Returns a string describing the hand's rank in an
    # appropriate way.
    #--------------------------------------------------------------------------
    def __str__(self):
        return  ("Three of a Kind " + str(self.cards[0].rank) + "s, " + 
                str(self.cards[3].rank) + "+" + str(self.cards[4].rank) + 
                " kicker.")

class TwoPair(HandRank):
    ''' Represents a two-pair ranked hand inheriting from the HandRank
        class. Has methods to compare two two-pair hands, as well as an
        appropriately defined __str__ method. '''
    def __init__(self, cards):
        ''' Initializes the rank to have a rank value of 3 and initializes the
            cards involved. '''
        HandRank.__init__(self, cards, 3, False)
    
    #--------------------------------------------------------------------------
    # Comparison operators - Enables use of the operators >, <, !=, == for
    # TwoPair objects. For these comparisons to work, IT IS IMPERATIVE that the
    # cards object is of the format RRSSK (where R = higher pair, S = lower
    # pair, and K is the kicker.
    #--------------------------------------------------------------------------
    def __lt__(self, other):
        if HandRank.__lt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[0] < other.cards[0]:
                return True
            elif self.cards[0].rank == other.cards[0].rank:
                if self.cards[2] < other.cards[2]:
                    return True
                elif self.cards[2].rank == other.cards[2].rank:
                    if self.cards[4] < other.cards[4]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __gt__(self, other):
        if HandRank.__gt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[0] > other.cards[0]:
                return True
            elif self.cards[0].rank == other.cards[0].rank:
                if self.cards[2] > other.cards[2]:
                    return True
                elif self.cards[2].rank == other.cards[2].rank:
                    if self.cards[4] > other.cards[4]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __eq__(self, other):
        if (HandRank.__eq__(self, other) and
            self.cards[0].rank == other.cards[0].rank and
            self.cards[2].rank == other.cards[2].rank and
            self.cards[4].rank == other.cards[4].rank):
            return True
        else:
            return False
    
    def __ne__(self, other):
        if (HandRank.__ne__(self, other) or
            self.cards[0].rank != other.cards[0].rank or
            self.cards[2].rank != other.cards[2].rank or
            self.cards[4].rank != other.cards[4].rank):
            return True
        else:
            return False
    
    #--------------------------------------------------------------------------
    # String operator - Returns a string describing the hand's rank in an
    # appropriate way.
    #--------------------------------------------------------------------------
    def __str__(self):
        return  ("Two Pair " + str(self.cards[0].rank) + "s and " + 
                str(self.cards[2].rank) + "s, " + str(self.cards[4].rank) + 
                " kicker.")

class Pair(HandRank):
    ''' Represents a pair ranked hand inheriting from the HandRank
        class. Has methods to compare two pair hands, as well as an
        appropriately defined __str__ method. '''
    def __init__(self, cards):
        ''' Initializes the rank to have a rank value of 2 and initializes the
            cards involved. '''
        HandRank.__init__(self, cards, 2, False)
    
    #--------------------------------------------------------------------------
    # Comparison operators - Enables use of the operators >, <, !=, == for
    # Pair objects. For these comparisons to work, IT IS IMPERATIVE that the
    # cards object is of the format PPIJK (where P = cards of same rank, and
    # I, J, K are kickers s.t. I > J > K).
    #--------------------------------------------------------------------------
    def __lt__(self, other):
        if HandRank.__lt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[0] < other.cards[0]:
                return True
            elif self.cards[0].rank == other.cards[0].rank:
                if self.cards[2] < other.cards[2]:
                    return True
                elif self.cards[2].rank == other.cards[2].rank:
                    if self.cards[3] < other.cards[3]:
                        return True
                    elif self.cards[3].rank == other.cards[3].rank:
                        if self.cards[4] < other.cards[4]:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __gt__(self, other):
        if HandRank.__gt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[0] > other.cards[0]:
                return True
            elif self.cards[0].rank == other.cards[0].rank:
                if self.cards[2] > other.cards[2]:
                    return True
                elif self.cards[2].rank == other.cards[2].rank:
                    if self.cards[3] > other.cards[3]:
                        return True
                    elif self.cards[3].rank == other.cards[3].rank:
                        if self.cards[4] > other.cards[4]:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __eq__(self, other):
        if (HandRank.__eq__(self, other) and
            self.cards[0].rank == other.cards[0].rank and
            self.cards[2].rank == other.cards[2].rank and
            self.cards[3].rank == other.cards[3].rank and
            self.cards[4].rank == other.cards[4].rank):
            return True
        else:
            return False
    
    def __ne__(self, other):
        if (HandRank.__ne__(self, other) or
            self.cards[0].rank != other.cards[0].rank or
            self.cards[2].rank != other.cards[2].rank or
            self.cards[3].rank != other.cards[3].rank or
            self.cards[4].rank != other.cards[4].rank):
            return True
        else:
            return False
    
    #--------------------------------------------------------------------------
    # String operator - Returns a string describing the hand's rank in an
    # appropriate way.
    #--------------------------------------------------------------------------
    def __str__(self):
        return  ("A Pair of " + str(self.cards[0].rank) + "s, " + 
                str(self.cards[2].rank) + "+" + str(self.cards[3].rank) + 
                "+" + str(self.cards[4].rank) + " kicker.")

class HighCard(HandRank):
    ''' Represents a high-card ranked hand inheriting from the HandRank
        class. Has methods to compare two high-card hands, as well as an
        appropriately defined __str__ method. '''
    def __init__(self, cards):
        ''' Initializes the rank to have a rank value of 1, and initializes
            the cards involved. '''
        HandRank.__init__(self, cards, 1, False)
    
    #--------------------------------------------------------------------------
    # Comparison operators - Enables use of the operators >, <, !=, == for
    # HighCard objects.
    #--------------------------------------------------------------------------
    def __lt__(self, other):
        if HandRank.__lt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[4] < other.cards[4]:
                return True
            elif self.cards[4].rank == other.cards[4].rank:
                if self.cards[3] < other.cards[3]:
                    return True
                elif self.cards[3].rank == other.cards[3].rank:
                    if self.cards[2] < other.cards[2]:
                        return True
                    elif self.cards[2].rank == other.cards[2].rank:
                        if self.cards[1] < other.cards[1]:
                            return True
                        elif self.cards[1].rank == other.cards[1].rank:
                            if self.cards[0] < other.cards[0]:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __gt__(self, other):
        if HandRank.__gt__(self, other):
            return True
        elif HandRank.__eq__(self, other):
            if self.cards[4] > other.cards[4]:
                return True
            elif self.cards[4].rank == other.cards[4].rank:
                if self.cards[3] > other.cards[3]:
                    return True
                elif self.cards[3].rank == other.cards[3].rank:
                    if self.cards[2] > other.cards[2]:
                        return True
                    elif self.cards[2].rank == other.cards[2].rank:
                        if self.cards[1] > other.cards[1]:
                            return True
                        elif self.cards[1].rank == other.cards[1].rank:
                            if self.cards[0] > other.cards[0]:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __eq__(self, other):
        if (HandRank.__eq__(self, other) and
            self.cards[4].rank == other.cards[4].rank and
            self.cards[3].rank == other.cards[3].rank and
            self.cards[2].rank == other.cards[2].rank and
            self.cards[1].rank == other.cards[1].rank and
            self.cards[0].rank == other.cards[0].rank):
            return True
        else:
            return False
    
    def __ne__(self, other):
        if (HandRank.__ne__(self, other) or
            self.cards[4].rank != other.cards[4].rank or
            self.cards[3].rank != other.cards[3].rank or
            self.cards[2].rank != other.cards[2].rank or
            self.cards[1].rank != other.cards[1].rank or
            self.cards[0].rank != other.cards[0].rank):
            return True
        else:
            return False
    
    #--------------------------------------------------------------------------
    # String operator - Returns a string describing the hand's rank in an
    # appropriate way.
    #--------------------------------------------------------------------------
    def __str__(self):
        return  ("High card " + str(self.cards[4].rank) + ", " + 
                str(self.cards[3].rank) + "+" + str(self.cards[2].rank) + "+" +
                str(self.cards[1].rank) + "+" + str(self.cards[0].rank) + " kickers.")