import pandas as pd 
import re     # to remove the special character from price and to extract the numbers(qty) from whole string character
import requests
from bs4 import BeautifulSoup
base_url = 'https://books.toscrape.com/'
res = requests.get('https://books.toscrape.com/')

data = BeautifulSoup(res.text, 'html.parser')

# print(data)

b1= data.find(class_='product_pod')
b1_url = base_url + b1.h3.a['href']
# print(b1_url)

res = requests.get(b1_url)
data = BeautifulSoup(res.text, 'html.parser')

title = data.h1.string
price = data.find(class_='price_color').string
price= float(re.search('[\d.]+', price).group())         #from  Â£51.77 to 51.77 this


qty = data.find(class_= 'instock availability')
qty = qty.contents[-1].strip()
qty=int(re.search('\d+', qty).group())             #remove the character and get only number, from (In stock (22 available)) to 22 this

# print(title,b1_url,price,qty)

book_details=[]
book_details.append([title,b1_url,price,qty])

df = pd.DataFrame(book_details, columns =['Title','Link','Price', 'Quantity in Stock'] )
# print(df)

df.to_csv('books.csv', index=False)


