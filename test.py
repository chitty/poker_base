from poker import poker, kind, two_pair, hand_rank, card_ranks, best_hand


def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split()  # Straight Flush
    fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
    fh = "TD TC TH 7C 7D".split()  # Full House
    tp = "5S 5D AC AS KS".split()  # Two Pair
    s1 = "AC 2S 3C 4D 5D".split()  # A-5 Straight
    s2 = "2S 3C 4D 5D 6S".split()  # 2-6 Straight
    ah = "AC 2S 9C 4D 6D".split()  # A High
    sh = "7C 2S 6C 3D 5D".split()  # 7 High
    assert poker([s1, s2, ah, sh]) == [s2]
    assert poker([s1, ah, sh]) == [s1]
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) is None
    assert kind(2, fkranks) is None
    assert kind(1, fkranks) == 7
    assert two_pair(fkranks) is None
    assert two_pair(tpranks) == (14, 5)
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([sf]) == [sf]
    assert poker([sf] + 99*[fh]) == [sf]
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return 'tests pass'

print test()


def test_best_hand():
    test_1 = sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
    assert (test_1 == ['6C', '7C', '8C', '9C', 'TC'])
    test_2 = sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
    assert (test_2 == ['8C', '8S', 'TC', 'TD', 'TH'])
    test_3 = sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
    assert (test_3 == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'

print test_best_hand()
