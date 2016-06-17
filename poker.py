def poker(hands):
    """Return the best hand: poker([hand,...]) => hand

	Args:
		hands: list of hands to compare.
    """
    return max(hands, key=hand_rank)


def card_ranks(cards):
    """Return a list of the ranks, sorted with higher first.

	Args:
		hand: list of 5 2-letter strings representing card rank and suit.
    """
    ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def straight(ranks):
    """Return True if the ordered ranks form a 5-card straight.
    
	Args:
		ranks: list of ranks of cards in descending order.
    """
    print ranks
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand):
    """"Return True if all the cards have the same suit.

	Args:
		hand: list of 5 2-letter strings representing card rank and suit.
    """
    return hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]


def kind(n, ranks):
	"""
	Return the first rank that this hand has exactly n of.
	Return None if there is no n-of-a-kind in the hand.

	Args:
		n: number of equal ranks to be checked. Valid values: 1 to 4.
		ranks: list of ranks of cards in descending order.
	"""
	for r in ranks:
		if ranks.count(r) == n:
			return r
	return None


def two_pair(ranks):
	"""If there are two pair, return the two ranks as a
	tuple: (highest, lowest); otherwise return None.

	Args:
		ranks: list of ranks of cards in descending order.
	"""
	pair = kind(2, ranks)
	lowpair = kind(2, list(reversed(ranks)))
	if pair and lowpair != pair:
		return (pair, lowpair)
	else:
		return None


def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), kind(1, ranks))
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)


def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "5S 5D AC AS KS".split() # Two Pair
    s1 = "AC 2S 3C 4D 5D".split() # A-5 Straight 
    s2 = "2S 3C 4D 5D 6S".split() # 2-6 Straight
    ah = "AC 2S 9C 4D 6D".split() # A High 
    sh = "7C 2S 6C 3D 5D".split() # 7 High
    assert poker([s1, s2, ah, sh]) == s2
    assert poker([s1, ah, sh]) == s1
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (14, 5)
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return 'tests pass'

print test()
