from main_folder.class_gladiator import UserGladiator, OpponentGladiator
import random


def user_move_left(distance_list: list, gladiator: UserGladiator):
    user_position = distance_list.index("Y")
    if user_position == 0:
        print(f"Jesteś na skraju areny! Nie możesz iść dalej! {gladiator.username} "
              f"pamiętaj się na przyszłość. Zmęczyłeś się tylko i tracisz kolejkę")
    else:
        distance_list[user_position - 1], distance_list[user_position] = "Y", "_"
        print("Pomyślnie poruszyłeś się o 1 w lewo")


def user_move_right(distance_list: list, gladiator: UserGladiator):
    user_position = distance_list.index("Y")
    opponent_position = distance_list.index("O")
    if user_position == opponent_position - 1:
        print(f"Wpadasz na przecwinika! Nie możesz iść dalej! {gladiator.username} "
              f"pamiętaj się na przyszłość. Zmęczyłeś się tylko i tracisz kolejkę")
    else:
        distance_list[user_position + 1], distance_list[user_position] = "Y", "_"
        print("Pomyślnie poruszyłeś się o 1 w prawo")


def opponent_move_left(distance_list: list):
    user_position = distance_list.index("Y")
    opponent_position = distance_list.index("O")
    if user_position == opponent_position - 1:
        print("Przeciwnika wpada na Ciebie. Nic się nie dzieje")
    else:
        distance_list[opponent_position - 1], distance_list[opponent_position] = "O", "_"
        print("Przeciwnik poruszył się o 1 w lewo")


def opponent_move_right(distance_list: list):
    opponent_position = distance_list.index("O")
    if opponent_position == 9:
        print("Przeciwnika wpada na bandę areny. Nic się nie dzieje")
    else:
        distance_list[opponent_position + 1], distance_list[opponent_position] = "O", "_"
        print("Przeciwnik poruszył się o 1 w prawo")


def opponent_tour(opponent: OpponentGladiator, distance_list, gladiator: UserGladiator):
    opponent_choice: int = random.randint(1, 3)
    if opponent_choice == 1:
        if opponent.stamina_in_fight < 10:
            opponent.stamina_in_fight += 30
            print("Przeciwnik odpoczywa.")
        else:
            opponent_move_left(distance_list)
            opponent.stamina_in_fight -= 10
    elif opponent_choice == 2:
        if opponent.stamina_in_fight < 10:
            opponent.stamina_in_fight += 30
            print("Przeciwnik odpoczywa.")
        else:
            opponent_move_right(distance_list)
            opponent.stamina_in_fight -= 10
    else:
        if opponent.stamina_in_fight < 10:
            opponent.stamina_in_fight += 30
            print("Przeciwnik odpoczywa.")
        else:
            user_distance = distance_list.index("O") - distance_list.index("Y")
            attack_multiplier_op: float = random.randint(5, 15) / 10
            fight_user_variable_op = random.randint(1, 15)
            fight_opponent_variable_op = random.randint(1, 10)
            if user_distance > 1:
                opponent_attack_chance = opponent.technik_long_distanse_fight / fight_opponent_variable_op
                user_defence = gladiator.defence / fight_user_variable_op
                if opponent_attack_chance >= user_defence:
                    gladiator.health_in_fight -= opponent.strenght_long * attack_multiplier_op
                    print("Przeciwnik przeprowadził udany atak z dystansu na Ciebie!")
                else:
                    print("Uniknąłeś ataku przeciwnika")
            else:
                opponent_attack_chance = opponent.technik_short_distanse_fight / fight_opponent_variable_op
                user_defence = gladiator.defence / fight_user_variable_op
                if opponent_attack_chance >= user_defence:
                    gladiator.health_in_fight -= opponent.strenght * attack_multiplier_op
                    print("Przeciwnik przeprowadził udany atak na Ciebie!")
                else:
                    print("Uniknąłeś ataku przeciwnika")
                opponent.stamina_in_fight -= 20


