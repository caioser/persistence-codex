import pandas as pd
from datetime import datetime, timedelta


class Divida:
    def __init__(self,
                 description,
                 value,
                 installments,
                 ini_date):
        self.description = description
        self.value = value
        self.installments = installments if installments != 0 else (13 - ini_date.month)
        self.ini_date = ini_date

        self.faturas = [self.value for i in range(self.installments)]
        self.total = sum(self.faturas)

        self.vencimentos = []
        y = self.ini_date.year
        m = self.ini_date.month - 1
        d = self.ini_date.day
        for i in range(self.installments):
            if m+1 > 12:
                m = 0
                y += 1
            self.vencimentos.append(datetime(y, m+1, d))
            m += 1

        self.days_until = [int((i - datetime.now()).total_seconds()/(60*60*24)) for i in self.vencimentos]
        self.values_per_day = [self.value / i for i in self.days_until]
        
        self.df = pd.DataFrame({
            "desc":[self.description for i in range(self.installments)],
            "valor": self.faturas,
            "vencimento": self.vencimentos,
            "por_dia": self.values_per_day,
            "dias ateh": self.days_until})


dividas = [
    Divida("RE itaú", -122.47, 14, datetime(2023,5,7)),
    Divida("parcela emp Nubank", -304.61, 6, datetime(2023,6,5)),
    Divida("agua", -29, 0, datetime(2023,5,10)),
    Divida("localizador", -49, 0, datetime(2023,5,10)),
    Divida("RE santander", -268.43, 57, datetime(2023,5,10)),
    Divida("academia", -140, 0, datetime(2023,5,10)),
    Divida("energia", -150, 0, datetime(2023,5,11)),
    Divida("oi fibra", -145, 0, datetime(2023,5,19)),
    Divida("prisma", -1116.46, 19, datetime(2023,5,9)),
    Divida("credito claro", -30, 0, datetime(2023,5,20))
]

for x in dividas:
    print(x.df)