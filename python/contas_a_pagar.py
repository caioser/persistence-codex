import pandas as pd
from datetime import datetime, timedelta
from pprint import pprint as pp

pd.options.display.float_format = "{:,.2f}".format

class Resumo:
    def __init__(self, list_of_dividas, money=0):
        self.money = money
        self.set_period()
        self.df = pd.concat([x.df for x in list_of_dividas])

    def set_money(self, m):
        self.money = m

    def set_period(self, a=datetime.now().year, m=datetime.now().month+2, d=1):
        if m > 12:
            m -= 12
            a += 1
        self.period = datetime(a, m, d)

    def info(self):
        print(f"""Totais:
a pagar: {self.total_valor:,.2f}
por dia: {self.total_pdia:,.2f}
saldo restante: {self.money_after_pay:,.2f}
restante: {self.restante_valor:,.2f}
restante por dia: {self.restante_pdia:,.2f}
dias ateh: {self.toPay["dias ateh"].min()}
""")
        
    def a(self):
        self.df.sort_values(by="vencimento", inplace=True)
        self.df.reset_index(drop=True, inplace=True)
        self.d = self.df[self.df["vencimento"] < self.period]
        self.d = self.d.assign(valor_cumulativo=[self.d.loc[:i, "valor"].sum() for i in self.d.index])

        self.canPay = self.d[self.d["valor_cumulativo"] + self.money >= 0]
        self.canPay.loc[:, ["por_dia", "proportions", "restante", "restante_pdia", "cumulativo", "valor_cumulativo"]] = 0
        self.money_after_pay = self.canPay["valor"].sum() + self.money

        self.toPay = self.d[self.d["valor_cumulativo"] + self.money < 0]
        self.toPay["valor_cumulativo"] = [self.toPay.loc[:i, "valor"].sum() for i in self.toPay.index]
        self.toPay = self.toPay.assign(proportions=self.toPay["valor"] / self.toPay["valor"].sum())
        self.toPay = self.toPay.assign(restante=(self.toPay["valor"].sum() + self.money_after_pay)*self.toPay["proportions"])
        self.toPay = self.toPay.assign(restante_pdia=(self.toPay["valor"].sum() + self.money_after_pay)*self.toPay["proportions"]/self.toPay["dias ateh"])
        self.toPay = self.toPay.assign(cumulativo=[self.toPay.loc[:i, "restante_pdia"].sum() for i in self.toPay.index])
        

        self.restante_valor = self.toPay["restante"].sum()
        self.restante_pdia = self.toPay["restante_pdia"].sum()
        self.total_pdia = self.toPay["por_dia"].sum()
        self.total_valor = self.toPay["valor"].sum()

        self.d = pd.concat([self.canPay, self.toPay])


        

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
        
    # def __str__(self):
    #     return f"{self.description}: {self.installments}x{self.value} ({self.total:.2})"
    
    def __repr__(self):
        return f"{self.description}: {self.installments}x{self.value} ({float(self.total):,.2f})"


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

# for x in dividas:
#     print(x.df)

z = Resumo(dividas, money=1949.08)

# print(z.df)
z.set_period(a=2023+10, m=12, d=31)
z.a()
d=z.d
for x, y in zip([0,60,120], [60,120,len(d)-1]):
    print(d.iloc[x:y, [0,1,3,4,5,6,7,8,9]])

z.info()




"""
(df[df["vencimento"] < "2023-06-01"].sort_values(by=["vencimento"])[:30]["por_dia"].sum() + (1703.84/prazo)) * prazo
   ^                                 ^                             ^    ^                    ^          ^
   |_ filter just may 2023           |                             |    |
                                     |_ sorting, ASC is default    |    |
"""