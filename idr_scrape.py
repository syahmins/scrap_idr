import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')
json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar", "rate":6.8686850286801e-5,"date":"Thu, 16 Jul 2020 00:00:01 GMT","inverseRate":14558.827429479},
             "eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":6.0079196769088e-5,"date":"Thu, 16 Jul 2020 00:00:01 GMT","inverseRate":16644.696563495}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])

