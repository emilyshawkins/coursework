import door
import random
class BasicDoor(door.Door):
  '''
  Represents a basic door in an escape room.

  Attributes:
  state (int): Is the current state of the door.
  input (int): Is the user's input.
  '''
  def __init__(self):
    self._state = random.randint(1, 2)
    self._input = 0

  def examine_door(self):
    '''Returns a description of the door.'''
    return f'You encounter a door that is either pushed or pulled.'
    
  def menu_options(self):
    '''Returns the door's interaction menu.'''
    return f'\n1. Push\n2. Pull'

  def get_menu_max(self):
    '''Returns the maximum number of options within the door's interaction menu.'''
    return 2

  def attempt(self, option):
    '''Sets the input to user's choice and returns a description of the action performed.'''
    self._input = option
    if option == 1:
      return f'\nYou push the door.'
    elif option == 2:
      return f'\nYou pull the door.'

  def is_unlocked(self):
    '''Checks if the current state of the door is the same as the user's input and returns true if it is and false otherwise.'''
    if self._state == self._input:
      return True
    else:
      return False

  def clue(self):
    '''Returns a clue for unlocking the door.'''
    return 'Try the other way.'

  def success(self):
    '''Returns a congratulatory message for unlocking the door.'''
    return '\nCongratulations, you opened the door!\n'