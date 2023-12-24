class Entity():
  '''
  Represents an entity

  Attributes:
  name (str): The name of the entity
  hp (int): The hit points of the entity
  max_hp (int): The maximum hit points of the entity
  '''
  def __init__(self, name, max_hp):
    self._name = name
    self._hp = max_hp
    self._max_hp = max_hp

  @property
  def name(self):
    '''Gets and returns the value of the entity's name.'''
    return self._name

  @property
  def hp(self):
    '''Gets and returns the value of the the entity's hit points.'''
    return self._hp

  def take_damage(self, dmg):
    '''Reduces the hit points of the entity by how much damage it takes.'''
    self._hp = self._hp - dmg
    # Checks if hp is less than 0, if it is reset to 0
    if self._hp < 0:
      self._hp = 0

  def __str__(self):
    '''Returns the name and the hit points out of total hit points.'''
    return f'{self._name}: {self._hp}/{self._max_hp}'
    

    