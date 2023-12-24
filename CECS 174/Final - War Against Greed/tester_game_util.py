import card_util as cu
import game_util as gu


def main():
    standard_deck = cu.create_std_deck()

    p1_hand = cu.deal_cards_from(standard_deck, 10)
    p2_hand = cu.deal_cards_from(standard_deck, 3)

    print("\nOriginal Player 1 hand...")
    cu.print_deck(p1_hand)
    print("Deck size:", len(p1_hand))
    print()

    print("Original Player 2 hand...")
    cu.print_deck(p2_hand)
    print("Deck size:", len(p2_hand))
    print()

    print("-" * 60)

    print()
    print("Player 1 WAR hand...")
    p1_war = gu.get_war_hand(p1_hand)
    print(p1_war[0])
    print()

    print("Player 2 WAR hand...")

    print()
    p2_war = gu.get_war_hand(p2_hand)
    print(p2_war[0])
    print()

    print("-" * 60)

    print()
    print("Player 1 hand AFTER WAR...")
    cu.print_deck(p1_hand)
    print("Deck size:", len(p1_hand))
    print()

    print("Player 2 hand AFTER WAR...")
    cu.print_deck(p2_hand)
    print("Deck size:", len(p2_hand))
    print()
