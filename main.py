import requests
import lxml
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return response.text

def get_soup(html):
    soup = BS(html , 'lxml')
    return soup


def get_page(soup):

    page = soup.find_all('div',class_='row')
    for pages in page:
        title = pages.find('div',class_='vm-col-1').text.split()
        try:
            name = pages.find('div',class_ = 'vm-col-1').find('span',class_='prouct_name').text.split()
        except:
            name = ''
        try:
            price = pages.find('div',class_ = 'vm-col-1').find('span',class_='price').text.split()
        except:
            price = ''
        try:
            img = pages.find('div',class_='product').find('img').get('src')
        except:
            img = ''
        image = 'https://enter.kg/'
        # print(img.attrs)
        data = {
            'title':name,
            'price':price,
            'image': image + img
        }
        write_csv(data)
        print(data)

def write_csv(data: dict) -> None:
    with open('data.csv', 'a') as csv_file:
        fieldnames = ['title','price','image']
        writer = csv.DictWriter(csv_file, delimiter='/', fieldnames=fieldnames)
        writer.writerow(data)



def main():
    url = 'https://enter.kg/computers/noutbuki_bishkek'
    
    html = get_html(url=url)
    soup = get_soup(html=html)
    get_page(soup)

main()
