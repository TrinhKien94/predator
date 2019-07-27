import psycopg2
from configuration.Configuration import Configuration
import psycopg2.extras

class DBConnection:
    def __init__(self):
        configuration = Configuration()
        self.configParser = configuration.getConfigParser()
        schema = self.configParser.get('POSTGRESQL', 'schema')
        self.conn = psycopg2.connect(
            "host='{}' dbname='{}' user='{}' password='{}' port='{}'". format(
                self.configParser.get('POSTGRESQL', 'host'),
                self.configParser.get('POSTGRESQL', 'dbname'),
                self.configParser.get('POSTGRESQL', 'username'),
                self.configParser.get('POSTGRESQL', 'password'),
                self.configParser.get('POSTGRESQL', 'port')))
        cur = self.conn.cursor()
        if schema is not None and schema != '':
            cur.execute("SET search_path TO {}". format(schema))

    def getDbConnection(self):
        return self.conn

    def fetchAll(self, query):
        cur = self._executeQuery(query)
        rows = cur.fetchall()
        return rows

    def fetchOne(self, query):
        cur = self._executeQuery(query)
        rows = cur.fetchone()
        return rows

	# Execute the query and return the cursor object
    def _executeQuery(self, query):
        cur = self.conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        cur.execute(query)
        return cur