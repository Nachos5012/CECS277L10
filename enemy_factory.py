import abc

class EnemyFactory(abc.ABC):
  """Abstract class representing an enemy factory."""

  @abc.abstractmethod
  def create_random_enemy(self):
    """Create a random enemy. """
    pass
