from enum import Enum
from pydantic import model_validator, BaseModel, Field, ValidationError
from datetime import datetime
from typing import List


class CrewRank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)

    name: str = Field(min_length=2, max_length=50)

    rank: CrewRank = Field(..., description="The official"
                           "hierarchy level of the crew member")

    age: int = Field(ge=18, le=80)

    specialization: str = Field(min_length=3, max_length=30)

    years_experience: int = Field(ge=0, le=50)

    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)

    mission_name: str = Field(min_length=3, max_length=100)

    destination: str = Field(min_length=3, max_length=50)

    launch_date: datetime = Field(..., description="The "
                                  "scheduled date and time"
                                  "for mission departure")

    duration_days: int = Field(ge=1, le=3650)

    crew: List[CrewMember] = Field(min_length=1, max_length=12)

    mission_status: str = "planned"

    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validation_mission(self):
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID Must Start With 'M'")
        if self.duration_days > 365:
            for rank in self.crew:
                if rank.years_experience < 5:
                    raise ValueError("Mission Denied: A Mission of "
                                     "+365 days need experienced "
                                     "crew member [ +5 Years ]")
                if not rank.is_active:
                    raise ValueError(f"The {rank.rank} is Not Active - All "
                                     "Crew Members Must Be Active")
        missing = False
        for member in self.crew:
            if member.rank.value in ['captain', 'commander']:
                missing = True
                break

        if not missing:
            raise ValueError("Mission must have at "
                             "least one Commander or Captain")
        return self


def main():
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        connor = CrewMember(member_id="C-7451", name="Sarah Connor",
                            rank="commander", age=49,
                            specialization="Mission Command",
                            years_experience=24, is_active=True)
        smith = CrewMember(member_id="L-6231", name="John Smith",
                           rank="lieutenant", age=41,
                           specialization="Navigation",
                           years_experience=19, is_active=True)
        johnson = CrewMember(member_id="O-3451", name="Alice Johnson",
                             rank="officer", age=24,
                             specialization="Engineering",
                             years_experience=6, is_active=True)

        # Invalid Officers With [ ALice Johnson ]
        invalid_officer = CrewMember(member_id="O-3657",
                                     name="carlos morgan",
                                     rank="officer", age=24,
                                     specialization="Engineering",
                                     years_experience=6, is_active=True)

        invalid_officer_2 = CrewMember(member_id="O-3658",
                                       name="frank lundy",
                                       rank="officer", age=24,
                                       specialization="Engineering",
                                       years_experience=6, is_active=True)

        crew_members = [connor, smith, johnson]

        valid_mission = SpaceMission(mission_name="Mars Colony Establishment",
                                     mission_id="M2024_MARS",
                                     destination="Mars", duration_days=900,
                                     budget_millions=2500.0, crew=crew_members,
                                     launch_date=datetime.now())

        print("Valid mission created:")
        print("Mission", valid_mission.mission_name)
        print("ID:", valid_mission.mission_id)
        print("Destination:", valid_mission.destination)
        print("Duration:", valid_mission.duration_days, "days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print("Crew size:", len(crew_members))
        print("Crew members:")
        for member in crew_members:
            print(f"- {member.name} ({member.rank.value}) - "
                  f"{member.specialization}")

        print("\n=========================================")
        print("Expected validation error:")

        invalid_crews = [johnson, invalid_officer, invalid_officer_2]
        invalid_mission = SpaceMission(mission_name="Moon Crew - 51",
                                       mission_id="M2025_MOON",
                                       destination="Moon", duration_days=650,
                                       budget_millions=2600.0,
                                       crew=invalid_crews,
                                       launch_date=datetime.now())
        invalid_mission.mission_name

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
