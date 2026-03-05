from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10,
                            description="Unique alphanumeric identifier "
                            "for the orbital facility")

    name: str = Field(..., min_length=1, max_length=50, description="The "
                      "official designated name of the space station")

    crew_size: int = Field(..., ge=1, le=20, description="Current "
                           "number of personnel stationed on board")

    power_level: float = Field(..., ge=0.0, le=100.0, description="Current "
                               "energy reserves expressed as a percentage")

    oxygen_level: float = Field(..., ge=0.0, le=100.0,
                                description="Atmospheric "
                                "oxygen concentration percentage")

    last_maintenance: datetime = Field(..., description="UTC"
                                       "timestamp of the last safety check")

    is_operational: bool = Field(True, description="Status "
                                 "flag indicating if the "
                                 "station is currently functional")

    notes: Optional[str] = Field(None, max_length=200, description="Additional"
                                 " technical remarks or status observations")


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
