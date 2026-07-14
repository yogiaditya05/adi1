import requests
import json

url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
payload = {
    "name": "Aditya Yogi",
    "regNo": "0827RL231005",
    "email": "adityayogi230523@acropolis.in"
}
headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(url, headers=headers, json=payload)
    print("Status Code:", response.status_code)
    print("Headers:", dict(response.headers))
    print("Body:", response.text)
except Exception as e:
    print("Error:", e)
