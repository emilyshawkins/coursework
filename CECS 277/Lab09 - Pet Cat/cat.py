import abc
class Cat(abc.ABC):
  '''Represents a cat
  
  Attributes
  name (str): Is the name the cat
  hunger (int): Is how full the cat's hunger bar is
  '''
  def __init__(self, name):
    self._name = name
    self._hunger = 5

  @property
  def name(self):
    '''gets the name value'''
    return self._name

  @property
  def hunger(self):
    '''gets the hunger value'''
    return self._hunger

  def update_hunger(self, val):
    '''value will be a positive or negative value that is added to the cat’s _hunger attribute.  Make sure that the value of _hunger never leaves the range of 1-10. '''
    self._hunger = self._hunger + val
    if self._hunger < 1:
      self._hunger = 1
    elif self._hunger > 10:
      self._hunger = 10

  def __str__(self):
    '''return a string with the cat’s name and then the cat’s hunger level as a bar graph that clearly shows whether the cat is hungry or full. '''
    plus_hunger = '+ '
    minus_hunger = '- '
    return f'{self._name}:\nStarving           Full\n| {plus_hunger * self._hunger}{minus_hunger * (10 -self._hunger)}|'

  #Create three abstract methods for feed, play, and pet
  @abc.abstractmethod
  def feed():
    pass
    
  @abc.abstractmethod
  def play():
    pass

  @abc.abstractmethod    
  def pet():
    pass