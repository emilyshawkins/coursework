import cat
import random
class Ocelot(cat.Cat):
  '''Represents an ocelot
  
  Attributes
  name (str): Is the name the ocelot
  hunger (int): Is how full the ocelot's hunger bar is
  '''
  def feed(self, player):
    '''Feeds cat based on hunger level, gives player random damage, and uses if statements to build a string representing feeding the cat based on the state of the cat’s hunger level.'''

    dmg_hungry = random.randint(3, 6)
    dmg_nhungry = random.randint(2, 4)
    
    if self.hunger <= 2:
      self.update_hunger(5)
      player.take_damage(dmg_hungry)
      return f'{self.name} is so hungry that when you set down the meat, {self.name} is so ecstatic it pounces on you, causing you to fall and get hurt for {dmg_hungry} damage.'
      
    elif self.hunger <= 5:
      self.update_hunger(3)
      player.take_damage(dmg_hungry)
      return f'{self.name} is pretty hungry and accidentally bites your hand when you feed it.'
      
    elif self.hunger <= 8:
      self.update_hunger(2)
      player.take_damage(dmg_nhungry)
      return f'{self.name} is not really hungry but the steak looks really delicious, so {self.name} takes it but accidently scratches you with its claws.'
    else:
      self.update_hunger(-1)
      return f'You dangle a piece of meat in front of {self.name} and they look at it but {self.name} is not hungry and puts it head back down.'

  def play(self, player):
    '''Decrements hunger, gives the player random damage, and use if statements to build a string representing playing with the cat 
based on the state of the cat’s hunger level.'''

    dmg_hungry = random.randint(3, 6)
    dmg_nhungry = random.randint(2, 4)
    
    if self.hunger <= 2:
      self.update_hunger(-2)
      player.take_damage(dmg_hungry)
      return f'{self.name} is starving, they do not want to play right now. {self.name} stares at you intently, narrowing its eyes, then jumps at you, tackling you for {dmg_hungry} damage.'
      
    elif self.hunger <= 5:
      self.update_hunger(-2)
      player.take_damage(dmg_hungry)
      return f'{self.name} looks the ball you have and then decides that you should be feeding it instead so {self.name} bites you for {dmg_hungry} damage because you are not feeding it.'
      
    elif self.hunger <= 8:
      self.update_hunger(-3)
      player.take_damage(dmg_nhungry)
      return f'{self.name} accidentally tackles you when you raise the cat toy a bit too high up.'
      
    else:
      self.update_hunger(-3)
      return f'{self.name} runs toward the ball that you threw and comes back excited and panting for another round of fetch.'

  def pet(self, player):
    '''Decrement hunger, give random damage to player, and uses if statements to build a string representing petting the cat based on the state of the cat’s hunger level'''

    dmg_hungry = random.randint(3, 6)
    dmg_nhungry = random.randint(2, 4)
    
    if self.hunger <= 2:
      self.update_hunger(-2)
      player.take_damage(dmg_hungry)
      return f'You try to pet {self.name}, but they are starving so they growl loudly at your hand and bites it for {dmg_hungry} damage.'
      
    elif self.hunger <= 5:
      self.update_hunger(-2)
      player.take_damage(dmg_hungry)
      return f'{self.name} is a bit hungry and sniffs your hand as you reach to pet them and decides to chew on your hand for {dmg_hungry} damage.'
      
    elif self.hunger <= 8:
      self.update_hunger(-2)
      player.take_damage(dmg_nhungry)
      return f'{self.name} happily allows you to pet them but accidentally swats your hand a bit too hard as you pet them.'
      
    else:
      self.update_hunger(-2)
      return f'{self.name} is incredibly full and purrs loudly when you give them pats.'