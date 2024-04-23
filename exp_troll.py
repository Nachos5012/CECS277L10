import entity
import random


class ExpTroll(entity.Entity):
  """Class representing an expert-level Troll enemy."""

  def __init__(self):
    """Initialize the Horrible Troll with default values."""
    super().__init__("Horrible Troll",
                     random.randint(15, 18))  # Difficult HP: 15-18

  def melee_attack(self, enemy):
    """Perform a melee attack on the given enemy."""
    damage = random.randint(8, 12)  # Difficult Dmg: 8-12
    enemy.take_damage(damage)
    return f"Horrible Troll crushes {enemy._name} for {damage} damage."
