import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

file_name = "dnac-proof.png"
path_to_file = "/home/devasc/Devasc_Skills/assets/task_10/"
text = "Task 10 screenshot"
room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vMDA1YjY5YjAtMTEyZi0xMWVlLWIzMDgtZGY2OGU0YTNmNzE2"

def get_token():
    with open("token.txt")as f:
        return f.read().strip("\n")

m = MultipartEncoder({'roomId': room_id,
                      'text': text,
                      'files': (file_name, open(path_to_file+file_name, 'rb'),
                      'image/png')})

r = requests.post('https://webexapis.com/v1/messages', data=m,
                  headers={'Authorization': f"Bearer {get_token()}",
                  'Content-Type': m.content_type})
print(r.text)

