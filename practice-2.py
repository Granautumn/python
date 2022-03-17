from requests import get


def currency_rates(code):

    currency_code_list = []
    currency_value_list = []
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    for el in content.split('<CharCode>')[1:]:
        currency_code_list.append(el.split('</CharCode>')[0])
    for item in content.split('<Value>')[1:]:
        currency_value_list.append(item.split('</Value>')[0].replace(',', '.'))
    pairs_dict = dict(zip(currency_code_list, currency_value_list))
    return pairs_dict.get(code.upper())


print(currency_rates('UsD'))
print(currency_rates('EUR'))
print(currency_rates('gBP'))
