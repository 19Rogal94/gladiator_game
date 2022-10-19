import math
from .class_opponent_gladiator import OpponentGladiator
from .core import Gladiator
from ..equipment.equipment_items import armors, helmets, long_distance_weapons, shields, short_distance_weapons


class UserGladiator(Gladiator):
    def __init__(self, username, strength=1, strength_long=1, stamina=1, technik_short_distance_fight=1,
                 technik_long_distance_fight=1, defence=1):
        super().__init__(strength, strength_long, stamina, technik_short_distance_fight,
                         technik_long_distance_fight, defence)
        self.username = username
        self.gold: int = 0
        self.weapons_short_distance_warehouse = {"Pięści": short_distance_weapons.piesci}
        self.weapons_long_distance_warehouse = {"Kamienie": long_distance_weapons.stones}
        self.helmet_warehouse = {}
        self.armor_warehouse = {}
        self.shield_warehouse = {}
        self.weapons_short_distance_in_use = short_distance_weapons.piesci
        self.weapons_long_distance_in_use = long_distance_weapons.stones
        self.helmet_in_use = helmets.no_helmet
        self.armor_in_use = armors.no_armor
        self.shield_in_use = shields.no_shield
        self.new_skill = 0

    def gladiator_skills(self) -> None:
        print(f"{self.username}, Twoje umiejętności wyglądają następująco: \nSiła: {self.strength} \n"
              f"Siła w walce na dystans: {self.strength_long} \n"
              f"Wytrzymałość: {self.stamina} \n"
              f"Technika walki na krótkim dystansie: {self.technik_short_distance_fight} \n"
              f"Technika walki na długim dystansie: {self.technik_long_distance_fight} \n"
              f"Uniki: {self.defence} \n")

    def gladiator_gold(self) -> None:
        print(f"Posiadasz obecnie {self.gold} złota\n")

    def gladiator_equipment_in_use(self) -> None:
        print(f"Masz na sobie założone następujące uzbrojenie:\n"
              f"Broń krótkodystansowa: {self.weapons_short_distance_in_use.name}\n"
              f"Broń długodystansowa: {self.weapons_long_distance_in_use.name}\n"
              f"Hełm: {self.helmet_in_use.name}\n"
              f"Zbroja: {self.armor_in_use.name}\n"
              f"Tarcze: {self.shield_in_use.name}\n")

    def choice_short_distance_weapon(self) -> None:
        while True:
            print(f"Znajdujesz się w magazynie broni krótkodystansowej. Obecnie w użyciu masz "
                  f"{self.weapons_short_distance_in_use.name}.\n")
            print("Obecnie posiadasz następującą broń któtkodystansową w magazynie:")
            for arg in self.weapons_short_distance_warehouse.values():
                print(f"{arg.name} - siła: {arg.strength} - wytrzymałość: "
                      f"{arg.stamina} - cena: {arg.price}")
            print("cofnij - wróć do menadżera postaci\n")
            charakter_manager_2 = input("Wybierz którą broń chcesz założyć\n")
            charakter_manager_2 = charakter_manager_2.capitalize()
            print()
            if charakter_manager_2 in self.weapons_short_distance_warehouse.keys():
                if self.stamina <= math.fabs(self.weapons_short_distance_warehouse[charakter_manager_2].stamina):
                    print("Niestety, nie masz wystarczającej wytrzymałości, aby założyć ten przedmiot")
                else:
                    print(f"Pomyślnie założyłeś {self.weapons_short_distance_warehouse[charakter_manager_2].name}")
                    self.strength -= self.weapons_short_distance_in_use.strength
                    self.stamina -= self.weapons_short_distance_in_use.stamina
                    self.weapons_short_distance_in_use = self.weapons_short_distance_warehouse[charakter_manager_2]
                    self.strength += self.weapons_short_distance_warehouse[charakter_manager_2].strength
                    self.stamina += self.weapons_short_distance_warehouse[charakter_manager_2].stamina
                    print()
            elif charakter_manager_2 == "Cofnij":
                break
            else:
                print("Nie posiadasz takiej broni w magazynie")
                continue

    def choice_long_distance_weapon(self) -> None:
        while True:
            print(
                f"Znajdujesz się w magazynie broni długodystansowej. Obecnie w użyciu masz "
                f"{self.weapons_long_distance_in_use.name}.\n")
            print("Obecnie posiadasz następującą broń długodystansową w magazynie:")
            for arg in self.weapons_long_distance_warehouse.values():
                print(f"{arg.name} - siła dalekiego dystansu: {arg.strength_long} - wytrzymałość: {arg.stamina} - "
                      f"cena: {arg.price}")
            print("cofnij - wróć do menadżera postaci\n")
            charakter_manager_2 = input("Wybierz którą broń chcesz założyć\n")
            charakter_manager_2 = charakter_manager_2.capitalize()
            print()
            if charakter_manager_2 in self.weapons_long_distance_warehouse.keys():
                print(f"Pomyślnie założyłeś "
                      f"{self.weapons_long_distance_warehouse[charakter_manager_2].name}")
                self.strength_long -= self.weapons_long_distance_in_use.strength_long
                self.weapons_long_distance_in_use = self.weapons_long_distance_warehouse[charakter_manager_2]
                self.strength_long += self.weapons_long_distance_warehouse[charakter_manager_2].strength_long
                print()
            elif charakter_manager_2 == "Cofnij":
                break
            else:
                print("Nie posiadasz takiej broni w magazynie")
                continue

    def choice_helmet(self) -> None:
        while True:
            print(f"Znajdujesz się w magazynie hełmów. Obecnie w użyciu masz {self.helmet_in_use.name}.\n")
            print("Obecnie posiadasz następujące hełmy w magazynie:")
            for arg in self.helmet_warehouse.values():
                print(f"{arg.name} - defensywa: {arg.defence} - wytrzymałość: {arg.stamina} - cena: {arg.price}")
            print("cofnij - wróć do menadżera postaci\n")
            charakter_manager_2 = input("Wybierz który hełm chcesz założyć\n")
            charakter_manager_2 = charakter_manager_2.capitalize()
            print()
            if charakter_manager_2 in self.helmet_warehouse.keys():
                if self.stamina <= math.fabs(self.helmet_warehouse[charakter_manager_2].stamina):
                    print("Niestety, nie masz wystarczającej wytrzymałości, aby założyć ten przedmiot")
                else:
                    print(f"Pomyślnie założyłeś {self.helmet_warehouse[charakter_manager_2].name}")
                    self.defence -= self.helmet_in_use.defence
                    self.stamina -= self.helmet_in_use.stamina
                    self.helmet_in_use = self.helmet_warehouse[charakter_manager_2]
                    self.defence += self.helmet_warehouse[charakter_manager_2].defence
                    self.stamina += self.helmet_warehouse[charakter_manager_2].stamina
                    print()
            elif charakter_manager_2 == "Cofnij":
                break
            else:
                print("Nie posiadasz takiego hełmu w magazynie")
                continue

    def choice_armor(self) -> None:
        while True:
            print(f"Znajdujesz się w magazynie zbroi. Obecnie w użyciu masz {self.armor_in_use.name}.\n")
            print("Obecnie posiadasz następujące zbroje w magazynie:")
            for arg in self.armor_warehouse.values():
                print(f"{arg.name} - defensywa: {arg.defence} - wytrzymałość: {arg.stamina} - cena: {arg.price}")
            print("cofnij - wróć do menadżera postaci\n")
            charakter_manager_2 = input("Wybierz którą zbroję chcesz założyć\n")
            charakter_manager_2 = charakter_manager_2.capitalize()
            print()
            if charakter_manager_2 in self.armor_warehouse.keys():
                if self.stamina <= math.fabs(self.armor_warehouse[charakter_manager_2].stamina):
                    print("Niestety, nie masz wystarczającej wytrzymałości, aby założyć ten przedmiot")
                else:
                    print(f"Pomyślnie założyłeś {self.armor_warehouse[charakter_manager_2].name}")
                    self.defence -= self.armor_in_use.defence
                    self.stamina -= self.armor_in_use.stamina
                    self.armor_in_use = self.armor_warehouse[charakter_manager_2]
                    self.defence += self.armor_warehouse[charakter_manager_2].defence
                    self.stamina += self.armor_warehouse[charakter_manager_2].stamina
                    print()
            elif charakter_manager_2 == "Cofnij":
                break
            else:
                print("Nie posiadasz takiej zbroi w magazynie")
                continue

    def choice_shield(self) -> None:
        while True:
            print(f"Znajdujesz się w magazynie tarcz. Obecnie w użyciu masz {self.shield_in_use.name}.\n")
            print("Obecnie posiadasz następujące tarcze w magazynie:")
            for arg in self.shield_warehouse.values():
                print(f"{arg.name} - defensywa: {arg.defence} - wytrzymałość: {arg.stamina} - cena: {arg.price}")
            print("cofnij - wróć do menadżera postaci\n")
            charakter_manager_2 = input("Wybierz którą tarczę chcesz założyć\n")
            charakter_manager_2 = charakter_manager_2.capitalize()
            print()
            if charakter_manager_2 in self.shield_warehouse.keys():
                if self.stamina <= math.fabs(self.shield_warehouse[charakter_manager_2].stamina):
                    print("Niestety, nie masz wystarczającej wytrzymałości, aby założyć ten przedmiot")
                else:
                    print(f"Pomyślnie założyłeś {self.shield_warehouse[charakter_manager_2].name}")
                    self.defence -= self.shield_in_use.defence
                    self.stamina -= self.shield_in_use.stamina
                    self.shield_in_use = self.shield_warehouse[charakter_manager_2]
                    self.defence += self.shield_warehouse[charakter_manager_2].defence
                    self.stamina += self.shield_warehouse[charakter_manager_2].stamina
                    print()
            elif charakter_manager_2 == "Cofnij":
                break
            else:
                print("Nie posiadasz takiej tarczy w magazynie")
                continue

    def charakter_manager(self) -> None:
        while True:
            print("Znajdujesz się w menadżerze postaci. Wybierz co chcesz zrobić:\n"
                  "1. Sprawdź ilość złota\n"
                  "2. Sprawdź swoje umiejętności\n"
                  "3. Sprawdź swoje założone uzbrojenie\n"
                  "4. Wybierz broń krótkodystansową\n"
                  "5. Wybierz broń długodystansową\n"
                  "6. Wybierz hełm\n"
                  "7. Wybierz zbroję\n"
                  "8. Wybierz tarczę\n"
                  "9. Wyjdź z menadżera postaci\n")
            character_manager_1 = input()
            print()
            if character_manager_1 == "1":
                self.gladiator_gold()
            elif character_manager_1 == "2":
                self.gladiator_skills()
            elif character_manager_1 == "3":
                self.gladiator_equipment_in_use()
            elif character_manager_1 == "4":
                self.choice_short_distance_weapon()
            elif character_manager_1 == "5":
                self.choice_long_distance_weapon()
            elif character_manager_1 == "6":
                self.choice_helmet()
            elif character_manager_1 == "7":
                self.choice_armor()
            elif character_manager_1 == "8":
                self.choice_shield()
            elif character_manager_1 == "9":
                break
            else:
                print("Wybrałeś nieprawidłową wartość. Wpisz poprawną!")
                continue

    def win_the_fight(self, opponent: OpponentGladiator):
        self.new_skill = opponent.new_skill
        self.gold += opponent.gold
