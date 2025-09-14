import random
import time
import json
import os

HIGH_SCORE_FILE = "high_scores.json"

# ----------------------------
# Helper functions for High Scores
# ----------------------------
def load_high_scores():
    if not os.path.exists(HIGH_SCORE_FILE):
        return {"hangman_wins": 0, "slots_high_balance": 0}
    with open(HIGH_SCORE_FILE, "r") as f:
        return json.load(f)

def save_high_scores(scores):
    with open(HIGH_SCORE_FILE, "w") as f:
        json.dump(scores, f)

# ----------------------------
# Hangman Game
# ----------------------------
words = ("loki", "thor", "michael", "finn", "soldier")
hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\")
}

def hangman(high_score):
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()

    print("\n🎯 Welcome to Hangman!\n")

    while True:
        print("**********")
        for line in hangman_art[wrong_guesses]:
            print(line)
        print("**********")
        print("Word: " + " ".join(hint))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            print("**********")
            print(" ".join(hint))
            print("🎉 YOU WIN!!")
            high_score += 1
            print(f"Your total Hangman wins: {high_score}")
            break
        elif wrong_guesses >= len(hangman_art) - 1:
            print("**********")
            print(" ".join(answer))
            print("💀 GAME OVER! Better luck next time!")
            print(f"Your total Hangman wins: {high_score}")
            break

    return high_score

# ----------------------------
# Slot Machine Game
# ----------------------------
symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

def spin_row():
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒": return bet * 3
        if row[0] == "🍉": return bet * 4
        if row[0] == "🍋": return bet * 5
        if row[0] == "🔔": return bet * 10
        if row[0] == "⭐": return bet * 20
    return 0

def slots(high_score):
    balance = 100
    max_balance = balance
    print("\n🎰 Welcome to Big Island Slots! 🍒🍉🍋🔔⭐")
    while balance > 0:
        print(f"\nCurrent Balance: R{balance:.2f}")
        bet = input("Place your bet: R")
        if not bet.isdigit():
            print("Please enter a valid number.")
            continue
        bet = int(bet)
        if bet > balance or bet <= 0:
            print("Invalid bet amount.")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning...\n")
        time.sleep(1)
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"Congrats! You won R{payout}.")
        else:
            print("Sorry, try again!")

        balance += payout
        if balance > max_balance:
            max_balance = balance

        play_again = input("Play again? (Y/N): ").upper()
        if play_again != "Y":
            break

    print(f"💰 Your ending balance: R{balance:.2f}")
    print(f"🏆 Highest balance this session: R{max_balance:.2f}")
    high_score = max(high_score, max_balance)
    return high_score

# ----------------------------
# Main Arcade Menu
# ----------------------------
def main():
    high_scores = load_high_scores()

    while True:
        print("\n🌟 Welcome to Python Arcade 🌟")
        print("1. Hangman")
        print("2. Slots")
        print("3. View High Scores")
        print("4. Exit")
        choice = input("Choose your game: ")

        if choice == "1":
            high_scores["hangman_wins"] = hangman(high_scores["hangman_wins"])
            save_high_scores(high_scores)
        elif choice == "2":
            high_scores["slots_high_balance"] = slots(high_scores["slots_high_balance"])
            save_high_scores(high_scores)
        elif choice == "3":
            print("\n🏅 High Scores")
            print(f"Hangman Wins: {high_scores['hangman_wins']}")
            print(f"Slots Highest Balance: R{high_scores['slots_high_balance']:.2f}")
        elif choice == "4":
            print("Thanks for playing at Python Arcade! Mahalo!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
