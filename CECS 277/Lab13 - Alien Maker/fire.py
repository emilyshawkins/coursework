import decorator

class Fire(decorator.Decorator):
  '''
  A Monster fire decorator
  
  Attributes:
  name(str): Monsters name with the added fire ability
  hp(int): Monsters new hp with added hp from fire ability
  monst(Monster): The monster to be decorated
  '''
  def __init__(self, monst):
    monst.name = 'Firey ' + monst.name
    monst.hp += 50
    super().__init__(monst)

  def attack(self):
    '''returns the new hp of the Monster'''
    return super().attack() + 30
    