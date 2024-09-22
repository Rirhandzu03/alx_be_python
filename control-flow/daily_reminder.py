
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound (yes/no): ")
                   


while True:
        if priority in ['high', 'medium', 'low']:
            break
        else:
            print("Invalid input. Please enter 'high', 'medium', or 'low'.")

    # Prompt for time sensitivity and validate input
while True:
        if time_bound in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Match Case for priority and customize reminder message
match priority:
        case 'high':
            reminder = f"'{task}' is a high priority task"
        case 'medium':
            reminder = f"'{task}' is a medium priority task"
        case 'low':
            reminder = f"'{task}' is a low priority task"

    # Use if statement for time-sensitive tasks
if time_bound == 'yes':
        reminder += " that requires immediate attention today!"
else:
        reminder += ". Consider completing it when you have free time."
    
    
print("\nReminder:", reminder)



                    


