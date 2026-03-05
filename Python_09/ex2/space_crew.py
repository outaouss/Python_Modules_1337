from enum import Enum
from pydantic import model_validator, BaseModel, Field, ValidationError


class CrewRank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)

    name: str = Field(min_length=2, max_length=50)

    rank: CrewRank

    age: int = Field(ge=18, le=80)

    specialization: str = Field(min_length=3, max_length=30)

    years_experience: int = Field(min_length=0, max_length=50)

    is_active: bool = True


class SpaceMission(BaseModel):
    