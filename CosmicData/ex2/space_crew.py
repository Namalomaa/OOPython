from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime
from typing import Self


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validation(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("mission_id must start with 'M'")

        has_leader = False
        for member in self.crew:
            if member.rank in [Rank.COMMANDER, Rank.CAPTAIN]:
                has_leader = True
                break
        if not has_leader:
            raise ValueError("Mission must have at least one "
                             "commander or captain")

        if self.duration_days > 365:
            experienced_count = sum(
                1 for m in self.crew if m.years_experience >= 5
            )
            if experienced_count < (len(self.crew) / 2):
                raise ValueError("Long missions (> 365 days) needs 50% "
                                 "experienced crew (+5 years)")

        for c in self.crew:
            if not c.is_active:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        commander = CrewMember(
            member_id="C001",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=45,
            specialization="Mission Command",
            years_experience=15
        )
        lieutenant = CrewMember(
            member_id="L001",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=35,
            specialization="Navigation",
            years_experience=8
        )
        officer = CrewMember(
            member_id="O001",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=28,
            specialization="Engineering",
            years_experience=3
        )

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-08-15T00:00:00",
            duration_days=900,
            crew=[commander, lieutenant, officer],
            budget_millions=2500.0
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for c in mission.crew:
            print(f"- {c.name} ({c.rank.value}) - {c.specialization}")

    except ValidationError as e:
        print(f"Unexpected Error: {e}")
        return

    print("\n=========================================")
    print("Expected validation error:")

    try:
        invalid_mission = SpaceMission(
            mission_id="M2024_MOON",
            mission_name="Lunar Outpost",
            destination="Moon",
            launch_date="2024-09-01T00:00:00",
            duration_days=30,
            crew=[lieutenant, officer],
            budget_millions=500.0
        )
        print(f"Mission: {invalid_mission.mission_name}")
        print(f"ID: {invalid_mission.mission_id}")
        print(f"Destination: {invalid_mission.destination}")
        print(f"Duration: {invalid_mission.duration_days} days")
        print(f"Budget: ${invalid_mission.budget_millions}M")
        print(f"Crew size: {len(invalid_mission.crew)}")
        print("Crew members:")
        for c in invalid_mission.crew:
            print(f"- {c.name} ({c.rank}) - {c.specialization}")
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
