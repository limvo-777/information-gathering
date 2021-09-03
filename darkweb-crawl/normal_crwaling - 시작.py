import urllib
import urllib.request
from bs4 import BeautifulSoup
import requests


def loadpage (url):

    html = urllib.request.urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    return(bsObject)

def extract_all_href (html_result):

    result = []

    ####################

    return (result)

if __name__ == '__main__':

    target_url = "https://thehiddenwiki.org/"

    page_source = loadpage(target_url)
    print(page_source)


    result = extract_all_href(page_source)

    print(
        "Target URL : " + target_url + "\n"
        "Onion Link : " + ', '.join(result)
    )
