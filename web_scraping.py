import requests
from bs4 import BeautifulSoup

response=requests.get('http://info.cern.ch/hypertext/WWW/TheProject.html')
# print(response)
html_data=response.text

data=BeautifulSoup(html_data, 'html.parser')
#Heading Extraction
# print(data.h1.string)

#Extract all the text
# print(data.get_text())


#Extracting all the hyperlinks and string available
# li = data.find_all('a')
# for i in li:
#     print(i)
#     print(i.string)

#Extracting the section hyperlinks
# section_hyperlinks=data.dl.find_all('a')
# for i in section_hyperlinks:
#     print(i.string)


# Extracting the dt only 
# li=data.dl.find_all('dt')
# print(len(li))
# for i in li:
#     print(i.a.string )


