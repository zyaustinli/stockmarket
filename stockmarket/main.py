import requests
from datetime import datetime, timedelta

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "TSLA",
    "interval": "60min",
    "apikey": ""
}




yesterday = datetime.now() - timedelta(1)
yesterday_date = yesterday.strftime('%Y-%m-%d')

day_before_yesterday = datetime.now() - timedelta(2)
day_before_yesterday_date = day_before_yesterday.strftime('%Y-%m-%d')

r_stock = requests.get("https://www.alphavantage.co/query", params=stock_params)
r_stock.raise_for_status()

data_stock = r_stock.json()

#stock market closes at 19:00:00
close_time = "19:00:00"

yesterday_close = float(data_stock["Time Series (60min)"][f"{yesterday_date} {close_time}"]["4. close"])
day_before_yesterday_close = float(data_stock["Time Series (60min)"][f"{day_before_yesterday_date} {close_time}"]["4. close"])


diff = abs(yesterday_close-day_before_yesterday_close)
percent_diff = diff*100/day_before_yesterday_close



def get_news():
    news_params ={
        'q': "Tesla",
        'apikey': ""

    }
    r_news = requests.get(NEWS_ENDPOINT, params=news_params)
    r_news.raise_for_status()

    news = r_news.json()

    for i in range(3):
        print(news['articles'][i]['title']+"\n"+ news['articles'][i]['description'] + "\n" + news['articles'][i]['url']+ "\n")



print(f"{yesterday_date} closing price: {yesterday_close}")
print(f"{day_before_yesterday_date} closing price: {day_before_yesterday_close}")
print(percent_diff)
get_news()

