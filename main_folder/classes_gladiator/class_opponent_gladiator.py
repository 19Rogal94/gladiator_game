from .core import Gladiator


class OpponentGladiator(Gladiator):
    def __init__(self, strength, strength_long, stamina, technik_short_distance_fight,
                 technik_long_distance_fight, defence, gold: int = 0, new_skill: int = 0):
        super().__init__(strength, strength_long, stamina, technik_short_distance_fight,
                         technik_long_distance_fight, defence)
        self.gold = gold
        self.new_skill = new_skill
