from .core import Gladiator


class OpponentGladiator(Gladiator):
    def __init__(self, strenght, strenght_long, stamina, technik_short_distanse_fight,
                 technik_long_distanse_fight, defence):
        super().__init__(strenght, strenght_long, stamina, technik_short_distanse_fight,
                         technik_long_distanse_fight, defence)
