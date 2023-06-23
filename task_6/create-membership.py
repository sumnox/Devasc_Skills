
import requests
import json

def get_token():
    with open("token.txt")as f:
        return f.read().strip("\n")

url = f"https://webexapis.com/v1/memberships"
room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vMDA1YjY5YjAtMTEyZi0xMWVlLWIzMDgtZGY2OGU0YTNmNzE2"
person_email = "yvan.rooseleer@biasc.be"
headers = {
        "Authorization": f"Bearer {get_token()}",
        "Content-Type": "application/json"
        }
params = { "roomId": room_id, "personEmail": person_email } 
res = requests.post(url, headers=headers, json=params)
print(json.dumps(res.json(), indent=4))
