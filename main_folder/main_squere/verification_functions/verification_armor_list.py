from ...classes_gladiator.class_user_gladiator import UserGladiator


def verification_armor_list(equipment_list: list, action: str, gladiator: UserGladiator) -> None:
    for arg in equipment_list:
        if arg.name == action.capitalize():
            if gladiator.gold < arg.price:
                print("Niestety nie masz wystarczającej ilości złota.")
            else:
                gladiator.armor_warehouse[arg.name] = arg
                gladiator.gold -= arg.price
                print(f"Pomyślnie kupiłeś przedmiot {arg.name}.")
                print()
