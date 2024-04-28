import random

def get_user_numbers():
    user_numbers = []
    while len(user_numbers) < 6:
        user_input = input("Enter a number (1-49): ")
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue
        number = int(user_input)
        if number < 1 or number > 49:
            print("Number must be in the range of 1-49.")
            continue
        if number in user_numbers:
            print("Number already entered.")
            continue
        user_numbers.append(number)
    user_numbers.sort()
    return user_numbers

def generate_lottery_numbers():
    return sorted(random.sample(range(1, 50), 6))

def check_matching_numbers(user_numbers, lottery_numbers):
    matches = 0
    for num in user_numbers:
        if num in lottery_numbers:
            matches += 1
    return matches

def main():
    print("Welcome to the LOTTO game!")
    print("Please enter 6 numbers.")

    user_numbers = get_user_numbers()
    print("Your numbers:", user_numbers)

    lottery_numbers = generate_lottery_numbers()
    print("Lottery numbers:", lottery_numbers)

    matched_numbers = check_matching_numbers(user_numbers, lottery_numbers)
    print("You have matched", matched_numbers, "numbers.")

if __name__ == "__main__":
    main()