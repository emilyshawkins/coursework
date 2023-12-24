import monster

class Alien(monster.Monster):
  '''
  Represents an Alien Monster

  Attributes:
  name(str): The name of the Alien
  hp(int): hp of the Alien
  '''
  def __init__(self):
    super().__init__('Alien', 100)

  def attack(self):
    '''return the attack power of the alien'''
    return 100

    

  