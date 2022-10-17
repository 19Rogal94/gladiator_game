from ...classes_gladiator.class_opponent_gladiator import OpponentGladiator
from ...classes_gladiator.class_user_gladiator import UserGladiator
from ...fight.fight import fight


def main_fight(gladiator: UserGladiator, opponent: OpponentGladiator) -> str:
    print("Stoczysz zaraz walkę z kolejnym przeciwnikiem. Postaraj się a będziesz bliżej wolnośći!")
    return fight(gladiator=gladiator, opponent=opponent)
