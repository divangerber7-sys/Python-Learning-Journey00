"""
Lesson: Working with Dates and Times in Python
----------------------------------------------
Covers creating, formatting, and comparing dates/times
using the datetime module.
"""

import datetime

# --- 1. Creating date, time, and datetime objects ---
date = datetime.date(2025, 6, 24)          # Specific date
today = datetime.date.today()              # Current date

time = datetime.time(hour=23, minute=59, second=59)  # Specific time
now = datetime.datetime.now()              # Current date and time

print("Specific date:", date)
print("Today:", today)
print("Specific time:", time)
print("Now (datetime object):", now)


# --- 2. Formatting datetime objects into strings ---
formatted_now = now.strftime("%H:%M:%S %m/%d/%Y")
print("Formatted datetime:", formatted_now)


# --- 3. Parsing strings into datetime objects ---
date_string = "15/09/2025 19:45:30"
parsed_date = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M:%S")
print("Parsed datetime:", parsed_date)


# --- 4. Comparing dates and times ---
target_datetime = datetime.datetime(2025, 6, 24, 23, 59, 59)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("⏰ Target date has passed")
else:
    print("⌛ Target date has not passed yet")


# --- 5. Doing date math (timedelta) ---
deadline = datetime.date(2025, 12, 31)
days_remaining = deadline - today
print(f"Days remaining until {deadline}: {days_remaining.days}")
