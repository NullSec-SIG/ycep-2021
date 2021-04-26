from multiprocessing import Process, freeze_support
import jwt
import string
import itertools


import requests

url = "http://127.0.0.1:5000"
resp = requests.post(f"{url}/api/login", json={"username": "hacker", "password": "KJ87^&%^&3JLH"})
print(resp.json())