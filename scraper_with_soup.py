from bs4 import BeautifulSoup as bs
import urllib.request as ureq

url = 'https://es.cointelegraph.com/bitcoin-price-index'

website = ureq.urlopen(url).read()

#print (website)

soup = bs(website, "html.parser")
tweets = soup.find_all('span', {'class':'title_text'})

tweets = list(map(lambda h: h.text.strip(), tweets))
print (tweets)