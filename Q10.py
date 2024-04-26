import calendar

def create_calendar(year, month):
    # Create a TextCalendar instance
    cal = calendar.TextCalendar(calendar.SUNDAY)  # Start weeks on Sunday

    # Format and print the calendar
    calendar_text = cal.formatmonth(year, month)
    print(calendar_text)

# Example usage:
year = 2024
month = 4
create_calendar(year, month)