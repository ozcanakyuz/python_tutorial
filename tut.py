
sayi1 = int(input('1.SAYI: '))
sayi2 = int(input('2.SAYI: '))

tam_bolunenler = []

for i in range(sayi1, sayi2+1):
    if i % 7 == 0 and i % 11 == 0:
        tam_bolunenler.append(i)
    
print("TAM BOLUNENLER: ", tam_bolunenler)