precent = input('Введите процент скидки: ')
for precent in range(1, 101):
    if 4 < precent % 100 <= 20:
        print(precent, 'процентов')
    elif precent % 10 == 1:
        print(precent, 'процент')
    elif 1 < precent % 10 < 5:
        print(precent, 'процента')
    else:
        print(precent, 'процентов')