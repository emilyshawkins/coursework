import decorator

class Lasers(decorator.Decorator):
  '''
  A monster decorator.

  Attributes:
  monster (Monster): The monster to be decorated
  '''
  def __init__(self, monst):
    monst.name = monst.name + ' with Lasers'
    monst.hp += 500
    super().__init__(monst)

  def attack(self):
    '''Returns attack power with additional poison attack power.'''
    return super().attack() + 1000
    