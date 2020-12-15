import requests
from bs4 import BeautifulSoup


def getData(license):
    req = requests.get('https://bizno.net/article/'+license)

    html = req.text
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('h4')
    print(title[0].text)

    location = soup.select('tr:nth-child(22)>td')

    return {
        'store_name': title[0].text,
        'address': location[0].text.strip()
    }