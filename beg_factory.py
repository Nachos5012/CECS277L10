import enemy_factory
import beg_goblin
import beg_troll
import random

class BeginnerFactory(enemy_factory.EnemyFactory):
  """Factory class for creating beginner enemies."""

  def create_random_enemy(self):
    if random.random() < 0.5:
      return beg_goblin.BegGoblin()
    else:
      return beg_troll.BegTroll()
