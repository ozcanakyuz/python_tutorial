print('1. Sinema')
print('2. Tiyatro')
tercih = int(input('Tercihinizi tuşlayiniz : '))
ogrenci_mi = input('Ogrenci misiniz? (E/H) : ')

#TAM BILET
sinema = 15
tiyatro = 10
#OGRENCI BILET
ogrenci_bilet_sinema = sinema * 0.5
ogrenci_bilet_tiyatro = tiyatro * 0.5

if tercih == 1:
    if ogrenci_mi == 'E' or ogrenci_mi == 'e':
        print('-----------------------------------------')
        print(f'Sinema icin ogrenci bilet fiyati : {ogrenci_bilet_sinema}TL')
        print('-----------------------------------------')
    elif ogrenci_mi == 'H' or ogrenci_mi == 'h':    
        print('-----------------------------------------')
        print(f'Sinema icin tam bilet fiyati : {sinema}TL')
        print('-----------------------------------------')
    else:
        print('YANLIS TUSLAMA YAPTINIZ!!')
elif tercih == 2:
    if ogrenci_mi == 'E' or ogrenci_mi == 'e':
        print('-----------------------------------------')
        print(f'Tiyatro icin ogrenci bilet fiyati : {ogrenci_bilet_tiyatro}TL')
        print('-----------------------------------------')
    elif ogrenci_mi == 'H' or ogrenci_mi == 'h':
        print('-----------------------------------------')    
        print(f'Tiyatro icin tam bilet fiyati : {tiyatro}TL')
        print('-----------------------------------------')
    else:
        print('**************************')
        print('YANLIS TUSLAMA YAPTINIZ!!')
        print('**************************')

else:
    print('**************************')
    print('YANLIS TUSLAMA YAPTINIZ!!')
    print('**************************')