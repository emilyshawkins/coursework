from entity import Entity
import random

class Dragon(Entity):

  def basic_attack(self, hero):
    '''– tail attack – the hero takes a random amount of damage in the 
range 3-7.  Return a string with the description of the attack and the damage dealt to the hero. '''
    damage = random.randint(3, 7)
    hero.take_damage(damage)

    return f'{self._name} smashes you with its tail for {damage} damage!'

  def special_attack(self, hero):
    '''– claw attack – the hero takes a random amount of damage in 
the range 4-8.  Return a string with the description of the attack and the damage dealt to the hero.  '''
    damage = random.randint(4, 8)
    hero.take_damage(damage)

    return f'{self._name} slashes you with its claw for {damage} damage!'