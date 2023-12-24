import abc

class EnemyFactory(abc.ABC):
  '''
  A factory to make enemies.
  '''
  @abc.abstractmethod
  def create_random_enemy(self):
    '''Creates a random enemy.'''
    pass