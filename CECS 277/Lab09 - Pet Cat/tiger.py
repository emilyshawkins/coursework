import cat
import random
class Tiger(cat.Cat):
  '''Represents a tiger
  
  Attributes
  name (str): Is the name the tiger
  hunger (int): Is how full the tiger's hunger bar is
  '''

  def feed(self, player):
    '''Feeds cat based on hunger level, gives player random damage, and uses if statements to build a string representing feeding the cat based on the state of the cat’s hunger level.'''

    dmg_hungry = random.randint(5, 7)
    dmg_nhungry = random.randint(3, 5)
    
    if self.hunger <= 2:
      self.update_hunger(5)
      player.take_damage(dmg_hungry)
      return f'{self.name} is so hungry that when you set down the steak, {self.name} mistakes you for food and bites you for {dmg_hungry} damage.'
      
    elif self.hunger <= 5:
      self.update_hunger(3)
      player.take_damage(dmg_hungry)
      return f'{self.name} is pretty hungry and accidentally bites you when it takes the steak from your hand.'
      
    elif self.hunger <= 8:
      self.update_hunger(2)
      player.take_damage(dmg_nhungry)
      return f'{self.name} is not really hungry but the steak looks really tempting, so {self.name} accepts it but accidently nips your hand.'
    else:
      player.take_damage(dmg_nhungry)
      self.update_hunger(-1)
      return f'You dangle a piece of meat in front of {self.name} but {self.name} is not hungry and smacks you.'

  def play(self, player):
    '''Decrements hunger, gives the player random damage, and use if statements to build a string representing playing with the cat 
based on the state of the cat’s hunger level.'''

    dmg_hungry = random.randint(5, 7)
    dmg_nhungry = random.randint(3, 5)
    
    if self.hunger <= 2:
      self.update_hunger(-3)
      player.take_damage(dmg_hungry)
      return f'{self.name} is starving, they do not want to play right now. {self.name} stalks you, chases you down, tackles you, and takes a large chunk out of your arm for {dmg_hungry} damage.'
      
    elif self.hunger <= 5:
      self.update_hunger(-2)
      player.take_damage(dmg_hungry)
      return f'{self.name} sniffs the basketball you have and then decides that you might be delicious. {self.name} bites you for {dmg_hungry} damage.'
      
    elif self.hunger <= 8:
      self.update_hunger(-3)
      player.take_damage(dmg_nhungry)
      return f'{self.name} jumps and plays with the soccer ball you threw, then accidentally tackles you when it comes running back.'
      
    else:
      self.update_hunger(-1)
      return f'{self.name} is so full, when your throw the ball, it lays there sleepily in the sun.'

  def pet(self, player):
    '''Decrement hunger, give random damage to player, and uses if statements to build a string representing petting the cat based on the state of the cat’s hunger level.'''

    dmg_hungry = random.randint(5, 7)
    
    if self.hunger <= 2:
      self.update_hunger(-2)
      player.take_damage(dmg_hungry)
      return f'You try to pet {self.name}, but they are starving so they turn their head and sinks its fangs into your arm for {dmg_hungry} damage.'
      
    elif self.hunger <= 5:
      self.update_hunger(-2)
      player.take_damage(dmg_hungry)
      return f'{self.name} is a bit hungry and sniffs your hand as you reach to pet them and decides to swipe its claws at you for {dmg_hungry}.'
      
    elif self.hunger <= 8:
      self.update_hunger(-1)
      return f'{self.name} happily allows you to pet them.'
      
    else:
      self.update_hunger(-1)
      return f'{self.name} is incredibly full and purrs happily as they drift off to sleep.'