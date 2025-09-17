# Higher-order functions
# filter(function, collection) = returns all elements that pass a condition

# Example 1: Using a named function
def is_passing(grade):
    return grade >= 60

grades = [90, 32, 83, 44, 75, 56, 67]

# Using filter with a named function
passing_grades = filter(is_passing, grades)
passing_grades = list(filter(is_passing, grades))

print("Passing grades (with named function):")
for grade in passing_grades:
    print(grade)

# Example 2: Using a lambda function
passing_grades = list(filter(lambda grade: grade >= 60, grades))

print("\nPassing grades (with lambda):")
print(passing_grades)


if __name__ == "__main__":
    # Quick check
    print("\nQuick rerun with lambda only:")
    print(list(filter(lambda g: g >= 60, grades)))
