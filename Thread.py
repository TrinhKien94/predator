from Crawl import Crawl
from datetime import tzinfo, timedelta, datetime
from bs4 import BeautifulSoup
from urllib import request
import threading
theTime = datetime.strptime('30/1/2019','%d/%M/%Y')
crawl = Crawl()
date = crawl.nextDate(theTime)
content = crawl.getWebContent(date)
soup = BeautifulSoup(content, 'html.parser')
print(soup.prettify())

threading._start_new_thread
