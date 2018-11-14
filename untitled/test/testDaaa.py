import  requests
from lxml import html
from bs4 import  BeautifulSoup
from lxml import etree

ss = requests.get('http://neihanshequ.com/')
# print(ss.text)
tree = html.fromstring(ss.text)
s = tree.xpath('//*[@id="detail-list"]/li[1]/div/div[3]/ul/li[4]/@data-text')
s1 = tree.xpath('//*[@id="detail-list"]/li[2]/div/div[2]/text()')#//*[@id="detail-list"]/li[2]/div/div[2]/a/div/h1/p/text()
# soup = BeautifulSoup(ss.content, 'lxml')
print(s)##detail-list > li:nth-child(2) > div > div.content-wrapper > a > div > h1 > p

soup =etree.HTML(ss.text)
s2 = soup.xpath('//*[@id="detail-list"]/li[2]/div/div[2]/a/div/h1/p/text()')

print(s2)

