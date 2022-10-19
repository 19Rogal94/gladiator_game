import random
from .functions_in_fight_function.opponent_tour import opponent_tour
from ..classes_gladiator.class_opponent_gladiator import OpponentGladiator
from ..classes_gladiator.class_user_gladiator import UserGladiator
from .functions_in_fight_function.user_moves import user_move_left, user_move_right


def fight(gladiator: UserGladiator, opponent: OpponentGladiator) -> str:
    gladiator.health_in_fight = 100
    gladiator.stamina_in_fight = gladiator.stamina * 50

    opponent.health_in_fight = 10
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
                    user_attack_chance = gladiator.technik_long_distance_fight / figth_user_variable
                    opponent_defence = opponent.defence / figth_opponent_variable

                    if user_attack_chance >= opponent_defence:
                        opponent.health_in_fight -= gladiator.strength_long * attack_multiplier
                        print("Udany atak z dystansu!")
                    else:
                        print("Przeciwnikowi udało się uniknąć ataku!")

                else:
                    figth_user_variable = random.randint(1, 15)
                    figth_opponent_variable = random.randint(1, 15)
                    user_attack_chance = gladiator.technik_short_distance_fight / figth_user_variable
                    opponent_defence = opponent.defence / figth_opponent_variable

                    if user_attack_chance >= opponent_defence:
                        opponent.health_in_fight -= gladiator.strength * attack_multiplier
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
