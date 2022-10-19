class Gladiator:
    def __init__(self, strength: int, strength_long: int, stamina: int, technik_short_distance_fight: int,
                 technik_long_distance_fight: int, defence: int):
        self.strength = strength
        self.strength_long = strength_long
        self.stamina = stamina
        self.technik_short_distance_fight = technik_short_distance_fight
        self.technik_long_distance_fight = technik_long_distance_fight
        self.defence = defence
        self.health_in_fight: int = 0
        self. stamina_in_fight: int = 0
