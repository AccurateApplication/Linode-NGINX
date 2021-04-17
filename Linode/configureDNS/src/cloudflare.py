import CloudFlare


class Cloudflare_class:
    def __init__(self,zone_name, node_ipv4):
        self.zone_name = zone_name
        self.cf = CloudFlare.CloudFlare()
        self.node_ipv4 = node_ipv4

    def list_dns(self):
        cf = self.cf
        zones = cf.zones.get(params={'per_page':50})
        try:
            zones = cf.zones.get(params = {'name':self.zone_name, 'per_page':1})
        except CloudFlare.exceptions.CloudFlareAPIError as e:
            exit('/zones.get %d %s - api call failed' % (e, e))
        except Exception as e:
            exit('/zones.get - %s - api call failed' % (e))
        if len(zones) == 0:
            exit('no zone found')

        # Get zone ID from zone_name
        zone = zones[0]
        zone_id = zone['id']

         #Get DNS records from zone ID
        try: 
            dns_records = cf.zones.dns_records.get(zone_id)
        except CloudFlare.exceptions.CloudFlareAPIError as e:
            exit('/zones/dns_records.get %d %s - api call failed' % (e, e))

        # Loop through DNS records and print out
        print('---\nCurrent DNS records for zone: {}'.format(self.zone_name))
        for dns_record in dns_records:
            r_type = dns_record['type']
            r_value = dns_record['content']
            print(f'Type: {r_type}, value: {r_value}')
        print("---")

    def add_dns_records(self):
        cf = self.cf
        try: 
            zones = cf.zones.get(params = {'name':self.zone_name, 'per_page':1})
        except CloudFlare.CloudFlareAPIError as e:
            exit('/zones.get %s - %d %s' % (self.zone_name, e, e))
        except Exception as e:
            exit('/zones.get %s - %s' % (self.zone_name, e))
        zone = zones[0]
        zone_id = zone['id']
        print(f"Will add {self.node_ipv4} to {self.zone_name} as A record.")
        # DNS records to add
        dns_records = [
            {'name': "@", 'type':'A',    'content':self.node_ipv4},
            {'name': "www."+self.zone_name,'type':'A',    'content':self.node_ipv4}
        ]
        # Loop through DNS records and add
        for dns_record in dns_records:
            print(f"Adding:\t{dns_record}")
            try:
                r = cf.zones.dns_records.post(zone_id, data=dns_record)
            except CloudFlare.exceptions.CloudFlareAPIError as e:
                exit('/zones.dns_records.post %s - %d %s' % (dns_record['name'], e, e))
        print(f"Successfully added {self.node_ipv4}.")
