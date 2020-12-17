import requests
from bs4 import BeautifulSoup


def getData(license):
    req = requests.get('https://bizno.net/article/'+license)

    html = req.text
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    try:
        title = soup.select('h4')[0].text
        location = soup.select('tr:nth-child(22)>td')[0].text
    except:
        return {
            'code': '1',
            "msg": "invalid license"
        }

    return {
        'code': '0',
        'store_name': title,
        'address': location
    }