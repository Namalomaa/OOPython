from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime
from typing import Optional, Self


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def alian_validation(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("contact_id must start with 'AC'")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contacts must be verified")

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError("Telepathic contacts must have at"
                             " least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must have a message received")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-06-01T14:30:00",
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
    except ValidationError as e:
        print(f"Unexpected Error: {e}")
        return
    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: '{contact.message_received}'")
    print()
    print("======================================")
    print("Expected validation error:")
    try:
        contact2 = AlienContact(
            contact_id="AC_2025_005",
            timestamp="2025-09-01T14:29:00",
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=7.0,
            duration_minutes=30,
            witness_count=2,
            message_received=None,
            is_verified=False
        )
        print("Valid contact report:")
        print(f"ID: {contact2.contact_id}")
        print(f"Type: {contact2.contact_type.value}")
        print(f"Location: {contact2.location}")
        print(f"Signal: {contact2.signal_strength}/10")
        print(f"Duration: {contact2.duration_minutes} minutes")
        print(f"Witnesses: {contact2.witness_count}")
        print(f"Message: '{contact2.message_received}'")
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
