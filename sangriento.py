from poker import poker, hand_rank
from deal import deal

hand_names = ["High Card", "Pair", "Two Pair", "3 of a Kind", "Straight",
              "Flush", "Full House", "4 of a Kind", "Straight Flush"]


def sangriento(n):
    hands = deal(n)
    for hand in hands:
        print hand

    winner = poker(hands)
    ranking = hand_rank(winner[0])[0]

    print "Winner hand(s):"
    print hand_names[ranking]

    return winner


players = 0
while players < 2 or players > 10:
    try:
        players = int(raw_input("Enter number of players (2-10): ").strip())
        if players > 1 and players < 11:
            print sangriento(players)
        else:
            print "Minimum players: 2. Maximum: 10."
    except:
        print "Invalid input"
