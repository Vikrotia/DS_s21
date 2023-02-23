import requests
import json

def convert2RU(currency, value):
    convert_value = 0.0
    exchange_rate = 0.0
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    dict_of_json = response.json()
    for key1, value1 in dict_of_json.items():
        if key1 == 'Valute':
            for key2, value2 in value1.items():
                if key2 == currency:
                    for key3, value3 in value2.items():
                        if key3 == 'Value':
                            exchange_rate = float(value3)
    convert_value = exchange_rate * value
    return convert_value
# Запуск
currency = 'USD'
value = 952.13
print("Стоимость 952.13 USD в рублях:", convert2RU(currency, value))
currency = 'EUR'
value = 521.59
print("Стоимость 521.59 EUR в рублях:", convert2RU(currency, value))
currency = 'GBP'
value = 112.38
print("Стоимость 112.38 GBP в рублях:", convert2RU(currency, value))