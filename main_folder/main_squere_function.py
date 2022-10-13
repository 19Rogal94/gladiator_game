import random
import main_folder.equipment
from main_folder.new_skills_function import new_skills_choice
from main_folder.class_gladiator import UserGladiator, OpponentGladiator
from main_folder.fight_function import fight


def verification_short_distance_weapon(equipment_list, action: str, gladiator: UserGladiator):
    for arg in equipment_list:
        if arg.name == action.capitalize():
            if gladiator.gold < arg.price:
                print(f"Niestety nie masz wystarczającej ilości złota.")
            else:
                gladiator.weapons_short_distance_warehouse[arg.name] = arg
                gladiator.gold -= arg.price
                print(f"Pomyślnie kupiłeś przedmiot {arg.name}.")
                print()


def verification_long_distance_weapon(equipment_list, action: str, gladiator: UserGladiator):
    for arg in equipment_list:
        if arg.name == action.capitalize():
            if gladiator.gold < arg.price:
                print(f"Niestety nie masz wystarczającej ilości złota.")
            else:
                gladiator.weapons_long_distance_warehouse[arg.name] = arg
                gladiator.gold -= arg.price
                print(f"Pomyślnie kupiłeś przedmiot {arg.name}.")
                print()


def verification_helmet_list(equipment_list, action: str, gladiator: UserGladiator):
    for arg in equipment_list:
        if arg.name == action.capitalize():
            if gladiator.gold < arg.price:
                print(f"Niestety nie masz wystarczającej ilości złota.")
            else:
                gladiator.helmet_warehouse[arg.name] = arg
                gladiator.gold -= arg.price
                print(f"Pomyślnie kupiłeś przedmiot {arg.name}.")
                print()


def verification_armor_list(equipment_list, action: str, gladiator: UserGladiator):
    for arg in equipment_list:
        if arg.name == action.capitalize():
            if gladiator.gold < arg.price:
                print(f"Niestety nie masz wystarczającej ilości złota.")
            else:
                gladiator.armor_warehouse[arg.name] = arg
                gladiator.gold -= arg.price
                print(f"Pomyślnie kupiłeś przedmiot {arg.name}.")
                print()


def verification_shield_list(equipment_list, action: str, gladiator: UserGladiator):
    for arg in equipment_list:
        if arg.name == action.capitalize():
            if gladiator.gold < arg.price:
                print(f"Niestety nie masz wystarczającej ilości złota.")
            else:
                gladiator.shield_warehouse[arg.name] = arg
                gladiator.gold -= arg.price
                print(f"Pomyślnie kupiłeś przedmiot {arg.name}.")
                print()


def verification_equipment_in_list(equipment_list, action: str):
    new_list = [arg.name for arg in equipment_list]
    return action.capitalize() in new_list


