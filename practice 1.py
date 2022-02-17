duration = int(input('Введите время в секундах: '))
day = duration // 86400
hour = (duration - day * 86400) // 3600
minute = ((duration - day * 86400) - hour * 3600) // 60
second = duration - day * 86400 - hour * 3600 - minute * 60
print(day, 'дн' ,hour, 'час' ,minute, 'мин' ,second, 'сек')





#3600
#86400