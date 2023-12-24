import monster

class Undead(monster.Monster):
  '''
  Represents an undead monster.

  Attributes:
  name (str): The name of the Undead
  hp (int): The hp of the Undead
  '''
  def __init__(self):
    super().__init__('Undead', 70)

  def attack(self):
    '''Returns the attack power of the Undead'''
    return 5000

    

  