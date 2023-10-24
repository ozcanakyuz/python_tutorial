# def bmi(boy, kilo):
#     return kilo/((boy**2))
# print('-----------------')
# print("BMI: ",bmi(1.85, 85))

def BMI(kilo, boy):
    return kilo / (boy ** 2)

print('****************************************')
print('BMI Programina Hos Geldiniz.')

boy = float(input('Metre cinsinden boyunuz: '))
kilo = int(input('Kilogram cinsinden kilonuz: '))

result = BMI(kilo, boy)
print('****************************************')
print(f'Vücut Kitle Endeksiniz (BMI) : {result}') 

if result > 25:
    print('Normal degerin ustundesiniz!! Normal Deger: 18,5 ile 24,9 arasidir.')
    print('****************************************')
elif 18.5 < result < 24.9:
    print('Normal degerdesiniz. Normal Deger: 18,5 ile 24,9 arasidir.')
    print('****************************************')
elif result < 18.5:
    print('Normal degerin altindasiniz!! Normal Deger: 18,5 ile 24,9 arasidir.')
    print('****************************************')
else:
    print('ERROR!')