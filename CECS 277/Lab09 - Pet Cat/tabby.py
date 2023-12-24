import cat
import random
class Tabby(cat.Cat):
  '''Represents a tabby cat
  
  Attributes
  name (str): Is the name the tabby
  hunger (int): Is how full the tabby's hunger bar is
  '''

  def feed(self, player):
    '''Feeds cat based on hunger level, gives player random damage, and uses if statements to build a string representing feeding the cat based on the state of the cat’s hunger level.'''

    dmg_hungry = random.randint(2, 5)
    dmg_nhungry = random.randint(1, 3)
    
    if self.hunger <= 2:
      self.update_hunger(5)
      player.take_damage(dmg_hungry)
      return f'{self.name} is so hungry that when you set down the bowl of food, {self.name} attacks and bites you for {dmg_hungry} damage because you did not feed it earlier.'
      
    elif self.hunger <= 5:
      self.update_hunger(3)
      player.take_damage(dmg_hungry)
      return f'{self.name} is pretty hungry and accidentally bites you when it takes the steak from your hand.'
      
    elif self.hunger <= 8:
      self.update_hunger(2)
      player.take_damage(dmg_nhungry)
      return f'{self.name} is not really hungry but the steak looks really tempting, so {self.name} accepts it but accidently scratches you when it grabs the steak.'
    else:
      player.take_damage(dmg_nhungry)
      self.update_hunger(-1)
      return f'You dangle a piece of meat in front of {self.name} but {self.name} is not hungry and smacks you.'

  def play(self, player):
    '''Decrements hunger, gives the player random damage, and use if statements to build a string representing playing with the cat 
based on the state of the cat’s hunger level.'''

    dmg_hungry = random.randint(2, 5)
    dmg_nhungry = random.randint(1, 3)
    
    if self.hunger <= 2:
      self.update_hunger(-1)
      player.take_damage(dmg_hungry)
      return f'{self.name} is starving, they do not want to play right now. {self.name} hisses loudly at you and scratches you for {dmg_hungry} damage.'
      
    elif self.hunger <= 5:
      self.update_hunger(-1)
      player.take_damage(dmg_hungry)
      return f'{self.name} sniffs the cat toy you have and then bites you for {dmg_hungry} damage because it thought you would give it food but you didn\'t.'
      
    elif self.hunger <= 8:
      self.update_hunger(-3)
      player.take_damage(dmg_nhungry)
      return f'{self.name} jumps and plays with the fuzzy cat toy you hold but accidentally scratches you when it tries to climb your leg'
      
    else:
      self.update_hunger(-1)
      return f'{self.name} is so full, when try to get its attention with a mouse toy, it lays there sleepily in near the window.'

  def pet(self, player):
    '''Decrement hunger, give random damage to player, and uses if statements to build a string representing petting the cat based on the state of the cat’s hunger level.'''

    dmg_hungry = random.randint(2, 5)
    dmg_nhungry = random.randint(1, 3)
    
    if self.hunger <= 2:
      self.update_hunger(-1)
      player.take_damage(dmg_hungry)
      return f'You try to pet {self.name}, but they are starving so they turn their head and chomp down on you fingers for {dmg_hungry} damage.'
      
    elif self.hunger <= 5:
      self.update_hunger(-2)
      player.take_damage(dmg_hungry)
      return f'{self.name} is a bit hungry and sniffs your hand as you reach to pet them and decides to swat your hand but accidentally scratches you for {dmg_hungry} damage.'
      
    elif self.hunger <= 8:
      self.update_hunger(-1)
      return f'{self.name} happily allows you to pet them, flipping so you can give them tummy rubs.'
      
    else:
      self.update_hunger(-1)
      return f'{self.name} is incredibly full and purrs happily as they drift off to sleep.'