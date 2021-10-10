from time import sleep
from math import trunc

def cronometer(min=1, sec=0):
    seconds = min * 60 #transforma os minutos em segundos
    seconds += sec
    while seconds:
        m, s = seconds // 60, seconds % 60
        print(f"tempo em minutos {trunc(m)}:{trunc(s)}")
        seconds -= 1
        sleep(1)
    print("fim do cronômetro")

while True:
    print('=====Iniciando pomodoro=====')
    for c in range(0, 4): #a cada 4 ciclos de produção o descanso irá ficar maior
        #marque o tempo de produção 
        print("=====Hora de trabalhar!=====")
        cronometer(25)
        #marque o tempo de descanso 
        print("=====Hora da pausa=====")
        cronometer(5)
    print("=====Descanse um pouco mais=====")
    cronometer(10)
    