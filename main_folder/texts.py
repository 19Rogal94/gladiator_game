from main_folder.classes_gladiator.class_user_gladiator import UserGladiator
from main_folder.classes_gladiator.opponent_object import opponent


def welcome_text():
    print("Witaj nieznajomy, mam dla ciebie dobrą i złą wiadomość. Ale zanim przejdę do rzeczy, powiedz jak się "
          "nazywasz?")


def first_fight_text(gladiator: UserGladiator):
    print(f"{gladiator.username}, twoja pierwsza walka zaczyna się właśnie teraz!")


def start_text(gladiator: UserGladiator):
    print(f"No więc {gladiator.username}, zostałeś pojmany w przegranej bitwie. Jesteś rosłym wojownikiem, zatem"
          f" dajemy Ci szanse odzyskać wolność. Będziesz musiał stoczyć szereg walk w konkursie gladiatorów. \n"
          f"Pierwszą walkę zaczynasz za chwilę. Na samym początku będziesz wyposażony jedynie w pięści i kamienie, "
          f"które znajdziesz pod nogami. Za każdą walkę będziesz otrzymywać pieniądze, \n"
          f"które możesz wydać zarówno na uzbrojenie, jak i na treningi. Pamiętaj, że z czasem twoi przeciwnicy będą "
          f"coraz silniejsi. No więc właśnie teraz zaczyna się twoja gladiatorska przygoda. \n"
          f"Powodzenia! Przyda się")
    print("...")
    print("Na sam początek rozdysponuj swoje umiejętności. Do rozdysponowania masz 7 umiejętności w następujących \n"
          "umiejętnościach: siła, wytrzymałość, technika walki na krótkim dystansie, technika walki na dalekim "
          "dystansie, uniki\n")


def after_2_opponent_text_1(gladiator: UserGladiator):
    print(f"Gratuluje {gladiator.username}! Pokonałeś już swojego drugiego przeciwnika i jesteś coraz bliższy "
          f"odzyskania wolności. Oczywiście w nagrodę za wygraną walkę otrzymujesz {opponent.level_2_opponent.gold} "
          f"złota oraz możesz rozdysponować swoje {opponent.level_2_opponent.new_skill} nowe umiejętności.\n")


def after_2_opponent_text_2():
    print("\nWracasz teraz do placu głównego. Przygotuj się do następnej walki!\n")


def after_3_opponent_text_1(gladiator: UserGladiator):
    print(f"{gladiator.username} ta walka była niesamowita. Coraz więcej ludzi chce przychodzić na twoje walki! "
          f"Zostało ci już dwóch oponentów do pokonania, jednak już nie będzie tak łatwo jak do tej pory. Trenuj "
          f"ciężko i nie poddawaj się! za tą wygraną otrzymujesz {opponent.level_3_opponent.gold} złota oraz kolejne "
          f"{opponent.level_3_opponent.new_skill} nowe umiejętności.\n")


def after_3_opponent_text_2():
    print("\nCoś czuję, że na placu głównym fani nie dadzą Ci spokoju. Ale musisz na niego wrócić.\n")


def after_4_opponent_text_1(gladiator: UserGladiator):
    print(f"To był twój przedostatni główny przeciwnik. Chyba na długo zapamięta tą walkę. Skup się została już "
          f"tylko jedna walka. {gladiator.username} dzieli cię już tylko krok od wolności i wieczej chwały. "
          f"Za tą walkę otrzymujesz {opponent.level_4_opponent.gold} złota i {opponent.level_4_opponent.new_skill} "
          f"nowe umiejętności.\n")


def after_4_opponent_text_2():
    print("\nMiejmy nadzieję, że już ostatni raz wracasz na ten plac...\n")


def end_text(gladiator: UserGladiator):
    print(f"{gladiator.username}! {gladiator.username}! {gladiator.username}! Tłum skanduje twoje imię. "
          f"Jesteś wolnym człowiekiem! Ponadto dzięki sławie nie musiśz się już martwić o swoją przyszłość. Ludzie cię "
          f"uwielbiają. Gratulujemy. Skończyłeś grę!")
    print("=" * 34 + "koniec gry " + "=" * 34)
