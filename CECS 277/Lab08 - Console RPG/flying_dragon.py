from dragon import Dragon
import random

class FlyingDragon(Dragon):
  '''
  Represents a flying dragon

  Attributes:
  name (str): The name of the flying dragon
  hp (int): The hit points of the flying dragon
  max_hp (int): The maximum hit points of the flying dragon
  swoops (int): Number of swoops attacks left
  '''
  def __init__(self, name, max_hp, swoops):
    super().__init__(name, max_hp)
    self._swoops = swoops

  def special_attack(self, hero):
    '''The hero takes a random amount of damage in the range 5 to 8'''
    if self._swoops > 0:
      damage = random.randint(5, 8)
      hero.take_damage(damage)
      # Decrements swoops when the dragon uses it
      self._swoops -= 1
      return f'{self._name} swoops and cuts you for {damage} damage!'
    else:
      return f"{self._name} cannot swoop anymore, you take 0 damage!"

  def __str__(self):
    '''Returns the dragon's name, hp, max hp, and the number of swoops the dragon has left'''
    return super().__str__() + '\n   Swoop attacks remaining: ' + str(self._swoops)