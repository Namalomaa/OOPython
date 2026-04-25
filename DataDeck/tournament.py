from ex0 import FlameFactory, AquaFactory
from ex0.factories import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (BattleStrategy, NormalStrategy, DefensiveStrategy,
                 AggressiveStrategy, StrategyError)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    for opponent in opponents:
        factory, strategy = opponent
        creature = factory.create_base()
        print("--- Turn ---")
        print(creature.describe())
        try:
            strategy.act(creature)
        except StrategyError as e:
            print(f"Strategy failed: {e}")


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggressive = AggressiveStrategy()

    fighters = [(flame, normal),
                (heal, defensive),
                (transform, aggressive),
                (aqua, aggressive)
                ]
    battle(fighters)
