from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    creature = factory.create_base()
    print(creature.describe())
    print(creature.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def battle(factory_1: CreatureFactory, factory_2: CreatureFactory) -> None:
    print("Testing battle")
    creature_1 = factory_1.create_base()
    print(creature_1.describe())
    print("vs.")
    creature_2 = factory_2.create_base()
    print(creature_2.describe())
    print("fight!")
    print(creature_1.attack())
    print(creature_2.attack())


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    test_factory(flame)
    print()
    test_factory(aqua)
    print()
    battle(flame, aqua)
