import random

print("Welcome in LOTTO GAME")
name = input("Enter your name: ")
print(f"Hi {name}, you need to choose 6 numbers from 1 to 49. Can you guess all 6?")

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

print(guess_numbers())
def lotto():
    return sorted(random.sample(range(1, 50), 6))

print(lotto())

# user_ressult = guess_numbers()
# lotto_ressult = lotto()
#
# def ressult():
#     matched_numbers: int = 0
#     for num in user_ressult:
#         if num in lotto_ressult:
#             matched_numbers += 1
#     return matched_numbers
#
# ressult(user_ressult, lotto_ressult)
# print(ressult)

