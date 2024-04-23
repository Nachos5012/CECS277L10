import entity
import random


class Hero(entity.Entity):
  """Class representing the hero character."""

  def __init__(self, name):
    """Initialize the hero with a name and default hit points (hp)."""
    super().__init__(name, 25)

  def melee_attack(self, enemy):
    """Perform a melee attack on the given enemy."""
    damage = random.randint(1, 6) + random.randint(1, 6)
    # 2D6 damage
    enemy.take_damage(damage)
    return f"{self._name} slashes {enemy._name} with a sword for {damage} damage."

  def ranged_attack(self, enemy):
    """Perform a ranged attack on the given enemy."""
    damage = random.randint(1, 12)  # 1D12 damage
    enemy.take_damage(damage)
    return f"{self._name} pierces {enemy._name} with an arrow for {damage} damage."
