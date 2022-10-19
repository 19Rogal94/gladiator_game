from .core import Equipment


class Weapon(Equipment):
    def __init__(self, name, strength: int, strenght_long: int, stamina, price, weapon_type):
        super().__init__(name, stamina, price)
        self.strength = strength
        self.strength_long = strenght_long
        self.type = weapon_type
