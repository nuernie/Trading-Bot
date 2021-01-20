import requests 
from bs4 import BeautifulSoup

r = requests.get("https://stocks.comment.ai/trending.html")
soup = BeautifulSoup(r.content, "html.parser")

stockList = soup.find_all('tr')

#start with 1 cause 0 are table headers
for i in range(len(stockList)):
	if(i == 0 or i > 7):
		continue
	infos = stockList[i].find_all('td')
	
	tradeInfos = infos[1].text.split()
	buy = tradeInfos[0]
	sell = tradeInfos[1]
	hold = tradeInfos[2]
	
	tickerName = infos[2].text
	
	print(tickerName + '\n\tBUY: ' + buy + '\n\tSell: ' + sell + '\n\tHOLD: ' + hold + '\n')