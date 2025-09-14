# Match-case statement (switch): An alternative to using many "elif" statements
#                                Execute some code if a value matches a "case"
#                                Benefits: cleaner, easier to read syntax

# Example 1: Classic if-elif-else chain
def day_of_week_if(day):
    if day == 1:
        return "It is Sunday"
    elif day == 2:
        return "It is Monday"
    elif day == 3:
        return "It is Tuesday"
    elif day == 4:
        return "It is Wednesday"
    elif day == 5:
        return "It is Thursday"
    elif day == 6:
        return "It is Friday"
    elif day == 7:
        return "It is Saturday"
    else:
        return "Not a valid day"

print("If-elif version:", day_of_week_if(7))

# Example 2: Using match-case (cleaner)
def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Not a valid day"

print("Match-case version:", day_of_week(7))

# Example 3: Match with multiple conditions (using | operator)
def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return "Not a valid day"

print("Is weekend (Friday?):", is_weekend("Friday"))
print("Is weekend (Sunday?):", is_weekend("Sunday"))
