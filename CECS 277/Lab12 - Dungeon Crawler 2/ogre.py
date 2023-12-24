import entity
import random

class Ogre(entity.Entity):
   '''
  Creates an easy ogre

  Attributes:
  name(str): The name of the Ogre
  hp (int): The hp the Ogre currently has.
  max_hp (int): The maximum hp the Ogre has.
  '''

   def __init__(self):
     super().__init__('Lumbering Ogre', random.randint(8, 12))

   def attack(self, entity):
     '''enemy attacks hero with randomized damage. The hero should take damage and returns a string to represent the attack.'''
     dmg = random.randint(6, 10)
     entity.take_damage(dmg)
     return f'{self.name} attacks a {entity.name} for {dmg} damage.'