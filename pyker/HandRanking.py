#******************************************************************************
# HandRanking.py                                    Author: Curtis Smith
# Written in Python 3.2
#
# Contains methods that determine a hand's poker rank.
#******************************************************************************

import HandRanks

MINSIZE = 5 # The minimum size of a valid poker hand.

def rankHandHi(hand, board):
    ''' Gives the hand a "High" ranking based on the rules of poker.
        Returns a HandRank object. '''
    cards = list(hand + board)
    sortHand(cards)
    checks = [  checkStraightFlush, checkQuads, checkFullHouse, checkFlush,
                checkStraight, checkTrips, checkTwoPair, checkPair,
                checkHighCard]
    for n in checks:
        rank = n(cards)
        if rank:
            return rank

def rankHandLow(hand, board, straightsCount, eightOrBetter, acesLow): #NYI
    ''' Gives the hand a "Low" ranking based on the rules of poker and returns
        a HandRank object. If straights count, the lowest hand possible is
        75432, and if they don't count then the lowest hand is 5432A (if
        aces are low). The eightOrBetter parameter indicates whether or not
        a low must be no higher than an 8. '''
    pass

def checkStraightFlush(hand):
    ''' Checks to see if the passed cards make a straight and a flush.
        Returns a HandRank object if they do, and None if they do not. '''
    i = 1
    while i <= 4:
        temp = []
        for n in hand:
            if n.suit.suit == i:
                temp.append(n)
        if len(temp) >= 5:
            rank = checkStraight(temp)
            if rank:
                return HandRanks.StraightFlush(rank.cards)
        i += 1
    return None

def checkQuads(hand):
    ''' Checks to see if the passed cards make 4-of-a-kind. Returns a HandRank
        object if they do, and None if they don't. '''
    index = findMultiples(hand, 4)
    if index < 0:
        return None
    else:
        if len(hand) - index == 1:
            return HandRanks.Quads( [hand[index], hand[index-1], hand[index-2],
                                    hand[index-3], hand[index-4]])
        else:
            return HandRanks.Quads( [hand[index], hand[index-1], hand[index-2],
                                    hand[index-3], hand[-1]])

def checkFullHouse(hand):
    ''' Checks to see if the passed cards make a full house. Returns a HandRank
        object if they do, and None if they don't. '''
    cards = list(hand)
    index = findMultiples(cards, 3)
    if index < 0:
        return None
    else:
        temp = []
        temp.append(cards.pop(index))
        temp.append(cards.pop(index-1))
        temp.append(cards.pop(index-2))
        index = findMultiples(cards, 2)
        if index < 0:
            return None
        else:
            temp.append(cards.pop(index))
            temp.append(cards.pop(index-1))
            return HandRanks.FullHouse(temp)

def checkFlush(hand):
    ''' Checks each suit to see if there are 5 of the same suit, and if there
        are 5 of the same suit, this method returns a Flush type HandRank
        object with the 5 cards in order. If there are no combinations with
        5 of the same suit, this returns None. '''
    i = 1
    while i <= 4:
        temp = []
        for n in hand:
            if n.suit.suit == i:
                temp.append(n)
        if len(temp) >= 5:
            return HandRanks.Flush(temp[len(temp) - 5 : len(temp)])
        i += 1
    return None

def checkStraight(hand):
    ''' Checks to see if the passed cards make a straight. Returns a HandRank
        object if they do, and None if they do not. Expects that the array of
        cards has already been sorted by rank. '''
    tempHand = list(hand)
    removeDuplicates(tempHand)
    if not checkSize(tempHand):
        return None
    if tempHand[-1].rank.rank == 14:
        tempHand.insert(0, tempHand[-1])
    i = len(tempHand) - 5
    while i >= 0:
        if tempHand[i].rank.rank == 14:
            if tempHand[i + 1].rank.rank - (tempHand[i].rank.rank - 13) == 1:
                if tempHand[i + 2].rank.rank - (tempHand[i].rank.rank - 13) == 2:
                    if tempHand[i + 3].rank.rank - (tempHand[i].rank.rank - 13) == 3:
                        if tempHand[i + 4].rank.rank - (tempHand[i].rank.rank - 13) == 4:
                            return HandRanks.Straight(tempHand[i:i+5])
        else:
            if tempHand[i + 1].rank.rank - tempHand[i].rank.rank == 1:
                if tempHand[i + 2].rank.rank - tempHand[i].rank.rank == 2:
                    if tempHand[i + 3].rank.rank - tempHand[i].rank.rank == 3:
                        if tempHand[i + 4].rank.rank - tempHand[i].rank.rank == 4:
                            return HandRanks.Straight(tempHand[i:i+5])
        i -= 1
    return None

