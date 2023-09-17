from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ConsumerAnnotation:
    name: str
    surname:str
    account: int


@dataclass(frozen=True, slots=True)
class HouseAnnotation:
    price: int
    square: int


    def make_discount(self):
        pass