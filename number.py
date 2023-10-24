import random
import time

random_sayi = random.randint(1,10)

hak = 5

while True:
    sayi = int(input('Bir sayi giriniz: '))
    if (sayi == random_sayi):
        print('Tebrikler. Bildiniz.')

        print(' . denemede bildiniz.')
        break
    elif (sayi > random_sayi):
        print('Asagi')
        
        hak -= 1
        print(f'Kalan hakkiniz: {hak}')
    elif (sayi < random_sayi):
        print('Yukari')
        hak -= 1
        print(f'Kalan hakkiniz: {hak}')
    if hak == 0:
        print('Hak kalmadı! Yeniden oyna? E/H')
        break    

