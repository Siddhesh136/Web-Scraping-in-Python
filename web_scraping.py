import requests
import bs4

res = requests.get('http://www.siddheshmkadam.esy.es')
print(type(res))
print(res.text)
soup = bs4.BeautifulSoup(res.text,'lxml')
print(type(soup))
print(soup.select('title'))
print(soup.select('.collapse'))
for i in soup.select('.collapse'):
    print(i.text)
