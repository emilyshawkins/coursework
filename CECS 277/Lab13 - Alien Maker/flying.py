import decorator

class Flying(decorator.Decorator):
  '''
  A Monster flying decorator
  
  Attributes:
  name(str): Monsters name with the added flying ability
  hp(int): Monsters new hp with added hp from flying  ability
  monst(Monster): The monster to be decorated
  '''
  def __init__(self, monst):
    monst.name = 'Flying ' + monst.name
    monst.hp += 20
    super().__init__(monst)

  def attack(self):
    '''returns the new hp of the Monster'''
    return super().attack() + 10
    