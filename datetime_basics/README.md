## Working with Dates and Times in Python 📅⏰

Python’s `datetime` module allows you to create, format, and compare dates and times.

---

### 1. Creating Dates and Times

```python
import datetime

date = datetime.date(2025, 6, 24)   # Specific date
today = datetime.date.today()       # Current date

time = datetime.time(23, 59, 59)    # Specific time
now = datetime.datetime.now()       # Current date + time

Formatting Dates and Times (-> Strings)
Use strftime() to format:

formatted = now.strftime("%H:%M:%S %m/%d/%Y")
print(formatted)   # e.g. "19:45:30 09/15/2025"
