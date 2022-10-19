from main_folder import texts
from main_folder.classes_gladiator.class_user_gladiator import UserGladiator
from main_folder.classes_gladiator.opponent_object import opponent
from main_folder.fight.fight import fight
from main_folder.fight.fight_result_function import result_1_fight
from main_folder.main_squere.main_squere_function import main_squere
from main_folder.new_skills_function.new_skills_function import new_skills_choice


texts.welcome_text()

user_name = input()
user_gladiator = UserGladiator(user_name)

texts.start_text(gladiator=user_gladiator)

user_gladiator.new_skill = 7
new_skills_choice(gladiator=user_gladiator)

print()

user_gladiator.gladiator_skills()

texts.first_fight_text(gladiator=user_gladiator)

fight_1_result = fight(gladiator=user_gladiator, opponent=opponent.level_1_opponent)
result_1_fight(result=fight_1_result, gladiator=user_gladiator, opponent=opponent.level_1_opponent)

main_squere(gladiator=user_gladiator,
            opponent_1=opponent.secondary_opponent_level_1_no1,
            opponent_2=opponent.secondary_opponent_level_1_no2,
            opponent_3=opponent.secondary_opponent_level_1_no3,
            main_opponent=opponent.level_2_opponent
            )

texts.after_2_opponent_text_1(gladiator=user_gladiator)
user_gladiator.win_the_fight(opponent=opponent.level_2_opponent)
new_skills_choice(gladiator=user_gladiator)
texts.after_2_opponent_text_2()

main_squere(gladiator=user_gladiator,
            opponent_1=opponent.secondary_opponent_level_2_no1,
            opponent_2=opponent.secondary_opponent_level_2_no2,
            opponent_3=opponent.secondary_opponent_level_2_no3,
            main_opponent=opponent.level_3_opponent
            )

texts.after_3_opponent_text_1(gladiator=user_gladiator)
user_gladiator.win_the_fight(opponent=opponent.level_3_opponent)
new_skills_choice(gladiator=user_gladiator)
texts.after_3_opponent_text_2()

main_squere(gladiator=user_gladiator,
            opponent_1=opponent.secondary_opponent_level_3_no1,
            opponent_2=opponent.secondary_opponent_level_3_no2,
            opponent_3=opponent.secondary_opponent_level_3_no3,
            main_opponent=opponent.level_4_opponent
            )

texts.after_4_opponent_text_1(gladiator=user_gladiator)
user_gladiator.win_the_fight(opponent=opponent.level_4_opponent)
new_skills_choice(gladiator=user_gladiator)
texts.after_4_opponent_text_2()

main_squere(gladiator=user_gladiator,
            opponent_1=opponent.secondary_opponent_level_4_no1,
            opponent_2=opponent.secondary_opponent_level_4_no2,
            opponent_3=opponent.secondary_opponent_level_4_no3,
            main_opponent=opponent.level_5_opponent
            )

texts.end_text(gladiator=user_gladiator)
stop = input("Kliknij enter aby wyjść")
