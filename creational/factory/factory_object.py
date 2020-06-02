from typing import Type

from creational.factory.core import *


class CarFactoryObject:
    @staticmethod
    def create_car(car_type: CarType) -> Car:
        if car_type == car_type.SUV:
            return SuvCar()
        elif car_type == CarType.VAN:
            return VanCar()
        elif car_type == CarType.WAGON:
            return WagonCar()


class CarStore:
    def __init__(self, factory: Type[CarFactoryObject]):
        self.factory = factory

    def order_car(self, car_type: CarType) -> OrderedCar:
        car = self.factory.create_car(car_type)
        car.prepare()
        car.polish()
        return OrderedCar(car)


if __name__ == "__main__":
    car_store = CarStore(CarFactoryObject)

    car = car_store.order_car(CarType.VAN)
    assert isinstance(car, VanCar)

    car = car_store.order_car(CarType.WAGON)
    assert isinstance(car, WagonCar)

    car = car_store.order_car(CarType.SUV)
    assert isinstance(car, SuvCar)
