import math
from equipment import *


class Gladiator:
    def __init__(self, strenght: int, strenght_long: int, stamina: int, technik_short_distanse_fight: int,
                 technik_long_distanse_fight: int, defence: int):
        self.strenght = strenght
        self.strenght_long = strenght_long
        self.stamina = stamina
        self.technik_short_distanse_fight = technik_short_distanse_fight
        self.technik_long_distanse_fight = technik_long_distanse_fight
        self.defence = defence
        self.health_in_fight: int = 0
        self. stamina_in_fight: int = 0


class UserGladiator(Gladiator):
    def __init__(self, username, strenght=1, strenght_long=1, stamina=1, technik_short_distanse_fight=1,
                 technik_long_distanse_fight=1, defence=1):
        super().__init__(strenght, strenght_long, stamina, technik_short_distanse_fight,
                         technik_long_distanse_fight, defence)
        self.username = username
        self.gold: int = 0
        self.weapons_short_distance_warehouse = {"Pięści": piesci}
        self.weapons_long_distance_warehouse = {"Kamienie": kamienie}
        self.helmet_warehouse = {}
        self.armor_warehouse = {}
        self.shield_warehouse = {}
        self.weapons_short_distance_in_use = piesci
        self.weapons_long_distance_in_use = kamienie
        self.helmet_in_use = brak_helmu
        self.armor_in_use = brak_zbroi
        self.shield_in_use = brak_tarczy

    def gladiator_skills(self):
        print(f"{self.username}, Twoje umiejętności wyglądają następująco: \nSiła: {self.strenght} \n"
              f"Siła w walce na dystans: {self.strenght_long} \n"
              f"Wytrzymałość: {self.stamina} \n"
              f"Technika walki na krótkim dystansie: {self.technik_short_distanse_fight} \n"
              f"Technika walki na długim dystansie: {self.technik_long_distanse_fight} \n"
              f"Uniki: {self.defence} \n")

    def gladiator_gold(self):
        print(f"Posiadasz obecnie {self.gold} złota\n")

    def gladiator_equipment_in_use(self):
        print(f"Masz na sobie założone następujące uzbrojenie:\n"
              f"Broń krótkodystansowa: {self.weapons_short_distance_in_use.name}\n"
              f"Broń długodystansowa: {self.weapons_long_distance_in_use.name}\n"
              f"Hełm: {self.helmet_in_use.name}\n"
              f"Zbroja: {self.armor_in_use.name}\n"
              f"Tarcze: {self.shield_in_use.name}\n")

    def choice_short_distance_weapon(self):
        while True:
            print(f"Znajdujesz się w magazynie broni krótkodystansowej. Obecnie w użyciu masz "
                  f"{self.weapons_short_distance_in_use.name}.\n")
            print(f"Obecnie posiadasz następującą broń któtkodystansową w magazynie:")
            for arg in self.weapons_short_distance_warehouse.values():
                print(f"{arg.name} - siła: {arg.strenght} - wytrzymałość: "
                      f"{arg.stamina} - cena: {arg.price}")
            print(f"cofnij - wróć do menadżera postaci\n")
            charakter_manager_2 = input("Wybierz którą broń chcesz założyć\n")
            print()
            if charakter_manager_2 in self.weapons_short_distance_warehouse.keys():
                if self.stamina <= math.fabs(self.weapons_short_distance_warehouse[charakter_manager_2].stamina):
                    print("Niestety, nie masz wystarczającej wytrzymałości, aby założyć ten przedmiot")
                else:
                    print(f"Pomyślnie założyłeś {self.weapons_short_distance_warehouse[charakter_manager_2].name}")
                    self.strenght -= self.weapons_short_distance_in_use.strenght
                    self.stamina -= self.weapons_short_distance_in_use.stamina
                    self.weapons_short_distance_in_use = self.weapons_short_distance_warehouse[charakter_manager_2]
                    self.strenght += self.weapons_short_distance_warehouse[charakter_manager_2].strenght
                    self.stamina += self.weapons_short_distance_warehouse[charakter_manager_2].stamina
                    print()
            elif charakter_manager_2 == "cofnij":
                break
            else:
                print(f"Nie posiadasz takiej broni w magazynie")
                continue

    def choice_long_distance_weapon(self):
        while True:
            print(
                f"Znajdujesz się w magazynie broni długodystansowej. Obecnie w użyciu masz "
                f"{self.weapons_long_distance_in_use.name}.\n")
            print(f"Obecnie posiadasz następującą broń długodystansową w magazynie:")
            for arg in self.weapons_long_distance_warehouse.values():
                print(f"{arg.name} - siła dalekiego dystansu: {arg.strenght_long} - wytrzymałość: {arg.stamina} - "
                      f"cena: {arg.price}")
            print(f"cofnij - wróć do menadżera postaci\n")
            charakter_manager_2 = input("Wybierz którą broń chcesz założyć\n")
            print()
            if charakter_manager_2 in self.weapons_long_distance_warehouse.keys():
                print(f"Pomyślnie założyłeś {self.weapons_long_distance_warehouse[charakter_manager_2].name}")
                self.strenght_long -= self.weapons_long_distance_in_use.strenght_long
                self.weapons_long_distance_in_use = self.weapons_long_distance_warehouse[charakter_manager_2]
                self.strenght_long += self.weapons_long_distance_warehouse[charakter_manager_2].strenght_long
                print()
            elif charakter_manager_2 == "cofnij":
                break
            else:
                print(f"Nie posiadasz takiej broni w magazynie")
                continue

    def choice_helment(self):
        while True:
            print(f"Znajdujesz się w magazynie hełmów. Obecnie w użyciu masz {self.helmet_in_use.name}.\n")
            print(f"Obecnie posiadasz następujące hełmy w magazynie:")
            for arg in self.helmet_warehouse.values():
                print(f"{arg.name} - defensywa: {arg.defence} - wytrzymałość: {arg.stamina} - cena: {arg.price}")
            print(f"cofnij - wróć do menadżera postaci\n")
            charakter_manager_2 = input("Wybierz który hełm chcesz założyć\n")
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
            elif charakter_manager_2 == "cofnij":
                break
            else:
                print(f"Nie posiadasz takiego hełmu w magazynie")
                continue

    def choice_armor(self):
        while True:
            print(f"Znajdujesz się w magazynie zbroi. Obecnie w użyciu masz {self.armor_in_use.name}.\n")
            print(f"Obecnie posiadasz następujące zbroje w magazynie:")
            for arg in self.armor_warehouse.values():
                print(f"{arg.name} - defensywa: {arg.defence} - wytrzymałość: {arg.stamina} - cena: {arg.price}")
            print(f"cofnij - wróć do menadżera postaci\n")
            charakter_manager_2 = input("Wybierz którą zbroję chcesz założyć\n")
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
            elif charakter_manager_2 == "cofnij":
                break
            else:
                print(f"Nie posiadasz takiej zbroi w magazynie")
                continue

    def choice_shield(self):
        while True:
            print(f"Znajdujesz się w magazynie tarcz. Obecnie w użyciu masz {self.shield_in_use.name}.\n")
            print(f"Obecnie posiadasz następujące tarcze w magazynie:")
            for arg in self.shield_warehouse.values():
                print(f"{arg.name} - defensywa: {arg.defence} - wytrzymałość: {arg.stamina} - cena: {arg.price}")
            print(f"cofnij - wróć do menadżera postaci\n")
            charakter_manager_2 = input("Wybierz którą tarczę chcesz założyć\n")
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
            elif charakter_manager_2 == "cofnij":
                break
            else:
                print(f"Nie posiadasz takiej tarczy w magazynie")
                continue

    def charakter_manager(self):
        while True:
            print(f"Znajdujesz się w menadżerze postaci. Wybierz co chcesz zrobić:\n"
                  f"1. Sprawdź ilość złota\n"
                  f"2. Sprawdź swoje umiejętności\n"
                  f"3. Sprawdź swoje założone uzbrojenie\n"
                  f"4. Wybierz broń krótkodystansową\n"
                  f"5. Wybierz broń długodystansową\n"
                  f"6. Wybierz hełm\n"
                  f"7. Wybierz zbroję\n"
                  f"8. Wybierz tarczę\n"
                  f"9. Wyjdź z menadżera postaci\n")
            character_manager_1 = int(input())
            print()
            if character_manager_1 == 1:
                self.gladiator_gold()
            elif character_manager_1 == 2:
                self.gladiator_skills()
            elif character_manager_1 == 3:
                self.gladiator_equipment_in_use()
            elif character_manager_1 == 4:
                self.choice_short_distance_weapon()
            elif character_manager_1 == 5:
                self.choice_long_distance_weapon()
            elif character_manager_1 == 6:
                self.choice_helment()
            elif character_manager_1 == 7:
                self.choice_armor()
            elif character_manager_1 == 8:
                self.choice_shield()
            elif character_manager_1 == 9:
                break
            else:
                print(f"Wybrałeś nieprawidłową wartość. Wpisz poprawną!")
                continue


class OpponentGladiator(Gladiator):
    def __init__(self, strenght, strenght_long, stamina, technik_short_distanse_fight,
                 technik_long_distanse_fight, defence):
        super().__init__(strenght, strenght_long, stamina, technik_short_distanse_fight,
                         technik_long_distanse_fight, defence)
