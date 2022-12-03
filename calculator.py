import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

math = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
if math == '1':
    logging.info("Wykonujemy dodawanie!")
    number = input("Podaj składnik 1.")
    number_two = input("Podaj składnik 2.")
    logging.debug(f"Dodaje {number} i {number_two} ")
    sum = int(number) + int(number_two)
    print(f"Wynik to {sum}")
    choice = input("Czy chcesz dorzucić jeszcze jeden składnik? Y/N: ")
    if choice == 'y':
        number_three = input("Podaj składnik 3.")
        logging.debug(f"Dodaje składnik 3. {number_three} do przprzedniej sumy {sum} ")
        secondsum = int(sum) + int(number_three)
        print(f"Nowy wynik to {secondsum}")
    elif choice == 'n':
        exit(1)
if math == '2':
    logging.info("Wykonujemy odejmowanie!")
    number = input("Podaj składnik 1.")
    number_two = input("Podaj składnik 2.")
    print(f"Odejmuje {number} i {number_two} ")
    diff = int(number) - int(number_two)
    print(f"Wynik to {diff}")
if math == '3':
    logging.info("Wykonujemy mnożenie!")
    number = input("Podaj składnik 1.")
    number_two = input("Podaj składnik 2.")
    print(f"Mnoże {number} i {number_two} ")
    mult = int(number) * int(number_two)
    print(f"Wynik to {mult}")
if math == '4':
    logging.info("Wykonujemy dzielenie!")
    number = input("Podaj składnik 1.")
    number_two = input("Podaj składnik 2.")
    print(f"Dzielę {number} i {number_two} ")
    div = int(number) / int(number_two)
    print(f"Wynik to {div}")
if math == 5:
    logging.error("Nie ma takiej funkcji!!")
    
