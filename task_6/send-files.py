import requests
import sys
from requests_toolbelt.multipart.encoder import MultipartEncoder

if len(sys.argv) != 2:
    print(f"usage {sys.argv[0]} <path_to_file>")
    sys.exit()

task = sys.argv[1].split("/")[0]
file_name = sys.argv[1].split("/")[1]
path_to_file = "/home/devasc/Devasc_Skills/assets/"+sys.argv[1]
text = task + " screenshot"
room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vMDA1YjY5YjAtMTEyZi0xMWVlLWIzMDgtZGY2OGU0YTNmNzE2"

def get_token():
    with open("token.txt")as f:
        return f.read().strip("\n")

def upload_file():
    m = MultipartEncoder({'roomId': room_id,
                          'text': text,
                          'files': (file_name, open(path_to_file, 'rb'),
                          'image/png')})

    r = requests.post('https://webexapis.com/v1/messages', data=m,
                      headers={'Authorization': f"Bearer {get_token()}",
                      'Content-Type': m.content_type})
    print(r.text)

upload_file()
