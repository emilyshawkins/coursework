# Megan Waples and Emily Hawkins
# Fall 2022
# An escape room that has the user open a series of 3 random doors 
import basic_door
import combo_door
import code_door
import check_input
import random

def open_door(door):
  '''Passes in a door object that the user will try to unlock. Displays the description of the door, its menu, and uses interaction with the door and the result of the interaction.'''
  print(door.examine_door())

  while True:
    
    print(door.menu_options())

    user_input = check_input.get_int_range('', 1, door.get_menu_max())
  
    print(door.attempt(user_input))

    # Checks if the door was unlocked
    if door.is_unlocked():
      print(door.success())
      break
    else:
      print(door.clue())

def main():

  print('Welcome to the Escape Room. You must unlock 3 doors to escape...\n')
  
  for k in range(3):

    # Chooses one of the three doors
    rand_door = random.randint(0, 2)

    if rand_door == 0:
      open_door(basic_door.BasicDoor())
    elif rand_door == 1:
      open_door(combo_door.ComboDoor())
    else:
      open_door(code_door.CodeDoor())
  
  print('Congratulations! You escaped... this time.')
  
main()