from .capabilities import HealCapability, TransformCapability
from ex0.creatures import Creature


class Sproutling(Creature, HealCapability):

    def __init__(self) -> None:
        Creature.__init__(self, "Sproutling", "Grass")
        HealCapability.__init__(self)

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):

    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")
        HealCapability.__init__(self)

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):

    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self) -> str:
        if not self.transformed:
            self.transformed = True
            return "Shiftling shifts into a sharper form!"
        else:
            return "Shiftling is already transformed."

    def revert(self) -> str:
        if self.transformed:
            self.transformed = False
            return "Shiftling returns to normal."
        else:
            return "Shiftling is already in its normal form."


class Morphagon(Creature, TransformCapability):

    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."

    def transform(self) -> str:
        if not self.transformed:
            self.transformed = True
            return "Morphagon morphs into a dragonic battle form!"
        else:
            return "Morphagon is already transformed."

    def revert(self) -> str:
        if self.transformed:
            self.transformed = False
            return "Morphagon stabilizes its form."
        else:
            return "Morphagon is already in its normal form."
