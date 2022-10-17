from .core import Equipment


class Helmet(Equipment):
    def __init__(self, name, defence, stamina, price):
        super().__init__(name, stamina, price)
        self.defence = defence
