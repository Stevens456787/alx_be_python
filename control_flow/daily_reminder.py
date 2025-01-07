# daily_reminder.py
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        priority_message = "high priority"
    case "medium":
        priority_message = "medium priority"
    case "low":
        priority_message = "low priority"
    case _:
        priority_message = "unknown priority"

if time_bound == "yes":
    time_message = "requires immediate attention today!"
else:
    time_message = "Consider completing it when you have free time."

print(f"Reminder: '{task}' is a {priority_message} task that {time_message}")
