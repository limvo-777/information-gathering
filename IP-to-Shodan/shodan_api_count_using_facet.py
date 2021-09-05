import shodan
import sys
import API_K

API_KEY = API_K.key
# The list of properties we want summary information on
FACETS = [
    ('country', 10),
    'city',
]
# default 5 for a facet. If you want to see more than 5, you could do ('country', 1000) for example

FACET_TITLES = {
    'country': 'Top 10 Countries',
    'city': 'Top 5 Cities',    
}

# Input validation

try:
    api = shodan.Shodan(API_KEY)

    query = 'port:80'

    result = api.count(query, facets=FACETS)

    print ('Shodan Summary Information')
    print ('Query: %s' % query)
    print ('Total Results: %s\n' % result['total'])

    # Print the summary info from the facets
    for facet in result['facets']:
        print (FACET_TITLES[facet])

        for term in result['facets'][facet]:
            print ('%s: %s' % (term['value'], term['count']))

        # Print an empty line between summary info
        print ('\n')
except:
    pass
