from main_folder.classes_gladiator.class_user_gladiator import UserGladiator


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
