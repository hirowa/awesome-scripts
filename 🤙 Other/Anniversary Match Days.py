from datetime import datetime, timedelta

def highlight_important_days(anniversary_date, interval_days, years):
    """
    Given an anniversary date, this function calculates and highlights 
    monthlyversaries that align with user-defined milestone intervals within a set timeframe.
    
    Parameters:
    - anniversary_date (str): Date in 'YYYY-MM-DD' format.
    - interval_days (int): Interval for milestone days (e.g., 100, 200, 1000).
    - years (int): Number of years to check.
    
    Returns:
    - List of matching dates where monthlyversaries coincide with milestone days.
    """
    # Convert input to datetime
    anniversary = datetime.strptime(anniversary_date, "%Y-%m-%d")

    # Generate milestone days
    milestone_days = [(anniversary + timedelta(days=interval_days * i)).date() for i in range(1, (years * 365) // interval_days + 1)]

    # Generate monthlyversaries
    monthlyversaries = []
    for i in range(1, years * 12 + 1):  # Up to 'years' years ahead
        month = anniversary.month + i
        year = anniversary.year + (month - 1) // 12
        month = (month - 1) % 12 + 1
        try:
            date = anniversary.replace(year=year, month=month).date()
        except ValueError:
            date = anniversary.replace(year=year, month=month, day=28).date()  # Handle February issues

        monthlyversaries.append(date)

    # Find matching dates
    matches = sorted(set(milestone_days).intersection(set(monthlyversaries)))

    return matches

# User input
anniversary_date = input("Enter your anniversary date (YYYY-MM-DD): ")
interval_days = int(input("Enter the milestone interval in days (e.g., 100, 200, 1000): "))
years = int(input("Enter the number of years to check: "))

# Get important dates
matches = highlight_important_days(anniversary_date, interval_days, years)

# Print results
print("\nImportant Matches:")
if matches:
    for date in matches:
        print(date.strftime("%Y-%m-%d"))
else:
    print("No matching dates found.")
