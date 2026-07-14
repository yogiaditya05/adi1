import requests
import json
from typing import Dict, Any

BASE_URL = "https://bfhldevapigw.healthrx.co.in/hiring"

def _post(endpoint: str, payload: Dict[str, Any]) -> requests.Response:
    url = f"{BASE_URL}/{endpoint}"
    headers = {"Content-Type": "application/json"}
    return requests.post(url, headers=headers, json=payload, timeout=10)

def generate_webhook(name: str, reg_no: str, email: str) -> Dict[str, str]:
    payload = {"name": name, "regNo": reg_no, "email": email}
    resp = _post("generateWebhook/PYTHON", payload)
    resp.raise_for_status()
    data = resp.json()
    return {"webhook": data["webhook"], "accessToken": data["accessToken"]}

def submit_solution(webhook_url: str, access_token: str, final_query: str) -> Dict[str, Any]:
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
    payload = {"finalQuery": final_query}
    resp = requests.post(webhook_url, headers=headers, json=payload, timeout=10)
    resp.raise_for_status()
    return resp.json()
