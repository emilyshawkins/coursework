import abc

class Entity(abc.ABC):
  '''
  Describes a character in the game.

  Attributes:
  name (str): The name of the character.
  hp (int): The hp the character currently has.
  max_hp (int): The maximum hp the character has.
  '''
  def __init__(self, name, max_hp):
    self._name = name
    self._hp = max_hp
    self._max_hp = max_hp

  @property
  def name(self):
    '''Gets the name of the character.'''
    return self._name

  @property
  def hp(self):
    '''Gets the hp of the character'''
    return self._hp

  def take_damage(self, dmg):
    '''Decrements the player's by the damage they take and resets to 0 if it becomes negative.'''
    self._hp -= dmg
    # Sets hp to 0 if its negative
    if self._hp < 0:
      self._hp = 0

  def heal(self):
    '''Restores the hp of the character to the character's maximum hp.'''
    self._hp = self._max_hp

  def __str__(self):
    '''Returns a string with the character's name and hp.'''
    return f'{self._name}\nHP: {self._hp}/{self._max_hp}'

  @abc.abstractmethod
  def attack(self, entity):
    '''Allows the character to attack an entity.'''
    pass