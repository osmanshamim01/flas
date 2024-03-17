import datetime

# Get the current system time
current_time = datetime.datetime.now()

# Format the time as "YYYY-MM-DD HH:MM:SS"
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# Print the formatted time
print(f"The current system time is {formatted_time}")