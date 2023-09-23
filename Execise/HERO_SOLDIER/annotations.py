from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GameAnnotation:
    stim: str


@dataclass(frozen=True, slots=True)
class HeroAnnotation:
    stim: str
    level: int


@dataclass(frozen=True, slots=True)
class SoldierAnnotation:
    stim: str


