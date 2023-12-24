import door
import random

class CodeDoor(door.Door):
  '''
  Represents a code door in an escape room.

  Attributes:
  correct_code (list): Is a list of three characters representing the correct code.
  input (list): Is a list of three characters changeable by the user.
  '''
  def __init__(self):
    code = [random.randint(1, 2), random.randint(1, 2), random.randint(1, 2)]
    for k in range(len(code)):
      if code[k] == 1:
        code[k] = 'O'
      else:
        code[k] = 'X'
      
    self._correct_code = code
    self._input = ['O', 'O', 'O']
    
  def examine_door(self):
    '''Returns a description of the door.'''
    return 'A door with a coded keypad with three characters. Each key toggles a value with an \'X\' or an \'O\''

  def menu_options(self):
    '''Returns the door's interaction menu.'''
    return f'\n1. Press Key 1\n2. Press Key 2\n3. Press Key 3'

  def get_menu_max(self):
    '''Returns the maximum number of options within the door's interaction menu.'''
    return 3

  def attempt(self, option):
    '''Sets the input to user's choice and returns a description of the action performed.'''
    # Checks what the current character is and switches it to the other
    if self._input[option - 1] == 'O':
      self._input[option - 1] = 'X'
    else:
      self._input[option - 1] = 'O'
    return f'\nYou toggle the key to {self._input[option - 1]}.'

  def is_unlocked(self):
    '''Checks if the correct code of the door is the same as the user's input and returns true if it is and false otherwise.'''
    if self._input == self._correct_code:
      return True
    else:
      return False

  def clue(self):
    '''Returns a clue for unlocking the door.'''
    counter = 0
    # Iterates through the correct code and checks it with the user's code and counts how many are the same
    for k in range(len(self._correct_code)):
      if self._correct_code[k] == self._input[k]:
        counter += 1
    return f'{counter} characters are correct.'

  def success(self):
    '''Returns a congratulatory message for unlocking the door.'''
    return '\nCongratulations, you got the code right and unlocked the door!\n'