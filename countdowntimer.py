import datetime
import time

def countdown_timer(target_date):
    while True:
        # Get the current time
        now = datetime.datetime.now()
        
        # Calculate the time difference
        time_left = target_date - now

        # If the target date has passed, exit the loop
        if time_left.total_seconds() <= 0:
            print("Countdown complete! The time has arrived!")
            break
        
        # Extract days, hours, minutes, and seconds from the time difference
        days = time_left.days
        hours = time_left.seconds // 3600
        minutes = (time_left.seconds % 3600) // 60
        seconds = time_left.seconds % 60
        
        # Print the remaining time
        print(f"Time remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", end="\r")
        
        # Wait for one second before updating
        time.sleep(1)

# Set your target date and time
# The format is: year, month, day, hour, minute, second
# Example: Christmas 2025 at midnight
target_datetime = datetime.datetime(2025, 12, 25, 0, 0, 0)

print(f"Starting countdown to {target_datetime}...")
countdown_timer(target_datetime)