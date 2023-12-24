# Megan Waples and Emily Hawkins
# Fall 2022
# Creates a Monster

import check_input
import alien
import beast
import undead
import fire
import flying
import lasers
import poison

def main():

  print('Monster Maker!')
  monster_menu = check_input.get_int_range('Choose a base monster:\n1. Alien\n2. Beast\n3. Undead\nEnter choice: ', 1, 3)

  if monster_menu == 1:
    monster = alien.Alien()
  elif monster_menu == 2:
    monster = beast.Beast()
  else:
    monster = undead.Undead()

  print(monster)

  ability = check_input.get_int_range('\nAdd an ability:\n1. Fire\n2. Flying\n3. Lasers\n4. Poison\n5. Quit\nEnter ability: ', 1, 5)

  while ability != 5:

    if ability == 1:
      monster = fire.Fire(monster)
    elif ability == 2:
     monster = flying.Flying(monster)
    elif ability == 3:
      monster = lasers.Lasers(monster)
    elif ability == 4:
      monster = poison.Poison(monster)

    print(monster, '\n')
      
    ability = check_input.get_int_range('Add an ability:\n1. Fire\n2. Flying\n3. Lasers\n4. Poison\n5. Quit\nEnter ability: ', 1, 5)

  print(f'\nYour final monster is:{monster}')

main()