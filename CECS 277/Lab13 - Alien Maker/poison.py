import decorator

class Poison(decorator.Decorator):
  '''
  A monster decorator.

  Attributes:
  name (str): The name of the Monster
  hp (int): The hp of the Monster
  monster (Monster): The monster to be decorated
  '''
  def __init__(self, monst):
    monst.name = 'Poison ' + monst.name
    monst.hp = monst.hp + 30
    super().__init__(monst)

  def attack(self):
    '''Returns attack power with additional poison attack power.'''
    return super().attack() + 15
    