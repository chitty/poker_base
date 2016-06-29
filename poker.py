import itertools


def card_ranks(cards):
    """Return a list of the ranks, sorted with higher first.

    Args:
        hand: list of 5 2-letter strings representing card rank and suit.
    """
    ranks = ['--23456789TJQKA'.index(r) for r, s in cards]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def straight(ranks):
    """Return True if the ordered ranks form a 5-card straight.

    Args:
        ranks: list of ranks of cards in descending order.
    """
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


def allmax(iterable, key=None):
    """Return a list of all items equal to the max of the iterable.
    This auxiliary function helps in handling ties.

    Args:
        iterable: list of all the items, poker hands.
        key: method to do comparisons.
    """
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result


def poker(hands):
    """Return a list of winning hands: poker([hand,...]) => [hand,...]

    Args:
        hands: list of hands to compare.
    """
    return allmax(hands, key=hand_rank)


def best_hand(hand):
    """From a n-card hand, return the best 5 card hand.

    Args:
        hand: a list with n cards, with n > 5.
    """
    return max(itertools.combinations(hand, 5), key=hand_rank)
