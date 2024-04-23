import entity
import random


class BegGoblin(entity.Entity):
  """Class representing a beginner-level Goblin enemy.
  Attributes:
  _name
  _hp
  
  melee_attack: does a random amount of damage ranging from 4-6 """

  def __init__(self):
    super().__init__("Goblin", random.randint(7, 9))

  def melee_attack(self, enemy):
    damage = random.randint(4, 6)
    enemy.take_damage(damage)
    return f"{self._name} hits {enemy._name} with a club for {damage} damage."