def checkTrips(hand):
    ''' Checks to see if the passed cards make 3-of-a-kind. Returns a HandRank
        object if they do, and None if they don't. '''
    index = findMultiples(hand, 3)
    if index < 0:
        return None
    else:
        if len(hand) - index == 1:
            return HandRanks.Trips( [hand[index], hand[index-1], hand[index-2],
                                    hand[index-3], hand[index-4]])
        elif len(hand) - index == 2:
            return HandRanks.Trips( [hand[index], hand[index-1], hand[index-2],
                                    hand[-1], hand[index-4]])
        else:
            return HandRanks.Trips( [hand[index], hand[index-1], hand[index-2],
                                    hand[-1], hand[-2]])

def checkTwoPair(hand):
    ''' Checks to see if the passed cards make two pair. Returns a HandRank
        object if they do, and None if they don't. '''
    cards = list(hand)
    index = findMultiples(cards, 2)
    if index < 0:
        return None
    else:
        temp = []
        temp.append(cards.pop(index))
        temp.append(cards.pop(index-1))
        index = findMultiples(cards, 2)
        if index < 0:
            return None
        else:
            temp.append(cards.pop(index))
            temp.append(cards.pop(index-1))
            temp.append(cards.pop(-1))
            return HandRanks.TwoPair(temp)

def checkPair(hand):
    ''' Checks to see if the passed cards make a pair. Returns a HandRank
        object if they do, and None if they don't. '''
    index = findMultiples(hand, 2)
    if index < 0:
        return None
    else:
        if len(hand) - index == 1:
            return HandRanks.Pair(  [hand[index], hand[index-1], hand[index-2],
                                    hand[index-3], hand[index-4]])
        elif len(hand) - index == 2:
            return HandRanks.Pair(  [hand[index], hand[index-1], hand[-1],
                                    hand[index-2], hand[index-3]])
        elif len(hand) - index == 3:
            return HandRanks.Pair(  [hand[index], hand[index-1], hand[-1],
                                    hand[-2], hand[index-2]])
        else:
            return HandRanks.Pair(  [hand[index], hand[index-1], hand[-1],
                                    hand[-2], hand[-3]])

def checkHighCard(hand):
    ''' Returns a high-card representation of the passed cards. Should be the
        last high-hand check called so that no better hands are missed. '''
    return HandRanks.HighCard(hand[len(hand)-5 : len(hand)])

def findMultiples(hand, targetMultiple):
    ''' Takes a sorted hand of cards and checks to see if there is a multiple
        of the target quantity. Returns the highest index where a multiple of
        the target quantity exists, or -1 if there isn't a multiple of the
        target quantity. '''
    i = len(hand) - 1
    while i > 0:
        count = 1
        while count <= i and hand[i].rank == hand[i-count].rank:
            count += 1
        if count >= targetMultiple:
            return i
        i = i - count
    return -1

def checkSize(hand):
    if len(hand) < MINSIZE:
        return False
    else:
        return True

def removeDuplicates(hand):
    ''' Removes any duplicate ranks from the hand to facilitate checking for
        straights. '''
    i = 0
    dups = []
    while i < len(hand) - 1:
        j = i + 1
        while j < len(hand):
            if hand[i].rank == hand[j].rank:
                if hand[j] not in dups:
                    dups.append(hand[j])
            j += 1
        i += 1
    if len(dups) > 0:
        i = len(dups) - 1
        while i >= 0:
            hand.remove(dups[i])
            i -= 1

def sortHand(hand, desc = False):
    ''' Uses Selection Sort on an array of card objects. Sorts in
        ascending order by default. '''
    i = 0
    while i < len(hand) - 1:
        j = i + 1
        min = i
        while j < len(hand):
            if desc:
                if hand[j] > hand[min]:
                    min = j
            else:
                if hand[j] < hand[min]:
                    min = j
            j += 1
        temp = hand[i]
        hand[i] = hand[min]
        hand[min] = temp
        i += 1

        