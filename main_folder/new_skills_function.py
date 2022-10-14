from main_folder.class_gladiator import UserGladiator


def increase_strenght(gladiator: UserGladiator):
    gladiator.strenght += 1
    print("Dodano 1 do siły")


def increase_stamina(gladiator: UserGladiator):
    gladiator.stamina += 1
    print("Dodano 1 do wytrzymałości")


def increase_technik_short_distanse_fight(gladiator: UserGladiator):
    gladiator.technik_short_distanse_fight += 1
    print("Dodano 1 do techniki walki na krótkie dystanse")


def increase_technik_long_distanse_fight(gladiator: UserGladiator):
    gladiator.technik_long_distanse_fight += 1
    print("Dodano 1 do techniki walki na długim dystanse")


def increase_defence(gladiator: UserGladiator):
    gladiator.defence += 1
    print("Dodano 1 do uników")


def new_skills_choice(skill_point, gladiator: UserGladiator):
    skill_point_1 = 0
    while skill_point_1 < skill_point:
        print("Wybierz umiejętność, którą chcesz polepszyć. Podaj jej numer:\n"
              "1. Siła\n"
              "2. Wytrzymałość\n"
              "3. Technika walki na krótkim dystansie\n"
              "4. Technika walki na długim dystansie\n"
              "5. Uniki\n")
        user_choice = int(input())
        if user_choice == 1:
            increase_strenght(gladiator)
            skill_point_1 += 1
        elif user_choice == 2:
            increase_stamina(gladiator)
            skill_point_1 += 1
        elif user_choice == 3:
            increase_technik_short_distanse_fight(gladiator)
            skill_point_1 += 1
        elif user_choice == 4:
            increase_technik_long_distanse_fight(gladiator)
            skill_point_1 += 1
        elif user_choice == 5:
            increase_defence(gladiator)
            skill_point_1 += 1
        else:
            print("Podałeś złą wartość, wprowadź ponownie poprawną\n")
            continue
