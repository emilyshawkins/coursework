import random
from card import Card


def add_cards_to(receiver_deck, giver_deck):
    """
  transfers all cards from a "giver" deck to a "receiver" deck 
  INPUT: 
        - receiver_deck : the list of Card objects that will be emptied upon transferring all cards 
        - giver_deck    : the list of Card objects that will receive the cards from the giver deck
  """
    for i in giver_deck:
        receiver_deck.append(i)
    giver_deck = []
    return


def deal_cards_from(deck, num):
    """
  deals a specified number of cards from the given deck
  INPUT: 
        - deck : a list of Card objects
        - num  : a positive integer
  OUTPUT:
        a list of Card objects of size 'num'
  """
    dealed_cards = []
    for i in range(len(deck) - num, len(deck)):
        dealed_cards.insert(0, deck[i])
    for i in range(num):
        deck.pop()
    return dealed_cards


def shuffle_cards(deck):
    """shuffles the given cards seven times
     INPUT: deck - a list of Card objects
     OUTPUT: None
  """
    # HINT: The 'random' module has a useful function
    for i in range(7):
        random.shuffle(deck)
    return


# -------------------------- DO NOT MODIFY THE FUNCTIONS BELOW --------------------------------- #


def create_std_deck():
    """
  creates a standard deck of 52 cards 
  OUTPUT: a list of 52 Card objects
  """
    deck = []
    for suit in ['HEARTS', 'SPADES', 'DIAMONDS', 'CLUBS']:
        for rank in range(1, 14):
            card = Card(rank, suit)
            deck.append(card)
    return deck


def print_deck(deck, revealed=True):
    """
  prints the cards in the given deck. If the second parameter is True, the suit and rank of the cards are printed.  If the second parameter is False, the cards are printed face-down symbolically using an X.
  INPUT: 
        - deck : the list of Card objects to print
        - revealed : Boolean value, defaults to True
  
  """
    if (revealed):
        i = 1
        for card in deck:
            print("%-3s" % card, end=" ")
            if (i % 13 == 0):
                print()
            i += 1
    else:
        i = 1
        for card in deck:
            print("X", end=" ")
            if (i % 13 == 0):
                print()
            i += 1
    print()
    return
