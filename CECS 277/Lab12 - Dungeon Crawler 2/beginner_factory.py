import random
import enemy_factory
import easy_troll
import easy_ogre
import easy_goblin

class BeginnerFactory(enemy_factory.EnemyFactory):
  '''
  A factory for beginner enemies.
  '''
  def create_random_enemy(self):
    '''Creates a random beginner enemy.'''
    enemy = random.randint(1, 3)
    if enemy == 1:
      monster = easy_troll.EasyTroll()
    elif enemy == 2:
      monster = easy_ogre.EasyOgre()
    else:
      monster = easy_goblin.EasyGoblin()
    return monster