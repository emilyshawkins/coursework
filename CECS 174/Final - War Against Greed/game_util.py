def get_war_hand(player_deck):
    """
  displays X's as the face-down cards that are at stake in a war hand, and returns a list of cards that make up a player's war hand.  If the given deck has 4 or more cards, XXX... will be displayed, 4 cards are removed from the given deck and returned as the playing war hand.  Otherwise, less X's are displayed and all cards are removed from the given deck and returned as the playing war hand.  The number of X's displayed in this case will be one minus the number of cards in the war hand.
  INPUT: player_deck - the list of cards from which the war cards will be taken
  OUTPUT: a list of 4 or less cards
  """
    war_hand = []
    if len(player_deck) < 4:
        print("X " * (len(player_deck) - 1) + "...")
        for i in range(0, len(player_deck)):
            war_hand.insert(0, player_deck[i])
        player_deck.clear()
    else:
        print("X X X ...")
        for i in range(len(player_deck) - 4, len(player_deck)):
            war_hand.insert(0, player_deck[i])
        for i in range(4):
            player_deck.pop()
    return war_hand
