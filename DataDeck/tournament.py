from ex0 import FlameFactory, AquaFactory
from ex0.factories import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (BattleStrategy, NormalStrategy, DefensiveStrategy,
                 AggressiveStrategy, StrategyError)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponennts involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            fighter1 = opponents[i]
            fighter2 = opponents[j]

            fact1, strat1 = fighter1
            fact2, strat2 = fighter2

            creature1 = fact1.create_base()
            creature2 = fact2.create_base()

            print()
            print("* Battle *")
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")

            try:
                strat1.act(creature1)
                strat2.act(creature2)
            except StrategyError as e:
                print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggressive = AggressiveStrategy()

    print("Tournament 0 (basic)")
    trnm1 = [(flame, normal), (heal, defensive)]
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle(trnm1)
    print()

    print("Tournament 1 (error)")
    trnm2 = [(flame, aggressive), (heal, defensive)]
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(trnm2)
    print()

    print("Tournament 2 (multiple)")
    trnm3 = [(aqua, normal), (heal, defensive), (transform, aggressive)]
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(trnm3)
