# craw tu 7/4/2006 den ngay hom nay
from datetime import tzinfo, timedelta, datetime
from bs4 import BeautifulSoup
from urllib import request
import threading
import logging
import concurrent.futures
class Crawl:
    def __init__(self):
        self.baseUrl = 'https://xskt.com.vn/ket-qua-xo-so-theo-ngay/mien-bac-xsmb/{0}.html'
    def nextDate(self,date):
        date = date + timedelta(days=1)
        return date
    def getWebContent(self,date):
        dateStr = date.strftime('%d-%m-%Y')
        url = self.baseUrl.format(dateStr)
        logging.info(url)
        print(url)
        try:
            content = request.urlopen(url)
            return content.read()
        except Exception as e:
            logging.error(url)
    def getContentUrls(self,startDate):
        present = datetime.now()
        date = startDate
        with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
            while date < present:
                executor.map(self.getWebContent,(date,))
                date = self.nextDate(date)
crawl = Crawl()
theTime = datetime.strptime('07-04-2016','%d-%m-%Y')
crawl.getContentUrls(theTime)