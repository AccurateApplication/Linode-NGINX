import requests
import sys

class Linode_class:
    def __init__(self,api_key,node_label):
        self.api_key= api_key
        self.node_label = node_label


# Returns json of all nodes running
    def get_instances(self):
        headers = { "Authorization": f"Bearer {self.api_key}" }
        url = 'https://api.linode.com/v4/linode/instances'
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            print("Linode resp status ok: " , resp.status_code)
        else: 
            sys.exit("Resp status not ok: ", (resp.status_code))
        response_json = resp.json()
        if len(response_json['data']) == 0:
            print(f" Linode data returned is 0.\n Bad response data from {url}\n Probably no instances up.")
            exit(1)


        return response_json

    # Get Node with matchning label
    def get_node(self, json_data):
        node = None
        print(f'Looking for linode instance with label set in variable file. ({self.node_label})')
        for data in json_data['data']:
            if data['label'] == self.node_label:
                node = data
                print("Found node with matching label.")
                print("IPv4 of node: ", data['ipv4'])
                break
            else: 
                node = 'Did not find matching label'
        return node
