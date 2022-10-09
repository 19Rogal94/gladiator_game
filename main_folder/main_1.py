import fight_result_function
import texts
from class_gladiator import UserGladiator
from new_skills_function import new_skills_choice
from fight_function import fight
from main_squere_function import main_squere
from opponent import *


texts.welcome_text()

user_name = input()
user_gladiator = UserGladiator(user_name)

texts.start_text(gladiator=user_gladiator)

new_skill: int = 7
new_skills_choice(skill_point=new_skill, gladiator=user_gladiator)

print()

user_gladiator.gladiator_skills()

texts.first_fight_text(gladiator=user_gladiator)

fight_1_result = fight(gladiator=user_gladiator, opponent=level_1_opponent)
fight_result_function.result_1_fight(result=fight_1_result, gladiator=user_gladiator, opponent=level_1_opponent)

main_squere(gladiator=user_gladiator,
            opponent_1=secondary_opponent_level_1_no1,
            opponent_2=secondary_opponent_level_1_no2,
            opponent_3=secondary_opponent_level_1_no3,
            main_opponent=level_2_opponent
            )

texts.after_2_opponent_text_1(gladiator=user_gladiator)
user_gladiator.gold += 750
new_skill += 3
new_skills_choice(skill_point=new_skill, gladiator=user_gladiator)
texts.after_2_opponent_text_2()

main_squere(gladiator=user_gladiator,
            opponent_1=secondary_opponent_level_2_no1,
            opponent_2=secondary_opponent_level_2_no2,
            opponent_3=secondary_opponent_level_2_no3,
            main_opponent=level_3_opponent
            )

texts.after_3_opponent_text_1(gladiator=user_gladiator)
user_gladiator.gold += 1000
new_skill += 3
new_skills_choice(skill_point=new_skill, gladiator=user_gladiator)
texts.after_3_opponent_text_2()

main_squere(gladiator=user_gladiator,
            opponent_1=secondary_opponent_level_3_no1,
            opponent_2=secondary_opponent_level_3_no2,
            opponent_3=secondary_opponent_level_3_no3,
            main_opponent=level_4_opponent
            )

texts.after_4_opponent_text_1(gladiator=user_gladiator)
user_gladiator.gold += 1250
new_skill += 3
new_skills_choice(skill_point=new_skill, gladiator=user_gladiator)
texts.after_4_opponent_text_2()

main_squere(gladiator=user_gladiator,
            opponent_1=secondary_opponent_level_4_no1,
            opponent_2=secondary_opponent_level_4_no2,
            opponent_3=secondary_opponent_level_4_no3,
            main_opponent=level_5_opponent
            )

texts.end_text(gladiator=user_gladiator)
stop = input("Kliknij enter aby wyjść")
