import random

class Die():
  '''
  Represents a die.
  
  Attributes:
  sides (int) : Number of sides for the die
  value (int) : Number on a side rolled by the die
  '''
  
  def __init__(self, sides = 6):
    
    self.sides = sides
    self.value = 0
    
  def roll(self):
    '''Generates a random number between 1 and the number of sides, which is set as the die's value and returned.'''

    # Generates a random value for the die
    ran_int = random.randint(1, self.sides) 
    self.value = ran_int
    
    return self.value

  def __str__(self):
    '''Returns the die’s value as a string.'''
    
    return f'{self.value}'

  def __lt__(self, other):
    '''Returns true if the value of a die is less than the other.'''

    if self.value < other.value:
      return True
    else:
      return False

  def __eq__(self, other):
    '''Returns true if the values of two die are equal.'''
    
    if self.value == other.value:
      return True
    else:
      return False

  def __sub__(self, other):
    '''Returns the difference between the values of two die. '''
    
    return self.value - other.value
    