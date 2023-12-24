class Rectangle:
  '''
  Represents a rectangle on a grid.
  
  Attributes:
  x (int) : x coordinate of top left corner of rectangle
  y (int) : y coordinate of top left corner of rectangle
  width (int) : width of rectangle
  height (int) : height of rectangle
  '''

  def __init__(self, w, h):
    self.w = w
    self.h = h
    self.x = 0
    self.y = 0

  def get_coords(self):
    """returns the x and y values as a pair"""
    return (self.x, self.y)

  def get_width(self):
    """return the rectangle's width """
    return self.w

  def get_height(self):
    """returns the rectangle's height"""
    return self.h

  def move_up(self):
    """Moves the rectangle up one row"""
    if self.y - 1 < 0: #Check if rectangle is at top grid edge
      print('Cannot move up!')
    else:
      self.y =  self.y - 1
      
  def move_down(self):
    """moves the rectangle down one row"""
    if self.y + self.h + 1 > 20: #Check if rectangle is at bottom grid edge
      print('Cannot move down!')
    else: 
      self.y = self.y + 1

  def move_left(self):
    """moves the rectangle left one column"""
    if self.x - 1 < 0: #Check if rectangle is at left grid edge
      print('Cannot move left!')
    else:
      self.x = self.x - 1

  def move_right(self):
    """moves the rectangle right one column"""
    if self.x + self.w + 1 > 20: #Check if rectangle is at right grid edge
      print('Cannot move right!')      
    else:
      self.x = self.x + 1

  