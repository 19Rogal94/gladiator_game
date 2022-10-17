from ...classes_gladiator.class_user_gladiator import UserGladiator
from ...new_skills_function.new_skills_function import new_skills_choice


def training_with_personal_trainer(gladiator: UserGladiator) -> None:
    if gladiator.gold < 200:
        print("Niestety, nie masz wystarczającej ilości złota")
        print()
    else:
        print("Wybrałeś trening z trenerem. Dostajesz za to dwie nowe umiejętności.")
        print()
        gladiator.gold -= 200
        new_skill = 2
        new_skills_choice(skill_point=new_skill, gladiator=gladiator)
