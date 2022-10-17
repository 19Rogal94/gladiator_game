from .core import Equipment


class Weapon(Equipment, ):
    def __init__(self, name, strenght: int, strenght_long: int, stamina, price, weapon_type):
        super().__init__(name, stamina, price)
        self.strenght = strenght
        self.strenght_long = strenght_long
        self.type = weapon_type
