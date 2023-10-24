import random
import time

random_sayi = random.randint(1,10)
sayac = 1
hak = 5

while True:
    sayi = int(input('Bir sayi giriniz: '))
    print('------------------------')
    if (sayi == random_sayi):
        print('Kontrol ediliyor...')
        time.sleep(1)
        print('***********************')
        print(f'TEBRIKLER!! {sayac}. DENEMEDE BILDINIZ.')
        print('***********************')
        break
    elif (sayi > random_sayi):
        print('Kontrol ediliyor...')
        time.sleep(1)
        print('------------------------')
        print('DOWN <')
        hak -= 1
        print(f'Kalan hakkiniz: {hak}')
        print('------------------------')
    elif (sayi < random_sayi):
        print('Kontrol ediliyor...')
        time.sleep(1)
        print('------------------------')
        print('UP >')
        hak -= 1
        print(f'Kalan hakkiniz: {hak}')
        print('------------------------')
    if hak == 0:
        print('Hak kalmadi! Yeniden oyna? (E/H)')
        print('*******************************')
        break
    sayac += 1    

