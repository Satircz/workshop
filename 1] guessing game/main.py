from random import randint


def guessing_game():
    random_number = randint(1, 100)
    print(random_number)
    """Vytiskne vybrané číslo,
     pro kontrolu při psaní kodů
    """
    while True:
        try:
            guess_number: int = int(input("\nPlease, insert your guess number from 1-100: "))
        except ValueError:
            print("is not a number, guess number again!")
            continue
"""
zjistí, zda je číslo int. pokud ne, vrátí nás k zadání čísla
"""
        print(f"Your guessed number is {guess_number}.")
        if guess_number < random_number:
            print("Too small!, try again!")
        elif guess_number > 100:
            print("You are out of range, choose 1-100!")
        elif guess_number > random_number:
            print("Too Big!Try again")
        elif guess_number == random_number:
            print(f"Guessed number was {guess_number} and you Win")
            while True:
                play_again = input("Do you want play again ? Y/N: ")
                cap_play_again = play_again.capitalize()
                if cap_play_again == "Y":
                    random_number = randint(1, 100)
                    print(f"\n{random_number}")
                    """Vytiskne vybrané číslo,
                     pro kontrolu při psaní kodů
                    """
                    guess_number = None
                elif cap_play_again == "N":
                    print("Thank you, Bye Bye")
                    break
                else:
                    print("invalid input, please input Y or N")
                    continue

guessing_game()

