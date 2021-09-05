import urllib
import urllib.request
from bs4 import BeautifulSoup
import requests


def loadpage (url):

    html = urllib.request.urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    return(bsObject)

def load_darkweb (url):

    session = requests.session()
    # 세션 유지
    session.proxies = {}
    session.proxies['http'] = 'socks5h://localhost:9150'
    session.proxies['https'] = 'socks5h://localhost:9150'
    res = session.get(url).text.encode('utf-8')

    bsObject = BeautifulSoup(res, "html.parser")
    return(bsObject)

def extract_href (html_result):

    result = []

    for link in html_result.find_all('a'):

        link_url = link.get('href')
        try:
            if link_url.find(".onion") != -1:
                result.append("http://"+str(link_url))
            else:
                pass
        except:
            pass

    return (result)


if __name__ == '__main__':

    target_url = "https://thehiddenwiki.org/"
    target_darkweb_url = "https://xdb3grkzc2fpo7ymzvru7v2rdahtcyaocldwr5rp27ag2bsfjo24anad.onion.ly/index.html"
    page_source = loadpage(target_url)
    darkweb_page_source = load_darkweb(target_darkweb_url)
    #print(page_source)

    result = extract_href(page_source)
    darkweb_result = extract_href(darkweb_page_source)

    print(
        "Target URL : " + target_url + "\n"
        "Onion Link : " + ', '.join(result)
    )

    print(
        "Target URL : " + target_darkweb_url + "\n"
        "Onion Link : " + ', '.join(darkweb_result)
    )