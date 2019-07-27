# -*- coding: utf-8 -*-
import sys
sys.path.insert(1, '/home/kl/projects/perdator')
from models.Kqxs import Kqxs
from configuration.DBConnection import DBConnection
db = DBConnection()
kqxs = Kqxs(db)
results = kqxs.getResults()
for result in results:
	print(result['id'], '', result['place'])