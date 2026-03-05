from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)

    name: str = Field(min_length=1, max_length=50)

    crew_size: int = Field(ge=1, le=20)

    power_level: float = Field(ge=0.0, le=100.0)

    oxygen_level: float = Field(ge=0.0, le=100.0)

    last_maintenance: datetime = Field(..., description="UTC"
                                       "timestamp of the last safety check")

    is_operational: bool = True

    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    try:
        space_valid = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )

        print("Valid station created:")
        print(f"ID: {space_valid.station_id}")
        print(f"Name: {space_valid.name}")
        print(f"Crew: {space_valid.crew_size} people")
        print(f"Power: {space_valid.power_level}%")
        print(f"Oxygen: {space_valid.oxygen_level}%")
        print("Status: "
              f"{'Operational' if space_valid.is_operational else 'Down'}")

    except ValidationError as e:
        print(f"Unexpected error in valid data: {e}")

    print("\n========================================")

    print("Expected validation error:")
    try:

        space_invalid = SpaceStation(
            station_id="MARS-01",
            name="Overcrowded Mars Base",
            crew_size=50,
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance=datetime.now()
        )

        space_invalid.name

    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg']}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected Error: {e}")
