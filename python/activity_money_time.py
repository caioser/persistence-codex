from datetime import datetime, timedelta
from time import sleep

grana_mes = 2000
hora_semanal = 40
hora_mes = 4 * hora_semanal
grana_hora = grana_mes / hora_mes
grana_minuto = grana_hora / 60
grana_segundo = grana_minuto / 60

def config():
    pr = [
        hora_semanal,
        hora_mes,
        grana_hora,
        grana_minuto,
        grana_segundo,
        grana_mes
    ]

    for i in pr:
        print(i)
        
init_work = datetime.now()

def main():
    print("\033c", end="")
    print(datetime.now().strftime("%y-%m-%d %H:%M"))
    while True:
        print(" "*25, end="\r")
        print((datetime.now() - init_work).total_seconds() * grana_segundo, end="\r")
        sleep(2)
        
main()