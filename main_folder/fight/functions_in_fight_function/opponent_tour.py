import random
from main_folder.classes_gladiator.class_opponent_gladiator import OpponentGladiator
from main_folder.classes_gladiator.class_user_gladiator import UserGladiator
from main_folder.fight.functions_in_fight_function.opponent_moves import opponent_move_left, opponent_move_right


def opponent_tour(opponent: OpponentGladiator, distance_list, gladiator: UserGladiator):
    opponent_choice: int = random.randint(1, 3)
    if opponent_choice == 1:
        if opponent.stamina_in_fight < 10:
            opponent.stamina_in_fight += 30
            print("Przeciwnik odpoczywa.")
        else:
            opponent_move_left(distance_list)
            opponent.stamina_in_fight -= 10
    elif opponent_choice == 2:
        if opponent.stamina_in_fight < 10:
            opponent.stamina_in_fight += 30
            print("Przeciwnik odpoczywa.")
        else:
            opponent_move_right(distance_list)
            opponent.stamina_in_fight -= 10
    else:
        if opponent.stamina_in_fight < 10:
            opponent.stamina_in_fight += 30
            print("Przeciwnik odpoczywa.")
        else:
            user_distance = distance_list.index("O") - distance_list.index("Y")
            attack_multiplier_op: float = random.randint(5, 15) / 10
            fight_user_variable_op = random.randint(1, 15)
            fight_opponent_variable_op = random.randint(1, 10)
            if user_distance > 1:
                opponent_attack_chance = opponent.technik_long_distance_fight / fight_opponent_variable_op
                user_defence = gladiator.defence / fight_user_variable_op
                if opponent_attack_chance >= user_defence:
                    gladiator.health_in_fight -= opponent.strength_long * attack_multiplier_op
                    print("Przeciwnik przeprowadził udany atak z dystansu na Ciebie!")
                else:
                    print("Uniknąłeś ataku przeciwnika")
            else:
                opponent_attack_chance = opponent.technik_short_distance_fight / fight_opponent_variable_op
                user_defence = gladiator.defence / fight_user_variable_op
                if opponent_attack_chance >= user_defence:
                    gladiator.health_in_fight -= opponent.strength * attack_multiplier_op
                    print("Przeciwnik przeprowadził udany atak na Ciebie!")
                else:
                    print("Uniknąłeś ataku przeciwnika")
                opponent.stamina_in_fight -= 20
