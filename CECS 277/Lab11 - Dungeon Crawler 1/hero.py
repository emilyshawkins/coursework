import entity
import random
import map

class Hero(entity.Entity):
  '''
  Represents the user's character in the game.

  Attributes:
  name (str): The name of the user's character.
  hp (int): The hp the user's character currently has.
  max_hp (int): The maximum hp the user's character has. 
  loc (int []) : The user's character's current location on the map.
  '''
  def __init__(self, name):
    super().__init__(name, 25)
    self._loc = [0, 0]

  @property
  def loc(self):
    '''Returns the location of the user's character.'''
    return self._loc

  def attack(self, entity):
    '''Allows the user's character to attack an entity.'''
    dmg = random.randint(2, 5)
    entity.take_damage(dmg)
    return f'{self.name} attacks a {entity.name} for {dmg} damage.'

  def go_north(self):
    '''Updates the character's location on the map, one up.'''
    dungeon = map.Map()
    # Checks if location is out of bounds
    if self._loc[0] - 1 < 0:
      return 'x'
    self._loc[0] = self._loc[0] - 1
    # Reveals location that player is at
    dungeon.reveal(self._loc)
    return dungeon[self._loc[0]][self._loc[1]]
     
  def go_south(self):
    '''Updates the character's location on the map, one down.'''
    dungeon = map.Map()
    # Checks if location is out of bounds
    if self._loc[0] + 1 > len(dungeon) - 1:
      return 'x'
    self._loc[0] = self._loc[0] + 1
    # Reveals location that player is at
    dungeon.reveal(self._loc)
    return dungeon[self._loc[0]][self._loc[1]]
    
  def go_east(self):
    '''Updates the character's location on the map, one right.'''
    dungeon = map.Map()
    # Checks if location is out of bounds
    if self._loc[1] + 1 > len(dungeon[self._loc[0]]) - 1:
      return 'x'
    self._loc[1] = self._loc[1] + 1
    # Reveals location that player is at
    dungeon.reveal(self._loc)
    return dungeon[self._loc[0]][self._loc[1]]
    
  def go_west(self):
    '''Updates the character's location on the map, one left.'''
    dungeon = map.Map()
    # Checks if location is out of bounds
    if self.loc[1] - 1 < 0:
      return 'x'
    self._loc[1] = self._loc[1] - 1
    # Reveals location that player is at
    dungeon.reveal(self._loc)
    return dungeon[self._loc[0]][self._loc[1]]
    
    