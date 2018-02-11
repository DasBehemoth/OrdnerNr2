import json
import urllib

def get_address_from_ip(ip_address):
    base_uri = "http://freegeoip.net/json/80.110.114.199"
    result = urliib.urlopen(base_uri+ip_address).read()
    data = json.loads(result)
    return result

if __name__ == '__main__':
    uri = "http://freegeoip.net/json/80.110.114.199"
    ip_address = "80.110.114.199"
    print get_address_from_ip(ip_address)