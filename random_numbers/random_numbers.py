#   Generating Random Numbers

import random

#   Rolling a six-sided dice
"""
number = random.randint(1, 6)
print(number)
"""

#   Random int within variable range
"""
low = 1
high = 25
number = random.randint(low, high)
print(number)
"""

#   Random float between 0.0 and 1.0
"""
number = random.random()
print(number)
"""

#   Random choice from a sequence
"""
options = ("Rock", "Paper", "Scissor")
option = random.choice(options)
print(option)
"""

#   Shuffle a list
"""
cards = ["2", "4", "6", "8", "10", "Jack", "Queen", "King", "Ace"]
random.shuffle(cards)
print(cards)
"""

#   EXERCISE - NUMBER GUESSING GAME
low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Please take a guess between ({low} and {high}): "))
    guesses += 1

    if guess < number:
        print(f"{guess} is too low.")
    elif guess > number:
        print(f"{guess} is too high.")
    else:
        print(f"Hey. Your guess of {guess} is spot on. Well Done!!!!")
        break

print(f"This round took you {guesses} guesses")
