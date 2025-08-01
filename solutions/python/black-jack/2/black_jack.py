"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    royals = ['J', 'Q', 'K']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10']

    if card in royals:
        result = 10
    elif card in numbers:
        result = int(card)
    elif card == 'A':
        result = 1
    return result


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if value_one == value_two:
        result = (card_one, card_two)
    elif value_one > value_two:
        result = card_one
    else:
        result = card_two
    return result


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    result = 0
    current_value = value_of_card(card_one) + value_of_card(card_two)
    if card_one == 'A' or card_two == 'A':
        result = 1
    elif current_value <= 10:
        result = 11
    elif current_value <= 20:
        result = 1
    return result


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    
    if card_one_value == 1 and card_two_value == 10:
        result = True
    elif card_one_value == 10 and card_two_value == 1:
        result = True
    elif card_one_value + card_two_value == 21:
        result = True
    else:
        result = False
    return result


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    return 9 <= (value_of_card(card_one) + value_of_card(card_two)) <= 11