def weapon_shop(gladiator: UserGladiator):
    while True:
        print(f"Znajdujesz się w sklepie z bronią. Powiedz którą broń chcesz obejrzeć (podaj liczbę).\n"
              f"1. Broń krótkodystanstowa\n"
              f"2. Broń długodystansowa\n"
              f"3. Wyjdź ze sklepu\n")
        weapon_shop_action_1 = input()
        if weapon_shop_action_1 == "1":
            while True:
                print(f"Oto dostępna broń krótkodystansowa:\n")
                for arg in main_folder.equipment.weapon_short_distance_list:
                    print(f"{arg.name} \t-\t siła: {arg.strenght} \t-\t wytrzymałość: {arg.stamina} \t-\t "
                          f"cena: {arg.price}")
                print(f"cofnij - wróć do sklepu\n")
                weapon_shop_action_2 = input(f"Podaj nazwę broni, którą chcesz kupić\n").capitalize()
                print()

                if weapon_shop_action_2 == "Cofnij":
                    break
                elif not verification_equipment_in_list(equipment_list=main_folder.equipment.weapon_short_distance_list,
                                                        action=weapon_shop_action_2):
                    print(f"Podałeś niepoprawną nazwę przedmiotu!\n")
                    continue
                else:
                    verification_short_distance_weapon(equipment_list=main_folder.equipment.weapon_short_distance_list,
                                                       action=weapon_shop_action_2, gladiator=gladiator)
                    continue

        elif weapon_shop_action_1 == "2":
            print(f"Oto dostępna broń długodystansowa:\n")
            while True:
                for arg in main_folder.equipment.weapon_long_distance_list:
                    print(f"{arg.name} \t-\t siła: {arg.strenght} \t-\t wytrzymałość: {arg.stamina} \t-\t "
                          f"cena: {arg.price}")
                print(f"cofnij - wróć do sklepu\n")
                weapon_shop_action_2 = input(f"Podaj nazwę broni, którą chcesz kupić\n").capitalize()
                print()
                if weapon_shop_action_2 == "Cofnij":
                    break
                elif not verification_equipment_in_list(equipment_list=main_folder.equipment.weapon_long_distance_list,
                                                        action=weapon_shop_action_2):
                    print(f"Podałeś niepoprawną nazwę przedmiotu!\n")
                    continue
                else:
                    verification_long_distance_weapon(equipment_list=main_folder.equipment.weapon_long_distance_list,
                                                      action=weapon_shop_action_2, gladiator=gladiator)
                    continue

        elif weapon_shop_action_1 == "3":
            break
        else:
            print(f"Wybrałeś nieprawidłową wartość. Wpisz poprawną!")
            continue


def armor_shop(gladiator: UserGladiator):
    while True:
        print(f"Znajdujesz się w sklepie z uzbrojeniem. Który typ uzbrojenia cię interesuje (podaj liczbę)?\n"
              f"1. Hełmy\n"
              f"2. Zbroje\n"
              f"3. Tarcze\n"
              f"4. Wyjdź ze sklepu\n")
        armament_shop_action_1 = input()
        if armament_shop_action_1 == "1":
            while True:
                print(f"Oto dostępna lista hełmów:\n")
                for arg in main_folder.equipment.helmet_list:
                    print(f"{arg.name} \t-\t defensywa: {arg.defence} \t-\t wytrzymałość: "
                          f"{arg.stamina} \t-\t cena: {arg.price}")
                print(f"cofnij - wróć do sklepu\n")
                armament_shop_action_2 = input("Podaj nazwę hełmu, który chcesz kupić\n").capitalize()
                print()

                if armament_shop_action_2 == "Cofnij":
                    break
                elif not verification_equipment_in_list(equipment_list=main_folder.equipment.helmet_list,
                                                        action=armament_shop_action_2):
                    print(f"Podałeś niepoprawną nazwę przedmiotu!\n")
                    continue
                else:
                    verification_helmet_list(equipment_list=main_folder.equipment.helmet_list,
                                             action=armament_shop_action_2, gladiator=gladiator)

        elif armament_shop_action_1 == "2":
            while True:
                print(f"Oto dostępna lista zbroi:\n")
                for arg in main_folder.equipment.armor_list:
                    print(f"{arg.name} \t-\t defensywa: {arg.defence} \t-\t wytrzymałość: "
                          f"{arg.stamina} \t-\t cena: {arg.price}")
                print(f"cofnij - wróć do sklepu\n")
                armament_shop_action_2 = input("Podaj nazwę zbroi, którą chcesz kupić\n").capitalize()
                print()

                if armament_shop_action_2 == "Cofnij":
                    break
                elif not verification_equipment_in_list(equipment_list=main_folder.equipment.armor_list,
                                                        action=armament_shop_action_2):
                    print(f"Podałeś niepoprawną nazwę przedmiotu!\n")
                    continue
                else:
                    verification_armor_list(equipment_list=main_folder.equipment.armor_list,
                                            action=armament_shop_action_2, gladiator=gladiator)

        elif armament_shop_action_1 == "3":
            while True:
                print(f"Oto dostępna lista tarcz:\n")
                for arg in main_folder.equipment.shield_list:
                    print(f"{arg.name} \t-\t defensywa: {arg.defence} \t-\t wytrzymałość: "
                          f"{arg.stamina} \t-\t cena: {arg.price}")
                print(f"cofnij - wróć do sklepu\n")
                armament_shop_action_2 = input("Podaj nazwę tarczy, którą chcesz kupić\n").capitalize()
                print()

                if armament_shop_action_2 == "Cofnij":
                    break
                elif not verification_equipment_in_list(equipment_list=main_folder.equipment.shield_list,
                                                        action=armament_shop_action_2):
                    print(f"Podałeś niepoprawną nazwę przedmiotu!\n")
                    continue
                else:
                    verification_shield_list(equipment_list=main_folder.equipment.shield_list,
                                             action=armament_shop_action_2, gladiator=gladiator)

        elif armament_shop_action_1 == "4":
            break
        else:
            print(f"Wybrałeś nieprawidłową wartość. Wpisz poprawną!")
            continue


