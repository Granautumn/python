import utils


current_list = ['EUR', 'USD', 'GMO', 'GbP']
for i in range(0, len(current_list)):
    print('Курс ', '"' + current_list[i] + '"', ' равен: ', utils.currency_rates(current_list[i]))