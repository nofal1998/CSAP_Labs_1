import requests
from requests.auth import HTTPBasicAuth
import json
from env import config
data = {}
data['devices'] = []

orgs_id = 549236
network_id = 'L_646829496481105433'
headers = {
    "X-Cisco-Meraki-API-Key": config['MERAKI_KEY']
}

orgs_url = f"{config['MERAKI_BASE_URL']}/organizations/{orgs_id}/networks"

resp = requests.get(orgs_url, headers = headers)

orgs_url1 = f"{config['MERAKI_BASE_URL']}/networks/{network_id}/devices"
resp1 = requests.get(orgs_url1, headers = headers)




if resp.status_code == 200:
    print("Access Granted \n")
    #print(resp1.json())

    for i in resp1.json():
        if 'name' in i:
            print("Device Name :" + i['name'])
        print("Device Type  :" + i['model'])
        print("Device MAC  :" + i['mac'])
        print("Device Serial  :" + i['serial'])
        print("\n")

        if 'name' in i:
            data['devices'].append({'Device Name ': i['name'], 'Device Type': i['model'],'Device MAC' : i['mac'], 'Device Serial' : i['serial'] })

        else:
            data['devices'].append({'Device Type': i['model'],'Device MAC' : i['mac'], 'Device Serial' : i['serial'] })

        with open('data.txt','w') as outfile:
            json.dump(data, outfile)

    




else:
    print("something went wrong: ", resp.status_code)

