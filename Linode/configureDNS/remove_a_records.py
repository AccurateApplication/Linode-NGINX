#!/usr/bin/env python
import CloudFlare
import var

zone_name = var.DOMAIN

cf = CloudFlare.CloudFlare()
try:
    zones = cf.zones.get(params = {'name':zone_name, 'per_page':1})
except CloudFlare.CloudFlareAPIError as e:
    exit('/zones.get %s - %d %s' % (zone_name, e, e))
except Exception as e:
    exit('/zones.get %s - %s' % (zone_name, e))

zone = zones[0]
zone_id = zone['id']

try:
    dns_records = cf.zones.dns_records.get(zone_id)
except CloudFlare.exceptions.CloudFlareAPIError as e:
    exit('/zones/dns_records.get %d %s - api call failed' % (e, e))

print(f"Looking for type A DNS records for domain: {var.DOMAIN}")
for dns_record in dns_records:
    r_type = dns_record['type']
    r_value = dns_record['content']
    r_id = dns_record['id']
    r_name = dns_record['name']
    r_content = dns_record['content']

    # Check if A record, if true, delete.
    if r_type == "A":
        try:
            dns_record = cf.zones.dns_records.delete(zone_id, r_id)
            print(f"Deleted: type: {r_type}, name: {r_name}, content: {r_content}")
        except CloudFlare.exceptions.CloudFlareAPIError as e:
            exit('/zones.dns_records.delete %s - %d %s - api call failed' % (dns_name, e, e))
    else:
        exit("Found no A type DNS records.")
