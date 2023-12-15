def true_date(date_to_prove):

    day, month, year = map(int, date_to_prove.split('.'))


    if year < 0:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    elif month == 2:

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_day = 29
        else:
            max_day = 28
    else:
        return False  


    if 1 <= day <= max_day:
        return True
    else:
        return False

date_to_prove = '0.5.2022'

print(true_date(date_to_prove))