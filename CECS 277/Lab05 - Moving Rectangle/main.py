# Megan Waples and Emily Hawkins
# Fall 2022
# Allows user to move a rectangle around a grid

import rectangle
import check_input

def display_grid(grid):
  ''' Displays a 20 x 20 grid of dots.'''
  
  print()
  for row in grid:
    for column in row:
      print(column, end= ' ')
    print()  

def reset_grid(grid):
  '''Resets the grid to an empty one.'''
  
  grid = []
  for i in range(20):
    line = []
    for j in range(20):
      line.append('.')
    grid.append(line)
  return grid

def place_rect(grid, rect):
  '''Places the rectangle, created with the user's dimensions, onto the grid'''

  #place rectangle according to the coordinate which is the top left point of the rectangle
  coord = rect.get_coords()
  x = coord[0]
  y = coord[1]
  
  for i in range(rect.get_height()):
    for j in range(rect.get_width()):
      grid[i + y][j + x] = '*'
  
def main():

  #get inputs and create a rectangle with them
  user_width = check_input.get_int_range('Enter rectangle width (1-5): ', 1, 5)
  user_height = check_input.get_int_range('Enter rectangle height (1-5): ', 1, 5)
  
  rect = rectangle.Rectangle(user_width, user_height)

  #create an empty grid and place the rectangle at the top left corner starting point
  grid = []
  
  for i in range(20):
    line = []
    for j in range(20):
      line.append('.')
    grid.append(line)

  place_rect(grid, rect)
  display_grid(grid)

  #Ask user to move the rectangle or quit
  user_input = check_input.get_int_range('\nEnter Direction:\n1. Up\n2. Down\n3. Left\n4. Right\n5. Quit\n', 1, 5)
  place_rect(grid, rect)

  while user_input != 5:

    if user_input == 1:
      rect.move_up()
    elif user_input == 2:
      rect.move_down()
    elif user_input == 3:
      rect.move_left()
    elif user_input == 4:
      rect.move_right()
    elif user_input == 5:
      break

    #reset grid and place rectangle according to the new coordinates that the user moved
    new_grid = reset_grid(grid)
    place_rect(new_grid, rect)
    display_grid(new_grid)
    user_input = check_input.get_int_range('\nEnter Direction:\n1. Up\n2. Down\n3. Left\n4. Right\n5. Quit\n', 1, 5)

main()


