# Credit Card Validator Program
# Algorithm = Luhn Algorithm
# Steps:
#   1. Remove any "-" or " "
#   2. Reverse the card number
#   3. Add all digits in the odd places from right to left
#   4. Double every second digit from right to left
#        (if result >= 10, split digits and add them)
#   5. Sum totals from step 3 & 4
#   6. If sum % 10 == 0 → Valid

# ------------------------------
# Step 1: Get and clean input
# ------------------------------
card_number = input("Please enter a credit card number: ")
card_number = card_number.replace("-", "").replace(" ", "")
card_number = card_number[::-1]  # reverse string

# ------------------------------
# Step 2: Process odd digits
# ------------------------------
sum_odd_digits = 0
for x in card_number[::2]:
    sum_odd_digits += int(x)

# ------------------------------
# Step 3: Process even digits
# ------------------------------
sum_even_digits = 0
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))  # same as sum(map(int, str(x)))
    else:
        sum_even_digits += x

# ------------------------------
# Step 4: Final total
# ------------------------------
total = sum_odd_digits + sum_even_digits

# ------------------------------
# Step 5: Check validity
# ------------------------------
if total % 10 == 0:
    print("✅ This is a valid credit card number")
else:
    print("❌ This is an invalid credit card number")
