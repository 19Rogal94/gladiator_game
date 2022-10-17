class Gladiator:
    def __init__(self, strenght: int, strenght_long: int, stamina: int, technik_short_distanse_fight: int,
                 technik_long_distanse_fight: int, defence: int):
        self.strenght = strenght
        self.strenght_long = strenght_long
        self.stamina = stamina
        self.technik_short_distanse_fight = technik_short_distanse_fight
        self.technik_long_distanse_fight = technik_long_distanse_fight
        self.defence = defence
        self.health_in_fight: int = 0
        self. stamina_in_fight: int = 0
