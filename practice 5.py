#prices = [57.8, 46.51, 97, 32.64, 55, 61, 20, 95.01, 36, 20, 340.23, 671, 157.35, 1.50]

#prices.sort()
#for i in prices:
#    r = int(i)
#    kk = (i - int(r)) * 100
#    print(f'{r} руб {kk:02.0f} коп', end=', ')

prices = [57.8, 46.51, 97, 32.64, 55, 61, 20, 95.01, 36, 20, 340.23, 671, 157.35, 1.50]

for i in sorted(prices) [::-1][:5]:
    r = int(i)
    kk = (i - int(i)) * 100
    print(f'{r} руб {kk:02.0f} коп', end=', ')