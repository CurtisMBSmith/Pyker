#******************************************************************************
# HandRankingTest.py                                    Author: Curtis Smith
# Written in Python 3.2
#
# Unit test class for HandRanking.
#******************************************************************************

import HandRanking
import Pyker.HandRanks
import Pyker.PlayingCards
import unittest

class KnownValues(unittest.TestCase):
    deck = PlayingCards.Deck() # Set up an unshuffled deck.
    
    #--------------------------------------------------------------------------
    # Unshuffled deck index table:
    #    0   1   2   3   4   5   6   7   8   9   10  11  12
    # 0  2c  3c  4c  5c  6c  7c  8c  9c  Tc  Jc  Qc  Kc  Ac
    # 1  2s  3s  4s  5s  6s  7s  8s  9s  Ts  Js  Qs  Ks  As
    # 2  2d  3d  4d  5d  6d  7d  8d  9d  Td  Jd  Qd  Kd  Ad
    # 3  2h  3h  4h  5h  6h  7h  8h  9h  Th  Jh  Qh  Kh  Ah
    # Multiply the value to the left of the row by 13 and add the column header
    # value to get the index of a given card.
    #--------------------------------------------------------------------------
    
    def test_straight_flush(self):
        ''' rankHandHi should return a StraightFlush object with appropriate input.'''
        # Test royal flush case, two intermediate cases, but not the ace-low case.
        known_values = ((   [self.deck.deck[8], self.deck.deck[9]], # Royal Flush case, full participation.
                            [self.deck.deck[10], self.deck.deck[11], self.deck.deck[12], self.deck.deck[25], self.deck.deck[38]],
                            HandRanks.StraightFlush([self.deck.deck[8], self.deck.deck[9], self.deck.deck[10], self.deck.deck[11], self.deck.deck[12]])),
                        (   [self.deck.deck[6], self.deck.deck[47]], # Hand does not participate in the straight flush.
                            [self.deck.deck[27], self.deck.deck[30], self.deck.deck[31], self.deck.deck[29], self.deck.deck[28]],
                            HandRanks.StraightFlush([self.deck.deck[27], self.deck.deck[28], self.deck.deck[29], self.deck.deck[30], self.deck.deck[31]])),
                        (   [self.deck.deck[49], self.deck.deck[25]], # One card from hand participates in the straight flush.
                            [self.deck.deck[47], self.deck.deck[48], self.deck.deck[45], self.deck.deck[32], self.deck.deck[46]],
                            HandRanks.StraightFlush([self.deck.deck[45], self.deck.deck[46], self.deck.deck[47], self.deck.deck[48], self.deck.deck[49]])) )
        for hand, board, ranking in known_values:
            result = HandRanking.rankHandHi(hand, board)
            self.assertIsInstance(result, HandRanks.StraightFlush) # Verify that this is a straight flush that was returned.
            self.assertEqual(result, ranking)
    
    def test_ace_low_straight_flush(self):
        ''' rankHandHi should return a StraightFlush object if Ace to 5 all of one suit. '''
        known_values = ((   [self.deck.deck[12], self.deck.deck[3]], # Hand fully participates in the straight flush.
                            [self.deck.deck[0], self.deck.deck[45], self.deck.deck[27], self.deck.deck[1], self.deck.deck[2]],
                            HandRanks.StraightFlush([self.deck.deck[12], self.deck.deck[0], self.deck.deck[1], self.deck.deck[2], self.deck.deck[3]])),
                        (   [self.deck.deck[12], self.deck.deck[3]], # Hand does not participate in the straight flush.
                            [self.deck.deck[25], self.deck.deck[13], self.deck.deck[15], self.deck.deck[16], self.deck.deck[14]],
                            HandRanks.StraightFlush([self.deck.deck[25], self.deck.deck[13], self.deck.deck[14], self.deck.deck[15], self.deck.deck[16]])),
                        (   [self.deck.deck[38], self.deck.deck[18]], # One card from hand participates in the straight flush.
                            [self.deck.deck[26], self.deck.deck[28], self.deck.deck[27], self.deck.deck[51], self.deck.deck[29]],
                            HandRanks.StraightFlush([self.deck.deck[38], self.deck.deck[26], self.deck.deck[27], self.deck.deck[28], self.deck.deck[29]])) )
        for hand, board, ranking in known_values:
            result = HandRanking.rankHandHi(hand, board)
            self.assertIsInstance(result, HandRanks.StraightFlush) # Verify that this is a straight flush that was returned.
            self.assertEqual(result, ranking)
    
    def test_quads(self):
        ''' rankHandHi should return a Quads object with appropriate input.'''
        # Test three possible combinations of cases.
        known_values = ((   [self.deck.deck[12], self.deck.deck[38]], # Full participation of hand in result case.
                            [self.deck.deck[10], self.deck.deck[26], self.deck.deck[51], self.deck.deck[25], self.deck.deck[50]],
                            HandRanks.Quads([self.deck.deck[12], self.deck.deck[25], self.deck.deck[38], self.deck.deck[51], self.deck.deck[50]])),
                        (   [self.deck.deck[6], self.deck.deck[47]], # Case where hand does not participate.
                            [self.deck.deck[7], self.deck.deck[20], self.deck.deck[33], self.deck.deck[11], self.deck.deck[46]],
                            HandRanks.Quads([self.deck.deck[7], self.deck.deck[29], self.deck.deck[33], self.deck.deck[46], self.deck.deck[11]])),
                        (   [self.deck.deck[4], self.deck.deck[26]], # One card from hand participates.
                            [self.deck.deck[17], self.deck.deck[30], self.deck.deck[22], self.deck.deck[25], self.deck.deck[43]],
                            HandRanks.Quads([self.deck.deck[4], self.deck.deck[17], self.deck.deck[30], self.deck.deck[43], self.deck.deck[25]])) )
        for hand, board, ranking in known_values:
            result = HandRanking.rankHandHi(hand, board)
            self.assertIsInstance(result, HandRanks.Quads) # Verify that the correct object was returned.
            self.assertEqual(result, ranking)
    
    def test_full_house(self):
        ''' rankHandHi should return a FullHouse object with appropriate input.'''
        # Test three possible combinations of cases, plus a double-trip scenario.
        known_values = ((   [self.deck.deck[6], self.deck.deck[19]], # Full participation of hand in result case.
                            [self.deck.deck[10], self.deck.deck[32], self.deck.deck[51], self.deck.deck[23], self.deck.deck[50]],
                            HandRanks.FullHouse([self.deck.deck[6], self.deck.deck[19], self.deck.deck[32], self.deck.deck[10], self.deck.deck[23]])),
                        (   [self.deck.deck[6], self.deck.deck[47]], # Case where hand does not participate.
                            [self.deck.deck[25], self.deck.deck[51], self.deck.deck[12], self.deck.deck[50], self.deck.deck[24]],
                            HandRanks.FullHouse([self.deck.deck[12], self.deck.deck[25], self.deck.deck[51], self.deck.deck[24], self.deck.deck[50]])),
                        (   [self.deck.deck[4], self.deck.deck[26]], # One card from hand participates.
                            [self.deck.deck[17], self.deck.deck[30], self.deck.deck[50], self.deck.deck[24], self.deck.deck[5]],
                            HandRanks.FullHouse([self.deck.deck[4], self.deck.deck[17], self.deck.deck[30], self.deck.deck[24], self.deck.deck[50]])),
                        (   [self.deck.deck[2], self.deck.deck[15]], # Test the double triple case.
                            [self.deck.deck[28], self.deck.deck[51], self.deck.deck[25], self.deck.deck[12], self.deck.deck[24]],
                            HandRanks.FullHouse([self.deck.deck[12], self.deck.deck[25], self.deck.deck[51], self.deck.deck[2], self.deck.deck[15]])) )
        for hand, board, ranking in known_values:
            result = HandRanking.rankHandHi(hand, board)
            self.assertIsInstance(result, HandRanks.FullHouse) # Verify that the correct object was returned.
            self.assertEqual(result, ranking)
    
    def test_flush(self):
        ''' rankHandHi should return a Flush object with appropriate input.'''
        # Test three possible combinations of cases, plus a 6-card, and 7-card flush scenario.
        known_values = ((   [self.deck.deck[2], self.deck.deck[5]], # Full participation of hand in result case.
                            [self.deck.deck[6], self.deck.deck[32], self.deck.deck[51], self.deck.deck[8], self.deck.deck[12]],
                            HandRanks.Flush([self.deck.deck[2], self.deck.deck[5], self.deck.deck[6], self.deck.deck[8], self.deck.deck[12]])),
                        (   [self.deck.deck[3], self.deck.deck[47]], # Case where hand does not participate.
                            [self.deck.deck[18], self.deck.deck[17], self.deck.deck[20], self.deck.deck[21], self.deck.deck[13]],
                            HandRanks.Flush([self.deck.deck[13], self.deck.deck[17], self.deck.deck[18], self.deck.deck[20], self.deck.deck[21]])),
                        (   [self.deck.deck[4], self.deck.deck[32]], # One card from hand participates.
                            [self.deck.deck[33], self.deck.deck[38], self.deck.deck[29], self.deck.deck[27], self.deck.deck[5]],
                            HandRanks.Flush([self.deck.deck[27], self.deck.deck[29], self.deck.deck[32], self.deck.deck[33], self.deck.deck[38]])),
                        (   [self.deck.deck[8], self.deck.deck[15]], # Test the 6-card flush case.
                            [self.deck.deck[4], self.deck.deck[5], self.deck.deck[2], self.deck.deck[10], self.deck.deck[11]],
                            HandRanks.Flush([self.deck.deck[4], self.deck.deck[5], self.deck.deck[8], self.deck.deck[10], self.deck.deck[11]])),
                        (   [self.deck.deck[39], self.deck.deck[50]], # Test the 7-card flush case.
                            [self.deck.deck[42], self.deck.deck[44], self.deck.deck[48], self.deck.deck[51], self.deck.deck[43]],
                            HandRanks.Flush([self.deck.deck[43], self.deck.deck[44], self.deck.deck[48], self.deck.deck[50], self.deck.deck[51]])))
        for hand, board, ranking in known_values:
            result = HandRanking.rankHandHi(hand, board)
            self.assertIsInstance(result, HandRanks.Flush) # Verify that the correct object was returned.
            self.assertEqual(result, ranking)
    
    def test_straight(self):
        ''' rankHandHi should return a Straight object with appropriate input.'''
        # Test three possible combinations of cases of non-ace-low straights.
        known_values = ((   [self.deck.deck[10], self.deck.deck[24]], # Full participation of hand in result case.
                            [self.deck.deck[9], self.deck.deck[51], self.deck.deck[8], self.deck.deck[13], self.deck.deck[44]],
                            HandRanks.Straight([self.deck.deck[8], self.deck.deck[9], self.deck.deck[10], self.deck.deck[24], self.deck.deck[51]])),
                        (   [self.deck.deck[51], self.deck.deck[24]], # Case where hand does not participate.
                            [self.deck.deck[26], self.deck.deck[2], self.deck.deck[27], self.deck.deck[42], self.deck.deck[43]],
                            HandRanks.Straight([self.deck.deck[26], self.deck.deck[27], self.deck.deck[2], self.deck.deck[42], self.deck.deck[43]])),
                        (   [self.deck.deck[4], self.deck.deck[25]], # One card from hand participates.
                            [self.deck.deck[44], self.deck.deck[32], self.deck.deck[7], self.deck.deck[34], self.deck.deck[23]],
                            HandRanks.Straight([self.deck.deck[4], self.deck.deck[44], self.deck.deck[32], self.deck.deck[7], self.deck.deck[34]])) )
        for hand, board, ranking in known_values:
            result = HandRanking.rankHandHi(hand, board)
            self.assertIsInstance(result, HandRanks.Straight) # Verify that the correct object was returned.
            self.assertEqual(result, ranking)
    
    def test_ace_low_straight(self):
        ''' rankHandHi should return an ace-low Straight object with appropriate input.'''
        # Test three possible combinations of cases of non-ace-low straights.
        known_values = ((   [self.deck.deck[51], self.deck.deck[28]], # Full participation of hand in result case.
                            [self.deck.deck[0], self.deck.deck[1], self.deck.deck[3], self.deck.deck[15], self.deck.deck[44]],
                            HandRanks.Straight([self.deck.deck[51], self.deck.deck[0], self.deck.deck[1], self.deck.deck[28], self.deck.deck[3]])),
                        (   [self.deck.deck[46], self.deck.deck[48]], # Case where hand does not participate.
                            [self.deck.deck[26], self.deck.deck[2], self.deck.deck[27], self.deck.deck[25], self.deck.deck[42]],
                            HandRanks.Straight([self.deck.deck[25], self.deck.deck[26], self.deck.deck[2], self.deck.deck[27], self.deck.deck[42]])),
                        (   [self.deck.deck[3], self.deck.deck[33]], # One card from hand participates.
                            [self.deck.deck[0], self.deck.deck[51], self.deck.deck[40], self.deck.deck[28], self.deck.deck[23]],
                            HandRanks.Straight([self.deck.deck[51], self.deck.deck[0], self.deck.deck[40], self.deck.deck[28], self.deck.deck[3]])) )
        for hand, board, ranking in known_values:
            result = HandRanking.rankHandHi(hand, board)
            self.assertIsInstance(result, HandRanks.Straight) # Verify that the correct object was returned.
            self.assertEqual(result, ranking)
    
    def test_trips(self):
        ''' rankHandHi should return a Trips object with appropriate input.'''
        # Test three possible combinations of cases.
        known_values = ((   [self.deck.deck[12], self.deck.deck[25]], # Full participation of hand in result case.
                            [self.deck.deck[51], self.deck.deck[19], self.deck.deck[17], self.deck.deck[3], self.deck.deck[50]],
                            HandRanks.Trips([self.deck.deck[12], self.deck.deck[25], self.deck.deck[51], self.deck.deck[50], self.deck.deck[19]])),
                        (   [self.deck.deck[6], self.deck.deck[47]], # Case where hand does not participate.
                            [self.deck.deck[51], self.deck.deck[49], self.deck.deck[3], self.deck.deck[16], self.deck.deck[42]],
                            HandRanks.Trips([self.deck.deck[3], self.deck.deck[16], self.deck.deck[42], self.deck.deck[51], self.deck.deck[49]])),
                        (   [self.deck.deck[4], self.deck.deck[26]], # One card from hand participates.
                            [self.deck.deck[0], self.deck.deck[13], self.deck.deck[22], self.deck.deck[25], self.deck.deck[41]],
                            HandRanks.Trips([self.deck.deck[0], self.deck.deck[13], self.deck.deck[26], self.deck.deck[25], self.deck.deck[22]])) )
        for hand, board, ranking in known_values:
            result = HandRanking.rankHandHi(hand, board)
            self.assertIsInstance(result, HandRanks.Trips) # Verify that the correct object was returned.
            self.assertEqual(result, ranking)
    
    def test_two_pair(self):
        ''' rankHandHi should return a TwoPair object with appropriate input.'''
        # Test three possible combinations of cases.
        known_values = ((   [self.deck.deck[11], self.deck.deck[25]], # Full participation of hand in result case.
                            [self.deck.deck[51], self.deck.deck[37], self.deck.deck[17], self.deck.deck[3], self.deck.deck[48]],
                            HandRanks.TwoPair([self.deck.deck[25], self.deck.deck[51], self.deck.deck[11], self.deck.deck[37], self.deck.deck[48]])),
                        (   [self.deck.deck[6], self.deck.deck[47]], # Case where hand does not participate.
                            [self.deck.deck[3], self.deck.deck[16], self.deck.deck[15], self.deck.deck[28], self.deck.deck[50]],
                            HandRanks.TwoPair([self.deck.deck[3], self.deck.deck[16], self.deck.deck[15], self.deck.deck[28], self.deck.deck[50]])),
                        (   [self.deck.deck[4], self.deck.deck[26]], # One card from hand participates.
                            [self.deck.deck[17], self.deck.deck[33], self.deck.deck[7], self.deck.deck[25], self.deck.deck[41]],
                            HandRanks.TwoPair([self.deck.deck[7], self.deck.deck[33], self.deck.deck[4], self.deck.deck[17], self.deck.deck[25]])) )
        for hand, board, ranking in known_values:
            result = HandRanking.rankHandHi(hand, board)
            self.assertIsInstance(result, HandRanks.TwoPair) # Verify that the correct object was returned.
            self.assertEqual(result, ranking)
    
    def test_pair(self):
        ''' rankHandHi should return a Pair object with appropriate input.'''
        # Test three possible combinations of cases.
        known_values = ((   [self.deck.deck[11], self.deck.deck[25]], # Full participation of hand in result case.
                            [self.deck.deck[50], self.deck.deck[33], self.deck.deck[17], self.deck.deck[3], self.deck.deck[49]],
                            HandRanks.Pair([self.deck.deck[11], self.deck.deck[50], self.deck.deck[25], self.deck.deck[49], self.deck.deck[33]])),
                        (   [self.deck.deck[0], self.deck.deck[44]], # Case where hand does not participate.
                            [self.deck.deck[3], self.deck.deck[16], self.deck.deck[38], self.deck.deck[37], self.deck.deck[6]],
                            HandRanks.Pair([self.deck.deck[3], self.deck.deck[16], self.deck.deck[38], self.deck.deck[37], self.deck.deck[6]])),
                        (   [self.deck.deck[4], self.deck.deck[26]], # One card from hand participates.
                            [self.deck.deck[0], self.deck.deck[33], self.deck.deck[37], self.deck.deck[25], self.deck.deck[2]],
                            HandRanks.Pair([self.deck.deck[26], self.deck.deck[0], self.deck.deck[25], self.deck.deck[37], self.deck.deck[33]])) )
        for hand, board, ranking in known_values:
            result = HandRanking.rankHandHi(hand, board)
            self.assertIsInstance(result, HandRanks.Pair) # Verify that the correct object was returned.
            self.assertEqual(result, ranking)
    
    def test_high_card(self):
        ''' rankHandHi should return a HighCard object with appropriate input.'''
        # Test three possible combinations of cases.
        known_values = ((   [self.deck.deck[11], self.deck.deck[25]], # Full participation of hand in result case.
                            [self.deck.deck[33], self.deck.deck[17], self.deck.deck[2], self.deck.deck[0], self.deck.deck[5]],
                            HandRanks.HighCard([self.deck.deck[17], self.deck.deck[5], self.deck.deck[33], self.deck.deck[11], self.deck.deck[25]])),
                        (   [self.deck.deck[0], self.deck.deck[28]], # Case where hand does not participate.
                            [self.deck.deck[51], self.deck.deck[36], self.deck.deck[34], self.deck.deck[29], self.deck.deck[17]],
                            HandRanks.HighCard([self.deck.deck[29], self.deck.deck[17], self.deck.deck[34], self.deck.deck[36], self.deck.deck[51]])),
                        (   [self.deck.deck[0], self.deck.deck[35]], # One card from hand participates.
                            [self.deck.deck[1], self.deck.deck[17], self.deck.deck[50], self.deck.deck[34], self.deck.deck[36]],
                            HandRanks.HighCard([self.deck.deck[17], self.deck.deck[34], self.deck.deck[35], self.deck.deck[36], self.deck.deck[50]])) )
        for hand, board, ranking in known_values:
            result = HandRanking.rankHandHi(hand, board)
            self.assertIsInstance(result, HandRanks.HighCard) # Verify that the correct object was returned.
            self.assertEqual(result, ranking)

if __name__ == '__main__':
    unittest.main()