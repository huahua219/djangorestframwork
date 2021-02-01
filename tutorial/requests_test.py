import requests
import json

data = {
    "code": "take me to you heart",
}

Header = {
    'Accept': 'application/json',
    # 'Accept': 'text/html'
}

url = "http://127.0.0.1:8000/snippets/21/"
res = requests.get(url=url, headers=Header, auth=('huahua', '1234')).json()
# res = requests.post(url=url, data=data, auth=('huahua', '1234'))
# res = requests.put(url=url, data=data, auth=('huahua', '1234'))

print(res)