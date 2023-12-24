import entity
import random

class EasyOgre(entity.Entity):
  '''
  Creates an easy ogre

  Attributes:
  name(str): The name of the Ogre
  hp (int): The hp the Ogre currently has.
  max_hp (int): The maximum hp the Ogre has.
  '''

  def __init__(self):
    '''initalizes Ogre with random max hp'''
    super().__init__('Lumbering Ore', random.randint(3, 5))

  def attack(self, entity):
    """enemy attacks hero with randomized damage. The hero should take damage and returns a string to represent the attack."""
    dmg = random.randint(1, 4)
    entity.take_damage(dmg)
    return f'{self.name} attacks a {entity.name} for {dmg} damage.'