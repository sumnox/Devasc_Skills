import requests
import datetime
import json
requests.packages.urllib3.disable_warnings()
# TODO
# Replace credentials


DNAC_scheme = 'https://'
DNAC_authority='sandboxdnac.cisco.com'
DNAC_port=':443'
DNAC_path_token='/dna/system/api/v1/auth/token'
DNAC_path='/dna/intent/api/v1/network-device'
auth=''

with open("credentials.txt", "rt") as f:
    auth = tuple(f.read().strip().split(':'))

# DATE AND TIME
print("Current date and time: ")
print(datetime.datetime.now())

# TOKEN REQUEST
token_req_url = DNAC_scheme+DNAC_authority+DNAC_path_token
req = requests.request('POST', token_req_url, auth=auth, verify=False)
token = req.json()['Token']


# INVENTORY REQUEST
req_url = DNAC_scheme+DNAC_authority+DNAC_port+DNAC_path
headers = {'X-AUTH-TOKEN': token}
resp_devices = requests.request('GET', req_url, headers=headers, verify=False)
resp_devices_json = resp_devices.json()

# FILTER RESPONSE DATA
for device in resp_devices_json['response']:
    if device['type'] != None:
        print('===')
        print('Hostname: ' + device['hostname'])
        print('Family  : ' + device['family'])
        print('MAC: '+ device['macAddress'])
        print('IP: ' + device['managementIpAddress'])
        print('Software version: ' + device['softwareVersion'])
        print('Reachability: ' + device['reachabilityStatus'])

