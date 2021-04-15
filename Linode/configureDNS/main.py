#!/usr/bin/env python
import var_file as var
import src.linode as Linode
import src.cloudflare as Cloudflare

def main():
    Cloudflare.list_dns(domain)
    json_data = Linode.get_instances(LINODE_API_KEY)
    x = Linode.getNode(json_data, node_label)
    print(x)
    exit(0)

# Variables from var_file
domain = var.Domain
CF_API_KEY = var.CF_API_KEY
LINODE_API_KEY = var.LINODE_API_KEY
node_label = var.Node_label

if __name__ == '__main__':
    main()
