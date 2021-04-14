#!/usr/bin/env python
import CloudFlare
def main():
    cf = CloudFlare.CloudFlare()
    zones = cf.zones.get(params={'per_page':50})
    for zone in zones: 
        zone_name = zone['name']
        zone_id = zone['id']
        print(zone_id, zone_name)

    # Get DNS records from zone ID
    try: 
        dns_records = cf.zones.dns_records.get(zone_id)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/zones/dns_records.get %d %s - api call failed' % (e, e))

    for dns_record in dns_records:
        r_name = dns_record['name']
        r_type = dns_record['type']
        r_value = dns_record['content']
        r_id = dns_record['id']
        print(r_id, r_name, r_type, r_value)

    exit(0)

if __name__ == '__main__':
    main()
