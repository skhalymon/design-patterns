from abc import ABC, abstractmethod

from creational.factory.core import *


class CarStore(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        ...

    def order_car(self) -> OrderedCar:
        car = self.create_car()
        car.prepare()
        car.polish()
        return OrderedCar(car)


class SuvCarStore(CarStore):
    def create_car(self) -> SuvCar:
        return SuvCar()


class VanCarStore(CarStore):
    def create_car(self) -> VanCar:
        return VanCar()


class WagonCarStore(CarStore):
    def create_car(self) -> WagonCar:
        return WagonCar()


if __name__ == "__main__":
    car = VanCarStore().order_car()
    assert isinstance(car, VanCar)

    car = WagonCarStore().order_car()
    assert isinstance(car, WagonCar)

    car = SuvCarStore().order_car()
    assert isinstance(car, SuvCar)
