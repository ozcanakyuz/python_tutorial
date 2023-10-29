#n sayi kadar tek ve cift ayrı ayrı ortalamasını bulma
tekAdet = 0
tekToplam = 0
ciftAdet = 0
cifToplam = 0
n = int(input('Kaca adet sayi girilecek: '))
for i in range(n):
    sayi = int(input('Sayi: '))
    if (sayi%2==0):
        ciftAdet += 1
        cifToplam += sayi
    else:
        tekAdet += 1
        tekToplam += sayi
    
if (tekAdet!=0):
    ortTek = tekToplam/tekAdet
    print("Ortalama Tek Sayilar : ",ortTek)
print("------------------------")
if (ciftAdet!=0):
    ortCift = cifToplam/ciftAdet
    print("Ortalama Cift Sayilar : ", ortCift)