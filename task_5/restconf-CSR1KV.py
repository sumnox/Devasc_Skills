import requests
import json
requests.packages.urllib3.disable_warnings()

url = "https://192.168.56.102:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"
url_post = "https://192.168.56.102:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/"
url_patch = "https://192.168.56.102:443/restconf/data/Cisco-IOS-XE-native:native"

post_data = json.dumps({"severity": "alerts"})
put_data = json.dumps({"severity": "warnings"})
patch_data = json.dumps({"native": {"logging": {"monitor": {"severity": "informational"}}}})

menu = """


API REQUESTS
------------
[+] GET
[+] OPTIONS
[+] POST
[+] PUT
[+] PATCH
[+] DELETE
[-] 'q' to quit
[-] 'show' to show this menu
------------
"""


headers = {
          'Content-Type': 'application/yang-data+json',
            'Accept': 'application/yang-data+json',
              }


with open("credentials.txt", "rt") as f:
    auth = tuple(f.read().strip().split(':'))

def api_call(rest_verb, url=url, headers=headers, auth=auth, data=""):
    return requests.request(rest_verb, url, headers=headers, auth=auth, data=data, verify=False)

def print_response(resp):
    print(f"\nSTATUS CODE: {resp.status_code} {resp.reason}")
    print("===========HEADERS============")
    print(json.dumps(dict(resp.headers), indent=4))
    if resp.text:
        print("===========CONTENT============")
        print(resp.text)

def main():
    print(menu)
    while True:
        choice = input("What would you like to do?\n")
        if choice == "GET":
            print_response(api_call("GET"))
        elif choice == "OPTIONS":
            print_response(api_call("OPTIONS"))
        elif choice == "POST":
            print_response(api_call("POST", data=post_data, url=url_post))
        elif choice == "PUT":
            print_response(api_call("PUT", data=put_data))
        elif choice == "PATCH":
            print_response(api_call("PATCH", data=patch_data, url=url_patch))
        elif choice == "DELETE": 
            print_response(api_call("DELETE"))
        elif choice == "show":
            print(menu)
        elif choice == "q":
            print("quitting the program, goodbye")
            break
        else:
            print("Please choose from the following options:")
            print(menu)


if __name__ == "__main__":
    main()

