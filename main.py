from bs4 import BeautifulSoup
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.today() - relativedelta(years=1)
print(today.strftime("%Y-%m-%d"))


#Date to epoch -> Datum immer auf Monat abgerundet

period1 = (datetune.today()).strftime("")
period2 = None

yf = f"https://finance.yahoo.com/quote/%5EGSPC/history?period1={period1}&period2={period2}&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true"