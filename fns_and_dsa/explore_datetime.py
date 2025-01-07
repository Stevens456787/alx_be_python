from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """
    Prompt the user for a number of days and calculate the future date.
    """
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=number_of_days)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def main():
    """
    Main function to call the datetime operations.
    """
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
