import entity
import random

class Goblin(entity.Entity):
  '''
  Creates an goblin.
  
  Attributes:
  name (str): The goblin name
  hp (int): The goblin's hp
  max_hp (int): The goblin's max_hp
  '''
  def __init__(self):
    super().__init__('Vicious Goblin', random.randint(6, 10))

  def attack(self, entity):
    '''Attacks an entity for 4 to 8 damage.'''
    dmg = random.randint(4, 8)
    entity.take_damage(dmg)
    return f'{self.name} attacks a {entity.name} for {dmg} damage.'