# -*- coding: utf-8 -*-
import sys
sys.path.insert(1, '/home/kl/projects/perdator')
from models.KqxsModel import KqxsModel
from configuration.DBConnection import DBConnection
db = DBConnection()
kqxs = KqxsModel(db)
results = kqxs.getResults()
for result in results:
	print(result['id'], '', result['place'])