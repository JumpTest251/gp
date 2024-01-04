def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """
 
    if len(date) == 0:
        return False

    # Split the date string into month, day, and year
    split_date = date.split("-")

    # Check if the date is in the correct format (mm-dd-yyyy)
    if len(split_date) != 3:
        return False

    # Extract the month, day, and year from the date string
    month = int(split_date[0])
    day = int(split_date[1])
    year = int(split_date[2])

    # Check if the month is valid (between 1 and 12)
    if not (1 <= month <= 12):
        return False

    # Check if the day is valid for the given month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if not (1 <= day <= 31):
            return False
    elif month in [4, 6, 9, 11]:
        if not (1 <= day <= 30):
            return False
    elif month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            # leap year
            if not (1 <= day <= 29):
                return False
        else:
            if not (1 <= day <= 28):
                return False
    else:
        # Month is invalid
        return False

    # If all checks pass, the date is valid
    return True