def fight(gladiator: UserGladiator, opponent: OpponentGladiator):
    gladiator.health_in_fight = 100
    gladiator.stamina_in_fight = gladiator.stamina * 50

    opponent.health_in_fight = 100
    opponent.stamina_in_fight = opponent.stamina * 50

    distance_list = ["_", "_", "Y", "_", "_", "_", "_", "O", "_", "_"]

    print(f"Zaczynacie walkę właśnie teraz. Wasze pierwotne położenie znajduje się poniżej:\n"
          f"{distance_list}")

    while True:
        print("Wybierz działanie:\n"
              "1. Idź w lewo\n"
              "2. Idź w prawo\n"
              "3. Odpocznij i zyskaj 30 wytrzymałości\n"
              "4. Atakuj! (atak kosztuje 20 wytrzymałości\n")
        user_action = input("Twój wybór:\n")
        print()
        if user_action == "1":
            if gladiator.stamina_in_fight < 10:
                gladiator.stamina_in_fight += 30
                print("Nie masz siły się ruszyć! Odpoczywasz tę kolejkę!")
            else:
                user_move_left(distance_list, gladiator)
                gladiator.stamina_in_fight -= 10
            opponent_tour(opponent=opponent, distance_list=distance_list, gladiator=gladiator)

        elif user_action == "2":
            if gladiator.stamina_in_fight < 10:
                gladiator.stamina_in_fight += 30
                print("Nie masz siły się ruszyć! Odpoczywasz tę kolejkę!")
            else:
                user_move_right(distance_list, gladiator)
                gladiator.stamina_in_fight -= 10
            opponent_tour(opponent=opponent, distance_list=distance_list, gladiator=gladiator)

        elif user_action == "3":
            gladiator.stamina_in_fight += 30
            print("Odpoczywasz, wróć silniejszy!")
            opponent_tour(opponent=opponent, distance_list=distance_list, gladiator=gladiator)

        elif user_action == "4":
            if gladiator.stamina_in_fight < 20:
                gladiator.stamina_in_fight += 30
                print("Nie masz siły się ruszyć! Odpoczywasz tę kolejkę!")
            else:
                users_distance = distance_list.index("O") - distance_list.index("Y")
                attack_multiplier: float = random.randint(5, 15) / 10

                if users_distance > 1:
                    figth_user_variable = random.randint(1, 15)
                    figth_opponent_variable = random.randint(1, 15)
                    user_attack_chance = gladiator.technik_long_distanse_fight / figth_user_variable
                    opponent_defence = opponent.defence / figth_opponent_variable

                    if user_attack_chance >= opponent_defence:
                        opponent.health_in_fight -= gladiator.strenght_long * attack_multiplier
                        print("Udany atak z dystansu!")
                    else:
                        print("Przeciwnikowi udało się uniknąć ataku!")

                else:
                    figth_user_variable = random.randint(1, 15)
                    figth_opponent_variable = random.randint(1, 15)
                    user_attack_chance = gladiator.technik_short_distanse_fight / figth_user_variable
                    opponent_defence = opponent.defence / figth_opponent_variable

                    if user_attack_chance >= opponent_defence:
                        opponent.health_in_fight -= gladiator.strenght * attack_multiplier
                        print("Udany atak!")
                    else:
                        print("Przeciwnikowi udało się uniknąć ataku!")

                gladiator.stamina_in_fight -= 20
            opponent_tour(opponent=opponent, distance_list=distance_list, gladiator=gladiator)
        else:
            print("Podałeś niepoprawną wartość. Wprowadź ponownie, tym razem poprawną wartość")
            continue

        print("=" * 79)

        if gladiator.health_in_fight > 0 and opponent.health_in_fight > 0:
            print(f"Po tej rundzie statystyki wyglądają nastepująco:\n"
                  f"Pole walki: {distance_list}\n"
                  f"{gladiator.username} -> Zdrowie: {gladiator.health_in_fight}, "
                  f"Wytrzymałość: {gladiator.stamina_in_fight}\n"
                  f"Przeciwnik -> Zdrowie: {opponent.health_in_fight}, Wytrzymałość: {opponent.stamina_in_fight}")
        elif gladiator.health_in_fight <= 0:
            print("=" * 79)
            print("=" * 30 + "Niestety przegrałeś" + "=" * 30)
            print("=" * 79)
            print("=" * 79)
            return "Loss"
        else:
            print("=" * 79)
            print("=" * 22 + "Gratulacje! Pokonałeś przeciwnika! " + "=" * 22)
            print("=" * 79)
            print("=" * 79)
            return "Win"
        print("=" * 79)
