#  Python compound interest calculator

""""
principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Please enter the principle amount: "))
    if principle <= 0:
        print("Please enter a positive principle number: ")

while rate <= 0:
    rate = float(input("Please enter the interest rate: "))
    if rate <= 0:
        print("Please enter a positive interest rate: ")

while time <= 0:
    time = int(input("Please enter the time period: "))
    if time <= 0:
        print("Please enter a positive time period: ")

total = principle * pow((1 + rate/100), time)

print(f"Here is your compound report:\n"
      f"For your investment of ${principle: .2f}\n"
      f"at an interest rate of {rate}%\n"
      f"over the span of {time} year/s,\n"
      f"Your new balance will be: ${total: .2f}")
"""


#   If you take out the = sign as value to 0,
#   it will say 0 for all values as loop is false from get go
#   and we never enter the while loop body.
#   by stating the while to be True, enters the loop and if the negative numbered enter, the break
#   function, gets out loop and move to next one. So below you can enter 0 as a value


principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Please enter the principle amount: "))
    if principle < 0:
        print("Please enter a positive principle number: ")
    else:
        break

while True:
    rate = float(input("Please enter the interest rate: "))
    if rate < 0:
        print("Please enter a positive interest rate: ")
    else:
        break

while True:
    time = int(input("Please enter the time period: "))
    if time < 0:
        print("Please enter a positive time period: ")
    else:
        break

total = principle * pow((1 + rate / 100), time)

print(f"Here is your compound report:\n"
      f"For your investment of ${principle: .2f}\n"
      f"at an interest rate of {rate}%\n"
      f"over the span of {time} year/s,\n"
      f"Your new balance will be: ${total: .2f}")
