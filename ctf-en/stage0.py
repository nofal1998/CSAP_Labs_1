import requests
from requests.auth import HTTPBasicAuth
import json
from env import config

headers = {
    "X-Cisco-Meraki-API-Key": config['MERAKI_KEY']
}

orgs_url = f"{config['MERAKI_BASE_URL']}/organizations"


resp = requests.get(orgs_url, headers = headers)
#org_id = json.dumps(resp.json(), indent=4, sort_keys=True)

json_2 = resp.json()


if resp.status_code == 200:
    print("It worked, access was granted")
   # print(org_id)

    for i in json_2:
        print("Org Name :" + i['name'])
        print("Org Id :" + i['id'])
        print("\n")
else:
    print("something went wrong: ", resp.status_code)

