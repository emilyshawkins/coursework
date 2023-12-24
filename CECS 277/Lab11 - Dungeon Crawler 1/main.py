# Megan Waples and Emily Hawkins
# Fall 2022
# User wanders through dungeon maze and fight monsters they encounter as they explore. The user wins if they reach the dungeon's exit alive.

import hero
import map
import enemy
import check_input
import random

def main():
  user_name = input('What is your name, traveler? ')

  player = hero.Hero(user_name)
  dungeon = map.Map() 

  print()
  print(player)
  print(dungeon.show_map(player.loc))
  print()

  user_input = check_input.get_int_range('1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit\n', 1, 5)

  while user_input != 5:

    if user_input == 1:
      encounter = player.go_north()
    elif user_input == 2:
      encounter = player.go_south()
    elif user_input == 3:
      encounter = player.go_east()
    elif user_input == 4:
      encounter = player.go_west()

    if encounter == 'm':
      monster = enemy.Enemy()
      print('\nYou encounter a', end= ' ')
      print(monster)

      # Loops until player dies or runs away
      while player.hp != 0:
        monster_menu = check_input.get_int_range(f'\n1. Attack {monster.name}\n2. Run Away\nEnter choice: ', 1, 2)
        if monster_menu == 1:
          print(f'\n{player.attack(monster)}')
          # Monster attacks if it's not dead
          if monster.hp > 0:
            print(monster.attack(player))    
          else:
            print(f'You have slain a {monster.name}\n')
            dungeon.remove_at_loc(player.loc)
            break
        elif monster_menu == 2:
          # If the user tries to run away player escapes in a random direction
          while True:
            escape = random.randint(1, 4)
            if escape == 1:
              encounter = player.go_north()
            elif escape == 2:
              encounter = player.go_south()
            elif escape == 3:
              encounter = player.go_east()
            elif escape == 4:
              encounter = player.go_west() 
            if encounter != 'x':
              break
          print('\nYou ran away!\n')
          break
      # If player dies, the game ends
      if player.hp == 0:
        print('\nYou have been slain.')
        break
    elif encounter == 'x':
      print('\nYou cannot go that way...\n')
    elif encounter == 'n':
      print('\nThere is nothing here...\n')
    elif encounter == 's':
      print('\nYou are back at the start.\n')
    elif encounter == 'i':
      print('\nYou found a Health Potion! You drink it to restore your health.\n')
      player.heal()
      dungeon.remove_at_loc(player.loc)

    # If user finds the exit, game ends
    elif encounter == 'f':
      print('\nCongratulations! You found the exit.')
      break
      
    print(player)
    print(dungeon.show_map(player.loc))
    
    user_input = check_input.get_int_range('\n1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit\n', 1, 5)

  print('\nGame Over')
    
main()