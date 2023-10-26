
text = input('TEXT: ')
search = input('Text icerisinde aramak istediginiz harfi giriniz : ')
def control(text):
    sayac = 0
    for ch in text:
        if ch == search.lower():
            sayac += 1
    if sayac >= 1 and search.lower() != ' ':
        print(f'{search} harfi toplam {sayac} adet bulunmaktadir.') 
    elif search == ' ':
        print(f'Space, toplam {sayac} adet bulunmaktadir.')
    else:
        print(f'{search} HARFI BULUNAMADI!!')

control(text)

        


