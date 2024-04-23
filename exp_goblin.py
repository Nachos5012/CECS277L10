import entity
import random


class ExpGoblin(entity.Entity):
  """Class representing an expert-level Goblin enemy."""

  def __init__(self):
    """Initialize the Angry Goblin with default values."""
    super().__init__("Angry Goblin", random.randint(12, 15))

  def melee_attack(self, enemy):
    """Perform a melee attack on the given enemy."""

    damage = random.randint(5, 8)
    enemy.take_damage(damage)
    return f"Angry Goblin slashes {enemy._name} for {damage} damage."
