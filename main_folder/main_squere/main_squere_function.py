from .other_functions_in_main_squere.main_fight import main_fight
from .other_functions_in_main_squere.secondary_fight import secondary_fight_in_squere
from .other_functions_in_main_squere.training_with_personal_trainer import training_with_personal_trainer
from .shops_functions.armor_shop import armor_shop
from ..classes_gladiator.class_opponent_gladiator import OpponentGladiator
from ..classes_gladiator.class_user_gladiator import UserGladiator
from .shops_functions.weapon_shop import weapon_shop


def main_squere(gladiator: UserGladiator, opponent_1: OpponentGladiator, opponent_2: OpponentGladiator,
                opponent_3: OpponentGladiator, main_opponent: OpponentGladiator) -> None:
    while True:
        print("Znajdujesz się na głównym placu. Oto miejsca, gdzie możesz się udać:\n"
              "1. Sklep z bronią (kupisz tutaj broń, która pomoże Ci w walce)\n"
              "2. Sklep z uzbrojenie (kupisz tutaj uzbrojenie, które wpłynie na twoje zdolności defensywne)\n"
              "3. Trening z trenerem ogólnorozwojowym (dwie nowe umiejętność - koszt 200 złota)\n"
              "4. Menadżer postaci (możesz tutaj użyć zakupionego wyposażenia)\n"
              "5. Walka poboczna (za stoczoną walkę możesz zarobić złoto)\n"
              "6. Walka główna turnieju (pokonaj następnego rywala z listy\n")
        action = input("Wybierz, co chcesz zrobić: \n")
        print()
        if action == "1":
            weapon_shop(gladiator=gladiator)
        elif action == "2":
            armor_shop(gladiator=gladiator)
        elif action == "3":
            training_with_personal_trainer(gladiator=gladiator)
        elif action == "4":
            gladiator.charakter_manager()
        elif action == "5":
            secondary_fight_in_squere(opponent_1=opponent_1, opponent_2=opponent_2,
                                      opponent_3=opponent_3, gladiator=gladiator)
        elif action == "6":
            main_fight_result = main_fight(gladiator=gladiator, opponent=main_opponent)
            if main_fight_result == "Win":
                break
            else:
                print(f"Przegrałeś walkę z przeciwnikiem. Musisz jeszcze podszkolić swoje umiejętności lub"
                      f"pomyśleć o lepszym wyposażeniu. {gladiator.username} nie poddawaj się!")
        else:
            print("Wybrałeś nieprawidłową wartość. Wpisz poprawną!")
            continue
