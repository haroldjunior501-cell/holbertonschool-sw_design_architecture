#!/usr/bin/env python3
class Bus:
    def mode(self):
        return "road"


class Train:
    def mode(self):
        return "rails"


class Bike:
    def mode(self):
        return "lane"


class Scooter:
    def mode(self):
        return "scooter_lane"


class VehicleFactory:
    def __init__(self):
        self._registry = {}
        self.register_kind("bus", Bus)
        self.register_kind("train", Train)
        self.register_kind("bike", Bike)

    def register_kind(self, name, cls):
        self._registry[name] = cls

    def create(self, kind):
        cls = self._registry.get(kind)
        if cls is None:
            raise ValueError("Unknown vehicle kind: {}".format(kind))
        return cls()


def main():
    factory = VehicleFactory()
    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    factory.register_kind("scooter", Scooter)
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
