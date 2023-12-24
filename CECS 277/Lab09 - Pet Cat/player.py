class Player():
  '''
  Represents a player.

  Attributes 
  hp (int): Is the hit points that a player has
  '''
  def __init__(self):
    self._hp = 25
    
  @property
  def hp(self):
    '''Gets the hp value of the player'''
    return self._hp

  def take_damage(self, dmg):
    '''Decrements the player's by the damage they take and resets to 0 if it becomes negative.'''
    self._hp = self._hp - dmg
    if self._hp < 0:
      self._hp = 0

  def __str__(self):
    '''Returns a string of the player's hp'''
    return f'\nYou have {self._hp} hp.'
    

    