from enum import Enum
from pydantic import model_validator, BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)

    timestamp: datetime

    location: str = Field(min_length=3, max_length=100)

    contact_type: ContactType = Field(..., description="The"
                                      "classification of the alien encounter")

    signal_strength: float = Field(ge=0.0, le=10.0)

    duration_minutes: int = Field(ge=1, le=1440)

    witness_count: int = Field(ge=1, le=100)

    message_received: Optional[str] = Field(None, max_length=500)

    is_verified: bool = False

    @model_validator(mode='after')
    def validation_custom(self):
        if not self.contact_id.startswith('AC'):
            raise ValueError("The Contact ID Must Start With 'AC'")
        if not self.is_verified:
            raise ValueError(f"The Verification is {self.is_verified}")
        if self.witness_count < 3:
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")
        if self.signal_strength <= 7.0:
            raise ValueError("Recieved Signal is Weak !")
        return self


def main():
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        alien_contact = AlienContact(contact_id="AC_2024_001",
                                     contact_type="radio",
                                     location="Area 51, Nevada",
                                     signal_strength=8.5,
                                     duration_minutes=45, witness_count=5,
                                     timestamp=datetime.now(),
                                     is_verified=True,
                                     message_received="'Greetings from "
                                     "Zeta Reticuli'")

        print("Valid contact report:")
        print("ID:", alien_contact.contact_id)
        print("Type:", alien_contact.contact_type)
        print("Location:", alien_contact.location)
        print(f"Signal: {alien_contact.signal_strength}/10")
        print(f"Duration: {alien_contact.duration_minutes} minutes")
        print("Witnesses:", alien_contact.witness_count)
        print("Message:", alien_contact.message_received)

    except ValidationError as e:
        print(f"Unexpected error in valid data: {e}")

    print("\n======================================")
    print("Expected validation error:")
    try:
        invalid_contact = AlienContact(contact_id="AC_2024_001",
                                       contact_type="radio",
                                       location="Area 51, Nevada",
                                       signal_strength=8.5,
                                       duration_minutes=45, witness_count=1,
                                       timestamp=datetime.now(),
                                       is_verified=True,
                                       message_received="'Greetings from "
                                       "Zeta Reticuli'")
        invalid_contact.contact_id
    except ValidationError as e:
        for error in e.errors():
            if 'Value error' in error['msg']:
                valid = error['msg'].split(',')
                print(valid[1].strip())
            else:
                print(error['msg'])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected Error: {e}")
