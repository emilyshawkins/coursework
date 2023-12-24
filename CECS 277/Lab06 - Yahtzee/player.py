import die

class Player:
  '''
  Represents a Yahtzee player.
  
  Attributes:
  dice (list) : A list of three die objects
  points (int) : The player's score in the game
  '''
  def __init__(self):
    
    self.dice = [die.Die(), die.Die(), die.Die()]
    self.points = 0

  def get_points(self):
    '''Returns the player’s points. '''
    
    return self.points

  def roll_dice(self):
    '''Rolls each of the die and sorts the list of dice. '''
    
    for i in self.dice:
      i.roll()
    #Sort dice least to greatest
    for j in range(len(self.dice) - 1):
      for k in range(1, len(self.dice)):
        if self.dice[j] > self.dice[k]:
          temp = self.dice[k]
          self.dice[k] = self.dice[j]
          self.dice[j] = temp

  def has_pair(self):
    '''Returns true if two dice in the list have the same value and adds 1 to the player's points.'''
    
    if (self.dice[0] == self.dice[1] or self.dice[1] == self.dice[2]) and self.dice[0] != self.dice[2]:
        self.points += 1
        return True

  def has_three_of_kind(self):
    '''Returns true if all three dice in the list have the same value and adds 3 to the player's points. '''
    
    if self.dice[0] == self.dice[1] == self.dice[2]:
      self.points += 3
      return True

  def has_series(self):
    '''Returns true if the values of each of the dice in the list are in a sequence and adds 2 to the player's points.'''
    
    if self.dice[2] - self.dice[1] == 1 and self.dice[1] - self.dice[0] == 1:
      self.points += 2
      return True

  def __str__(self):
    '''Formats and returns a string of the three dice values.'''

    return f'\nD1 = {self.dice[0]}, D2 = {self.dice[1]}, D3 = {self.dice[2]}'
