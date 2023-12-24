
import abc

class Monster():
  '''
  Represents a Monster.

  Attributes:
  name (str): The name of the Monster
  hp (int): The hp of the Monster
  '''
  def __init__(self, name, hp):
    self._name = name
    self._hp = hp

  @property
  def name(self):
    '''Returns the name of the monster'''
    return self._name

  @name.setter
  def name(self, name):
    '''Sets the name of the monster'''
    self._name = name

  @property
  def hp(self):
    '''Sets the hp of the monster'''
    return self._hp 

  @hp.setter
  def hp(self, hp):
    '''Gets the hp of the monster'''
    self._hp = hp

  @abc.abstractmethod
  def attack(self):
    '''Returns the attack power of the monster'''
    pass

  def __str__(self):
    '''Returns the monster's name, hp, and attack power'''
    return f'\nName: {self._name}\nHp: {self._hp}\nAttack: {self.attack()}'
    
    