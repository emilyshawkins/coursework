import abc
class Door(abc.ABC):
  '''
  Represents a basic door in an escape room.
  '''
  
  @abc.abstractmethod
  def examine_door(self):
    '''Returns a description of the door.'''
    pass

  @abc.abstractmethod
  def menu_options(self):
    '''Returns the door's interaction menu.'''
    pass

  @abc.abstractmethod
  def get_menu_max(self):
    '''Returns the maximum number of options within the door's interaction menu.'''
    pass

  @abc.abstractmethod
  def attempt(self, option):
    '''Sets the input to user's choice and returns a description of the action performed.'''
    pass

  @abc.abstractmethod
  def is_unlocked(self):
    '''Checks if the door is unlocked, returns true if it is and false otherwise.'''
    pass

  @abc.abstractmethod
  def clue(self):
    '''Returns a clue for unlocking the door.'''
    pass

  @abc.abstractmethod
  def success(self):
    '''Returns a congratulatory message for unlocking the door.'''
    pass