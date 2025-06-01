# daily_reminder.py

def main():
    # Get user input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Match Case for priority
    match priority:
        case "high":
            message = f"Reminder: '{task}' is a high priority task"
        case "medium":
            message = f"Note: '{task}' is a medium priority task"
        case "low":
            message = f"Note: '{task}' is a low priority task"
        case _:
            message = f"Reminder: '{task}' has an unrecognized priority"

    # Time sensitivity check
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        if priority in ["medium", "low"]:
            message += ". Consider completing it when you have free time."
        elif priority == "high":
            message += ", but it's not time-bound — still, don’t slack! 😅"

    print("\n" + message)

if __name__ == "__main__":
    main()

