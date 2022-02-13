duration = int(input('Введите время в секундах: '))
hour = duration // 3600
day = duration // 8600
minute = (duration - hour * 3600)// 60
second = duration % (24 * 3600)
second_duration = duration - (hour * 3600 + minute * 60)
print (second, 'сек')
print(minute, 'мин' ,second_duration, 'сек')
print(hour, 'час' ,minute, 'мин' ,second_duration, 'сек')
print(day, 'дн' ,hour, 'час' ,minute, 'мин' ,second_duration, 'сек')





#3600
#86400