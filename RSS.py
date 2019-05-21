import feedparser, sys, requests,
from bs4 import BeautifulSoup

d = feedparser.parse('https://feeds.feedburner.com/disdain/shiftcodes/ps3.rss')

f = open('blands.txt', mode = 'w+', encoding = "utf-8")
for i in range(0, 10):
        f.write(d.entries[i].description)
        i = i+1

f = re.sub("<.*?>", "", text)
f.close()

print('Downloading golden keys...')
print('Complete.')

