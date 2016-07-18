import random

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']


def deal(players, n=5, deck=mydeck):
    """Shuffle the deck and deal out n-cards to each player

    Args:
        players: int indicates number of players.
        n: int indicates number of cards to be dealt to each player.
        deck: a list with all the cards available in the deck.
    """
    random.shuffle(deck)
    return [deck[n*player:n*(player+1)] for player in range(players)]


def texas_holdem_deal(players, deck=mydeck):
    """
    Shuffle the deck and deal out 2 cards to each player, deals
    flop, turn and river.


    Args:
        players: int indicates number of players.
        deck: a list with all the cards available in the deck.
    """
    random.shuffle(deck)
    # Flop, turn and river are the last 5 cards
    community_cards = deck[-5:]
    return [deck[2*player:2*(player+1)]+community_cards
            for player in range(players)]
