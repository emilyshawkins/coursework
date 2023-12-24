# Megan Waples and Emily Hawkins
# Fall 2022
# Has the user fight as a hero to defeat three dragons to win.

import hero
import dragon
import fire_dragon
import flying_dragon
import check_input
import random

def main():

  user_name = input('What is your name, challenger?\n')
  print('Welcome to dragon training,', user_name, '\nYou must defeat 3 dragons.\n')

#Create hero object and list containing each dragon
  player = hero.Hero(user_name, 50)
  dragon_list = [dragon.Dragon('Deadly Nader', 10), fire_dragon.FireDragon('Gronckle', 15, 3), flying_dragon.FlyingDragon('Timberjack', 20, 5)]


#Loop until player dies or wins
  while True:
    print(f'\n{player}')

    #display list of dragons 
    count = 1
    for i in dragon_list:
      print(f'{count}. Attack {i}')
      count += 1

    dragon_menu = check_input.get_int_range('Choose a dragon to attack: ', 1, len(dragon_list))

    attacked_dragon = dragon_list[dragon_menu - 1]

    attack_menu = check_input.get_int_range('\nAttack with:\n1. Arrow (1 D12)\n2. Sword (2 D6)\nEnter weapon: ', 1, 2)

    if attack_menu == 1:
      print(player.arrow_attack(attacked_dragon))
    else:
      print(player.sword_attack(attacked_dragon))

    if attacked_dragon.hp == 0:
      dragon_list.pop(dragon_menu - 1)
      if len(dragon_list) == 0: #If there are no dragons alive, display player wins
        print('\nCongratulations! You have defeated all 3 dragons, you have passed the trials.')
        break

    #choose a random dragon to attack the player and choose random type of dragon attack
    attack = random.randint(1, 2)
    attacking_dragon = dragon_list[random.randint(0, len(dragon_list) - 1)]
    if attack == 1:
      print(attacking_dragon.basic_attack(player))
    else:
      print(attacking_dragon.special_attack(player))
    if player.hp == 0: #if player runs out of hp end game and display they loose
      print('\nYou have failed to defeat all the dragons!')
      break
      
  
main()