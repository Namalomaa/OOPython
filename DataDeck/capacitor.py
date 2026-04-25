from ex0 import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_factory(factory: CreatureFactory) -> None:
    creature = factory.create_base()
    evolved = factory.create_evolved()
    if (isinstance(creature, HealCapability) and
            isinstance(evolved, HealCapability)):
        print("Testing Creature with healing capability")
        print("base:")
        print(creature.describe())
        print(creature.attack())
        print(creature.heal())
        print("evolved:")
        print(evolved.describe())
        print(evolved.attack())
        print(evolved.heal())

    elif (isinstance(creature, TransformCapability) and
          isinstance(evolved, TransformCapability)):
        print("Testing Creature with transform capability")
        print("base:")
        print(creature.describe())
        print(creature.attack())
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
        print("evolved:")
        print(evolved.describe())
        print(evolved.attack())
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    test_factory(healing_factory)
    print()
    test_factory(transform_factory)
