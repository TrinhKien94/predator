class KqxsModel:
	def __init__(self, database):
		self.db = database
	def getResults(self):
		query = "SELECT id, place FROM kqxs"
		return self.db.fetchAll(query)
	def getResult(self, id):
		query = "SELECT id, place FROM kqxs WHERE id = {};". format(id)
		return self.db.fetchOne(query)