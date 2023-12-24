import random
import enemy_factory
import troll
import ogre
import goblin

class ExpertFactory(enemy_factory.EnemyFactory):
  '''A factory for expert enemies.'''
  def create_random_enemy(self):
    '''Creates random expert enemies.'''
    enemy = random.randint(1, 3)
    if enemy == 1:
      monster = troll.Troll()
    elif enemy == 2:
      monster = ogre.Ogre()
    else:
      monster = goblin.Goblin()
    return monster