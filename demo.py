import requests

response = requests.get('www.baidu.com')
print(response.text)
