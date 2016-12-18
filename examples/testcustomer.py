import requests
import json
print requests
params = {
    "email": "test@gmail.com",
    "shipping": {
        "first_name": "Abe"
    }
}

payload = {'key1': 'value1', 'key2': {'value2' : 'value3'}}

# r = requests.post("http://httpbin.org/post", data=json.dumps(payload))





