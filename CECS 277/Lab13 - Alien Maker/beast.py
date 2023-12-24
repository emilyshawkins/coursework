import monster

class Beast(monster.Monster):
  '''
  Represents an Beast Monster
   
  Attributes:
  name(str): The name of the Beast
  hp(int): hp of the beast
  '''
  
  def __init__(self):
    super().__init__('Beast', 50)

  def attack(self):
    '''return the attack power of the alien'''
    return 30

    

  