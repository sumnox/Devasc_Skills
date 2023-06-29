#!/bin/bash

IP_HOST="192.168.56.102" 
CREDENTIALS=$(cat credentials.txt)
DATA_FORMAT='application/yang-data+json'
LOOPBACK_INTERFACE="Loopback199"
LOOPBACK_IP="10.1.99.1"

api_url="https://$IP_HOST/restconf/data/ietf-interfaces:interfaces"
api_url_put="$api_url/interface=$LOOPBACK_INTERFACE"
accept_header="Accept: $DATA_FORMAT"
content_header="Content-type: $DATA_FORMAT"

data=$(cat <<EOF
{
  "ietf-interfaces:interface": {
     "name": "Loopback199",
     "description": "RESTCONF => Loopback199",
     "type": "iana-if-type:softwareLoopback",
     "enabled": true,
     "ietf-ip:ipv4": {
         "address": [
             {
                 "ip": "$LOOPBACK_IP",
                 "netmask": "255.255.255.0"
             }
         ]
     }
 }
}
EOF
)

### API CALL 1 ###
output_api_1="$(curl -k -s \
	--no-progress-meter \
	-w "%{http_code}\n" \
	-H "$accept_header" \
	-H "$content_header" \
	-u $CREDENTIALS \
	-o /dev/null \
	-X PUT $api_url_put \
	-d "$data")"

if [[ "$output_api_1" -ge 200 && "$output_api_1" -le 300 ]];
then output_api_1="status OK: $output_api_1"
else output_api_1="ERROR: $output_api_1"
fi

### API CALL 2 ###
output_api_2="$(curl -k -s \
	--no-progress-meter \
	-w "%{http_code}\n" \
	-H "$accept_header" \
	-H "$content_header" \
	-u $CREDENTIALS \
	-o interfaces.txt \
	$api_url)"

### OUTPUT ###
date +"%d/%m/%y"
echo START REST API CALL
echo ============
echo first API CALL
echo ============
echo $output_api_1
echo ============
echo second API CALL
echo ============
echo Status Code: $output_api_2
echo Interfaces: "$(cat interfaces.txt)"
echo END REST API CALL
