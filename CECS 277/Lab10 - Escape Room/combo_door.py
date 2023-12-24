import door
import random

class ComboDoor(door.Door):
  '''
  Represents a combo door in an escape room.

  Attributes:
  correct_value (int): Is the correct value for the combo door.
  input (int): Is the user's input.
  '''
  def __init__(self):
    self._correct_value = random.randint(1, 10)
    self._input = 0

  def examine_door(self):
    '''Returns a description of the door.'''
    return f'You encounter a door with a combination lock. You can spin the dial to a number 1 - 10.'

  def menu_options(self):
    '''Returns the door's interaction menu.'''
    return f'\nEnter # 1 - 10:'

  def get_menu_max(self):
    '''Returns the maximum number of options within the door's interaction menu.'''
    return 10

  def attempt(self, option):
    '''Sets the input to user's choice and returns a description of the action performed.'''
    self._input = option
    return f'\nYou turn the dial to... {option}.'

  def is_unlocked(self):
    '''Checks if the current state of the door is the same as the user's input and returns true if it is and false otherwise.'''
    if self._input == self._correct_value:
      return True
    else:
      return False

  def clue(self):
    '''Returns a clue for unlocking the door.'''
    # Checks if the user's input is greater than or less than the correct value in order to return the clue
    if self._input > self._correct_value:
      return f'Try a lower number.'
    elif self._input < self._correct_value:
      return f'Try a higher number.'

  def success(self):
    '''Returns a congratulatory message for unlocking the door.'''
    return f'\nYou found the correct value and opened the door.\n'