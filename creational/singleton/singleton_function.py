def registry_singleton():
    ...


def add(obj):
    registry_singleton.i += 1
    registry_singleton.registry[registry_singleton.i] = obj


registry_singleton.i = -1
registry_singleton.registry = {}
registry_singleton.add = add


if __name__ == "__main__":
    registry_singleton.add("test")
    assert {0: "test"} == registry_singleton.registry
