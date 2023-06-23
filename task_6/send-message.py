import requests
import json

def get_token():
    with open("token.txt")as f:
        return f.read().strip("\n")

message = "Here are my **screenshots** of devasc skills-based exam"
room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vMDA1YjY5YjAtMTEyZi0xMWVlLWIzMDgtZGY2OGU0YTNmNzE2"
url = f"https://webexapis.com/v1/messages"
headers = {
        "Authorization": f"Bearer {get_token()}",
        "Content-Type": "application/json"
        }
params = { "roomId": room_id, 'markdown': message } 
res = requests.post(url, headers=headers, json=params)
print(json.dumps(res.json(), indent=2))

