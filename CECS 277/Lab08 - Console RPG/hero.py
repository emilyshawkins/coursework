from entity import Entity
import random

class Hero(Entity):
  '''
  Represents a hero

  Attributes:
  name (str): The name of the hero
  hp (int): The hit points of the hero
  max_hp (int): The maximum hit points of the hero
  '''
  
  def sword_attack(self, dragon):
    '''The dragon takes a random amount of damage depending on the rolls of two six-sided dice'''
    damage = random.randint(1, 6) + random.randint(1, 6)
    dragon.take_damage(damage)

    return f'\nYou slash the {dragon.name} with your sword for {damage} damage.'
    
  def arrow_attack(self, dragon):
    '''The dragon takes a random amount of damage depending on the roll of a twelve-sided die'''
    damage = random.randint(1, 12)
    dragon.take_damage(damage)

    return f'\nYou hit the {dragon.name} with an arrow for {damage} damage.'