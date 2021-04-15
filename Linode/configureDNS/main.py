#!/usr/bin/env python
import var_file as var
import src.linode as Linode
import src.cloudflare as Cloudflare
from src.cloudflare import Cloudflare_class 
from src.linode import Linode_class

def main():

    linode = Linode_class(api_key=LINODE_API_KEY, node_label = node_label )
    json_data = linode.get_instances()
    node_response = linode.get_node(json_data)
    node_ipv4 = node_response['ipv4']
    cf_class = Cloudflare_class(zone_name=domain, node_ipv4=node_ipv4[0])
    cf_class.list_dns()
    cf_class.add_dns_records()


    exit(0)

#print("IPV4:\t", node_ipv4, type(node_ipv4),"\n\n")
# Variables from var_file
domain = var.domain
CF_API_KEY = var.CF_API_KEY
LINODE_API_KEY = var.LINODE_API_KEY
node_label = var.Node_label

if __name__ == '__main__':
    main()
