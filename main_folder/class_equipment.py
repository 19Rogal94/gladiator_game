class Equipment:
    def __init__(self, name: str, stamina: int, price: int):
        self.name = name
        self.stamina = stamina
        self.price = price


class Weapon(Equipment, ):
    def __init__(self, name, strenght: int, strenght_long: int, stamina, price, weapon_type):
        super().__init__(name, stamina, price)
        self.strenght = strenght
        self.strenght_long = strenght_long
        self.type = weapon_type


class Helmet(Equipment):
    def __init__(self, name, defence, stamina, price):
        super().__init__(name, stamina, price)
        self.defence = defence


class Armor(Equipment):
    def __init__(self, name, defence, stamina, price):
        super().__init__(name, stamina, price)
        self.defence = defence


class Shield(Equipment):
    def __init__(self, name, defence, stamina, price):
        super().__init__(name, stamina, price)
        self.defence = defence
