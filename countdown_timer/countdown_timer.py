# COUNTDOWN TIMER

import time

# Example 1: Sleep for a few seconds
"""
time.sleep(5)
print("Time is Up good mam")
"""

# Example 2: Simple timer that counts up
"""
my_time = int(input("Please enter the time in seconds: "))

for x in range(0, my_time):
    print(x)
    time.sleep(1)

print("Time is up!!!!")
"""

# Example 3: Countdown (backwards)
"""
my_time = int(input("Please enter the time in seconds: "))

for x in range(my_time, 0, -1):
    print(x)
    time.sleep(1)

print("Time is up!!!!")
"""

# Example 4: Digital clock with seconds only
"""
my_time = int(input("Please enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    print(f"00:00:{seconds:02}")
    time.sleep(1)

print("Time is up!!!!")
"""

# Example 5: Digital clock with minutes + seconds
"""
my_time = int(input("Please enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    print(f"00:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time is up!!!!")
"""

# Example 6: Digital clock with hours + minutes + seconds
my_time = int(input("Please enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time is up!!!!")
