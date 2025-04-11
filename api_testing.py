import requests

response = requests.get("http://localhost:8081/transactions")
print(response.json())