#   Python Number Guessing Game

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Aloha, Welcome to the Number Guessing Game!")
print(f"Please take your best shot between {lowest_num} and {highest_num}:")

while is_running:
    guess = input("Please enter your choice: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("I am sorry but that guess is not in the range")
            print(f"Please take another shot between {lowest_num} and {highest_num}:")
        elif guess < answer:
            print("Your guess is too low!! Please try again.")
        elif guess > answer:
            print("Your guess is too high!! Please try again.")
        else:
            print(f"Spot On!! Your guess of {guess} is correct")
            print(f"You took {guesses} guesses to get the correct answer!!")
            print("Thank you for playing!\nMahalo")
            is_running = False
    else:
        print("I am sorry but that is an invalid guess.")
        print(f"Please take another shot between {lowest_num} and {highest_num}:")
