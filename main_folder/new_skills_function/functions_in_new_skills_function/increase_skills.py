from main_folder.classes_gladiator.class_user_gladiator import UserGladiator


def increase_strength(gladiator: UserGladiator) -> None:
    gladiator.strenght += 1
    print("Dodano 1 do siły")


def increase_stamina(gladiator: UserGladiator) -> None:
    gladiator.stamina += 1
    print("Dodano 1 do wytrzymałości")


def increase_technik_short_distance_fight(gladiator: UserGladiator) -> None:
    gladiator.technik_short_distanse_fight += 1
    print("Dodano 1 do techniki walki na krótkie dystanse")


def increase_technik_long_distance_fight(gladiator: UserGladiator) -> None:
    gladiator.technik_long_distanse_fight += 1
    print("Dodano 1 do techniki walki na długim dystanse")


def increase_defence(gladiator: UserGladiator) -> None:
    gladiator.defence += 1
    print("Dodano 1 do uników")
