#!/usr/bin/env python
import var
from src.cloudflare import Cloudflare_class
from src.linode import Linode_class

def main():

    linode = Linode_class(api_key=var.LINODE_API_KEY, node_label=var.NODE_LABEL)
    json_data = linode.get_instances()
    node_response = linode.get_node(json_data)
    node_ipv4 = node_response['ipv4']

    # cloudflare class is dependant on getting an node IP.
    cf_class = Cloudflare_class(zone_name=var.DOMAIN, node_ipv4=node_ipv4[0])
    cf_class.list_dns()
    cf_class.add_dns_records()
    cf_class.remove_dns_records()

    exit(0)

if __name__ == '__main__':
    main()
