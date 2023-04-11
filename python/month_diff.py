from datetime import date, datetime, timedelta


def months_to(dt1, dt2):
    # months_from_year
    y = (dt2.year - dt1.year)*12
    # months mod
    m = dt2.month - dt1.month
    tt =  y + m + 1
    return tt

def bus_day(start, end):
    all_days = (start + timedelta(x + 1) for x in range((end - start).days))
    count = sum(1 for day in all_days if day.weekday() < 5)
    return count

def gen_bill_dates(start, nbills):
    # all bill dates
    y = start.year
    m = start.month - 1
    d = start.day
    abd = []
    for i in range(nbills):
        if m+1 > 12:
            m = 0
            y += 1
        abd.append(datetime(y, m+1, d))
        m += 1
    return abd

dt = '%Y-%m-%d %H:%M'
di = datetime(2023, 5, 9)
df = datetime(2024, 11,9)
v = 1116.46
m = months_to(di, df)
du = df - datetime.now()
bd = bus_day(di, df)
nper_day = (m*v)/du.days
nper_bday = (m*v)/bd
bills_dates = gen_bill_dates(di, m)


txt = f'''{datetime.now().strftime(dt)}

valor: R$ {v:,.2f}
parcelas restantes: {m}

a pagar: R$ {m*v:,.2f}
dias até:   {du.days}, R$ {nper_day:,.2f}/dia
dias uteis: {bd}, R$ {nper_bday:,.2f}/dia

30x{nper_day:,.2f} = {30*nper_day:,.2f}
22x{nper_bday:,.2f} = {22*nper_bday:,.2f}
'''

print('\033c', end='')
print(txt)

sum = 0
for x in bills_dates:
    dsutl = (x - datetime.now()).days
    sum += v / dsutl
    print(
        bills_dates.index(x)+1,
        ' '*(2-len(str(bills_dates.index(x)+1))),
        #x.strftime(dt[:8]),
        f'{v / (x - datetime.now()).days:,.2f}',
        f'in {(x - datetime.now()).days} day{"" if (x - datetime.now()).days == 1 else "s"}'
    )
