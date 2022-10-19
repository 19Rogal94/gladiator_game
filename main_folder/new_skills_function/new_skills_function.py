from .functions_in_new_skills_function.increase_skills import increase_strength, increase_stamina, \
    increase_technik_short_distance_fight, increase_technik_long_distance_fight, increase_defence
from ..classes_gladiator.class_user_gladiator import UserGladiator


def new_skills_choice(gladiator: UserGladiator):
    # skill_point_1 = 0
    # while skill_point_1 < skill_point:
    while gladiator.new_skill > 0:
        print("Wybierz umiejętność, którą chcesz polepszyć. Podaj jej numer:\n"
              "1. Siła\n"
              "2. Wytrzymałość\n"
              "3. Technika walki na krótkim dystansie\n"
              "4. Technika walki na długim dystansie\n"
              "5. Uniki\n")
        user_choice = input()
        if user_choice == "1":
            increase_strength(gladiator)
            gladiator.new_skill -= 1
        elif user_choice == "2":
            increase_stamina(gladiator)
            gladiator.new_skill -= 1
        elif user_choice == "3":
            increase_technik_short_distance_fight(gladiator)
            gladiator.new_skill -= 1
        elif user_choice == "4":
            increase_technik_long_distance_fight(gladiator)
            gladiator.new_skill -= 1
        elif user_choice == "5":
            increase_defence(gladiator)
            gladiator.new_skill -= 1
        else:
            print("Podałeś złą wartość, wprowadź ponownie poprawną\n")
            continue
