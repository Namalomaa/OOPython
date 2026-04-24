from abc import ABC, abstractmethod
from .creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base():
        pass

    @abstractmethod
    def create_evolved():
        pass


class FlameFactory(CreatureFactory):
    def create_base():
        pass

    def create_evolved():
        pass


class AquaFactory(CreatureFactory):
    def create_base():
        pass

    def create_evolved():
        pass
