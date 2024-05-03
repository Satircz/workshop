import random


def user_input():
    possible_input = ["too small", "too big", "you win"]
    while True:
        user_answer = input().lower()
        if user_answer in possible_input:
            break
        print("Input is no in ['too small', 'too big', 'you win']")
    return user_answer


def guess_game():
    print("Think about a number from 0 to 1000 and let me guess it!")
    print("Write number and press 'Enter' to continue")
    input()
    min_number = 0
    max_number = 1000
    user_answer = ""
    while user_answer != "you win":
        guess = int((max_number - min_number) // 2 + min_number)
        print(f"Your number is: {guess}")
        user_answer = user_input()
        if user_answer == "too big":
            max_number = guess
        if user_answer == "too small":
            min_number = guess

    print("You Win!")



if __name__ == "__main__":
    print(guess_game())
