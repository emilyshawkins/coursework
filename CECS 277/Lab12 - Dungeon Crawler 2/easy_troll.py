import entity
import random

class EasyTroll(entity.Entity):
  '''
  Creates an easy Troll

  Attributes:
  name(str): The name of the Troll
  hp (int): The hp the Troll currently has.
  max_hp (int): The maximum hp the Troll has.
  '''

  def __init__(self):
    '''initalizes Troll with random max hp'''
    super().__init__('Tremendous Troll', random.randint(4, 5))

  def attack(self, entity):
    '''enemy attacks hero with randomized damage. The hero should take damage and returns a string to represent the attack.'''
    dmg = random.randint(1, 5)
    entity.take_damage(dmg)
    return f'{self.name} attacks a {entity.name} for {dmg} damage.'