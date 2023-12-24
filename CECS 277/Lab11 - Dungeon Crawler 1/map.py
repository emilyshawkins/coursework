
class Map:
  '''
  Represents a dungeon maze map.

  Attributes:
  map (char [][]): A 2D list of all the encounters in the form of single characters in the dungeon maze map.
  revealed (boolean [][]): A 2D list of booleans to determine if characters in the map are revealed or not.
  '''
  _instance = None
  _initialized = False

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self):
    if not Map._initialized:
      dungeon = open('map.txt')
      # Creates a 2D list of the game map 
      dungeon_2list = []
      for row in dungeon:
        dungeon_1list = []
        for item in row:
          if item != ' ' and item != '\n':
            dungeon_1list.append(item)
        dungeon_2list.append(dungeon_1list)
          
      self._map = dungeon_2list

      # Creates a 2D list of booleans
      reveal_2 = []
      for i in range(len(self._map)):
        reveal_1 = []
        for j in range(len(self._map[i])):
          reveal_1.append(False)
        reveal_2.append(reveal_1)
        
      self._revealed = reveal_2
      
      Map._initialized = True

  def __getitem__(self, row):
    '''Returns the row of the map, provided the index.'''
    return self._map[row]

  def __len__(self):
    '''Returns the number of rows in the map.'''
    return len(self._map)

  def show_map(self, loc):
    '''Returns the map as a string where revealed locations are from the map and unrevealed locations are x's.'''
    map_str = ''
    for row in range(0, len(self._map)):
        for column in range(0, len(self._map[row])):
            # If its the hero's location, concatenate a *
            if loc[0] == row and loc[1] == column:
              map_str += '* '
              self._revealed[row][column] = True
            # If the location has been visited, concatenate the letter from the map
            elif self._revealed[row][column]:
              map_str += f'{self._map[row][column]} '
            # Concatenate x if the location has not been visited
            else:
              map_str += 'x '
        map_str += '\n'
    return map_str

  def reveal(self, loc):
    '''Sets values in the 2D revealed list at the specific location to true.'''
    self._revealed[loc[0]][loc[1]] = True

  def remove_at_loc(self, loc):
    '''Overwrites the character in the map list at a specified location with an n'''
    self._map[loc[0]][loc[1]] = 'n'