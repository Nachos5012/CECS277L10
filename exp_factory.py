import enemy_factory
import exp_goblin
import exp_troll
import random


class ExpertFactory(enemy_factory.EnemyFactory):
  """Represents a factory to create expert-level enemies."""

  def create_random_enemy(self):
    if random.random() < 0.5:
      return exp_goblin.ExpGoblin()
    else:
      return exp_troll.ExpTroll()
