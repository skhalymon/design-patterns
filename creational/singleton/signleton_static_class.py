class RegistrySingleton:
    i = -1
    registry = {}

    @staticmethod
    def add(obj):
        RegistrySingleton.i += 1
        RegistrySingleton.registry[RegistrySingleton.i] = obj


if __name__ == "__main__":
    registry = RegistrySingleton()
    RegistrySingleton.add("test")
    assert registry.registry is RegistrySingleton.registry
    assert {0: "test"} == registry.registry
