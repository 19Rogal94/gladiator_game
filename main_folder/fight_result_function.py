from main_folder.class_gladiator import UserGladiator, OpponentGladiator
from main_folder.new_skills_function import new_skills_choice
from main_folder.fight_function import fight


def result_1_fight(result: str, gladiator: UserGladiator, opponent: OpponentGladiator):
    while True:
        if result == "Win":
            print("Gratulacje! Dzięki wygranej wchodzisz w świat gladiatorów. W nagrodę za wygraną dostajesz "
                  "500 złotych monet. Dodatkowo masz do dyspozycji 3 nowych umiejętności do rozdysponowania")
            gladiator.gold += 500
            new_skill = 3
            new_skills_choice(skill_point=new_skill, gladiator=gladiator)
            print()
            gladiator.gladiator_skills()
            break
        else:
            print(f"Niestety {gladiator.username}, przegrałeś swoją pierwszą walkę, Musisz ją stoczyć ponownie\n")
            result = fight(gladiator=gladiator, opponent=opponent)
            continue
