import tester_card
import tester_card_util
import tester_game_util
import war_game

main_menu = "\n" + "=" * 70 + "\nWhat would you like to do?\n1.  Test Card class.\n2.  Test card utility functions.\n3.  Test game utility function.\n4.  Play War Against Greed.\n5.  Exit.\n"

print(main_menu)
selection = input("Your selection: ")

while selection != '5':
    if selection == '1':
        print("\n" + "=" * 20 + " Testing Card Class " + "=" * 20)
        tester_card.main()
    elif selection == '2':
        print("\n" + "=" * 20 + " Testing Card Util Functions " + "=" * 20)
        tester_card_util.main()
    elif selection == '3':
        print("\n" + "=" * 20 + " Testing Game Util Functions " + "=" * 20)
        tester_game_util.main()
    elif selection == '4':
        war_game.play()
    elif selection != '5':
        print("Invalid selection. Please try again.")

    print(main_menu)
    selection = input("Your selection: ")
