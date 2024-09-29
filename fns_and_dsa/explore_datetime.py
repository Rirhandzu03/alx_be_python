from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("current_date and time:", formatted_date)

def calculate_future_date(days_in_future):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_in_future)
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    print(f"Future date after {days_in_future} days:", formatted_future_date)


#Main Script logic
if __name__ == "__main__":
    display_current_datetime()

    try:
        days = int(input("Enter the numbers of days to add to current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer for the number  of days.")




    
    






