import random
from ...classes_gladiator.class_opponent_gladiator import OpponentGladiator
from ...classes_gladiator.class_user_gladiator import UserGladiator
from ...fight.fight import fight


def secondary_fight_in_squere(opponent_1: OpponentGladiator, opponent_2: OpponentGladiator,
                              opponent_3: OpponentGladiator, gladiator: UserGladiator) -> None:
    opponent_list = [opponent_1, opponent_2, opponent_3]
    secondary_choice = random.randint(0, 2)
    secondary_opponent = opponent_list[secondary_choice]
    opponent_fight = fight(gladiator=gladiator, opponent=secondary_opponent)
    if opponent_fight == "Win":
        print("Gratulacje, wygrałeś. W nagrodę otrzymujesz 250 złota")
        gladiator.gold += 250
    else:
        print("Niestety przegrałeś")
