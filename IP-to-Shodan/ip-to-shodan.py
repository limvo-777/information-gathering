import shodan
import sys
import re
import API_K

API_KEY = API_K.key


try:

    api = shodan.Shodan(API_KEY)
    ip_address = "67.207.47.210"
    ip_result = api.host(ip_address)
    region_code = ip_result['region_code']
    country = ip_result['country_code']
    city = ip_result['city']
    vulns = ', '.join(ip_result['vulns'])
    org = ip_result['org']
    ports = ', '.join(str(e) for e in ip_result['ports'])
    print(

        "IP Address : " + ip_address +"\n"
        "Region : " + region_code +"\n"
        "Country : " + country +"\n"
        "City : " + city +"\n"
        "Vulns : " + vulns +"\n"
        "Org : " + org +"\n"
        "Ports : " + ports +"\n"

    )



except Exception as e:
        print('Error: %s' % e)
