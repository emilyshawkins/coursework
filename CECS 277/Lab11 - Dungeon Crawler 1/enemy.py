import random
import entity

class Enemy(entity.Entity):
  '''
  Describes an enemy in the game.

  Attributes:
  name (str): The name of the enemy.
  hp (int): The hp the enemy currently has.
  max_hp (int): The maximum hp the enemy has.
  '''
  def __init__(self):
    name = ['Goblin', 'Ghoul', 'Troll', 'Skeleton', 'Ghost']
    super().__init__(name[random.randint(0, len(name) - 1)], random.randint(4, 8))

  def attack(self, entity):
    '''Allows the enemy to attack an entity.'''
    dmg = random.randint(1, 4)
    entity.take_damage(dmg)
    return f'{self._name} attacks a {entity.name} for {dmg} damage.'