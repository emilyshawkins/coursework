
import monster

class Decorator(monster.Monster):
  '''
  A monster decorator
  
  Attributes:
  name (str): The name of the Monster
  hp (int): The hp of the Monster
  monster (Monster): The monster to be decorated
  '''
  def __init__(self, monst):
    super().__init__(monst.name, monst.hp)
    self._monster = monst

  def attack(self):
    '''Returns the attack power of the monster'''
    return self._monster.attack()