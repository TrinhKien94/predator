# craw tu 7/4/2006 den ngay hom nay
# -*- coding: utf-8 -*-
import sys
sys.path.insert(1, '/home/kl/projects/perdator')
from datetime import tzinfo, timedelta, datetime
from bs4 import BeautifulSoup
from urllib import request
import threading
import logging
import concurrent.futures
import re
from configuration.DBConnection import DBConnection
from entities.KqxsEntity import KqxsEntity
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
            contentStr = content.read()
            self.processContent(contentStr,date)
        except Exception as e:
            logging.error(url)
    def processContent(self, content,date):
        conn = DBConnection()
        soup = BeautifulSoup(content,'html.parser')
        tableResult = soup.find(id='MB0')
        for br in tableResult.find_all("br"):
            br.replace_with(" ")
        kqxsEntity = KqxsEntity()
        kqxsEntity.dayOfWeek = self.convertDayOfWeekToNumber(tableResult.select('th:first-child a')[1].text)
        kqxsEntity.place = re.search('\((.*)\)',tableResult.select('th:first-child')[0].text).group(1)
        trs = tableResult.select('tr')
        kqxsEntity.db = trs[1].select('em')[0].text
        kqxsEntity.g1 = trs[2].select('p')[0].text
        kqxsEntity.g21, kqxsEntity.g22 = trs[3].select('p')[0].text.split(" ")
        kqxsEntity.g31, kqxsEntity.g32, kqxsEntity.g33, kqxsEntity.g34, kqxsEntity.g35, kqxsEntity.g36 = trs[4].select('p')[0].text.split(' ')
        kqxsEntity.g41, kqxsEntity.g42, kqxsEntity.g43, kqxsEntity.g44 = trs[6].select('p')[0].text.split(' ')
        kqxsEntity.g51, kqxsEntity.g52, kqxsEntity.g53, kqxsEntity.g54, kqxsEntity.g55, kqxsEntity.g56 = trs[7].select('p')[0].text.split(' ')
        kqxsEntity.g61, kqxsEntity.g62, kqxsEntity.g63 = trs[9].select('p')[0].text.split(' ')
        kqxsEntity.g71, kqxsEntity.g72, kqxsEntity.g73, kqxsEntity.g74 = trs[10].select('p')[0].text.split(' ')
        kqxsEntity.tail0 = trs[1].select('td')[3].text
        kqxsEntity.tail1 = trs[2].select('td')[3].text
        kqxsEntity.tail2 = trs[3].select('td')[3].text
        kqxsEntity.tail3 = trs[4].select('td')[3].text
        kqxsEntity.tail4 = trs[5].select('td')[1].text
        kqxsEntity.tail5 = trs[6].select('td')[3].text
        kqxsEntity.tail6 = trs[7].select('td')[3].text
        kqxsEntity.tail7 = trs[8].select('td')[1].text
        kqxsEntity.tail8 = trs[9].select('td')[3].text
        kqxsEntity.tail9 = trs[10].select('td')[3].text
        kqxsEntity.date = date
        conn.session.add(kqxsEntity)
        conn.session.commit()       
    def getContentUrls(self,startDate):
        present = datetime.now()
        date = startDate
        with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
            while date < present:
                executor.map(self.getWebContent,(date,))
                date = self.nextDate(date)
    def convertDayOfWeekToNumber(self,dayOfWeek):
        if dayOfWeek == 'Chủ Nhật':
            return 1
        elif dayOfWeek == 'Thứ 2':
            return 2
        elif dayOfWeek == 'Thứ 3':
            return 3
        elif dayOfWeek == 'Thứ 4':
            return 4
        elif dayOfWeek == 'Thứ 5':
            return 5
        elif dayOfWeek == 'Thứ 6':
            return 6
        elif dayOfWeek == 'Thứ 7':
            return 7
crawl = Crawl()
theTime = datetime.strptime('07-04-2016','%d-%m-%Y')
crawl.getContentUrls(theTime)
# crawl.getWebContent(theTime)