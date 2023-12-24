import entity
import random

class EasyGoblin(entity.Entity):
  '''
  Creates an easy goblin.
  
  Attributes:
  name (str): The easy goblin name
  hp (int): The easy goblin's hp
  max_hp (int): The easy goblin's max_hp
  '''
  def __init__(self):
    '''initalizes Goblin with random max hp'''
    super().__init__('Vicious Goblin', random.randint(3, 4))

  def attack(self, entity):
    """enemy attacks hero with randomized damage. The hero should take damage and returns a string to represent the attack."""
    dmg = random.randint(1, 3)
    entity.take_damage(dmg)
    return f'{self.name} attacks a {entity.name} for {dmg} damage.'