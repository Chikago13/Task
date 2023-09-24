from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TransportAnnotation:
    speed: int
    capacity: int


@dataclass(frozen=True, slots=True)
class BusAnnotation:
    speed: int
    capacity: int
    route_number: str


@dataclass(frozen=True, slots=True)
class TrainAnnotation:
    speed: int
    capacity: int
    has_restoran:bool