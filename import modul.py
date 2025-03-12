from datetime import datetime, timedelta

# i. Print date, time for today and now
now = datetime.now()
print(f"Current date and time: {now}")

# ii. Add some days to your present date and print the date added
days_to_add = 5  # Change this to the number of days you want to add
new_date = now + timedelta(days=days_to_add)
print(f"Date after adding {days_to_add} days: {new_date}")

# iii. Print date, time using date and time functions
current_date = now.date()
current_time = now.time()
print(f"Current date using date function: {current_date}")
print(f"Current time using time function: {current_time}")
