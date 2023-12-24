
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

      self._map = self.load_map(1)
        
      self._revealed = None
      
      Map._initialized = True

  def __getitem__(self, row):
    '''Returns the row of the map, provided the index.'''
    return self._map[row]

  def __len__(self):
    '''Returns the number of rows in the map.'''
    return len(self._map)

  def load_map(self, map_num):
    '''Passes in an integer for the map numer and fills in the 2D map list from the file and resets the 2D revealed list with all False values.'''
    if map_num == 1:
      game_map = 'map1.txt'
    elif map_num == 2:
      game_map = 'map2.txt'
    else:
      game_map = 'map3.txt'

    dungeon = open(game_map)

    # Creates a 2D list of the game map 
    self._map = []
    for row in dungeon:
      dungeon_list = []
      for item in row:
        if item != ' ' and item != '\n':
          dungeon_list.append(item)
      self._map.append(dungeon_list)

    # Creates a 2D list of booleans
      self._revealed = []
      for i in range(len(self._map)):
        reveal = []
        for j in range(len(self._map[i])):
          reveal.append(False)
        self._revealed.append(reveal)    

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