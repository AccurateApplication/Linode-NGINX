import requests
import sys

# Returns json of all nodes running
def get_instances(api_key):
    headers = { "Authorization": f"Bearer {api_key}" }
    url = 'https://api.linode.com/v4/linode/instances'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        print("Resp status ok: " , resp.status_code)
    else: 
        sys.exit("Resp status not ok: ", (resp.status_code))

    response_json = resp.json()
    return response_json

# Get Node with matchning label
def getNode(json_data, node_label):
    Node = None
    for data in json_data['data']:
        if data['label'] == node_label:
            Node = data
            print("Found node with matching label..\n")
            print("IPv4 of node: ", data['ipv4'])
            break
        else: 
            Node = 'Did not find matching label'
    #if Node == None:
    #    print("Did not find matching label")
    return Node
