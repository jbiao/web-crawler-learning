from urllib.request import Request, urlopen
import re
from bs4 import BeautifulSoup

url = Request('https://www.couriermail.com.au/news', headers={'User-Agent': 'Mozilla/5.0'})

try:
    html = urlopen(url).read()
except urlopen.HTTPError as e:
	print(e)
	exit()
	
soup_news = BeautifulSoup(html, 'lxml')
data = soup_news.find_all("a", class_="tge-cardv2_wrapper")  
#all_news_summary = soup_news.find_all("a", class_="tge-cardv2_wrapper").find_all("p", class_="tge-cardv2_standfirst")

for i in range(len(data)):
	headline = data[i].find_all("a", class_="tge-cardv2_wrapper").text
	print(headline)
#	try:
#		print(news_headline.text)
#		for news_summary in all_news_summary:
#			try:
#				print(news_summary.string.strip())
#			except AttributeError as e:
#				print(e)
#				exit()
#	except AttributeError as e:
#		print(e)
#		exit()
				