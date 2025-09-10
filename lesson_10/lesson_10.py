# Conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          x if condition else y

num = 9
a = 6
b = 7
age = 21
temperature = 33
user_role = "admin"

# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Minor"
# weather = "Hot as Balls" if temperature > 20 else "Its good outside"

access_level = "Full Access" if user_role == "admin" else "Restricted Access"

print(access_level)
