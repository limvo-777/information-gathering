import shodan
import sys

import API_K

API_KEY = API_K.key

try:
    api = shodan.Shodan(API_KEY)
    query = "qeury"
    
    result = api.search(query)
    
    print(result)


except Exception as e:
        print('Error: %s' % e)