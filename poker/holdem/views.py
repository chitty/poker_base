from django.shortcuts import render

from poker.urls import *
from poker_base.poker import poker, hand_rank
from poker_base.deal import texas_holdem_deal


hand_names = ["High Card", "Pair", "Two Pair", "3 of a Kind", "Straight",
              "Flush", "Full House", "4 of a Kind", "Straight Flush"]


def index(request):
    # v1: Limited to two players for now. Player vs CPU.
    hands = texas_holdem_deal(2)
    player_hand = format_card(hands[0][:2])
    cpu_hand = format_card(hands[1][:2])
    community_cards = format_card(hands[0][2:])

    winning_hands = poker(hands)
    ranking = hand_rank(winning_hands[0])[0]

    if len(winning_hands) > 1:
        outcome = "Draw you both have a %s" % hand_names[ranking]
    elif winning_hands[0] == hands[0]:
        outcome = "You won with a %s" % hand_names[ranking]
    else:
        outcome = "You lost to a %s" % hand_names[ranking]

    context = {'player': player_hand, 'cpu': cpu_hand,
               'outcome': outcome, 'community_cards': community_cards}

    return render(request, 'holdem/index.html', context)


def format_card(cards):
    """
    Returns a dictionary with the passed cards rank, color, and suit.

    Args:
        cards: A list of 2-letter strings representing card rank and suit.
    """
    formated_cards = []

    for card in cards:
        if card[0] == 'T':
            card_dict = {'rank': '10'}
        else:
            card_dict = {'rank': card[0]}
        if card[1] == 'C':
            card_dict['color'] = 'black'
            card_dict['suit'] = 'clubs'
        elif card[1] == 'D':
            card_dict['color'] = 'red'
            card_dict['suit'] = 'diams'
        elif card[1] == 'H':
            card_dict['color'] = 'red'
            card_dict['suit'] = 'hearts'
        elif card[1] == 'S':
            card_dict['color'] = 'black'
            card_dict['suit'] = 'spades'
        formated_cards.append(card_dict)

    return formated_cards
