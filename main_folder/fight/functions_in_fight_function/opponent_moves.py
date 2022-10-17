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
