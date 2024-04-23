import entity
import random


class BegTroll(entity.Entity):
  """Class representing a beginner-level Troll enemy."""

  def __init__(self):
    """Initialize the Troll with default values."""
    super().__init__("Troll", random.randint(8, 10))  # Easy HP: 8-10

  def melee_attack(self, enemy):
    """Perform a melee attack on the given enemy."""
    damage = random.randint(5, 9)  # Easy Dmg: 5-9
    enemy.take_damage(damage)
    return f"Troll bashes {enemy._name} for {damage} damage."
