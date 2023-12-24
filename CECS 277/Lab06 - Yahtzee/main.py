# Megan Waples and Emily Hawkins
# Fall 2022
# A dice game that awards points to the player for pairs, three of a kind, and series (Yahtzee)

import player
import check_input

def take_turn(player):
  '''Rolls the player’s dice, displays the dice, checks for and displays win types (pair, series, three-of-a-kind), and displays the updated score. '''
  
  player.roll_dice()
  print(player)

  #Check is user got a series, pair, or three of a kind
  if player.has_pair() == True:
    print('You got a pair!')
  elif player.has_three_of_kind() == True:
    print('You got a 3 of a kind!')
  elif player.has_series() == True:
    print('You got a series of 3!')
  else:
    print('Aww. Too bad.')
    
  print('Score =', player.get_points())

  return

def main():
  
  print('-Yahtzee-')
  
  user = player.Player()
  take_turn(user)
  
  player_input = check_input.get_yes_no('\nPlay again? (Y/N): ')

  #Run until user enters 'N'
  if player_input == True:
    while player_input == True:
      take_turn(user)
      player_input = check_input.get_yes_no('\nPlay again? (Y/N): ')

  #When player enters 'N' indicate game is over and display score
  print('\nGame Over.')
  print('Final Score =', user.get_points())
  
main()