# Megan Waples and Emily Hawkins
# Fall 2022
# An interactive pet game where the user has life points and interacts with different types of cats

import check_input
import tabby
import tiger
import ocelot
import player

def interact_cat(cat, player):
  '''Displays the cat interation menu and gets the users input to feed, play, or pet the cat.'''
  print(player)
  print(cat)
  interact_menu = check_input.get_int_range('Cat Menu:\n1. Feed your cat\n2. Play with your cat\n3. Pet your cat\nEnter choice: ', 1, 3)

  if interact_menu == 1:
    print(cat.feed(player))
  elif interact_menu == 2:
    print(cat.play(player))
  else:
    print(cat.pet(player))
  
def main():
  
  cat_menu = check_input.get_int_range('Cat Selection:\n1. Tabby Cat\n2. Ocelot\n3. Tiger\nEnter choice: ', 1, 3)
  cat_name = input('Name your kitty: ')

  # construct the cat choosen by the user 
  if cat_menu == 1:
    cat = tabby.Tabby(cat_name)
  elif cat_menu == 2:
    cat = ocelot.Ocelot(cat_name)
  else:
    cat = tiger.Tiger(cat_name)

  user = player.Player()

  # Checks if the user has 0 hp
  while user.hp != 0:
    interact_cat(cat, user)


  print('\nYour cat killed you...')
  
main()