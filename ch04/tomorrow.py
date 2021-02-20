def read_date():
    year, month, day = tuple(map(int, input().split()))
    return year, month, day

def print_date(date):
    year, month, day = date
    print("%02d/%02d/%04d" % (month, day, year))

def advance_day(date):
    year, month, day = date
    
    # end_of_month = (month == 1 and day == 31) or \
               # (month == 2 and day == 28) or \
               # (month == 3 and day == 31) or \
               # (month == 4 and day == 30) or \
               # (month == 5 and day == 31) or \
               # (month == 6 and day == 30) or \
               # (month == 7 and day == 31) or \
               # (month == 8 and day == 31) or \
               # (month == 9 and day == 30) or \
               # (month == 10 and day == 31) or \
               # (month == 11 and day == 30) or \
               # (month == 12 and day == 31)
    
    #end_of_month = (month in [1, 3, 5, 7, 8, 10, 12] and day == 31) or \
    #                     (month in [4, 6, 9, 11] and day == 30) or \
    #                     (month == 2 and day == 28)
    
    end_of_month = (month, day) in [(1, 31), (2, 28), (3, 31), (4, 30), (5,
        31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]
    
    end_of_year = month == 12 and day == 31
    
    if end_of_month:
        if end_of_year:
            year += 1
            month = 1
            day = 1
        else:
            month += 1
            day = 1
    else:
        day += 1
    
    return year, month, day
    
if __name__ == "__main__":
    today = read_date()
    print_date(today)
    tomorrow = advance_day(today)
    print_date(tomorrow)