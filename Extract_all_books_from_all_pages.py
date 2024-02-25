import requests
from bs4 import BeautifulSoup



#Extract all the books from all the pages
base_url = 'https://books.toscrape.com/catalogue/'
all_urls = ['https://books.toscrape.com/catalogue/page-1.html']
current_page = 'https://books.toscrape.com/catalogue/page-1.html'


res = requests.get(current_page)

while res.status_code == 200 :
    data=BeautifulSoup(res.text, 'html.parser')
    next_page=data.find(class_='next')
    if next_page is None:
        break
    next_page_url= base_url + next_page.a['href']
    # print(next_page_url)
    all_urls.append(next_page_url)
    current_page = next_page_url
    # print(current_page)
    res = requests.get(current_page)

# print(all_urls)

for i in all_urls:
    response = requests.get(i)
    html_data = response.text
    data = BeautifulSoup(html_data, 'html.parser')
    books=data.find_all(class_='product_pod')
    for i in books:
        print(i.h3.a['title'])