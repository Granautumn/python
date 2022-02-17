percent = input('Введите процент скидки: ')
for percent in range(1, 101):
    if 4 < percent % 100 <= 20:
        print(percent, 'процентов')
    elif precent % 10 == 1:
        print(percent, 'процент')
    elif 1 < percentt % 10 < 5:
        print(percent, 'процента')
    else:
        print(percent, 'процентов')
