from abc import ABC, abstractmethod


class Carrier:
    def __init__(self, carrier_id, places, card_number):
        self.carrier_id = carrier_id
        self.places = places
        self.card_number = card_number


class CarrierRepo(ABC):
    @abstractmethod
    def add_carrier(self, carrier):
        pass

    @abstractmethod
    def remove_carrier(self, carrier_id):
        pass

    @abstractmethod
    def get_carrier(self, carrier_id):
        pass


class CarrierRepository(CarrierRepo):
    def __init__(self):
        self.carriers = {}

    def add_carrier(self, carrier):
        self.carriers[carrier.carrier_id] = carrier

    def remove_carrier(self, carrier_id):
        if carrier_id in self.carriers:
            del self.carriers[carrier_id]

    def get_carrier(self, carrier_id):
        return self.carriers.get(carrier_id, None)
