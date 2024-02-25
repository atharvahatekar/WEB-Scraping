import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

base_url = 'https://books.toscrape.com/catalogue/'
all_urls = ['https://books.toscrape.com/catalogue/page-1.html']
current_page = 'https://books.toscrape.com/catalogue/page-1.html'

all_book_urls = []

book_details =[]



res = requests.get(current_page)

while res.status_code==200:
    data = BeautifulSoup(res.text, 'html.parser')
    next_page = data.find(class_='next')
    if next_page is None:
            break        
    next_page_url= base_url + next_page.a['href']
    all_urls.append(next_page_url)
    current_page = next_page_url
    res = requests.get(current_page)
# print(all_urls)


for i in all_urls:
    res = requests.get(i)
    html_data = res.text
    data = BeautifulSoup(html_data, 'html.parser')
    books=data.find_all(class_='product_pod')
    
    for b in books:
        book_url=base_url + b.h3.a['href']
        all_book_urls.append(book_url)

# print(len(all_book_urls))

for book_url in all_book_urls:
    res=requests.get(book_url)
    data= BeautifulSoup(res.text, 'html.parser')
    
    title = data.h1.string
    
    price = data.find(class_='price_color').string
    price= float(re.search('[\d.]+', price).group())
    
    qty = data.find(class_= 'instock availability')
    qty = qty.contents[-1].strip()
    qty=int(re.search('\d+', qty).group())
    
    book_details.append([title,book_url,price,qty])


df = pd.DataFrame(book_details, columns =['Title','Link','Price', 'Quantity in Stock'] )
# print(df)

df.to_csv('books.csv', index=False)
