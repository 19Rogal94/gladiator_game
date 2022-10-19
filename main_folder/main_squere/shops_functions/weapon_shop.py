from ...classes_gladiator.class_user_gladiator import UserGladiator
from ...equipment.equipment_items.long_distance_weapons import weapon_long_distance_list
from ...equipment.equipment_items.short_distance_weapons import weapon_short_distance_list
from ..verification_functions.verification_equipment_in_list import verification_equipment_in_list
from ..verification_functions.verification_long_distance_weapon import verification_long_distance_weapon
from ..verification_functions.verification_short_distance_weapon import verification_short_distance_weapon


def weapon_shop(gladiator: UserGladiator) -> None:
    while True:
        print("Znajdujesz się w sklepie z bronią. Powiedz którą broń chcesz obejrzeć (podaj liczbę).\n"
              "1. Broń krótkodystanstowa\n"
              "2. Broń długodystansowa\n"
              "3. Wyjdź ze sklepu\n")
        weapon_shop_action_1 = input()

        if weapon_shop_action_1 == "1":
            while True:
                print("Oto dostępna broń krótkodystansowa:\n")
                for arg in weapon_short_distance_list:
                    print(f"{arg.name} \t-\t siła: {arg.strength} \t-\t wytrzymałość: {arg.stamina} \t-\t "
                          f"cena: {arg.price}")
                print("cofnij - wróć do sklepu\n")
                weapon_shop_action_2 = input("Podaj nazwę broni, którą chcesz kupić\n").capitalize()
                print()

                if weapon_shop_action_2 == "Cofnij":
                    break
                elif not verification_equipment_in_list(equipment_list=weapon_short_distance_list,
                                                        action=weapon_shop_action_2):
                    print("Podałeś niepoprawną nazwę przedmiotu!\n")
                    continue
                else:
                    verification_short_distance_weapon(equipment_list=weapon_short_distance_list,
                                                       action=weapon_shop_action_2, gladiator=gladiator)
                    continue

        elif weapon_shop_action_1 == "2":
            print("Oto dostępna broń długodystansowa:\n")
            while True:
                for arg in weapon_long_distance_list:
                    print(f"{arg.name} \t-\t siła: {arg.strength} \t-\t wytrzymałość: {arg.stamina} \t-\t "
                          f"cena: {arg.price}")
                print("cofnij - wróć do sklepu\n")
                weapon_shop_action_2 = input("Podaj nazwę broni, którą chcesz kupić\n").capitalize()
                print()
                if weapon_shop_action_2 == "Cofnij":
                    break
                elif not verification_equipment_in_list(equipment_list=weapon_long_distance_list,
                                                        action=weapon_shop_action_2):
                    print("Podałeś niepoprawną nazwę przedmiotu!\n")
                    continue
                else:
                    verification_long_distance_weapon(equipment_list=weapon_long_distance_list,
                                                      action=weapon_shop_action_2, gladiator=gladiator)
                    continue

        elif weapon_shop_action_1 == "3":
            break
        else:
            print("Wybrałeś nieprawidłową wartość. Wpisz poprawną!")
            continue
