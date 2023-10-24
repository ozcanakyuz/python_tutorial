def topla(x,y):
    return x+y
def cikar(x,y):
    return x-y
def carp(x,y):
    return x*y
def bol(x,y):
    return x/y

print('1. Toplama')
print('2. Cikarma')
print('3. Carpma')
print('4. Bolme')
islem = int(input('Yapmak istediginiz islemi seciniz: '))
sayi1 = float(input("Birinci sayiyi giriniz: "))
sayi2 = float(input("Ikinci sayiyi giriniz: "))
if islem == 1:
    print(sayi1, '+', sayi2, '=', topla(sayi1,sayi2))
elif islem == 2:
    print(sayi1, '-', sayi2, '=', cikar(sayi1,sayi2))   
elif islem == 3:
    print(sayi1, '*', sayi2, '=', carp(sayi1,sayi2))
elif islem == 4:
    if sayi2 == 0:
        print("Hicbir sayi 0'a bolunmez o yuzden gecersiz islem.")
    else:
        print(sayi1, '/', sayi2, '=', bol(sayi1,sayi2))
else:
    print('GECERSIZ ISLEM')   