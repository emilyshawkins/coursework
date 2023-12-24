from dragon import Dragon
import random

class FireDragon(Dragon):
  '''
  Represents a Fire Dragon

  Attributes:
  name (str): The name of the fire dragon
  hp (int): The hit points of the fire dragon
  max_hp (int): The maximum hit points of the fire dragon
  f_shots(int): The number of fire shots the fire dragon has
  '''

  def __init__(self, name, max_hp, f_shots):
    super().__init__(name, max_hp)
    self._fire_shots = f_shots

  def special_attack(self, hero):
    '''– overridden fire attack – if the dragon has any fire_shots left, then the hero takes a random amount of damage in the range 5-9 and the number of fire_shots is decremented and a string with the description of the attack and the damage dealt to the hero is returned.  Otherwise, no damage is dealt and a string with the description of the failure is returned.'''
    if self._fire_shots > 0:
      damage = random.randint(5, 9)
      hero.take_damage(damage)
      # Decrements fire shots when dragon uses it
      self._fire_shots -= 1
      return f'{self._name} engulfs you in flames for {damage} damage!'
    else:
      return f"{self._name} doesn't have any shots left, you take 0 damage!"

  def __str__(self):
    '''use super to get the __str__ from the entity class, then concatenate on the 
number of fire_shots. '''
    return super().__str__() + '\n   Fire Shots remaining: ' + str(self._fire_shots)