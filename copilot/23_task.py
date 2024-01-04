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
    if date == '':
        return False
    else:
        date = date.split('-')
        if len(date) != 3:
            return False
        else:
            if len(date[0]) != 2 or len(date[1]) != 2 or len(date[2]) != 4:
                return False
            else:
                if date[0][0] == '0':
                    date[0] = date[0][1]
                if date[1][0] == '0':
                    date[1] = date[1][1]
                if date[2][0] == '0':
                    date[2] = date[2][1:]
                if date[0] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11','12']:
                    return False
                else:
                    if date[1] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11','12']:
                        return False
                    else:
                        if date[2] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11','12']:
                            return False
                        else:
                            if date[0] in ['1','3','5','7','8','10','12'] and int(date[1]) > 31:
                                return False
                            else:
                                if date[0] in ['4','6','9','11'] and int(date[1]) > 30:
                                    return False
                                else:
                                    if date[0] == '2' and int(date[1]) > 29:
                                        return False
                                    else:
                                        return True