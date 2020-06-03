class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class RegistrySingletonMeta(metaclass=Singleton):
    i = -1
    registry = {}

    def add(self, obj):
        self.i += 1
        self.registry[self.i] = obj


if __name__ == "__main__":
    registry1 = RegistrySingletonMeta()
    registry1.add("test")
    registry2 = RegistrySingletonMeta()
    assert registry1 is registry2
    assert {0: "test"} == registry1.registry
