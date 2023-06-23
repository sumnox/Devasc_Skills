import requests
import json

def get_token():
    with open("token.txt")as f:
        return f.read().strip("\n")

url = f"https://webexapis.com/v1/rooms"
headers = {
        "Authorization": f"Bearer {get_token()}",
        "Content-Type": "application/json"
        }
params = { "title": "devasc_skills_al" } 
res = requests.post(url, headers=headers, json=params)
print(json.dumps(res.json(), indent=4))

