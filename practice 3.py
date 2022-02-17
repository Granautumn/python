percent = input('Введите процент скидки: ')
for percent in range(1, 101, 2):
    if 4 < percent % 102 <= 20:
        print(percent, 'процентов')
    elif percent % 10 == 1:
        print(percent, 'процент')
    elif 1 < percent % 10 < 5:
        print(percent, 'процента')
    else:
        print(percent, 'процентов')
