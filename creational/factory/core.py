from __future__ import annotations
from enum import Enum, auto
from typing import NewType


class CarType(Enum):
    SUV = auto()
    VAN = auto()
    WAGON = auto()


class Car:
    def prepare(self) -> PreparedCar:
        ...

    def polish(self) -> PolishedCar:
        ...


class SuvCar(Car):
    ...


class VanCar(Car):
    ...


class WagonCar(Car):
    ...


OrderedCar = NewType("OrderedCar", Car)
PreparedCar = NewType("PreparedCar", Car)
PolishedCar = NewType("PolishedCar", Car)
