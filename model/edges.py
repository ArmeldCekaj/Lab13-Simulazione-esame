from dataclasses import dataclass
from model.drivers import Drivers
@dataclass
class Edges:
    node1: Drivers
    node2: Drivers
    weight: int

