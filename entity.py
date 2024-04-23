import abc


class Entity(abc.ABC):
  """Abstract class representing entities in the game."""

  def __init__(self, name, hp):
    """Initialize the entity with a name and hit points (hp)."""
    self._name = name
    self._hp = hp

  def name(self):
    """Get the name of the entity."""
    return self._name

  def hp(self):
    """Get the hit points (hp) of the entity."""
    return self._hp

  #def melee_attack(self, enemy):
  #  """Perform a melee attack on the given enemy."""
  #  pass

  def take_damage(self, dmg):
    """Take damage by subtracting it from hit points (hp).
    Args:
        dmg (int): The amount of damage to take.
    """
    self._hp -= dmg
    if self._hp < 0:
      self._hp = 0

  def __str__(self):
    """String representation of the entity, displaying its name and hit points (hp)."""
    return f"{self._name} HP: {self._hp}"

  @abc.abstractmethod
  def melee_attack(self, enemy):
    pass
