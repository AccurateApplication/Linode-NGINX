import CloudFlare

def list_dns(zone_name):

    cf = CloudFlare.CloudFlare()
    zones = cf.zones.get(params={'per_page':50})
    try:
        zones = cf.zones.get(params = {'name':zone_name, 'per_page':1})
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/zones.get %d %s - api call failed' % (e, e))
    except Exception as e:
        exit('/zones.get - %s - api call failed' % (e))
    if len(zones) == 0:
        exit('no zone found')

    # Get zone ID from zone_name
    zone = zones[0]
    zone_id = zone['id']
    print("Zone ID:\t", zone_id)

     #Get DNS records from zone ID
    try: 
        dns_records = cf.zones.dns_records.get(zone_id)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/zones/dns_records.get %d %s - api call failed' % (e, e))

    # Loop through DNS records and print out
    print('DNS records for zone: %s' % (zone_name))
    for dns_record in dns_records:
        r_name = dns_record['name']
        r_type = dns_record['type']
        r_value = dns_record['content']
        r_id = dns_record['id']
        print('\t', r_id, r_name, r_type, r_value)
