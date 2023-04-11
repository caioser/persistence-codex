from datetime import date, datetime, timedelta

dt = '%Y-%m-%d %H:%M'
di = datetime(2023, 5, 9)
df = datetime(2024, 11,9)
v = 1116.46
def months_to(dt1, dt2):
    # months_from_year
    y = (dt2.year - dt1.year)*12
    # months mod
    m = dt2.month - dt1.month
    tt =  y + m
    return tt

m = months_to(di, df)
du = df - datetime.now()
txt = '''{5}

valor: R$ {0:,.2f}
parcelas restantes: {1}

a pagar: R$ {2:,.2f}
dias até: {3}

Necessário R$ {4:,.2f} por dia

30x{4:,.2f} = {6:,.2f}
'''.format(
    v,
    m,
    m*v,
    du.days,
    (m*v)/du.days,
    datetime.now().strftime(dt),
    30*((m*v)/du.days)
)

print('\033c', end='')
print(txt)
