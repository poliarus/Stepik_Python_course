import requests

# r = requests.get('http://example.com')      # простой get запрос
# print(r.text)

url = "http://example.com"
par = {'ke1': 'value1', 'key2': 'value2'}
r = requests.get(url, params=par)  # передача параметров в запрос
print(r.url)  # сформированный url адрес с параметрами get запроса

url = "http://httpbin.org/cookies"
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies=cookies)  # отправка сформированных cookies на сервер
print(r.text)

# print(r.cookies['example_cookie_name'])  # использование cookies полученных от сервера