def training_with_personal_trainer(gladiator: UserGladiator):
    if gladiator.gold < 200:
        print(f"Niestety, nie masz wystarczającej ilości złota")
        print()
    else:
        print(f"Wybrałeś trening z trenerem. Dostajesz za to dwie nowe umiejętności.")
        print()
        gladiator.gold -= 200
        new_skill = 2
        new_skills_choice(skill_point=new_skill, gladiator=gladiator)


def secondary_fight_in_squere(opponent_1: OpponentGladiator, opponent_2: OpponentGladiator,
                              opponent_3: OpponentGladiator, gladiator: UserGladiator):
    opponent_list = [opponent_1, opponent_2, opponent_3]
    secondary_choice = random.randint(0, 2)
    secondary_opponent = opponent_list[secondary_choice]
    opponent_fight = fight(gladiator=gladiator, opponent=secondary_opponent)
    if opponent_fight == "Win":
        print(f"Gratulacje, wygrałeś. W nagrodę otrzymujesz 250 złota")
        gladiator.gold += 250
    else:
        print(f"Niestety przegrałeś")


def main_fight(gladiator: UserGladiator, opponent: OpponentGladiator):
    print(f"Stoczysz zaraz walkę z kolejnym przeciwnikiem. Postaraj się a będziesz bliżej wolnośći!")
    return fight(gladiator=gladiator, opponent=opponent)


def main_squere(gladiator: UserGladiator, opponent_1: OpponentGladiator, opponent_2: OpponentGladiator,
                opponent_3: OpponentGladiator, main_opponent: OpponentGladiator):
    while True:
        print(f"Znajdujesz się na głównym placu. Oto miejsca, gdzie możesz się udać:\n"
              f"1. Sklep z bronią (kupisz tutaj broń, która pomoże Ci w walce)\n"
              f"2. Sklep z uzbrojenie (kupisz tutaj uzbrojenie, które wpłynie na twoje zdolności defensywne)\n"
              f"3. Trening z trenerem ogólnorozwojowym (dwie nowe umiejętność - koszt 200 złota)\n"
              f"4. Menadżer postaci (możesz tutaj użyć zakupionego wyposażenia)\n"
              f"5. Walka poboczna (za stoczoną walkę możesz zarobić złoto)\n"
              f"6. Walka główna turnieju (pokonaj następnego rywala z listy\n")
        action = input("Wybierz, co chcesz zrobić: \n")
        print()
        if action == "1":
            weapon_shop(gladiator=gladiator)
        elif action == "2":
            armor_shop(gladiator=gladiator)
        elif action == "3":
            training_with_personal_trainer(gladiator=gladiator)
        elif action == "4":
            gladiator.charakter_manager()
        elif action == "5":
            secondary_fight_in_squere(opponent_1=opponent_1, opponent_2=opponent_2,
                                      opponent_3=opponent_3, gladiator=gladiator)
        elif action == "6":
            main_fight_result = main_fight(gladiator=gladiator, opponent=main_opponent)
            if main_fight_result == "Win":
                break
            else:
                print(f"Przegrałeś walkę z przeciwnikiem. Musisz jeszcze podszkolić swoje umiejętności lub"
                      f"pomyśleć o lepszym wyposażeniu. {gladiator.username} nie poddawaj się!")
        else:
            print(f"Wybrałeś nieprawidłową wartość. Wpisz poprawną!")
            continue
