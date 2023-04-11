from datetime import date, datetime, timedelta

# date format
dt = '%Y-%m-%d'
ym = [2023, 12]

def month_end(y=None, m=None): # -> datetime.date
    y = datetime.now().year if y == None else y
    m = datetime.now().month if m == None else m
    decrement = 1
    if m == 12:
        y += 1
        m = 1
        decrement = 0
    a = date(y, m + decrement, 1) + timedelta(days=-1)
    return a

print(
    type(month_end(*ym)),
    month_end(*ym).strftime(dt),
    month_end().strftime(dt),
    sep='\n')
