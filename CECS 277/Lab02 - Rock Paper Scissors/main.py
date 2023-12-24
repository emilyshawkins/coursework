# Megan Waples and Emily Hawkins
# Fall 2022
# User plays rock paper scissors against the computer and displays score.
import random
import check_input
  
def weapon_menu():
  '''Asks the user to input their choice: (R)ock, (P)aper, (S)cissors, or (B)ack.  Checks user input for validity and then returns the inputted value.'''
  player_weapon = input('Choose your weapon:\n     R. Rock\n     P. Paper\n     S. Scissors\n     B. Back\n')
  if player_weapon.upper() == "R":
    return 'R'
  elif player_weapon.upper() == "P":
    return 'P'
  elif player_weapon.upper() == "S":
    return 'S'
  elif player_weapon.upper() == "B":
    return 'B'
  else: # any non strings and strings other than R, P, S, and B are invalid
    print('Invalid input\n')

def comp_weapon():
  '''Randomly chooses the computer’s throw and returns an “R”, “P”, or “S”.'''
  weapon = random.randint(1, 3)
  if weapon == 1:
    return 'R'
  elif weapon == 2:
    return 'P'
  elif weapon == 3:
    return 'S'


def find_winner(player, comp):
  '''Passes in the two weapons (R, P, or S), displays the throws, compares the two weapons and displays the result and returns who is the winner of that round (0=Tie, 1=Player, 2=Computer).'''

  if player == 'R':
    print('\nPlayer chose Rock')
  elif player == 'P':
    print('\nPlayer chose Paper')
  elif player == 'S':
    print('\nPlayer chose Scissors')

  if comp == 'R'and (player == 'R' or player == 'P' or player == 'S'):
    print('Computer chose Rock')
  elif comp == 'P' and (player == 'R' or player == 'P' or player == 'S'):
    print('Computer chose Paper')
  elif comp == 'S' and (player == 'R' or player == 'P' or player == 'S'):
    print('Computer chose Scissors')

  # Compares player weapon input with computers to determine winner and displays result to the user
  if player == comp:
    print("\nTie\n")
    return 0
  elif player == 'R' and comp == 'S' or player == 'S' and comp == 'P' or player == 'P' and comp == 'R':
    print("\nPlayer wins\n")
    return 1
  elif comp == 'R' and player == 'S' or comp == 'S' and player == 'P' or comp == 'P' and player == 'R':
    print("\nComputer wins\n")
    return 2

def displayscore(player, comp):
  '''Displays the scores'''
    
  print("\n   Player =", player)
  print("   Computer =", comp, '\n')

  return ""

def main():

  # Get and Validate user input and set scores to zero
  user_input = check_input.get_int_range('RPS Menu:\n     1. Play game\n     2. Show score\n     3. Quit\n', 1, 3) 
  player_score = 0
  computer_score = 0

  while user_input != 3:
    # Repeats game menu and game while the user does not quit
    if user_input == 1:
      player = weapon_menu()

      while player != 'B':  
        comp = comp_weapon()
        winner = find_winner(player, comp)
        # Adds points depending on the winner of the round
        if winner == 1:
          player_score += 1
        elif winner == 2:
          computer_score += 1
        player = weapon_menu()
    elif user_input == 2:
      displayscore(player_score, computer_score)
    user_input = check_input.get_int_range('RPS Menu:\n1. Play game\n2. Show score\n3. Quit\n', 1, 3)

  print("\nFinal Score:")
  print(displayscore(player_score, computer_score))
  
main()