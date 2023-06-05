import bs4
from pathlib import Path

pth = Path.home() / Path('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy', 'The Code', '02 Practical applications using Python', '10 Web Scraping', 'example.html')
file = open(pth)

searchSoup = bs4.BeautifulSoup(file, 'html.parser')

print(searchSoup.text)

selector = searchSoup.select('p')

print(selector)
print(selector[0].getText())
print(selector[1].attrs)