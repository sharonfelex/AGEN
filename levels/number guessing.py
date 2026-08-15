import random

computer_number = random.randint(1, 10)
attempts = 0
while True:
    user_number = int(input("Enter a number: "))
    attempts += 1

    if computer_number == user_number:
        print("You guessed the number correctly!")
        break


    elif computer_number > user_number:
        print("more, try again.")

    elif computer_number < user_number:
        print("less, try again.")

print(f"You guessed the number in {attempts} attempts.")