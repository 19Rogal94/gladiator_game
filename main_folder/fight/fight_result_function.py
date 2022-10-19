from ..classes_gladiator.class_opponent_gladiator import OpponentGladiator
from ..classes_gladiator.class_user_gladiator import UserGladiator
from .fight import fight
from ..classes_gladiator.opponent_object.opponent import level_1_opponent
from ..new_skills_function.new_skills_function import new_skills_choice


def result_1_fight(result: str, gladiator: UserGladiator, opponent: OpponentGladiator) -> None:
    while True:
        if result == "Win":
            print(f"Gratulacje! Dzięki wygranej wchodzisz w świat gladiatorów. W nagrodę za wygraną dostajesz "
                  f"{opponent.gold} złotych monet. Dodatkowo masz do dyspozycji {opponent.new_skill} nowych "
                  f"umiejętności do rozdysponowania")
            gladiator.win_the_fight(opponent=level_1_opponent)
            new_skills_choice(gladiator=gladiator)
            print()
            gladiator.gladiator_skills()
            break
        else:
            print(f"Niestety {gladiator.username}, przegrałeś swoją pierwszą walkę, Musisz ją stoczyć ponownie\n")
            result = fight(gladiator=gladiator, opponent=opponent)
            continue
