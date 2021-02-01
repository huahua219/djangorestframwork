import requests
import json

data ={
    "code": "huahua huang new year!",
}


url = "http://127.0.0.1:8000/snippets/12/"
# res = requests.get(url=url).json()
# res = requests.post(url=url, data=data)
res = requests.put(url=url, data=json.dumps(data))

print(res)