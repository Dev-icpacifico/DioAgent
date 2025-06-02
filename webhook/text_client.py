import requests
import json

WEBHOOK_URL = "http://localhost:8000/webhook/"

with open("example_payload.json") as f:
    data = json.load(f)

response = requests.post(WEBHOOK_URL, json=data)
print("📨 Enviado al webhook:", response.status_code)
print(response.text)
