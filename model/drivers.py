from dataclasses import dataclass
from datetime import datetime


@dataclass
class Drivers:
    driverId: int
    driverRef: str
    number: int
    code: str
    forename: str
    surname: str
    dob: datetime
    nationality: str
    url: str

    def __str__(self):
        return f"{self.forename} {self.surname}"

    def __hash__(self):
        return hash(self.driverId)