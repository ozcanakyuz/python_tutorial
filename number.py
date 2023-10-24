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
        print('Hak kalmadi!')
        answer = input('Yeniden oyna? (E/H): ')
        print('*******************************')
        if (answer == 'H'):
            print('Oyun bitti!')
            break
        elif (answer == 'h'):
            print('Oyun bitti!')
            break
        else:
            print('---------------------------')
    sayac += 1    

