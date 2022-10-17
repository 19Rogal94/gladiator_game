from ...classes_gladiator.class_user_gladiator import UserGladiator
from ...equipment.equipment_items.armors import armor_list
from ...equipment.equipment_items.helmets import helmet_list
from ...equipment.equipment_items.shields import shield_list
from ..verification_functions.verification_armor_list import verification_armor_list
from ..verification_functions.verification_equipment_in_list import verification_equipment_in_list
from ..verification_functions.verification_helmet_list import verification_helmet_list
from ..verification_functions.verification_shield_list import verification_shield_list


def armor_shop(gladiator: UserGladiator) -> None:
    while True:
        print("Znajdujesz się w sklepie z uzbrojeniem. Który typ uzbrojenia cię interesuje (podaj liczbę)?\n"
              "1. Hełmy\n"
              "2. Zbroje\n"
              "3. Tarcze\n"
              "4. Wyjdź ze sklepu\n")
        armament_shop_action_1 = input()

        if armament_shop_action_1 == "1":
            while True:
                print("Oto dostępna lista hełmów:\n")
                for arg in helmet_list:
                    print(f"{arg.name} \t-\t defensywa: {arg.defence} \t-\t wytrzymałość: "
                          f"{arg.stamina} \t-\t cena: {arg.price}")
                print("cofnij - wróć do sklepu\n")
                armament_shop_action_2 = input("Podaj nazwę hełmu, który chcesz kupić\n").capitalize()
                print()

                if armament_shop_action_2 == "Cofnij":
                    break
                elif not verification_equipment_in_list(equipment_list=helmet_list, action=armament_shop_action_2):
                    print("Podałeś niepoprawną nazwę przedmiotu!\n")
                    continue
                else:
                    verification_helmet_list(equipment_list=helmet_list, action=armament_shop_action_2,
                                             gladiator=gladiator)

        elif armament_shop_action_1 == "2":
            while True:
                print("Oto dostępna lista zbroi:\n")
                for arg in armor_list:
                    print(f"{arg.name} \t-\t defensywa: {arg.defence} \t-\t wytrzymałość: "
                          f"{arg.stamina} \t-\t cena: {arg.price}")
                print("cofnij - wróć do sklepu\n")
                armament_shop_action_2 = input("Podaj nazwę zbroi, którą chcesz kupić\n").capitalize()
                print()

                if armament_shop_action_2 == "Cofnij":
                    break
                elif not verification_equipment_in_list(equipment_list=armor_list, action=armament_shop_action_2):
                    print("Podałeś niepoprawną nazwę przedmiotu!\n")
                    continue
                else:
                    verification_armor_list(equipment_list=armor_list, action=armament_shop_action_2,
                                            gladiator=gladiator)

        elif armament_shop_action_1 == "3":
            while True:
                print("Oto dostępna lista tarcz:\n")
                for arg in shield_list:
                    print(f"{arg.name} \t-\t defensywa: {arg.defence} \t-\t wytrzymałość: "
                          f"{arg.stamina} \t-\t cena: {arg.price}")
                print("cofnij - wróć do sklepu\n")
                armament_shop_action_2 = input("Podaj nazwę tarczy, którą chcesz kupić\n").capitalize()
                print()

                if armament_shop_action_2 == "Cofnij":
                    break
                elif not verification_equipment_in_list(equipment_list=shield_list, action=armament_shop_action_2):
                    print("Podałeś niepoprawną nazwę przedmiotu!\n")
                    continue
                else:
                    verification_shield_list(equipment_list=shield_list, action=armament_shop_action_2,
                                             gladiator=gladiator)

        elif armament_shop_action_1 == "4":
            break
        else:
            print("Wybrałeś nieprawidłową wartość. Wpisz poprawną!")
            continue
