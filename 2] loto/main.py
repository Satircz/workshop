import random




def guess_numbers() -> object:
    user_numbers = []
    while len(user_numbers) < 6:
        user_guess = input("Guess number from 1 to 49: ")

        if not user_guess.isdigit():
            print("You need enter a valid number.")
            continue
        number = int(user_guess)
        if number < 1 or number > 49:
            print("You need enter number from 1-49")
            continue
        if number in user_numbers:
            print("your number is already guessed")
            continue
        user_numbers.append(number)
        user_numbers.sort()
    return user_numbers


def lotto():
    lotto_numbers = sorted(random.sample(range(1, 50), 6))
    return lotto_numbers


def result():
    user_numbers = guess_numbers()
    print(f"User Numbers: {user_numbers}")
    lotto_numbers = lotto()
    print(f"LOTTO Numbers: {lotto_numbers}")
    matched_numbers: int = 0
    for num in user_numbers:
        if num in lotto_numbers:
            matched_numbers += 1
    return f"You get {matched_numbers} from {lotto_numbers}"


if __name__ == "__main__":
    print("Welcome in LOTTO GAME")
    name = input("Enter your name: ")
    print(f"Hi {name}, you need to choose 6 numbers from 1 to 49. Can you guess all 6?")
    print(result())

