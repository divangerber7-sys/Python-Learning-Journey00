#   Python Dice Roller Game
#   Using ASCII/Unicode art to render dice visually

import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"),
}

dice = []
total = 0

num_of_dice = int(input("Aloha.\nHow many dice would you like to roll? "))

# Roll dice
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# Print dice horizontally, side by side
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end=" ")
    print()

# Calculate total
for die in dice:
    total += die

print(f"\nThe total of your dice is: {total}")
print("Thank you for playing.\nMahalo")
