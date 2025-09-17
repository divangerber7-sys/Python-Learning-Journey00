# Recursion in Python
# A recursive function is a function that calls itself.
# Useful for breaking problems into smaller steps.

# ---------------- ITERATIVE WALK ----------------
def walk_iterative(steps):
    for step in range(1, steps + 1):
        print(f"You have taken step number {step}")

walk_iterative(5)  # Example


# ---------------- RECURSIVE WALK ----------------
def walk_recursive(steps):
    if steps == 0:  # base case
        return
    walk_recursive(steps - 1)  # recursive call
    print(f"You have taken step number {steps}")

walk_recursive(5)  # Example


# ---------------- FACTORIAL ITERATIVE ----------------
def factorial_iterative(n):
    result = 1
    if n > 0:
        for i in range(1, n + 1):
            result *= i
    return result

print("Factorial (iterative):", factorial_iterative(5))


# ---------------- FACTORIAL RECURSIVE ----------------
def factorial_recursive(n):
    if n == 1:  # base case
        return 1
    else:
        return n * factorial_recursive(n - 1)

print("Factorial (recursive):", factorial_recursive(5))
