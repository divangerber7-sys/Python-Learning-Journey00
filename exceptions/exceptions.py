# Exception Handling in Python
# An exception is an event that interrupts the normal flow of a program.
# Examples: ZeroDivisionError, TypeError, ValueError, etc.

# ---------------- TRY / EXCEPT ----------------
try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("❌ You can't divide by zero")
except ValueError:
    print("❌ You didn't enter a valid number")
except Exception as e:
    print(f"❌ Something went wrong: {e}")
finally:
    print("✅ Goodbye - this will always run")
